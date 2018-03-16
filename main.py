from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

# print_matrix( make_bezier() )
# print
# print_matrix( make_hermite() )
# print

add_box(5,5,10)
save_extension(screen, 'boop.png')
display(screen)

#parse_file( 'script', edges, transform, screen, color )
