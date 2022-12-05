from ursina import *
from PIL import Image
from random import uniform

width = 20
height = 20

# img = Image.new(mode="RGB", size=(width, height))

# for w in range(0, width):
#     for h in range(0, height):
#         grade = int(uniform(100, 150))
#         img.putpixel((w, h), (grade, grade, grade))

# img.save('terrain.png')

app = Ursina()

asteroid_terrain = Terrain(heightmap='terrain.png', skip=1)
terrain_entity = Entity(model=asteroid_terrain, texture='terrain.png', rotation=Vec3(180, 45, 0), position=(0, 0.39, 0))

top_layer = Plane(subdivisions=(width, height), mode='triangle')
build_entity = Entity(model=top_layer, color=color.red, rotation=Vec3(0, 45, 0))

EditorCamera()

app.run()