from ursina import Ursina, Entity, Mesh, DirectionalLight
from ursina import EditorCamera, color
from ursina.shaders import lit_with_shadows_shader

from math import sin

app = Ursina(size=(1024, 768), borderless=False)

v = []

for x in range(0, 100):
    for z in range(0, 100):
        h = sin(x) * 0.25 + sin(z) * 0.25
        i = sin(x + 1) * 0.25 + sin(z) * 0.25
        j = sin(x) + 0.25 + sin(z + 1) * 0.25
        v.append((x,h,z))
        v.append((x+1,i,z))
        v.append((x+1,i,z+1))
        v.append((x+1,i,z+1))
        v.append((x,h,z+1))
        v.append((x,h,z))

floor = Entity(position=(-50,0,-50), model=Mesh(vertices=v), shader=lit_with_shadows_shader, color=color.gray)

camera = EditorCamera()
camera.set_position((0, 15, 0))
pivot = Entity()
DirectionalLight(parent=pivot, y=2, z=3, shadows=True, rotation=(45, -45, 45))

app.run()