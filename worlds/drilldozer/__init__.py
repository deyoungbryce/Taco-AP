import math
import settings
import typing
import logging

from BaseClasses import ItemClassification, Region, CollectionState, MultiWorld
from worlds.AutoWorld import WebWorld, World
from typing import Dict, List, Any
from Utils import visualize_regions
from Fill import fill_restrictive

from .items import item_table, DrillDozerItem, DrillDozerItemData
from .locations import location_table, location_name_to_id, DrillDozerLocation, DrillDozerLocationData
from .regions import drilldozer_regions
from .options import DrillDozerGameOptions


class DrillDozerWeb(WebWorld):
    theme: str = ""
    game: str = "Drill Dozer"


class DrillDozerWorld(World):
    game = "Drill Dozer"
    web = DrillDozerWeb()

    options_dataclass = DrillDozerGameOptions
    options: DrillDozerGameOptions


    def create_regions(self):

        for region_name in drilldozer_regions:
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        for region_name, exits in drilldozer_regions.items():
            region = self.multiworld.get_region(region_name, self.player)
            region.add_exits(exits)

        regions_to_exclude = []

        for location_name, location_id in location_name_to_id.items():
            if location_table[location_name].region not in regions_to_exclude:
                region = self.multiworld.get_region(location_table[location_name].region, self.player)
                location = DrillDozerLocation(self.player, location_name, location_id, region)
                region.locations.append(location)