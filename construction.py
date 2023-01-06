from csv import reader
from typing import List
from uuid import uuid1
from ursina import Vec3, Entity, Text, color, camera, destroy

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

    groups: dict[str, List[Entity]]

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
        self.groups = {}

    def load_buildings(self):
        with open('data/buildings.csv') as buildings_file:
            rows = reader(buildings_file)
            next(rows) # skipping header
            
            for row in rows:
                name, cost, hp, time, height, model, size = row

                # model checks
                if model == '':
                    model = 'cube'
                else:
                    model = 'assets/models/' + model

                building = Structure(name, int(cost), int(hp), int(time), int(height) + 1, model, int(size))
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
        # scale for different size buildings
        self.placement_tile.scale_x = self.building.size
        self.placement_tile.scale_y = self.building.size

        # position and visibility
        if target != None:
            self.placement_tile.visible = True
            
            # position offset for larger buildings
            if self.building.size == 2:
                self.placement_tile.set_position(Vec3(target.position.x + 0.5, target.position.y + target.scale_y / 2 + 0.01, target.position.z + 0.5))
            else:
                self.placement_tile.set_position(Vec3(target.position.x, target.position.y + target.scale_y / 2 + 0.01, target.position.z))
        else:
            self.placement_tile.visible = False

    def start_building(self):
        # calculate build time
        interval = int(self.building.build_time / self.building.scaffold_height)
        bt = 0

        # generate unique ID for scaffolding
        group = uuid1()

        # place staffolding in event queue
        for height in range(self.building.scaffold_height):
            if self.building.size == 2:
                for x in range(2):
                    for y in range(2):
                        self.events.add_event(self.place_model, Geom (
                            model='assets/models/ConstructionStruts.obj', 
                            texture='assets/texture.png', 
                            position=(self.placement_tile.position.x - 0.5 + x, height, self.placement_tile.position.z - 0.5 + y),
                            group=group
                            ), bt)
                        bt += interval / 4
            else:
                self.events.add_event(self.place_model, Geom (
                    model='assets/models/ConstructionStruts.obj', 
                    texture='assets/texture.png', 
                    position=(self.placement_tile.position.x, height, self.placement_tile.position.z),
                    group=group
                    ), bt)
                bt += interval

        # remove scaffolding immediately
        self.events.add_event(self.remove_scaffold, group, bt + 1)

        # replace with final building model
        self.events.add_event(self.place_model, Geom (
                model=self.building.model, 
                texture='assets/texture.png', 
                position=(self.placement_tile.position.x, 0, self.placement_tile.position.z)), 
                bt)

    def remove_scaffold(self, group: str):
        for scaffold in self.groups[group]:
            self.events.add_event(destroy, scaffold, 0)

    def place_model(self, geom: Geom):
        building = Entity(model=geom.model, texture=geom.texture, position=geom.position)
        if geom.group != None:
            if geom.group not in self.groups.keys():
                self.groups[geom.group] = []
            self.groups[geom.group].append(building)

    def tick(self):
        self.events.tick()

    @property
    def building(self) -> Structure:
        return self.structures[self.building_index]

    @property
    def is_valid(self) -> bool:
        return self.placement_tile.visible