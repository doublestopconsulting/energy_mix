# energy_mix
Explore US energy data

## Data sources

- [State Energy Data System](https://www.eia.gov/state/seds/seds-data-complete.php?sid=US#CompleteDataFile) [SEDS] from the US Energy Information Administration.
- [This site](https://geojson-maps.kyd.au) to download world geojson
- US states downloaded from [natural earth](https://www.naturalearthdata.com/downloads/110m-cultural-vectors/110m-admin-1-states-provinces/)
- US Major Cities, downloaded from [ESRI/ArcGIS](https://hub.arcgis.com/datasets/esri::usa-major-cities-3/explore)

## Projects

### Energy Night Lights

Let's create an animation of energy consumption over time, similar to "lights at night" satellite images. See this [NASA Earth Observatory site](https://earthobservatory.nasa.gov/features/NightLights) for some examples.

We will use the "TETCB" data in the SEDS data -- total energy consumption in billion BTU for each state.

#### Methods
- We have energy at the state level, but we want to visualize this at the city level to approximate the night lights images. (Of course, this will result in false precision!)
We'll use the US Major Cities dataset, which includes coordinates and 2020 population for cities with 10,000+ people. For each state, we calculate the fraction of people living in each of the state's cities, then use that to allocate the portions of the state's total energy to each city.

There are a bunch of assumptions built into this visualization.




### Energy Explorer

A dashboard to show & explore SEDS energy data by state, sector, and source over time.
