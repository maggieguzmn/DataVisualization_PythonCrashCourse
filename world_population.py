import json

import pygal_maps_world.maps as pgmaps

from country_codes import get_country_code

# Load the data into a list.
filename = 'data/population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
    
# Build a dictionary of population data
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
            
wm = pgmaps.World()
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_populations)

wm.render_to_file('world_population.svg')
            