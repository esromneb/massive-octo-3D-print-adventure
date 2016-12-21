from solid import *
d = difference()(
    cube(10),
    sphere(15)
)
print(scad_render(d))

