# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import asyncio
import logging
from config import Config
from pyrogram import Client as VJ, idle
from logging.handlers import RotatingFileHandler

# IMPORTANT:
# Do NOT import restart_forwards here (top-level).
# We'll import it inside main() after loop is set.


if __name__ == "__main__":
    # Force ONE asyncio loop for everything (Pyrogram + Motor DB)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    VJBot = VJ(
        "VJ-Forward-Bot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=120,
        plugins=dict(root="plugins"),
    )

    async def main():
        # Import AFTER loop is set so DB/Motor uses same loop
        from plugins.regix import restart_forwards

        await VJBot.start()
        await VJBot.get_me()

        await restart_forwards(VJBot)

        print("Bot Started.")
        await idle()

    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
