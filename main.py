from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 219,112,147 ]
edges = []
transform = new_matrix()

#dwsource
parse_file( 'script', edges, transform, screen, color )

#uncomment for boop script
#parse_file( 'boop', edges, transform, screen, color )

