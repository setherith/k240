import math
from ursina.camera import Camera
from ursina import Vec3

class CameraControl:

    camera: Camera
    angle: float
    radius: float
    tilt: float

    camera_speed: float = 0.01
    initial_angle: float = 0.7 # Radians?
    initial_radius: float = -16
    initial_tilt: float = 15

    fov_min: int = 0
    fov_max: int = 50

    def __init__(self, camera: Camera):
        self.camera = camera
        self.angle = self.initial_angle
        self.radius = self.initial_radius
        self.tilt = self.initial_tilt

        # camera setup...
        self.camera.position = (self.camera.position.x, 5, self.camera.position.z)
        self.camera.fov = 25
        self.camera.orthographic = True
        self.camera.rotation = Vec3(0, 0, 0)
        self.update()

    def turn_left(self):
        self.angle -= self.camera_speed
        self.update()

    def turn_right(self):
        self.angle += self.camera_speed
        self.update()

    def zoom_out(self):
        if self.camera.fov > self.fov_min:
            self.camera.fov -= 1
        self.update()

    def zoom_in(self):
        if self.camera.fov < self.fov_max:
            self.camera.fov += 1
        self.update()

    def tilt_up(self):
        self.tilt += 1
        self.update()

    def tilt_down(self):
        self.tilt -= 1
        self.update()

    def update(self):
        x = self.radius * math.sin(self.angle) + 10
        y = self.radius * math.cos(self.angle) + 10
        self.camera.set_position(Vec3(x, self.camera.position.y, y))
        self.camera.rotation_y = math.degrees(self.angle)
        self.camera.rotation_x = self.tilt
        print (f"Pos: {self.camera.position}, Rot: {self.camera.rotation}, FOV: {self.camera.fov}")