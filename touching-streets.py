# script for getting the names of connecting streets for each centreline
# also computes the length of each street

import pandas as pd
import geopandas as gpd
import numpy as np

dfs = gpd.read_file('data/centreline/Centreline - Version 2.geojson')

dfs["connecting_streets"] = None  

i = 0

for index, street in dfs.iterrows():

    # get touching streets
    constr = dfs[dfs.geometry.touches(street.geometry)].LINEAR_NAME_FULL.tolist()

    # remove own name of the country from the list
    constr = [ name for name in constr if street.LINEAR_NAME_FULL != name ]
    
    # remove duplicates
    constr = list(set(constr))

    # add names of neighbors as NEIGHBORS value
    dfs.at[index, "connecting_streets"] = ", ".join(constr)
    
    i+=1
    
    if i % 100 == 0:
        print(i)
        
# also compute length for each centreline
dfs.geometry = dfs.geometry.to_crs('epsg:32617')
dfs["length"] = dfs.geometry.length.astype(int)
dfs.geometry = dfs.geometry.to_crs('epsg:4326')

print(dfs)

# save as a new file
dfs.to_file('data/centreline/centreline-with-connections.geojson')
    