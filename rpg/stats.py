from abc import abstractmethod, ABC
from typing import Callable


class StatsHolder(ABC):

    _health: int
    _max_health: int
    _mana: int
    _max_mana: int
    _hunger: int

    trigger: Callable[[object], None]

    def __init__(self, health: int, max_health: int, mana: int, max_mana, hunger: int, trigger: Callable[[object], None] = lambda item: ...):
        self._health = health
        self._max_health = max_health
        self._mana = mana
        self._max_mana = max_mana
        self._hunger = hunger
        self.trigger = trigger

    def set_max_health(self, max_health: int):
        self._max_health = max(1, max_health)
        self.trigger(self)

    def set_max_mana(self, max_mana: int):
        self._max_mana = max(1, max_mana)
        self.trigger(self)

    def set_health(self, health: int):
        self._health = min(max(0, health), self._max_health)
        self.trigger(self)

    def set_mana(self, mana: int):
        self._mana = min(max(0, mana), self._max_mana)
        self.trigger(self)

    def set_hunger(self, hunger: int):
        self._hunger = min(max(0, hunger), 20)
        self.trigger(self)

    def get_max_health(self) -> int:
        return self._max_health

    def get_max_mana(self) -> int:
        return self._max_mana

    def get_health(self) -> int:
        return self._health

    def get_mana(self) -> int:
        return self._mana

    def get_hunger(self) -> int:
        return self._hunger

    @abstractmethod
    def has_arrows(self, amount: int) -> bool:
        pass

    @abstractmethod
    def reduce_arrows(self, amount: int):
        pass
