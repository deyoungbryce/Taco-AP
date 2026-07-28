import typing

from BaseClasses import Region, MultiWorld, Location, Entrance


class DrillDozerRegion(Region):
    game: str = "Drill Dozer"

def create_regions(world: MultiWorld, player: int):
    menu_region = Region("Menu", player, world, "Stage Select")
    world.regions.append(menu_region)