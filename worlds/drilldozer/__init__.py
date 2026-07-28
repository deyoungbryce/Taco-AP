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
from .locations import location_table, DrillDozerLocation, DrillDozerLocationData
from .options import DrillDozerGameOptions


class DrillDozerWeb(WebWorld):
    theme: str = ""
    game: str = "Drill Dozer"


class DrillDozerWorld(World):
    game = "Drill Dozer"
    web = DrillDozerWeb()

    options_dataclass = DrillDozerGameOptions
    options: DrillDozerGameOptions