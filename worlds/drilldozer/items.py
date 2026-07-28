from itertools import groupby
from typing import Dict, List, Set, NamedTuple
from BaseClasses import ItemClassification, Item


class DrillDozerItem(Item):
    game: str = "Drill Dozer"

item_base_id: int = 431732704

class DrillDozerItemData(NamedTuple):
    classification: ItemClassification
    item_id_offset: int
    item_group: str = ""


item_table: Dict[str, DrillDozerItemData] = {
    
}