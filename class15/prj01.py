#######################模組#######################
import asyncio
import discord
import os
import requests
from dotenv import load_dotenv
from gary.gary import WeatherAPI, AIAssistant

#######################初始化#######################
load_dotenv()
asyncio.set_event_loop(asyncio.new_event_loop())
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(bot)
weather_api = WeatherAPI(os.getenv("OPENWEATHER_API_KEY"))
ai_assistant = AIAssistant(os.getenv("OPENAI_API_KEY"))

# 限制讀取的歷史訊息數量，避免一次把整個頻道都交給 AI。
CHANNEL_HISTORY_LIMIT = 15

# system_prompt 像是給 AI 的角色卡，會影響 AI 回覆的語氣和工作方式。
CHAT_SYSTEM_PROMPT = """
你是一個在 Discord 群組頻道中協助大家的 AI 助手。
請根據頻道歷史判斷大家正在討論什麼，再回答最新提到你的問題。
回覆請使用繁體中文，語氣自然、簡短、適合國小學生閱讀。
如果頻道歷史不足以判斷答案，請說明你還需要哪一個資訊。
如果需要提到特定使用者或其他 bot，請複製歷史訊息裡的 mention：<@使用者ID>。
使用 mention 時，請直接放在一般文字中，不要寫成 @名字，也不要加反斜線、反引號或程式碼區塊。
不要使用 @everyone、@here 或角色標記，也不要自己編造 mention ID。
"""

# 允許 AI 回覆中提到「使用者或 bot」，但不要讓 AI 觸發 @everyone、@here 或角色標記。
# bot 在 Discord 裡也屬於 user，所以 users=True 就可以提到其他 bot。
AI_REPLY_ALLOWED_MENTIONS = discord.AllowedMentions(
    everyone=False,
    users=True,
    roles=False,
    replied_user=True,
)


def build_weather_embed(weather_summary):
    """把整理好的天氣摘要排成Discord卡片"""
    embed = discord.Embed(
        title=f"{weather_summary['city_name']}的當前天氣",
        description=weather_summary["description"],
        color=discord.Color.from_str("#1E90FF"),
    )
    icon_url = weather_api.get_icon_url(weather_summary["icon_code"])
    print(icon_url)
    embed.set_thumbnail(url=icon_url)

    embed.add_field(name="溫度", value=f"{weather_summary['temperature_celsius']}°C")
    return embed


def build_forecast_embed(forecast_summary):
    """把未來多筆資料排成Discord卡片"""
    embeds = []

    for forecast in forecast_summary:
        embed = discord.Embed(
            title=f"{forecast['city_name']}天氣預報-{forecast['datetime']}",
            description=f"描述:{forecast['description']}",
            color=discord.Color.from_str("#1E90FF"),
        )
        icon_url = weather_api.get_icon_url(forecast["icon_code"])
        embed.set_thumbnail(url=icon_url)
        embed.add_field(name="溫度", value=f"{forecast['temperature_celsius']}°C")
        embeds.append(embed)
    return embeds


async def get_channel_history(channel, bot_user, limit=15, before=None):
    """讀取 Discord 頻道中的舊訊息，整理成 OpenAI 可以使用的 messages。"""
    old_messages = []
    history_messages = []
    # Discord API 讀頻道訊息時，預設會先拿較新的訊息。
    # 這裡先明確抓「最近的幾則」，把「抓資料」和「排成對話順序」分成兩步。
    # oldest_first=False 代表先拿最接近 before 的新訊息。
    # 下面再反轉成「舊到新」交給 AI，比較像大家平常閱讀對話的順序。
    async for old_message in channel.history(
        limit=limit,
        before=before,
        oldest_first=False,
    ):
        old_messages.append(old_message)

    # Discord 抓回來的是「新到舊」，但 AI 閱讀對話時需要「舊到新」。
    for old_message in reversed(old_messages):
        # 這裡使用 message.content，而不是 clean_content。
        # message.content 會保留 <@使用者ID> 這種真正的 mention 格式。
        content = old_message.content.strip()
        if not content:
            continue  # 空白訊息不用交給 AI，避免浪費上下文空間

        if old_message.author.id == bot_user.id:
            # 機器人自己以前說過的話，用 assistant 角色放回歷史中。
            history_messages.append({"role": "assistant", "content": content})
        else:
            # 其他同學和其他 bot 都標上名字，AI 才知道是誰說的。
            speaker_type = "機器人" if old_message.author.bot else "同學"
            speaker_mention = old_message.author.mention
            user_content = (
                f"{old_message.author.display_name}"
                f"（{speaker_type}，mention：{speaker_mention}）說：{content}"
            )
            history_messages.append({"role": "user", "content": user_content})

    return history_messages


async def ask_with_discord_history(message):
    """當機器人被提到時，整理Discord頻道歷史訊息，交給AI分析後回覆"""
    history_messages = await get_channel_history(
        channel=message.channel,
        bot_user=bot.user,
        limit=CHANNEL_HISTORY_LIMIT,
        before=message,
    )

    user_question = message.content.replace(f"<@{bot.user.id}>", "").strip()
    if not user_question:
        user_question = "請根據前面的平到問題，接著回答。"

    user_message = (
        f"{message.author.display_name}"
        f"(mention:{message.author.mention})提到你：{user_question}"
    )

    return ai_assistant.ask(
        system_prompt=CHAT_SYSTEM_PROMPT,
        user_message=user_message,
        temperature=0.5,
        history_messages=history_messages,
    )


#######################事件#######################
@bot.event
async def on_ready():
    print(f"{bot.user}is redy and online!")
    await tree.sync()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "hellow":
        await message.channel.send("Hey ")
    elif bot.user in message.mentions:
        async with message.channel.typing():
            answer, error = await ask_with_discord_history(message)

        if error:
            await message.channel.send(error)
        else:
            await message.reply(
                answer,
                mention_author=True,
                allowed_mentions=AI_REPLY_ALLOWED_MENTIONS,
            )


#######################指令#######################
@tree.command(name="hellow", description="測試機器人是否在線")
async def hellow(interaction: discord.Interaction):
    """輸入/hellow.機器人會回傳HEY!"""
    await interaction.response.send_message("Hey!")


@tree.command(name="weather", description="查詢當前天氣")
async def weather(
    interaction: discord.Interaction,
    city: str,
    forecast: bool = False,
    ai: bool = False,
):
    """輸入/weather [城市名稱].機器人會回傳該城市的當前天氣"""
    await interaction.response.defer()  # 告訴Discord我們正在處理指令，避免超時

    city = city.strip()

    if not weather_api.api_key:
        await interaction.followup.send(
            "尚未設定 WEATHER_API_KEY請先在..env檔案中設定。"
        )
        return
    try:
        if not forecast:
            weather_summary = weather_api.get_weather_summary(city)
            print(weather_summary)
            if weather_summary is None:
                await interaction.followup.send(
                    f"找不到{city}的天氣資料，請確認城市名稱是否正確。"
                )
                return

            embed = build_weather_embed(weather_summary)  # 把天氣摘要整理成Discord卡片
            await interaction.followup.send(embed=embed)  # 把卡片回.傳給使用者
            return
        if not ai:
            forecast_summary = weather_api.get_forecast_summary(city)
            if forecast_summary is None:
                await interaction.followup.send(
                    f"找不到{city}的天氣預報資料，請確認城市名稱是否正確。"
                )
                return
            embeds = build_forecast_embed(
                forecast_summary
            )  # 把天氣摘要整理成Discord卡片
            await interaction.followup.send(embeds=embeds[:10])  # 把卡片回傳給
            return
        raw_forecast = weather_api.get_forecast(city)
    except (requests.RequestException, ValueError):
        await interaction.followup.send(embeds=embeds)  # 把卡片回傳給使用者
        return
    analysis, error = ai_assistant.ask(
        system_prompt="你是一個天氣分析師，請根據提供的天氣預報資料進行分析，並提供有用的建議。",
        user_message=f"請分析以下天氣預報資料，並提供建議:\n{raw_forecast}",
    )

    if error:
        await interaction.followup.send(error)
    else:
        await interaction.followup.send(f"**{city}的天氣分析與建議:**\n{analysis}")


#######################啟動#######################
def main():
    bot.run(os.getenv("DC_BOT_TOKEN"))


if __name__ == "__main__":
    main()
