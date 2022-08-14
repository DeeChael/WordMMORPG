from abc import ABC, abstractmethod
from typing import Callable

from .player_class import PlayerClass
from .stats import StatsHolder


class ItemType(ABC):

    identity: str
    display_name: str
    stackable: bool

    def __init__(self, identity: str, display_name: str, stackable: bool):
        self.identity = identity
        self.display_name = display_name
        self.stackable = stackable

    @abstractmethod
    def is_weapon(self) -> bool:
        pass

    @abstractmethod
    def is_usable(self) -> bool:
        pass


class WeaponItemType(ItemType):

    weapon_type: PlayerClass
    damage: float

    def __init__(self, identity: str, display_name: str, stackable: bool, weapon_type: PlayerClass, damage: float):
        super().__init__(identity, display_name, stackable)
        self.weapon_type = weapon_type
        self.damage = damage

    def is_weapon(self) -> bool:
        return True

    def can_use(self, player_class: PlayerClass) -> bool:
        return player_class == self.weapon_type

    def is_usable(self) -> bool:
        return False


class UsableItemType(ItemType, ABC):

    def __init__(self, identity: str, display_name: str, stackable: bool):
        super().__init__(identity, display_name, stackable)

    def is_weapon(self) -> bool:
        return False

    def is_usable(self) -> bool:
        return True

    @abstractmethod
    def on_use(self, stats_holder: StatsHolder):
        pass


class FoodItemType(UsableItemType):

    hunger: int

    def __init__(self, identity: str, display_name: str, stackable: bool, hunger: int):
        super().__init__(identity, display_name, stackable)
        self.hunger = hunger

    def on_use(self, stats_holder: StatsHolder):
        stats_holder.hunger = min(stats_holder.hunger + self.hunger, 100)


class PotionItemType(UsableItemType):

    def __init__(self, identity: str, display_name: str, stackable: bool):
        super().__init__(identity, display_name, stackable)

    def on_use(self, stats_holder: StatsHolder):
        pass


class BowItemType(WeaponItemType, UsableItemType):

    arrows_cost: int

    def __init__(self, identity: str, display_name: str, stackable: bool, weapon_type: PlayerClass, damage: float, arrows_cost: int):
        super().__init__(identity, display_name, stackable, weapon_type, damage)
        self.arrows_cost = arrows_cost

    def is_weapon(self) -> bool:
        return True

    def is_usable(self) -> bool:
        return True

    def on_use(self, stats_holder: StatsHolder):
        if stats_holder.has_arrows(self.arrows_cost):
            stats_holder.reduce_arrows(self.arrows_cost)


class ItemStack:
    type: ItemType
    _amount: int = 1

    trigger: Callable[[object], None]

    def __init__(self, type: ItemType, trigger: Callable[[object], None]):
        self.type = type
        self.trigger = trigger

    def set_amount(self, amount: int):
        if not self.type.stackable:
            raise TypeError("The type of the item is un-stackable")
        self._amount = amount
        self.trigger(self)

    def get_amount(self) -> int:
        return self._amount