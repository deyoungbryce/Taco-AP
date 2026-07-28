from dataclasses import dataclass
from Options import Toggle, Range, Choice, PerGameCommonOptions


class Goal(Choice):
    display_name: str = "Goal"

class GearRando(Choice):
    """Choose how gears will be randomized into the multiworld
    Gears will always be progressive unlocks, but there are options for how restrictive the progression will be
    - Per Stage: Each gear unlock is tied to a specific stage. For example, you could recieve 'Progressive Gear - Sculker Hideout' which would allow you to obtain and use the first gear in any of the Sculker Hideout levels
    - Per Level: Each gear unlock is tied to an individual level. Example is the same as 'Per Stage', however the gear unlock would come in the form of 'Progressive Gear - Sculker Hideout Level 1'
    - Progressive: Each gear unlock is progressive across the entire game. If you recieve a progressive gear unlock you can then use that gear in any level"""
    display_name: str = "Gear Randomization"
    option_per_stage = 0
    option_per_level = 1
    option_progressive = 2
    default = 0

class LevelRando(Choice):
    """Choose how levels will be randomized into the multiworld
    - Stages: Levels are unlocked by stage. Levels are shuffled in groups of three by stage in the item pool
    - Individual Levels: Each level of each stage is shuffled into the item pool"""
    display_name: str = "Level Randomization"
    option_stages = 0
    option_individual_levels = 1
    default = 0


@dataclass
class DrillDozerGameOptions(PerGameCommonOptions):
    goal:Goal