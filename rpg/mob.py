from abc import ABC, abstractmethod
from typing import Callable

from .entity import EntityType
from .item import ItemStack
from .item_type import NONE
from .stats import StatsHolder


class Entity(StatsHolder, ABC):

    _type: EntityType
    _item_in_hand: ItemStack = ItemStack(NONE)

    def __init__(self, type: EntityType, health: int, max_health: int, mana: int, max_mana: int, hunger: int, trigger: Callable[[object], None] = lambda item: ...):
        super().__init__(health, max_health, mana, max_mana, hunger, trigger)
        self._type = type

    def get_type(self) -> EntityType:
        return self._type

    def attack(self, entity: StatsHolder):
        entity.set_max_health(int(entity.get_max_health() - (self._item_in_hand.damage() + self.base_damage())))

    @abstractmethod
    def base_damage(self) -> float:
        pass


class Mob(Entity):

    level: int

    def __init__(self, level: int, type: EntityType, health: int, trigger: Callable[[object], None] = lambda item: ...):
        max_health = type.level_health.get(level, type.max_health)
        if health == -1:
            health = max_health
        super().__init__(type, health, max_health, 0, 0, 0, trigger)
        self.level = level

    def has_arrows(self, amount: int) -> bool:
        return True

    def reduce_arrows(self, amount: int):
        return

    def base_damage(self) -> float:
        return self.get_type().level_damage.get(self.level, 1.0)
