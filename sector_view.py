from ursina import Ursina, Entity, color, camera
from ursina.shaders import lit_with_shadows_shader

SHADER = False
MAX_ASTEROIDS = 24

from random import uniform
from typing import List

app = Ursina(size=(1024, 768), borderless=False)
camera.fov = 1

Entity(model='quad', texture='assets/stars.png', scale=250)

asteroids_in_sector: List[Entity] = []

for asteroids in range(MAX_ASTEROIDS):

    horizontal = 25
    vertical = 18
    offset_x, offset_y = uniform(-horizontal, horizontal), uniform(-vertical, vertical)

    shade = uniform(50, 100)
    nucleus = None
    for roids in range(50):
        size = uniform(0.5, 0.75)
        jiggle = [-0.5, 0.5]
        jiggled_position = (uniform(min(jiggle), max(jiggle)) + offset_x, 
                            uniform(min(jiggle), max(jiggle)) + offset_y, 
                            uniform(min(jiggle), max(jiggle)))

        clustoid = None

        if SHADER:
            clustoid = Entity(world_parent='scene', model='sphere', color=color.rgb(shade, shade, shade), 
                    scale=size, position=jiggled_position, 
                    shader=lit_with_shadows_shader)
        else:
            clustoid = Entity(world_parent='scene', model='sphere', color=color.rgb(shade, shade, shade), 
                    scale=size, position=jiggled_position)

        if clustoid != None:
            if nucleus == None:
                nucleus = clustoid
                nucleus.spin = uniform(-0.02, 0.02)
            else:
                # bond non-nucleus clustoids to nucleus
                clustoid.world_parent = nucleus

    asteroids_in_sector.append(nucleus)

def update():
    for asteroid in asteroids_in_sector:
        asteroid.rotation_z += asteroid.spin

while True:
    app.step()