from ursina import Ursina, Entity, Mesh
from ursina import EditorCamera

from random import uniform

app = Ursina(size=(1024, 768), borderless=False)

v = []

for x in range(0, 100):
    for z in range(0, 100):
        h = uniform(-1, 1)
        v.append((x,h,z))
        v.append((x+1,h,z))
        v.append((x+1,h,z+1))
        v.append((x+1,h,z+1))
        v.append((x,h,z+1))
        v.append((x,h,z))

floor = Entity(position=(-50,0,-50), model=Mesh(vertices=v))

camera = EditorCamera()
camera.set_position((0, 15, 0))

app.run()