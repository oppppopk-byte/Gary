#######################模組#######################
import asyncio
import discord
import os
from dotenv import load_dotenv
#######################初始化#######################
load_dotenv()
asyncio.set_event_loop(asyncio.new_event_loop())
intents = discord.Intents.default()
intents.message_content = True
bot=discord.Client(intents=intents)
tree=discord.app_commands.CommandTree(bot)
#######################事件#######################
@bot.event
async def on_ready():
    print(f'{bot.user}is redy and online!')
    await tree.sync()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "hellow":
        await message.channel.send("Hey ")
#######################指令#######################
@tree.command(name="hellow",description="測試機器人是否在線")
async def hellow(interaction:discord.Interaction):
    """輸入/hellow.機器人會回傳HEY! """
    await interaction.response.send_message("Hey!")  
#######################啟動#######################
def main():
    bot.run(os.getenv("DC_BOT_TOKEN"))

if __name__ == "__main__":
    main()