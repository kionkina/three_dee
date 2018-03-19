from display import *
from matrix import *
from math import *

def add_box( points, x, y, z, width, height, depth ):
    h = height
    w = width
    d = depth
    # front face
    add_edge(points, x,y,z, x, y-h, z)
    add_edge(points, x, y-h, z, x+w, y-h, z)
    add_edge(points, x+w, y-h, z, x+w, y, z)
    add_edge(points, x,y,z, x+w, y, z)
    #depth edges
    add_edge(points, x,y,z, x, y, z+d)
    add_edge(points, x+w, y, z, x+w, y, z+d)
    add_edge(points, x, y-h, z, x,y-h,z+d)
    add_edge(points, x+w, y-h, z, x+w, y-h, z+d)
    #back face
    add_edge(points, x,y,z+d, x+w, y, z+d)
    add_edge(points,x+w,y,z+d, x+w, y-h, z+d)
    add_edge(points,x+w, y-h, z+d, x, y-h, z+d)
    add_edge(points,x, y-h, z+d, x,y,z+d)

    
def add_sphere( points, cx, cy, cz, r, step ):
    # theta is the angle of circle creation 0 --> 2pi
    # phi is the angle of circle rotation 0 --> phi
    theta = 0
    phi = 0
    while (phi < 2*math.pi):
        while (theta < pi):
            x = r*math.cos(theta*2*math.pi) + cx
            y = r*math.sin(theta*2*math.pi)*cos(phi) + cy
            z = r*math.sin(theta*2*math.pi)*sin(phi) + cz
            theta += step
            add_point(points, x, y, z)
        phi += step
    



def generate_sphere( points, cx, cy, cz, r, step ):
    pass
    
#r0 is inner circle radius
#r1 is tube radius
def add_torus( points, cx, cy, cz, r0, r1, step ):
    phi = 0
    theta = 0
    while (phi < 2*math.pi):
        while (theta < 2*math.pi):
            x = (r0 + r1*math.cos(theta))*math.cos(phi)
            y = (r0 + r1*math.cos(theta))*math.sin(phi)
            z = r1*math.sin(theta)
            theta += step
            add_point(points, x,y,z)
        phi += step
        



def generate_torus( points, cx, cy, cz, r0, r1, step ):
    pass

def add_circle( points, cx, cy, cz, r, step ):
    x0 = r + cx
    y0 = cy
    i = 1
    while i <= step:
        t = float(i)/step
        x1 = r * math.cos(2*math.pi * t) + cx;
        y1 = r * math.sin(2*math.pi * t) + cy;

        add_edge(points, x0, y0, cz, x1, y1, cz)
        x0 = x1
        y0 = y1
        i+= 1

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):

    xcoefs = generate_curve_coefs(x0, x1, x2, x3, curve_type)[0]
    ycoefs = generate_curve_coefs(y0, y1, y2, y3, curve_type)[0]

    i = 1
    while i <= step:
        t = float(i)/step
        x = xcoefs[0] * t*t*t + xcoefs[1] * t*t + xcoefs[2] * t + xcoefs[3]
        y = ycoefs[0] * t*t*t + ycoefs[1] * t*t + ycoefs[2] * t + ycoefs[3]

        add_edge(points, x0, y0, 0, x, y, 0)
        x0 = x
        y0 = y
        i+= 1

def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print 'Need at least 2 points to draw'
        return
    
    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)    
        point+= 2
        
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)
    
def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )
    



def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:            
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
