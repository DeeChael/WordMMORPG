import copy
import json
import logging
from typing import Dict, Union

from khl import Bot, Message, MessageTypes, EventTypes, Event, api, User
from khl.card import Element, Types, CardMessage, Card, Module

import message_builder
from configuration import JsonConfiguration

quanjiaokongge = "　"


config = JsonConfiguration('config.json')
bot = Bot(token=config.get('token'))


@bot.command(name="3rdw")
async def third_world(msg: Message, *args):
    await msg.ctx.channel.send(message_builder.choose_class(), type=MessageTypes.CARD)
    ...


def load_player_config(uid: str) -> JsonConfiguration:
    player_cfg = JsonConfiguration(f'player-stats/{uid}/data.json')
    return player_cfg


if __name__ == "__main__":
    bot.run()