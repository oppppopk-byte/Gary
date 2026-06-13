#######################模組#######################
import asyncio
import discord
import os
import requests
from dotenv import load_dotenv
from gary.gary import WeatherAPI
#######################初始化#######################
load_dotenv()
asyncio.set_event_loop(asyncio.new_event_loop())
intents = discord.Intents.default()
intents.message_content = True
bot=discord.Client(intents=intents)
tree=discord.app_commands.CommandTree(bot)
weather_api = WeatherAPI(os.getenv("OPENWEATHER_API_KEY"))
def build_weather_embed(weather_summary):
    """把整理好的天氣摘要排成Discord卡片"""
    embed = discord.Embed(
        title=f"{weather_summary['city_name']}的當前天氣",
        description=weather_summary['description'],
        color=discord.Color.from_str("#1E90FF")
    )
    icon_url = weather_api.get_icon_url(weather_summary['icon_code'])
    embed.set_thumbnail(url=icon_url)

    embed.add_field(name="溫度", value=f"{weather_summary['temperature_celsius']}°C")
    return embed
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


@tree.command(name="weather",description="查詢當前天氣")
async def weather(interaction:discord.Interaction, city_name:str):
    """輸入/weather [城市名稱].機器人會回傳該城市的當前天氣"""  
    await interaction.response.defer() #告訴Discord我們正在處理指令，避免超時

    city=city_name.strip()

    if not weather_api.api_key:
        await interaction.followup.send("尚未設定 WEATHER_API_KEY請先在..env檔案中設定。")
        return 
    try:
        #向OpenWeatherAPI請求天氣資料
        #主程式只處理結果，把API的細節封裝在WeatherAPI類別裡
        weather_summary = weather_api.get_weather_summary(city)
    except (requests.RequestException, ValueError):
        await interaction.followup.send("無法取得天氣資料，請稍後再試。")
        return 

    if weather_summary is None:
        #如果API回傳的資料不包含預期的欄位，或是城市名稱無效，就會得到None
        await interaction.followup.send(f"找不到{city}的天氣資料，請確認城市名稱是否正確。")
        return
    
    embed = build_weather_embed(weather_summary)#把天氣摘要整理成Discord卡片
    await interaction.followup.send(embed=embed)#把卡片回.傳給使用者
#######################啟動#######################
def main():
    bot.run(os.getenv("DC_BOT_TOKEN"))

if __name__ == "__main__":
    main()