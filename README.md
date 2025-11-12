# energy_mix
Explore US energy data

## Data sources

- [State Energy Data System](https://www.eia.gov/state/seds/seds-data-complete.php?sid=US#CompleteDataFile) [SEDS] from the US Energy Information Administration.
- [This site](https://geojson-maps.kyd.au) to download world geojson
- US states downloaded from [natural earth](https://www.naturalearthdata.com/downloads/110m-cultural-vectors/110m-admin-1-states-provinces/)
- US Major Cities, downloaded from [ESRI/ArcGIS](https://hub.arcgis.com/datasets/esri::usa-major-cities-3/explore)
- US Population Data from the [US Census](https://www.census.gov/data/tables/time-series/dec/popchange-data-text.html)

## Projects

### Energy Night Lights

Let's create an animation of energy consumption over time, similar to "lights at night" satellite images. See this [NASA Earth Observatory site](https://earthobservatory.nasa.gov/features/NightLights) for some examples.

Here's the current 

We will use the "TETCB" data in the SEDS data described above -- total energy consumption in billion BTU for each state.

#### Methods
- We have energy at the state level, but we want to visualize this at the city level to approximate the night lights images. (Of course, this will result in false precision!)
- We'll use the US Major Cities dataset, which includes coordinates and 2020 population for cities with 10,000+ people. For each state, we calculate the fraction of people living in each of the state's cities, then use that to allocate the portions of the state's total energy to each city.
- Regarding coordinate systems: geometries are stored in EPSG:4326  (lat & lon coordinates). To create a curved-looking image, we can use either convert the underlying coordinates to a different projection using [geopandas](https://geopandas.org/en/stable/docs/user_guide/projections.html), or we can leverage the projection features in [matplotlib](https://matplotlib.org/stable/api/projections_api.html). Looks like changing the first option is going to require less boilerplace code, so let's do that.
There are a bunch of options for CRS; I picked EPSG [9311](https://spatialreference.org/ref/epsg/9311/) & [6350](https://spatialreference.org/ref/epsg/6350/). EPSG 9311 created some funky artifacts when plotted, so I'll go with 6350, which is an Albers projection based on the continental US.


### Energy Explorer

A dashboard to show & explore SEDS energy data by state, sector, and source over time.