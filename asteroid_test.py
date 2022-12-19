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
    red_button = Entity(model='quad', texture='assets/red_button.png', position=(0.59, y, 0), scale=(0.14, 0.07), parent=camera.ui)
    buttons_left.append(red_button)
    y -= 0.44 / 5

blue_button = Entity(model='quad', texture='assets/blue_button.png', position=(0.59, -0.42, 0), scale=(0.14, 0.07), parent=camera.ui)

example_building = Entity(model='models_compressed/shipyard.obj', texture='models_compressed/texture.png', position=(3.5, 0, 3.5))

current_selected_building = Entity(parent=camera.ui, scale=0.05, \
                                    rotation=Vec3(-20, 45, 19), position=(0.58, -0.2, 0), \
                                    model='models_compressed/StorageTower.obj', \
                                    texture='models_compressed/texture.png')

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

building_placement_tile = Entity(model='quad', color=color.cyan, rotation=(90, 0, 0))

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
    if held_keys['w']:
        camera_controls.tilt_up()
    if held_keys['s']:
        camera_controls.tilt_down()
    if held_keys['d']:
        camera_controls.turn_right()
    if held_keys['a']:
        camera_controls.turn_left()

    # detect hover for building placement
    entity: Entity = mouse.hovered_entity
    if entity != None:
        building_placement_tile.visible = True
        building_placement_tile.set_position(Vec3(entity.position.x, entity.position.y + entity.scale_y / 2 + 0.01, entity.position.z))
    else:
        building_placement_tile.visible = False

    # mouse input for camera
    def input(keys):
        if keys == 'scroll up': 
            camera_controls.zoom_out()
        if keys == 'scroll down': 
            camera_controls.zoom_in()

    app.step()