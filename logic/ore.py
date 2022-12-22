from random import uniform
from typing import Dict, List

class OreConfig:

    name: str
    chance: float
    minimum: int
    maximum: int
    home_value: int

    def __init__(self, name: str, chance: float, min: int, max: int, start: int):
        self.name = name
        self.chance = chance
        self.minimum = min
        self.maximum = max
        self.home_value = start

class Ore:
    """
    A class for handling all aspects of Ore in the game
    """

    OreConfigs: List[OreConfig] = []

    def __init__(self):
        # load ore configuration from file
        with open('data/ore.csv', 'r') as ore_file:
            lines = ore_file.readlines()
            for line in lines[1:]:
                values = line.strip().split(',')
                n, c, mn, mx, s = values
                ore_config = OreConfig(n, float(c), int(mn), int(mx), int(s))
                self.OreConfigs.append(ore_config)

    def generate_ore_for_asteroid(self, starting_asteroid: bool) -> Dict[str, int]:

        ore_available: Dict[str, int] = {}

        if starting_asteroid:
            for config in self.OreConfigs:
                ore_available[config.name] = config.home_value
        else:
            for config in self.OreConfigs:
                if uniform(0, 1) < config.chance:
                    ore_available[config.name] = int(uniform(config.minimum, config.maximum))
                else:
                    ore_available[config.name] = 0

        return ore_available