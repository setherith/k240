from random import uniform
from ursina import Entity, color

from random import choice
from string import ascii_uppercase, digits

class Asteroid:
    """Generates asteroids"""

    height: int
    width: int
    name: str = ''

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        for w in range(0, self.width):
            for h in range(0, self.height):
                size = int(uniform(1, 5))
                gray = int(uniform(50, 100))
                
                # erode the edges of the asteroid
                errosion_factor = 3
                if w < errosion_factor or w > self.width - errosion_factor or h > self.height - errosion_factor or h < errosion_factor:
                    if uniform(0, 1) > 0.8:
                        Entity(model='cube', scale_y=size, position=(w,0 - size / 2,h), color=color.rgb(gray, gray, gray), collider='box')
                else:
                    # stability of asteroid
                    stability_factor = 90
                    if uniform(0, 100) < stability_factor:
                        Entity(model='cube', scale_y=size, position=(w,0 - size / 2,h), color=color.rgb(gray, gray, gray), collider='box')
        
        # name it
        self.generate_name()
        print (self.name)

    def generate_name(self):
        for l in range(10):
            if choice([0, 1]) == 1:
                self.name += choice(ascii_uppercase)
            else:
                self.name += choice(digits)