import os
import discord
from dotenv import load_dotenv
print("Checking for .env file...")
if not os.path.exists(".env"):
    with open(".env", "w") as file:
        print("Environment file not found, creating a new one.")
        discord_token = input("Insert Discord Bot Token: ")
        file.write(f"DISCORD_TOKEN={discord_token}")
load_dotenv(override=True)

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
intents.guilds = True

bot = discord.Bot(intents=intents, debug_guilds=[1108473633191501935])

@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))

if __name__ == "__main__":
    for ex in os.listdir(os.getcwd() + '/cogs'):
        try:
            ex = ex.split('.')[0]
            bot.load_extension(f"cogs.{ex}")
            print(ex, 'loaded.')
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(ex, exc))
    bot.run(os.getenv("DISCORD_TOKEN"))