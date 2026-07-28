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