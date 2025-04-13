import os

API_ID = os.environ.get("API_ID", "3737117")

API_HASH = os.environ.get("API_HASH", "f466ca6ff400954d192ce0992ddf8b5d")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1110590703))

LOG = -1002679053494,

UPDATE_GRP = , # bot sat group

auth_chats = []

try:
    ADMINS=[1110590703]
    #for x in (os.environ.get("ADMINS", "1110590703").split()):
        #ADMINS.append(int(x))
except ValueError:
        #raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
