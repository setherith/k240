from csv import reader
from typing import List
from ursina import Vec3, Entity, Text, color, camera

from models.structure import Structure, Geom
from game_time import EventManager

class ConstructionControl:
    """
    Handles the currently selected building type on the UI
    """

    events: EventManager

    structures: List[Structure]
    placement_tile: Entity
    current_building: Entity
    building_index: int
    building_number: Text

    def __init__(self):

        self.structures = []
        self.load_buildings()

        self.building_index = 0
        self.placement_tile = Entity(model='quad', color=color.rgb(0, 153, 255), rotation=(90, 0, 0))

        self.current_building = Entity(parent=camera.ui, scale=0.05, \
                                        rotation=Vec3(-20, 45, 19), position=(0.59, -0.34, 0), \
                                        model=self.building.model, \
                                        texture='assets/texture.png')

        self.building_number = Text(parent=camera.ui, scale=1.5, 
                                    text=self.building_index + 1, position=(0.58, -0.405, 0))

        self.events = EventManager()

    def load_buildings(self):
        with open('data/buildings.csv') as buildings_file:
            rows = reader(buildings_file)
            next(rows) # skipping header
            
            for row in rows:
                name, cost, hp, time, height, model = row

                # model checks
                if model == '':
                    model = 'cube'
                else:
                    model = 'assets/models/' + model

                building = Structure(name, int(cost), int(hp), int(time), int(height) + 1, model)
                self.structures.append(building)

    def next_building(self):
        """Select the next available building"""
        self.building_index += 1
        if self.building_index > len(self.structures) - 1:
            self.building_index = 0
        self.update_model_view()

    def previous_building(self):
        """Select the previous available building"""
        self.building_index -= 1
        if self.building_index < 0:
            self.building_index = len(self.structures) - 1
        self.update_model_view()

    def update_model_view(self):
        self.building_number.text = self.building_index + 1
        self.current_building.model = self.building.model

    def update_placement_tile(self, target: Entity | None):
        if target != None:
            self.placement_tile.visible = True
            self.placement_tile.set_position(Vec3(target.position.x, target.position.y + target.scale_y / 2 + 0.01, target.position.z))
        else:
            self.placement_tile.visible = False

    def start_building(self):
        # calculate build time
        interval = int(self.building.build_time / self.building.scaffold_height)
        bt = 0

        # place staffolding in event queue
        for height in range(self.building.scaffold_height):
            self.events.add_event(self.place_model, Geom (
                model='assets/models/ConstructionStruts.obj', 
                texture='assets/texture.png', 
                position=(self.placement_tile.position.x, height, self.placement_tile.position.z))
                , bt)
            bt += interval

        # remove scaffolding immediately


        # replace with final building model

    def place_model(self, geom: Geom):
        Entity(model=geom.model, texture=geom.texture, position=geom.position)

    def tick(self):
        self.events.tick()

    @property
    def building(self) -> Structure:
        return self.structures[self.building_index]

    @property
    def is_valid(self) -> bool:
        return self.placement_tile.visible