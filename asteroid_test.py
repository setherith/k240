from ursina import *
from random import uniform

from camera import CameraControl

width = 20
height = 20

app = Ursina(size=(1024, 768), borderless=False)

# buttons...
buttons_left = []
y = 0.44
for count in range(5):
    red_button = Entity(model='quad', texture='resources/red_button.png', position=(0.59, y, 0), scale=(0.14, 0.07), parent=camera.ui)
    buttons_left.append(red_button)
    y -= 0.44 / 5

blue_button = Entity(model='quad', texture='resources/blue_button.png', position=(0.59, -0.42, 0), scale=(0.14, 0.07), parent=camera.ui)

# date...
eons = 2
years = 380
days = 1
date_text = Text(f'E{int(eons)}.{int(years):003}.{int(days):002}', origin=(-0.75, 0.5))
date_entity = Entity(model=date_text, parent=camera.ui, position=(0.50, -0.465, 0))

# generate star field...
import star_field
sf_width = 5000
sf_height = 5000
star_field.generate_stars(sf_width, sf_height)
background = Entity(model=Plane(), texture='stars.png', rotation=(0, 0, 0), position=(0, -5, 0), scale=200)

# using cubes to represent asteroid as can't get the above piece to work correctly! (see: experimental_code.py)
for w in range(0, width):
    for h in range(0, height):
        size = int(uniform(1, 5))
        gray = int(uniform(50, 100))
        Entity(model='cube', scale_y=size, position=(w,0 - size / 2,h), color=color.rgb(gray, gray, gray))

# test object for camera...
test = Entity(model='cube', color=color.blue, position=(5, 0, 5), scale=1)

counter = 0
camera_controls = CameraControl(camera)

while True:

    counter += time.dt
    
    # tick...
    if counter > 1:
        # update date in game...
        days += 0.5
        if days == 100:
            years += 1
            days = 1
        if years == 1000:
            eons += 1
            years = 1
        if days % 1 == 0:
            date_text.text = f'E{int(eons)}.{int(years):003}.{int(days):002}'

        counter = 0

    # camera control...
    if held_keys['d']:
        camera_controls.turn_right()
    if held_keys['a']:
        camera_controls.turn_left()

    app.step()