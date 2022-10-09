import discord
from discord.ext import commands

config: list[str] = ["", ""]


def get_config():
    """
    Get default configs from config/config
    If a setting is missing in the config set it to a default value
    """
    prefix: bool = False  # used to check if prefix was set multiple times
    status: bool = False  # used to check if status was set multiple times

    line_num: int = 0  # line count

    # used to store configs
    bot_prefix: str = ""
    bot_status: str = ""

    config_file = open("config/config", "r")
    for line in config_file.readlines():
        line_num += 1
        if line.startswith(";"):  # ignore comments
            continue
        elif line.startswith("prefix:"):  # if the line in config file starts with "prefix:"
            if not prefix:  # and the prefix wasn't set before
                prefix = True
                bot_prefix = line.replace("prefix:", "")  # remove "prefix:"
                bot_prefix.replace(" ", "")  # and whitespaces
                print("Config: prefix set to " + bot_prefix)
            else:
                print("Config-error: [line " + str(line_num) + "] prefix was set before.")
        elif line.startswith("status:"):  # do the same for "status:"
            if not status:
                status = True
                bot_status = line.replace("status:", "")
                bot_status.replace(" ", "")
                print("Config: status set to " + bot_status)
            else:
                print("Config-error: [line " + str(line_num) + "] status was set before.")
        else:  # return error when user is trying to change non-existent setting
            print("Config-error: [line " + str(line_num) + "] unrecognized value: " + line)
    # if there are values missing in config file, set them to defaults
    if not prefix:
        bot_prefix = ","
        print("Config: prefix set to a default value    " + bot_prefix)
    if not status:
        bot_status = "hey!"
        print("Config: status set to a default value    " + bot_status)
    global config
    config = [bot_prefix, bot_status]


def get_token() -> str:
    """
    Returns token as string
    Token should be located in token/.token
    """
    try:
        token_file = open("token/.token", "r")
        return token_file.readline()
    except IOError:
        print("Error reading token")


intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = commands.Bot(command_prefix=config[0], intents=intents)

token = get_token()
if token.isspace():  # exit if token is empty
    print("No token specified! Put token in token/.token")
    exit()

# run the bot
client.run(token)
