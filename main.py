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

add_box(transform, 200, 200, 0, 50,50,100)

boop = make_rotZ(50)
matrix_mult(boop, transform)
boop = make_rotX(50)
matrix_mult(boop, transform)
draw_lines(transform, screen, color)
print_matrix(transform)


#add_sphere(transform, 100, 100, 0, 50, .001)
#add_torus( points, cx, cy, cz, r0, r1, step )
add_torus(transform, 100, 100, 0, 5, 10, .001)
draw_lines(transform, screen, color)
print_matrix(transform)
save_extension(screen, 'boop.png')
display(screen)

#parse_file( 'script', edges, transform, screen, color )
