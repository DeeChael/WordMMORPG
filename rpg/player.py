from typing import List

from .entity_type import PLAYER
from .item import ItemStack, ItemType
from .item_type import NONE, ARROW
from .mob import Entity
from .player_class import PlayerClass, SubClass


class Player(Entity):
    """
    Lv1: 0
    Lv5: 200
    Lv10: 800
    Lv15: 2200
    Lv20: 5200
    Lv25: 10200
    Lv30: 17000
    Lv35: 27000
    Lv40: 43000
    Lv45: 67000
    Lv49: 97000
    Lv50 197000

    Lv1 - Lv5, 50 exp every level
    Lv6 - Lv10, 150 exp every level
    Lv11 - Lv15, 350 exp every level
    Lv16 - Lv20, 750 exp every level
    Lv21 - Lv25, 1250 exp every level
    Lv26 - Lv30, 1700 exp every level
    Lv31 - Lv35, 2500 exp every level
    Lv36 - Lv40, 4000 exp every level
    Lv41 - Lv45, 6000 exp every level
    Lv46 - Lv49, 10000 exp every level
    Lv49 - Lv50, 100000 exp

    Player will unlock sub-class when they reached Lv50

    Maximum level: Lv50
    """

    player_class: PlayerClass
    sub_class: SubClass
    id: str
    name: str
    experience: int
    _head: ItemStack = NONE
    _chest: ItemStack = NONE
    _legs: ItemStack = NONE
    _feet: ItemStack = NONE
    _glove: ItemStack = NONE
    _inventory: List[ItemStack]
    _active_arrow: ItemType = NONE

    def __init__(self, player_class: PlayerClass, sub_class: SubClass, id: str, name: str,
                 experience: int, health: int, max_health: int, mana: int, max_mana, hunger: int):
        self.player_class = player_class
        self.sub_class = sub_class
        self.id = id
        self.name = name
        self.experience = experience
        super().__init__(PLAYER, health, max_health, mana, max_mana, hunger)

    def level(self) -> int:
        if self.experience >= 197000:
            return 50
        elif self.experience >= 97000:
            return 49
        elif self.experience >= 67000:
            rest = self.experience - 67000
            return rest // 10000 if rest % 10000 == 0 else rest // 10000 + 1
        elif self.experience >= 43000:
            rest = self.experience - 43000
            return rest // 6000 if rest % 6000 == 0 else rest // 6000 + 1
        elif self.experience >= 27000:
            rest = self.experience - 27000
            return rest // 4000 if rest % 4000 == 0 else rest // 4000 + 1
        elif self.experience >= 17000:
            rest = self.experience - 17000
            return rest // 2500 if rest % 2500 == 0 else rest // 2500 + 1
        elif self.experience >= 10200:
            rest = self.experience - 10200
            return rest // 1700 if rest % 1700 == 0 else rest // 1700 + 1
        elif self.experience >= 5200:
            rest = self.experience - 5200
            return rest // 1250 if rest % 1250 == 0 else rest // 1250 + 1
        elif self.experience >= 2200:
            rest = self.experience - 2200
            return rest // 750 if rest % 750 == 0 else rest // 750 + 1
        elif self.experience >= 800:
            rest = self.experience - 800
            return rest // 350 if rest % 350 == 0 else rest // 350 + 1
        elif self.experience >= 200:
            rest = self.experience - 200
            return rest // 150 if rest % 150 == 0 else rest // 150 + 1
        else:
            rest = self.experience
            return rest // 50 if rest % 50 == 0 else rest // 50 + 1

    def has_arrows(self, amount: int) -> bool:
        for item_stack in self.inventory:
            if item_stack.get_type() == ARROW:
                if item_stack.get_amount() >= amount:
                    return True
        return False

    def reduce_arrows(self, amount: int):
        for item_stack in self.inventory:
            if item_stack.get_type() == ARROW:
                if item_stack.get_amount() > amount:
                    item_stack.set_amount(item_stack.get_amount() - amount)
                elif item_stack.get_amount() == amount:
                    self.inventory.remove(item_stack)
        pass
