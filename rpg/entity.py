from typing import Dict

from .loot import Lootable


class EntityType(Lootable):

    identity: str
    display_name: str
    max_health: int
    level_health: Dict[int, int]
    level_damage: Dict[int, float]

    def __init__(self, identity: str, display_name: str, max_health: int, level_health: Dict[int, int], level_damage: Dict[int, float]):
        self.identity = identity
        self.display_name = display_name
        self.max_health = max_health
        self.level_damage = level_damage
        self.level_health = level_health
