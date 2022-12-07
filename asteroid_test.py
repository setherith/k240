from ursina import *
from random import uniform

width = 20
height = 20

app = Ursina()

red_button = Entity(model='quad', texture='resources/red_button.png', position=(0.0225,0.022,0), scale=0.004, parent=camera.ui)
blue_button = Entity(model='quad', texture='resources/blue_button.png', position=(0.0225,-0.022,0), scale=0.004, parent=camera.ui)

# generate star field...
import star_field
sf_width = 5000
sf_height = 5000
star_field.generate_stars(sf_width, sf_height)
background = Entity(model=Plane(), texture='stars.png', rotation=(0, 0, 0), position=(0, -5, 0), scale=200)
camera.fov = 20

# using cubes to represent asteroid as can't get the above piece to work correctly! (see: experimental_code.py)
for w in range(0, width):
    for h in range(0, height):
        size = int(uniform(1, 5))
        gray = int(uniform(50, 100))
        Entity(model='cube', scale_y=size, position=(w,0 - size / 2,h), color=color.rgb(gray, gray, gray))


#EditorCamera()
camera.rotation = Vec3(10, 225, 0)
camera.position = Vec3(25, 5, 25)
camera.orthographic = True

def update():
    if held_keys['d']:
        camera.rotation_y += time.dt * 40
    if held_keys['a']:
        camera.rotation_y -= time.dt * 40
    if held_keys['w']:
        camera.rotation_x += time.dt * 40
    if held_keys['s']:
        camera.rotation_x -= time.dt * 40

    # print (camera.rotation, camera.position)

app.run()