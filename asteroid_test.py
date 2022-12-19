from ursina import *

from random import uniform

from camera import CameraControl
from construction import ConstructionControl
from game_time import Stardate

width = 20
height = 20

app = Ursina(size=(1024, 768), borderless=False)

# buttons...
buttons_left = []
y = 0.44
for count in range(5):
    red_button = Entity(model='quad', texture='assets/red_button.png', position=(0.59, y, 0), scale=(0.14, 0.07), parent=camera.ui)
    buttons_left.append(red_button)
    y -= 0.44 / 5

blue_button = Entity(model='quad', texture='assets/blue_button.png', position=(0.59, -0.42, 0), scale=(0.14, 0.07), parent=camera.ui)

example_building = Entity(model='assets/models/shipyard.obj', texture='assets/texture.png', position=(3.5, 0, 3.5))

# construction controls (view and logic)
construction_controls = ConstructionControl()

# in game time mechanics
game_time = Stardate()

# generate star field...
import star_field
sf_width = 5000
sf_height = 5000
star_field.generate_stars(sf_width, sf_height)
Sky(texture='assets/stars.png', scale=50)

# using cubes to represent asteroid as can't get the above piece to work correctly! (see: experimental_code.py)
for w in range(0, width):
    for h in range(0, height):
        size = int(uniform(1, 5))
        gray = int(uniform(50, 100))
        
        # erode the edges of the asteroid
        errosion_factor = 3
        if w < errosion_factor or w > width - errosion_factor or h > height - errosion_factor or h < errosion_factor:
            if random.uniform(0, 1) > 0.8:
                Entity(model='cube', scale_y=size, position=(w,0 - size / 2,h), color=color.rgb(gray, gray, gray), collider='box')
        else:
            # stability of asteroid
            stability_factor = 90
            if random.uniform(0, 100) < stability_factor:
                Entity(model='cube', scale_y=size, position=(w,0 - size / 2,h), color=color.rgb(gray, gray, gray), collider='box')

counter = 0
camera_controls = CameraControl(camera)

while True:

    counter += time.dt
    if counter > 1:
        game_time.tick()
        counter = 0

    # camera control
    if held_keys['w']:
        camera_controls.tilt_up()
    if held_keys['s']:
        camera_controls.tilt_down()
    if held_keys['d']:
        camera_controls.turn_right()
    if held_keys['a']:
        camera_controls.turn_left()

    # detect hover for building placement
    construction_controls.update_placement_tile(mouse.hovered_entity)

    def input(keys):
        # mouse input for camera
        if keys == 'scroll up': 
            camera_controls.zoom_out()
        if keys == 'scroll down': 
            camera_controls.zoom_in()

        # construction view controls
        if keys == '[':
            construction_controls.previous_building()
        if keys == ']':
            construction_controls.next_building()

    app.step()