import copy
import json
import logging
from typing import Dict, Union

from khl import Bot, Message, MessageTypes, EventTypes, Event, api, User
from khl.card import Element, Types, CardMessage, Card, Module

import message_builder
from configuration import JsonConfiguration
from rpg.player import Player
from rpg.player_class import PlayerClass, class_chinese_name

quanjiaokongge = "　"


config = JsonConfiguration('config.json')
bot = Bot(token=config.get('token'))


cache: Dict[str, Player] = dict()


@bot.command(name="3rdw")
async def third_world(msg: Message, *args):
    user = msg.author
    channel = msg.ctx.channel
    guild = msg.ctx.guild
    player_config = load_player_config(msg.author_id)
    if not player_config.exists():
        await msg.ctx.channel.send(message_builder.choose_class(), type=MessageTypes.CARD, temp_target_id=msg.author_id)
        return
    if len(args) == 1:
        arg0 = str(args[0]).lower()
        if arg0 == "stats":
            if user.id not in cache:
                cache[user.id] = Player(config=player_config, **player_config.dict_copy())
            await msg.reply(message_builder.stat_card(cache[user.id]), type=MessageTypes.CARD)


@bot.on_event(EventTypes.MESSAGE_BTN_CLICK)
async def button_clicked(b: Bot, event: Event):
    value = str(event.extra['body']['value'])
    user_id = event.extra['body']['user_id']
    msg_id = event.extra['body']['msg_id']
    channel_id = event.extra['body']['target_id']
    if user_id not in cache:
        player_config = load_player_config(user_id)
        if player_config.exists():
            if value.startswith("player_class_choose_"):
                await send2channel(channel_id, message_builder.failed_message(user_id, "你已经创建过角色了！"), user_id)
                return
        else:
            user = await bot.fetch_user(user_id)
            if value.startswith("player_class_choose_"):
                player_class = PlayerClass(value[20:])
                if player_class is None:
                    await send2channel(channel_id, message_builder.failed_message(user_id, "创建失败，未知的职业"), user_id)
                    return
                player_obj = Player(config=player_config, **{"id": user_id, "name": user.username, "class": player_class.value})
                player_obj.save_config()
                cache[user_id] = player_obj
                await send2channel(channel_id, message_builder.success_message(user_id,
                                                                               f"创建成功！您的职业为：{class_chinese_name(player_class)}"))


async def send2channel(channel: str, message: CardMessage, user: str = None):
    if user is None:
        await bot.client.gate.exec_req(api.Message.create(target_id=channel,
                                                          content=json.dumps(message),
                                                          type=10))
    else:
        await bot.client.gate.exec_req(api.Message.create(target_id=channel,
                                                          content=json.dumps(message),
                                                          type=10,
                                                          temp_target_id=user))


def load_player_config(uid: str) -> JsonConfiguration:
    player_cfg = JsonConfiguration(f'player-stats/{uid}/data.json')
    return player_cfg


if __name__ == "__main__":
    bot.run()