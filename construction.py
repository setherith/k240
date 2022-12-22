from os import listdir
from typing import List
from ursina import Vec3, Entity, Text, color, camera

class ConstructionControl:
    """
    Handles the currently selected building type on the UI
    """

    models: List[str]
    placement_tile: Entity
    current_building: Entity
    building_index: int
    building_number: Text

    def __init__(self):
        self.models = listdir('assets/models')

        self.building_index = 0
        self.placement_tile = Entity(model='quad', color=color.rgb(0, 153, 255), rotation=(90, 0, 0))

        self.current_building = Entity(parent=camera.ui, scale=0.05, \
                                        rotation=Vec3(-20, 45, 19), position=(0.59, -0.34, 0), \
                                        model=self.models[self.building_index], \
                                        texture='assets/texture.png')

        self.building_number = Text(parent=camera.ui, scale=1.5, 
                                    text=self.building_index + 1, position=(0.58, -0.405, 0))

    def next_building(self):
        """Select the next available building"""
        self.building_index += 1
        if self.building_index > len(self.models) - 1:
            self.building_index = 0
        self.update_model_view()

    def previous_building(self):
        """Select the previous available building"""
        self.building_index -= 1
        if self.building_index < 0:
            self.building_index = len(self.models) - 1
        self.update_model_view()

    def update_model_view(self):
        self.building_number.text = self.building_index + 1
        self.current_building.model = self.models[self.building_index]

    def update_placement_tile(self, target: Entity | None):
        if target != None:
            self.placement_tile.visible = True
            self.placement_tile.set_position(Vec3(target.position.x, target.position.y + target.scale_y / 2 + 0.01, target.position.z))
        else:
            self.placement_tile.visible = False

    def place_building(self):
        Entity(model=self.models[self.building_index], texture='assets/texture.png', \
                position=(self.placement_tile.position.x, 0, self.placement_tile.position.z))

    @property
    def is_valid(self) -> bool:
        return self.placement_tile.visible