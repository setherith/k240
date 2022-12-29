from abc import abstractmethod
from models.states import PlantState

class Structure:

    name: str
    cost: int
    health: int
    max_health: int
    build_time: int
    scaffold_height: int
    model: str

    level: int = 1
    multiplier: float = 1.1
    state: PlantState = PlantState.BUILDING

    def __init__(self, name: str, cost: int, hp: int, time: int, height: int, model: str):
        self.cost = cost
        self.name = name
        self.max_health = hp
        self.health = hp
        self.build_time = time
        self.scaffold_height = height
        self.model = model

    @abstractmethod
    def proc(self, value: float) -> float:
        if self.health < (0.25 * self.max_health):
            self.state = PlantState.DAMAGED
            return value * 0.5

        if self.state == PlantState.OPERATIONAL:
            return value

        return 0.0

class Geom:

    model: str
    texture: str
    position: tuple
    group: str

    def __init__(self, model: str, texture: str, position: tuple, group: str = None):
        self.model = model
        self.texture = texture
        self.position = position
        self.group = group