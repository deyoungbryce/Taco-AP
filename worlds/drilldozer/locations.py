from typing import Dict, List, NamedTuple, Set, Optional
from BaseClasses import Location

from .options import DrillDozerGameOptions


class DrillDozerLocation(Location):
    game: str = "Drill Dozer"

location_base_id: int = 431732704

class DrillDozerLocationData(NamedTuple):
    region: str
    location_id_offset: int
    location_group: Optional[str] = None


location_table: Dict[str, DrillDozerLocationData] = {
    
}

location_name_to_id: Dict[str, int] = {}

for name, data in location_table.items():
    if data.location_id_offset != None:
        location_name_to_id.update({name:data.location_id_offset + location_base_id})

def get_location_group(location_name: str) -> str:
    return location_table[location_name].location_group