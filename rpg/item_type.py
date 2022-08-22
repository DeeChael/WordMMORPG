from .entity_type import SLIME
from .item import SimpleItemType, WeaponItemType, Rarity, BowItemType, WandItemType, SummonThingItemType
from .player_class import PlayerClass

NONE = SimpleItemType("", "", False, Rarity.NONE)

# OTHERS
ARROW = SimpleItemType("arrow", "箭矢", True, Rarity.COMMON)

# WEAPONS
# SWORDS
WOODEN_SWORD = WeaponItemType("wooden_sword", "木剑", False, 2, Rarity.COMMON, PlayerClass.KNIGHT, PlayerClass.WARRIOR)
BONE_SWORD = WeaponItemType("bone_sword", "骸骨之剑", False, 3, Rarity.COMMON, PlayerClass.KNIGHT, PlayerClass.WARRIOR)
UNDEAD_SWORD = WeaponItemType("undead_sword", "不死之剑", False, 5, Rarity.UNCOMMON, PlayerClass.KNIGHT, PlayerClass.WARRIOR)
IRON_SWORD = WeaponItemType("iron_sword", "铁剑", False, 6, Rarity.UNCOMMON, PlayerClass.KNIGHT, PlayerClass.WARRIOR)
CLEAVER = WeaponItemType("cleaver", "裂刃", False, 7, Rarity.UNCOMMON, PlayerClass.KNIGHT, PlayerClass.WARRIOR)
RAIDER_AXE = WeaponItemType("raider_axe", "维京战斧", False, 10, Rarity.RARE, PlayerClass.WARRIOR)
WOLFS_FANG = WeaponItemType("wolfs_fang", "狼牙之刃", False, 11, Rarity.RARE, PlayerClass.KNIGHT)
KATANA = WeaponItemType("katana", "武士刀", False, 12, Rarity.RARE, PlayerClass.KNIGHT)
WEAK_SWORD = WeaponItemType("weak_sword", "虚弱之剑", False, 12, Rarity.EPIC, PlayerClass.KNIGHT, PlayerClass.WARRIOR)
EMBER_SWORD = WeaponItemType("ember_sword", "余烬之剑", False, 14, Rarity.EPIC, PlayerClass.KNIGHT, PlayerClass.WARRIOR)
ASPECT_OF_THE_DRAGONS = WeaponItemType("aspect_of_the_dragons", "龙之剑", False, 22, Rarity.LEGENDARY, PlayerClass.KNIGHT, PlayerClass.WARRIOR)
MIDAS_SWORD = WeaponItemType("midas_sword", "贪婪之剑", False, 10, Rarity.LEGENDARY, PlayerClass.KNIGHT, PlayerClass.WARRIOR)
GERRYS_SWORD = WeaponItemType("gerrys_sword", "格里的剑", False, 30, Rarity.LEGENDARY, PlayerClass.KNIGHT, PlayerClass.WARRIOR)
REAPER_SCYTHE = WeaponItemType("reaper_scythe", "死神之镰", False, 27, Rarity.LEGENDARY, PlayerClass.WARRIOR)

# BOWS
WOODEN_BOW = BowItemType("wooden_bow", "木弓", False, 2, 1, Rarity.COMMON, PlayerClass.ARCHER)
SHORTBOW_OF_BONE = BowItemType("shortbow_of_bone", "骨之短弓", False, 31, 3, Rarity.EPIC, PlayerClass.ARCHER)

# WAND
WOODEN_WAND = WandItemType("wooden_wand", "木制法杖", False, 3, 1, Rarity.COMMON, PlayerClass.MAGE, PlayerClass.PRIEST)
HOLY_WAND = WandItemType("holy_wand", "圣杖", False, 53, 25, Rarity.LEGENDARY, PlayerClass.MAGE, PlayerClass.PRIEST)

# SHIELD
WOODEN_SHIELD = WeaponItemType("wooden_shield", "木制盾牌", False, 2, Rarity.COMMON, PlayerClass.TANK)

# DAGGER
WOODEN_DAGGER = WeaponItemType("wooden_dagger", "木制匕首", False, 4, Rarity.COMMON, PlayerClass.ASSASSIN)

# SUMMON-THING
WAND_OF_SLIME = SummonThingItemType("wand_of_slime", "史莱姆法杖", False, 5, 3, Rarity.COMMON, SLIME, PlayerClass.SUMMONER)


# ADMIN'S WEAPONS
DEECHAELS_SWORD = WeaponItemType("deechaels_sword", "迁冥的剑", False, 1283, Rarity.RELIC, PlayerClass.KNIGHT, PlayerClass.WARRIOR)
DEECHAELS_SHIELD = WeaponItemType("deechaels_shield", "迁冥的盾", False, 1283, Rarity.RELIC, PlayerClass.TANK)
DEECHAELS_SHORTBOW = BowItemType("deechaels_shortbow", "迁冥的短弓", False, 1283, 0, Rarity.RELIC, PlayerClass.ARCHER)
DEECHAELS_DAGGER = WeaponItemType("deechaels_dagger", "迁冥的匕首", False, 1283, Rarity.RELIC, PlayerClass.ASSASSIN)
DEECHAELS_WAND = WandItemType("deechaels_wand", "迁冥的法杖", False, 1283, 0, Rarity.RELIC, PlayerClass.MAGE, PlayerClass.PRIEST)
