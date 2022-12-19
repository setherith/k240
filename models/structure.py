from abc import abstractmethod
from states import PlantState

class Structure:

    health: int
    max_health: int
    level: int = 1
    multiplier: float = 1.1
    state: PlantState = PlantState.BUILDING

    def __init__(self, hp: int):
        self.max_health = hp
        self.health = hp

    @abstractmethod
    def proc(self, value: float) -> float:
        if self.health < (0.25 * self.max_health):
            self.state = PlantState.DAMAGED
            return value * 0.5

        if self.state == PlantState.OPERATIONAL:
            return value

        return 0.0