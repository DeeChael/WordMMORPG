from enum import Enum


class PlayerClass(Enum):
    KNIGHT = "knight" # 骑士，使用单手剑（可双持）
    WARRIOR = "warrior" # 战士，使用单手剑或双手剑
    TANK = "tank" # 坦克，使用盾牌
    MAGE = "mage" # 法师，使用法杖
    ARCHER = "archer" # 射手，使用弓箭
    PRIEST = "priest" # 牧师，使用法杖
    ASSASSIN = "assassin" # 刺客，使用双持匕首
    SUMMONER = "summoner" # 召唤师，使用召唤物


class SubClass(Enum):
    NONE = "none"
    COOK = "cook" # 厨师，可以烹饪食物
    BLACKSMITH = "blacksmith" # 铁匠，可以打造装备
    CARPENTER = "carpenter" # 木工，暂时无用
    TRAINER = "trainer" # 驯兽师，可以驯服野兽
    SCHOLAR = "scholar" # 学者，可以为武器附魔
