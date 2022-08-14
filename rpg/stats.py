from abc import abstractmethod, ABC


class StatsHolder(ABC):

    health: int
    max_health: int
    mana: int
    max_mana: int
    hunger: int

    def __init__(self, health: int, max_health: int, mana: int, max_mana, hunger: int):
        self.health = health
        self.max_health = max_health
        self.mana = mana
        self.max_mana = max_mana
        self.hunger = hunger

    @abstractmethod
    def has_arrows(self, amount: int) -> bool:
        pass

    @abstractmethod
    def reduce_arrows(self, amount: int):
        pass
