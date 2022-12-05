from ursina import *
from PIL import Image
from random import uniform

width = 20
height = 20

app = Ursina()

# generate star field...
import star_field
sf_width = 1920
sf_height = 1080
star_field.generate_stars(sf_width, sf_height)
background = Entity(model=Plane(), texture='stars.png', rotation=(0, 0, 0), position=(0, -5, 0), scale=100)
camera.clip_plane_near = 0

# using cubes to represent asteroid as can't get the above piece to work correctly! (see: experimental_code.py)
for w in range(0, width):
    for h in range(0, height):
        size = int(uniform(1, 5))
        gray = int(uniform(50, 100))
        Entity(model='cube', scale_y=size, position=(w,0 - size / 2,h), color=color.rgb(gray, gray, gray))

EditorCamera()
camera.orthographic = True
camera.rotate((45, 45, 0))
camera.z = -5

def update():
    print(camera.rotation)

app.run()