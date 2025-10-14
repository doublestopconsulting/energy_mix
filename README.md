# energy_mix
Explore US energy data

## Data sources

- [State Energy Data System](https://www.eia.gov/state/seds/seds-data-complete.php?sid=US#CompleteDataFile) [SEDS] from the US Energy Information Administration.
- [This site](https://geojson-maps.kyd.au) to download world geojson
- US states downloaded from [natural earth](https://www.naturalearthdata.com/downloads/110m-cultural-vectors/110m-admin-1-states-provinces/)
- US Major Cities, downloaded from [ESRI/ArcGIS](https://hub.arcgis.com/datasets/esri::usa-major-cities-3/explore)

## Initial ideas
- Create a heatmap of energy consumption that evolves over time -- getting brighter as energy consumption increases. See if we can come up with something to mimic the "lights at night" images, like those found on this [NASA Earth Observatory site](https://earthobservatory.nasa.gov/features/NightLights).
  - Use the "TETCB" data in SEDS -- total energy consumption in billion BTU for each state
  - See `energy_night_lights.py` for a work in progress
  - Meant to be an artistic rendering
- A dashboard to show & explore energy data by state, sector, and source
