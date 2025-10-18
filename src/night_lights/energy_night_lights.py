"""
Need to have ffmpeg installed to write to mp4 (`brew install ffmpeg` on mac osx)
"""
import geopandas as gpd
import pandas as pd
import matplotlib.animation as animation
import matplotlib.pyplot as plt

class StatesTotalEMap:
    
    def __init__(self):

        # load data; geometries are in crs: EPSG 4326 (lat/lon)
        self.us_polygons = gpd.read_file('../../data/derived/us_state_polygons.geojson')
        self.world_polygons = gpd.read_file('../../data/derived/world_polygons.geojson')
        self.cities = gpd.read_file('../../data/derived/us_cities_population_fraction.geojson')
        self.total_e = gpd.read_file('../../data/derived/state_year_total_e.csv')

        # process data
        self.cities = self.cities.merge(self.total_e, how = 'inner', left_on='state', right_on='StateCode')
        self.cities['state_energy'] = self.cities['Data'].astype('float')
        self.cities['energy_used'] = self.cities['state_energy']*self.cities['population_fraction_in_state']
        self.cities['Year'] = self.cities.Year.astype('int32')

        self.__add_scaling_factor(energy_max_value=2663540.0,
                                marker_max_size=12.0,
                                marker_min_size = 0.001)

    def __add_scaling_factor(self, energy_max_value=2663540.0,
                                marker_max_size=1000.0,
                                marker_min_size = 0):
        scaling_factor = (marker_max_size / energy_max_value) + marker_min_size
        self.cities['marker_size'] = scaling_factor * self.cities['energy_used']
        print(f'{scaling_factor=}')

    def __plot_year(self, ax, year, tmp: gpd.GeoDataFrame):
        self.world_polygons.plot(ax=ax, color='dimgray', edgecolor='white', linewidth=0.3)
        self.us_polygons.plot(ax=ax, color='dimgray', edgecolor='white', linewidth=0.3)
        tmp.plot(ax=ax, markersize=tmp.marker_size, color='yellow', alpha=0.2)
        # for now, let's stick with CONUS
        ax.set_ylim([23, 52])
        ax.set_xlim([-130, -65])
        ax.set_facecolor('lightslategrey')
        ax.set_title(f'Year: {year}', color='gold')

    def create_animation(self, start_year = 1960):
        fig, ax = plt.subplots(figsize=(10, 8), facecolor='black')
        # could opt to turn off frame: frameon=False
        fig.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.9)

        def update(frame):
            ax.clear()
            tmp = self.cities[self.cities['Year']==frame]
            self.__plot_year(ax,frame,tmp)
            print(f'finished year: {frame}')

        ani = animation.FuncAnimation(fig=fig, func=update, frames=range(start_year, 2024))

        # writer = animation.PillowWriter(fps=1)
        # ani.save('us_cities_animation.gif', writer=writer)
        ani.save('us_cities_animation.mp4', writer='ffmpeg', fps=4)


if __name__=='__main__':
    map = StatesTotalEMap()
    map.create_animation(start_year=1960)