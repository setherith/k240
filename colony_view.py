from ursina import Ursina, Entity, time, held_keys
from ursina import camera, mouse

from camera import CameraControl
from construction import ConstructionControl
from game_time import Stardate
from star_field import Background
from asteroid import Asteroid

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

# generate star field
Background(5000, 5000)

# using cubes to represent asteroid as can't get the above piece to work correctly! (see: experimental_code.py)
Asteroid(20, 20)

# set up camera controls
camera_controls = CameraControl(camera)

ticks = 0

while True:

    ticks += time.dt
    if ticks > 1:
        game_time.tick()
        ticks = 0

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

        # build structure
        if keys == 'left mouse down' and construction_controls.is_valid:
            construction_controls.place_building()

        # construction view controls
        if keys == '[':
            construction_controls.previous_building()
        if keys == ']':
            construction_controls.next_building()

    app.step()