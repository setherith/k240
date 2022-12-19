from PIL import Image
from random import uniform
from os.path import exists
from ursina import Sky

class Background:

    width: int
    height: int

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        
        self.generate_stars()
        Sky(texture='assets/stars.png', scale=50)

    def generate_stars(self):

        if exists('assets/stars.png'):
            return

        stars = Image.new(mode="RGB", size=(self.width, self.height))
        for x in range(self.width):
            for y in range(self.height):
                if uniform(0, 1) > 0.999:
                    stars.putpixel((x,y), (int(uniform(100, 150)), int(uniform(100, 150)), int(uniform(100, 150))))

        stars.save('stars.png')