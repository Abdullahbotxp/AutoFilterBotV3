import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = 'LuciferMoringstar_Robot'
API_ID = 29514095
API_HASH = 'c17fef5596d69ef2910d3f74e743eb73'
BOT_TOKEN = '6133107220:AAGHQrtyuuj_sCICm7BQAiExsukbWwGisgE'

# Bot settings
CACHE_TIME = 300
USE_CAPTION_FILTER = False

BROADCAST_CHANNEL = -1001964286309
ADMIN_ID = 5071390190
DB_URL = 'mongodb+srv://BOTXP:BOTXP@cluster0.lvvmb9h.mongodb.net/?retryWrites=true&w=majority'
BROADCAST_AS_COPY = True

# Admins, Channels & Users
ADMINS = 5071390190
CHANNELS = -1001901200484
auth_users = []
AUTH_USERS = []
auth_channel = -1001416467235
AUTH_CHANNEL = -1001416467235
AUTH_GROUPS = None
TUTORIAL = "https://youtu.be/5hnYOKBzyi8"
# MongoDB information
DATABASE_URI = "mongodb+srv://BOTXP:BOTXP@cluster0.lvvmb9h.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = 'LuciferMoringstar_Robot'
COLLECTION_NAME = 'Telegram_files'

# Messages
default_start_msg = """
**Hi, I'm Auto Filter V3**

Here you can search files in Inline mode as well as PM, Use the below buttons to search files or send me the name of file to search.
"""
START_MSG = environ.get('START_MSG', default_start_msg)

FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
OMDB_API_KEY = 'e882d08a'
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY
