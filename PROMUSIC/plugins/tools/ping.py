from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message
from config import *
from PROMUSIC import app
from PROMUSIC.core.call import PRO
from PROMUSIC.utils import bot_sys_stats
from PROMUSIC.utils.decorators.language import language
from PROMUSIC.utils.inline import supp_markup
from config import BANNED_USERS


@app.on_message(filters.command("ping", prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_video(
        video="https://files.catbox.moe/8r1mq7.jpg",
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await PRO.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )
