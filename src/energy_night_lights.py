import geopandas as gpd
import pandas as pd
import matplotlib.animation as animation
import matplotlib.pyplot as plt

class StatesTotalEMap:
    
    def __init__(self):

        # load data
        self.us_polygons = gpd.read_file('../data/derived/us_state_polygons.geojson')
        self.world_polygons = gpd.read_file('../data/derived/world_polygons.geojson')
        self.cities = gpd.read_file('../data/derived/us_cities_population_fraction.geojson')
        self.total_e = gpd.read_file('../data/derived/state_year_total_e.csv')

        # process data
        self.cities = self.cities.merge(self.total_e, how = 'inner', left_on='state', right_on='StateCode')
        self.cities['state_energy'] = self.cities['Data'].astype('float')
        self.cities['energy_used'] = self.cities['state_energy']*self.cities['population_fraction_in_state']
        self.cities['Year'] = self.cities.Year.astype('int32')

        self.__add_scaling_factor(energy_max_value=2663540.0,
                                marker_max_size=9.0,
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
        tmp.plot(ax=ax, markersize=tmp.marker_size, color='yellow', alpha=0.3)
        # for now, let's stick with CONUS
        ax.set_ylim([23, 52])
        ax.set_xlim([-130, -65])
        ax.set_facecolor('lightslategrey')
        ax.set_title(f'Year: {year}')


    def create_animation(self, start_year = 1960):

        tmp = self.cities[self.cities['Year']==start_year]
        fig, ax = plt.subplots(figsize=(10, 8))
        self.__plot_year(ax,start_year,tmp)

        def update(frame):
            ax.clear()
            # we'll set frame as an iterable from 1961 - 2023
            tmp = self.cities[self.cities['Year']==frame]
            self.__plot_year(ax,frame,tmp)
            print(f'finished year: {frame}')

        ani = animation.FuncAnimation(fig=fig, func=update, frames=range(1961, 2024), interval=1000)
        # may have to fuss with backend to make this work...
        writer = animation.PillowWriter(fps=1)
        ani.save('us_cities_animation.gif', writer=writer)


if __name__=='__main__':
    map = StatesTotalEMap()
    map.create_animation(start_year=1960)