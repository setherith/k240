from structure import Structure

class Mine(Structure):

    production_rate: int = 1
    base_rate: int = 100

    def __init__(self):
        super(500)

    def proc(self) -> float:
        return super().proc(self.base_rate + (self.level - 1) * self.multiplier * self.production_rate)