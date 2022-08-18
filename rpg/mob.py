from abc import ABC
from typing import Callable

from .entity import EntityType
from .item import ItemStack
from .item_type import NONE
from .stats import StatsHolder


class Entity(StatsHolder, ABC):

    _type: EntityType
    _item_in_hand: ItemStack = ItemStack(NONE)

    def __init__(self, type: EntityType, health: int, max_health: int, mana: int, max_mana: int, hunger: int, trigger: Callable[[object], None] = lambda item: ...):
        super().__init__(health, max_health, mana, max_mana, 0, trigger)
        self._type = type

    def get_type(self) -> EntityType:
        return self._type

    def attack(self, entity: StatsHolder):
        entity.set_max_health(int(entity.get_max_health() - self._item_in_hand.damage()))


class Mob(Entity):

    level: int

    def __init__(self, level: int, type: EntityType, health: int, trigger: Callable[[object], None] = lambda item: ...):
        if health == -1:
            health = type.max_health
        super().__init__(type, health, type.max_health, 0, 0, 0, trigger)
        self.level = level