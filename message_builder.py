from typing import Union

from khl import User
from khl.card import Element, Types, CardMessage, Card, Module

from configuration import JsonConfiguration
from rpg.player import Player
from rpg.player_class import PlayerClass, class_chinese_name, class_description


def choose_class() -> CardMessage:
    message = CardMessage()
    modules = list()
    modules.append(Module.Header(
        text="欢迎进入MMORPG游戏“第三世界”！"
    ))
    modules.append(Module.Section(
        text="您是第一次游玩！\n请选择您的职业并创建角色！"
    ))
    for player_class in PlayerClass:
        modules.append(Module.Divider())
        modules.append(
            Module.Section(
                text=Element.Text(f"**{class_chinese_name(player_class)}**: {class_description(player_class)}", type=Types.Text.KMD),
                mode=Types.SectionMode.RIGHT,
                accessory=Element.Button(
                    text="我要选这个",
                    theme=Types.Theme.PRIMARY,
                    click=Types.Click.RETURN_VAL,
                    value="player_class_choose_" + player_class.value
                )
            )
        )
    modules.append(Module.Divider())
    modules.append(Module.Context(Element.Text("本机器人由DeeChael开发 开源于[Github](https://github.com/DeeChael/WordMMORPG)", type=Types.Text.KMD)))
    message.append(Card(
        theme=Types.Theme.NONE,
        *modules
    ))
    return message


def stat_card(player: Player) -> CardMessage:
    message = CardMessage()
    message.append(Card(
        theme=Types.Theme.NONE,
        *(Module.Header("玩家数据"),
          Module.Section(Element.Text(
              f"**玩家名称**: {player.name}\n"
              f"**玩家等级**: {player.level()}\n"
              f"**当前经验值**: {player.experience}\n"
              f"**血量**: {player.get_health()}/{player.get_max_health()}\n"
              f"**魔力**: {player.get_mana()}/{player.get_max_mana()}\n"
              f"**饥饿值**: {player.get_hunger()}",
              type=Types.Text.KMD
          ))
          )
    ))
    return message


def success_message(user: Union[User, str, None], message: str) -> CardMessage:
    if isinstance(user, User):
        user = user.id
    card_message = CardMessage()
    card = Card(theme=Types.Theme.SUCCESS)
    card.append(Module.Header('成功'))
    card.append(Module.Section(Element.Text((f'(met){user}(met) ' if user is not None else "") + f'{message}', type=Types.Text.KMD)))
    card_message.append(card)
    return card_message


def primary_message(user: Union[User, str, None], message: str) -> CardMessage:
    if isinstance(user, User):
        user = user.id
    card_message = CardMessage()
    card = Card(theme=Types.Theme.PRIMARY)
    card.append(Module.Header('信息'))
    card.append(Module.Section(Element.Text((f'(met){user}(met) ' if user is not None else "") + f'{message}', type=Types.Text.KMD)))
    card_message.append(card)
    return card_message


def failed_message(user: Union[User, str, None], message: str) -> CardMessage:
    if isinstance(user, User):
        user = user.id
    card_message = CardMessage()
    card = Card(theme=Types.Theme.DANGER)
    card.append(Module.Header('失败'))
    card.append(Module.Section(Element.Text((f'(met){user}(met) ' if user is not None else "") + f'{message}', type=Types.Text.KMD)))
    card_message.append(card)
    return card_message
