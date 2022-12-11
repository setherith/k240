import math
from ursina.camera import Camera
from ursina import Vec3

class CameraControl:

    camera: Camera
    angle: float
    radius: float

    camera_speed: float = 0.01
    initial_angle: float = 90
    initial_radius: float = 5

    def __init__(self, camera: Camera):
        self.camera = camera
        self.angle = self.initial_angle
        self.radius = self.initial_radius

        # camera setup...
        self.camera.fov = 25
        self.camera.orthographic = True
        self.camera.rotation = Vec3(30, 225, 0)
        self.camera.position = Vec3(25, 12, 25)

    def turn_left(self):
        self.angle -= self.camera_speed
        self.update()

    def turn_right(self):
        self.angle += self.camera_speed
        self.update()

    def update(self):
        x = self.radius * math.sin(self.angle)
        y = self.radius * math.cos(self.angle)
        self.camera.set_position(Vec3(x, self.camera.position.y, y))
