import discord
from discord.ext import commands

config: list[str] = ["", ""]


def get_config():
    """
    Get default configs from config/config
    If a setting is missing in the config set it to a default value
    """
    prefix: bool = False
    status: bool = False

    line_num: int = 0

    bot_prefix: str = ""
    bot_status: str = ""

    config_file = open("config/config", "r")
    line_num += 1
    for line in config_file.readlines():
        if line.startswith(";"):  # ignore comments
            continue
        elif line.startswith("prefix:"):
            if not prefix:
                prefix = True
                bot_prefix = line.replace("prefix:", "")
                bot_prefix.replace(" ", "")
                print("Config: prefix set to " + bot_prefix)
            else:
                print("Config-error: [line " + str(line_num) + "] prefix was set before.")
        elif line.startswith("status:"):
            if not status:
                status = True
                bot_status = line.replace("status:", "")
                bot_status.replace(" ", "")
                print("Config: status set to " + bot_status)
            else:
                print("Config-error: [line " + str(line_num) + "] status was set before.")
        else:
            print("Config-error: [line " + str(line_num) + "] unrecognized value: " + line)
    if not prefix:
        bot_prefix = ","
        print("Config: prefix set to a default value    " + bot_prefix)
    if not status:
        bot_status = "hey!"
        print("Config: status set to a default value    " + bot_status)
    global config
    config = [bot_prefix, bot_status]


def get_token() -> str:
    try:
        token_file = open("token/.token", "r")
        token = token_file.readline()
        return token
    except IOError:
        print("Error reading token")


intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = commands.Bot(command_prefix=config[0], intents=intents)

client.run(get_token())
