from PIL import Image
from random import uniform
from os.path import exists

def generate_stars(width, height):

    if exists('stars.png'):
        return

    stars = Image.new(mode="RGB", size=(width, height))
    for x in range(width):
        for y in range(height):
            if uniform(0, 1) > 0.999:
                stars.putpixel((x,y), (int(uniform(100, 150)), int(uniform(100, 150)), int(uniform(100, 150))))

    stars.save('stars.png')