import time
from abc import ABC, abstractmethod
from enum import Enum
from typing import Callable, Tuple

from .entity import EntityType
from .player_class import PlayerClass
from .stats import StatsHolder


class Rarity(Enum):
    NONE = "none" # grey
    COMMON = "common" # white
    UNCOMMON = "uncommon" # green
    RARE = "rare" # blue
    EPIC = "epic" # purple
    LEGENDARY = "legendary" # orange or gold
    MYTHIC = "mythic" # pink
    SPECIAL = "special" # red
    RELIC = "relic" # black


class ItemType(ABC):

    identity: str
    display_name: str
    stackable: bool
    rarity: Rarity

    def __init__(self, identity: str, display_name: str, stackable: bool, rarity: Rarity):
        self.identity = identity
        self.display_name = display_name
        self.stackable = stackable
        self.rarity = rarity

    @abstractmethod
    def is_weapon(self) -> bool:
        pass

    @abstractmethod
    def is_usable(self) -> bool:
        pass


class WeaponItemType(ItemType):

    weapon_type: Tuple[PlayerClass]
    damage: float

    def __init__(self, identity: str, display_name: str, stackable: bool, damage: float, rarity: Rarity, *weapon_type: PlayerClass):
        super().__init__(identity, display_name, stackable, rarity)
        self.weapon_type = weapon_type
        self.damage = damage

    def is_weapon(self) -> bool:
        return True

    def can_use(self, player_class: PlayerClass) -> bool:
        return player_class == self.weapon_type

    def is_usable(self) -> bool:
        return False


class UsableItemType(ItemType, ABC):

    def __init__(self, identity: str, display_name: str, stackable: bool, rarity: Rarity):
        super().__init__(identity, display_name, stackable, rarity)

    def is_weapon(self) -> bool:
        return False

    def is_usable(self) -> bool:
        return True

    @abstractmethod
    def on_use(self, stats_holder: StatsHolder):
        pass


class FoodItemType(UsableItemType):

    hunger: int

    def __init__(self, identity: str, display_name: str, stackable: bool, hunger: int, rarity: Rarity):
        super().__init__(identity, display_name, stackable, rarity)
        self.hunger = hunger

    def on_use(self, stats_holder: StatsHolder):
        stats_holder.hunger = min(stats_holder.hunger + self.hunger, 100)


class PotionItemType(UsableItemType):

    def __init__(self, identity: str, display_name: str, stackable: bool, rarity: Rarity):
        super().__init__(identity, display_name, stackable, rarity)

    def on_use(self, stats_holder: StatsHolder):
        pass


class BowItemType(WeaponItemType, UsableItemType):

    arrows_cost: int

    def __init__(self, identity: str, display_name: str, stackable: bool, damage: float, arrows_cost: int, rarity: Rarity, *weapon_type: PlayerClass):
        super().__init__(identity, display_name, stackable, damage, rarity, *weapon_type)
        self.arrows_cost = arrows_cost

    def is_weapon(self) -> bool:
        return True

    def is_usable(self) -> bool:
        return True

    def on_use(self, stats_holder: StatsHolder):
        if stats_holder.has_arrows(self.arrows_cost):
            stats_holder.reduce_arrows(self.arrows_cost)


class WandItemType(WeaponItemType, UsableItemType):

    mana_cost: int

    def __init__(self, identity: str, display_name: str, stackable: bool, damage: float, mana_cost: int, rarity: Rarity, *weapon_type: PlayerClass):
        super().__init__(identity, display_name, stackable, damage, rarity, *weapon_type)
        self.mana_cost = mana_cost

    def is_weapon(self) -> bool:
        return True

    def is_usable(self) -> bool:
        return True

    def on_use(self, stats_holder: StatsHolder):
        if stats_holder.get_mana() >= self.mana_cost:
            stats_holder.set_mana(stats_holder.get_mana() - self.mana_cost)


class SummonThingItemType(WandItemType):

    max_amount: int
    summon_type: EntityType

    def __init__(self, identity: str, display_name: str, stackable: bool, max_amount: int, mana_cost: int, rarity: Rarity, summon_type: EntityType, *weapon_type: PlayerClass):
        super().__init__(identity, display_name, stackable, 0, mana_cost, rarity, *weapon_type)
        self.max_amount = max_amount
        self.summon_type = summon_type

    def is_weapon(self) -> bool:
        return True

    def is_usable(self) -> bool:
        return True


class ItemStack:

    _type: ItemType
    _amount: int = 1

    trigger: Callable[[object], None]
    create_time: time.time()

    def __init__(self, type: ItemType, trigger: Callable[[object], None] = lambda item: ..., create_time: float = 0.0):
        self._type = type
        self.trigger = trigger
        if create_time != 0.0:
            self.create_time = create_time

    def get_type(self) -> ItemType:
        return self._type

    def set_amount(self, amount: int):
        if not self._type.stackable:
            raise TypeError("The type of the item is un-stackable")
        self._amount = amount
        self.trigger(self)

    def get_amount(self) -> int:
        return self._amount

    def is_weapon(self) -> bool:
        return self._type.is_weapon()

    def is_usable(self) -> bool:
        return self._type.is_usable()

    def damage(self) -> float:
        if isinstance(self._type, WeaponItemType):
            return self._type.damage
        return 1

    def __eq__(self, other):
        if other is None:
            return False
        if self == other:
            return True
        if not isinstance(other, self.__class__):
            return False
        if self.create_time != other.create_time:
            return False
        if self._type != other._type:
            return False
        return self._amount == other._amount
