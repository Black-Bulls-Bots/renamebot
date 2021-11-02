"""
Rename Bot by Black Bulls - https://t.me/blackbulls_support
Original code - https://github.com/prgofficial/RenameBot-PermTB
Rewritten by Kishore - https://t.me/kishoreee
"""

import time
from datetime import datetime
from configparser import ConfigParser
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from renamebot import *

class RenameBot(Client):
    CREATOR_ID = 2094704420
    BOT_ID = 2054753655    


    def __init__(self):
        name = self.__class__.__name__.lower()
       

        super().__init__(
            name,
            api_id = API_ID,
            api_hash = API_HASH, 
            bot_token = TG_BOT_TOKEN,
            workers=8,
            plugins=dict(
                root=f"{name}.plugins"
                ),
            sleep_threshold=180
        )

        
        self.uptime_reference = time.monotonic_ns()
        self.start_datetime = datetime.utcnow()

    async def start(self):
        await super().start()

        me = await self.get_me()
        print(f"Rename Bot of Black Bulls, Running on Pyrogram v{__version__} (layer {layer}) started on @{me.username}")
    
    async def stop(self, *args):
        await super().stop()
        print("Pyrogram Assistant stopped. Bye.")

RenameBot().run()