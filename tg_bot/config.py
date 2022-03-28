# if not __name__.endswith("sample_config"):
#     import sys
#     print("The README is there to be read. Extend this sample config to a config file, don't just rename and change "
#           "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)
#     quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "5115523156:AAFjt1ov62a5gBHpMBG4CGrSk-mShLz1WA4"
    OWNER_ID = "1248688275" # If you dont know, run @MissRose_bot and do /id in pm
    OWNER_USERNAME = "xy0ke"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'sqldbtype://username:pw@hostname:port/db_name'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /
    API_OPENWEATHER = False #Get API_OPENWEATHER FROM OFFICAL SITE https://da.gd/VAW3
    TEMPORARY_DATA = None # Temporary data for backup module, use int number


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
