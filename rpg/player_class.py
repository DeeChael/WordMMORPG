from enum import Enum


class PlayerClass(Enum):
    KNIGHT = "knight" # 骑士，使用单手剑（可双持）
    WARRIOR = "warrior" # 战士，使用单手剑或双手剑
    TANK = "tank" # 坦克，使用盾牌
    MAGE = "mage" # 法师，使用法杖
    ARCHER = "archer" # 射手，使用弓箭
    PRIEST = "priest" # 牧师，使用法杖
    ASSASSIN = "assassin" # 刺客，使用双持匕首
    SUMMONER = "summoner" # 召唤师，使用召唤代物


class SubClass(Enum):
    NONE = "none"
    COOK = "cook" # 厨师，可以烹饪食物
    BLACKSMITH = "blacksmith" # 铁匠，可以打造装备
    CARPENTER = "carpenter" # 木工，暂时无用
    TRAINER = "trainer" # 驯兽师，可以驯服野兽
    SCHOLAR = "scholar" # 学者，可以为武器附魔


def class_chinese_name(player_class: PlayerClass) -> str:
    if player_class == PlayerClass.KNIGHT:
        return "骑士"
    elif player_class == PlayerClass.WARRIOR:
        return "战士"
    elif player_class == PlayerClass.TANK:
        return "坦克"
    elif player_class == PlayerClass.MAGE:
        return "法师"
    elif player_class == PlayerClass.ARCHER:
        return "射手"
    elif player_class == PlayerClass.PRIEST:
        return "牧师"
    elif player_class == PlayerClass.ASSASSIN:
        return "刺客"
    elif player_class == PlayerClass.SUMMONER:
        return "召唤师"
    else:
        return "未知"


def class_description(player_class: PlayerClass) -> str:
    if player_class == PlayerClass.KNIGHT:
        return "可以使用剑类和刀类武器"
    elif player_class == PlayerClass.WARRIOR:
        return "可以使用剑类和战斧类武器"
    elif player_class == PlayerClass.TANK:
        return "可以使用剑类和盾牌类武器"
    elif player_class == PlayerClass.MAGE:
        return "可以使用魔剑类和法杖类武器"
    elif player_class == PlayerClass.ARCHER:
        return "可以使用弓类和枪类武器"
    elif player_class == PlayerClass.PRIEST:
        return "可以使用法杖类武器"
    elif player_class == PlayerClass.ASSASSIN:
        return "可以使用刀类、匕首类、剑类、弓类和魔剑类武器"
    elif player_class == PlayerClass.SUMMONER:
        return "可以使用法杖类武器和召唤代物"
    else:
        return "未知"


def subclass_chinese_name(sub_class: SubClass) -> str:
    if sub_class == SubClass.NONE:
        return "无"
    elif sub_class == SubClass.COOK:
        return "厨师"
    elif sub_class == SubClass.BLACKSMITH:
        return "铁匠"
    elif sub_class == SubClass.CARPENTER:
        return "木工"
    elif sub_class == SubClass.TRAINER:
        return "驯兽师"
    elif sub_class == SubClass.SCHOLAR:
        return "学者"
    else:
        return "未知"
