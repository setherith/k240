from ursina import Text, Entity, camera

class Stardate:
    """
    A class for handling the flows of time in the game (set in the future...)
    """

    eons = 2
    years = 380
    days = 1

    def __init__(self):
        self.date_text = Text(f'E{int(self.eons)}.{int(self.years):003}.{int(self.days):002}', origin=(-0.75, 0.5))
        self.date_entity = Entity(model=self.date_text, parent=camera.ui, position=(0.50, -0.465, 0))

    def tick(self):
        """Tick from game advances game clock by 0.5 day"""
        self.days += 0.5
        if self.days == 100:
            self.years += 1
            self.days = 1
        if self.years == 1000:
            self.eons += 1
            self.years = 1
        if self.days % 1 == 0:
            self.date_text.text = f'E{int(self.eons)}.{int(self.years):003}.{int(self.days):002}'