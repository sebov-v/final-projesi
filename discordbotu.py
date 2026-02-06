import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents) #prefix olup olmadan fark etmiyor

# Basit görsel linkleri (gerçek ve güvenilir)
IMAGES = {
    "nedir": "https://climate.nasa.gov/system/internal_resources/details/original/647_Climate_Change_Indicators.jpg",
    "neden": "https://climate.nasa.gov/system/internal_resources/details/original/651_co2-graph-021916.jpg",
    "sonuc": "https://climate.nasa.gov/system/internal_resources/details/original/648_sea_level_rise.jpg",
    "cozum": "https://climate.nasa.gov/system/internal_resources/details/original/652_global_temp.jpg",
    "link": "https://climate.nasa.gov/system/internal_resources/details/original/646_earth-at-night.jpg"
}

@bot.event
async def on_ready():
    print(f"{bot.user} aktif! 🌍")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content.lower()
    gorsel_istendi = "(görsel)" in msg

    async def send_with_optional_image(text, image_key=None, title=""):
        if gorsel_istendi and image_key:
            embed = discord.Embed(
                title=title,
                description=text,
                color=0x2ecc71
            )
            embed.set_image(url=IMAGES[image_key])
            await message.channel.send(embed=embed)
        else:
            await message.channel.send(text)
    

    if "iklim değişikliği nedir" in msg:
        await send_with_optional_image(
            "🌍 **İklim Değişikliği Nedir?**\n"
            "İklim değişikliği, Dünya’nın uzun yıllardır sahip olduğu "
            "hava düzeninin bozulmasıdır 😵‍💫",
            image_key="nedir",
            title="İklim Değişikliği"
        )

    elif "neden oluyor" in msg or "nedenleri" in msg:
        await send_with_optional_image(
            "🔥 **Neden Oluyor?**\n"
            "Fabrikalar 🏭, arabalar 🚗, fosil yakıtlar ve ormanların kesilmesi 🌳❌ "
            "sera gazlarını artırır ve Dünya’yı ısıtır 🥵",
            image_key="neden",
            title="İklim Değişikliğinin Nedenleri"
        )

    elif "sonuçları neler" in msg or "etkileri" in msg:
        await send_with_optional_image(
            "❄️➡️💧 **Sonuçları / Etkileri**\n"
            "- Buzullar eriyor ❄️😢\n"
            "- Deniz seviyesi yükseliyor 🌊\n"
            "- Kuraklık ve seller artıyor 🌵⛈️\n"
            "- Hayvanlar yaşam alanlarını kaybediyor 🐧💔",
            image_key="sonuc",
            title="İklim Değişikliğinin Sonuçları"
        )

    elif "ne yapabiliriz" in msg or "çözüm" in msg:
        await send_with_optional_image(
            "💚 **Ne Yapabiliriz?**\n"
            "- Geri dönüşüm ♻️\n"
            "- Su ve elektrik tasarrufu 🚿💡\n"
            "- Ağaç dikmek 🌳\n"
            "- Doğayı korumak 🌍✨",
            image_key="cozum",
            title="Çözüm Yolları"
        )

    elif "site" in msg or "link" in msg:
        await send_with_optional_image(
            "🔗 **Güvenilir Kaynak:**\n"
            "🌍 NASA – Climate Change\n"
            "https://climate.nasa.gov/",
            image_key="link",
            title="İklim Değişikliği Kaynağı"
        )

    await bot.process_commands(message)

# BOT TOKENİNİ BURAYA YAZ
bot.run("")
