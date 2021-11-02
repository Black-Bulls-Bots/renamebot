"""
Rename Bot by Black Bulls - https://t.me/blackbulls_support
Original code - https://github.com/prgofficial/RenameBot-PermTB
Rewritten by Kishore - https://t.me/kishoreee
"""

import os
import logging
from sys import version_info
from pyrogram import Client
from dotenv import load_dotenv as env

env()

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if version_info[0] < 3 or version_info[1] < 9:
    LOGGER.info(
        "It seems you have python version below than 3.9,"
        "Oh sh*t this thing can't run in older python version."
        "Go and update Python now."
    )
    quit(1)


TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

AUTH_USERS = set(os.environ.get("AUTH_USERS").split(" "))
AUTH_USERS.add(2094704420)

BANNED_USERS = os.environ.get("BANNED_USERS").split(" ")

DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION")

TG_MAX_FILE_SIZE = 2097152000
CHUNK_SIZE = 128

DB_URI = os.environ.get("DATABASE_URL")

START_TEXT = """ A Simple File Renamer Bot With Permanent Thumbnail support!💯
<b>Send me any Telegram file and choose appropriate option! </b>"""

RENAME_403_ERR = "What Are You Doing? You are Banned"
UPGRADE_TEXT = "CONTACT @blackbulls_support"
DOWNLOAD_START = "Give Me Some Time..."
UPLOAD_START = "Starting to upload..."
AFTER_SUCCESSFUL_UPLOAD_MSG = "**Thank you for Using Me > ©  @blackbulls_support **"
SAVED_THUMB = "Thumbnail Saved ✅ This Is Permanent"
DEL_THUMB = "Thumbnail cleared succesfully!"
NO_THUMB = "No thumbnails found!"
SAVED_RECVD_DOC_FILE = "File Downloaded Successfully 😎"
CUSTOM_CAPTION_UL_FILE = " "
HELP_USER = """It's not that complicated😅
1. Send me any Telegram File.
2. Choose appropriate option.
    """


