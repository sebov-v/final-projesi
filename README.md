
## Projemizin türü:
> biz çevre kirliliği ile ilgili bir discord botu yapacağız. Bu bot çevre kirliliği ile ilgili herhangi bir soru sorduğumuzda yapabildiği kadar detaylı cevaplayacak

## Kullanacağımız kütüphaneler:
- discord

## İşe yarayabilecek referanslar:
- Referans 1 chatgpt
  
  import discord
  from discord.ext import commands
  import random

  intents = discord.Intents.default()
  bot = commands.Bot(command_prefix="!", intents=intents)

  cevre_sorunlari = [
      "🌍 **Küresel Isınma:** Dünya sıcaklığı insan faaliyetleri nedeniyle artıyor.",
      "🌊 **Deniz Kirliliği:** Plastik ve atıklar deniz canlılarını tehdit ediyor.",
      "🌳 **Ormansızlaşma:** Ağaçların yok edilmesi ekosistemi bozuyor.",
      "🏭 **Hava Kirliliği:** Fabrika ve araç gazları sağlığı olumsuz etkiliyor."
  ]

  @bot.event
  async def on_ready():
      print(f"{bot.user} olarak giriş yapıldı!")

  @bot.command()
  async def cevre(ctx):
      mesaj = random.choice(cevre_sorunlari)
      await ctx.send(mesaj)

  bot.run("BURAYA_BOT_TOKENINI_YAZ")


## Geliştirme sırasında bize yardımcı olabilecek kılavuz kaynaklar
vikipedia , chatgpt veya google kullanacağız.
