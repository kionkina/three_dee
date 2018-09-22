# Work 6
add the following commands to the parser
* clear: clears the edge matrix of all points
* box: adds a rectangular prism (box) to the edge matrix - takes 6 parameters (x, y, z, width, height, depth)
* sphere: adds a sphere to the edge matrix - takes 4 parameters (x, y, z, radius)
* torus: adds a torus to the edge matrix - takes 5 parameters (x, y, z, radius1, radius2)
* radius1 is the radius of the circle that makes up the torus
* radius2 is the full radius of the torus (the translation factor). You can think of this as the distance from the center of the torus to the center of any circular slice of the torus.
You should actually add edges to draw the box.
* For the sphere and torus, just add the points (for each point on the surface, and an edge from it to a point 1 pixel away to make it easier to see.
