# Name: Team 19 Wild Fire Model
# Dimensions: 2
# --- Set up executable path, do not edit ---
import sys
import inspect
this_file_loc = (inspect.stack()[0][1])
main_dir_loc = this_file_loc[:this_file_loc.index('ca_descriptions')]
sys.path.append(main_dir_loc)
sys.path.append(main_dir_loc + 'capyle')
sys.path.append(main_dir_loc + 'capyle/ca')
sys.path.append(main_dir_loc + 'capyle/guicomponents')
# ---

from capyle.ca import Grid2D, Neighbourhood, CAConfig, randomise2d
import capyle.utils as utils
import numpy as np 
import math


#The function to assign fuel parameter to a cell depending
#on the type of terrain it is representing. 
#takes an array as an iput and returns the array with updated values.
def construct_fuel_parameters(grid):

    fuel_grid=np.zeros(grid.shape)
    
    #assign fuel parameter depending on the variety of 
    #the cell according to the terrain.
    # terrain types:
    # 0 - chaparral
    # 1 - canyon
    # 2 - forest
    # 3 - lake
    # 4 - town
    chap=(grid == 0)
    fuel_grid[chap]=28

    canyon=(grid == 1)
    fuel_grid[canyon]=3

    forest=(grid == 2)
    fuel_grid[forest]=120

    lake=(grid == 3)
    fuel_grid[lake]=-1

    town=(grid == 4)
    fuel_grid[town]=5
   
    return fuel_grid

