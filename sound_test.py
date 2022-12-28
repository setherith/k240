from ursina import *

app = Ursina()

Audio('/resources/galaxia_resources/sfx/ping.wav')

Text('our computers have been tampered with!', font='assets/yearone.ttf')

app.run()