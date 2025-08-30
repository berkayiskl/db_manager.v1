import discord
from discord.ext import commands     # Gerekli Modül Ve Kütüphaneleri Ekliyoruz!
from discord.utils import get
import sqlite3

# Token Alıyoruz!

TOKEN = "BOTUNUZUN_TOKENİNİ_BURAYA_YAZIN"

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Komutları Çalıştırmak İçin Gerekli İşaretimiz!

bot = commands.Bot(command_prefix="!", intents=intents)

# Veritabanımızı Botumuza Entegre Ediyoruz!

conn = sqlite3.connect("football.db")
cursor = conn.cursor()

# Botumuz Sorunsuz Çalışıyorsa Terminalde Bu mesajı Alacağız!
@bot.event
async def on_ready():
    print(f"{bot.user.name} botu çalışmaya hazır!")

@bot.event
async def on_member_join(member):
    channel = get(member.guild.text_channels, name="ortak")
    if channel:
        await channel.send(f"Sunucuya hoş geldin, {member.mention}!")

# Basit Komutlar!
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Merhaba, {ctx.author.mention}!")

# Kullanıcının Mesajını Tekrarlayan !echo Komutu
@bot.command()
async def echo(ctx, *, message: str):
    await ctx.send(message)


# Veritabanımızdan Veri Çekerek Komutlar Oluşturuyoruz! 
@bot.command()
async def worldcup(ctx):
    cursor.execute("SELECT year, champion FROM world_cup")
    records = cursor.fetchall()
    if records:
        text = "\n".join([f"Turnuva: {r[0]} | Şampiyon: {r[1]}" for r in records])
        await ctx.send(text[:4000])
    else:
        await ctx.send("Hiç Veri Bulunamadı!")

@bot.command()
async def rank(ctx):
    cursor.execute("SELECT team, rank FROM fifa_rank")
    records = cursor.fetchall()
    if records:
        text = "\n".join([f"Takım: {r[0]} | Fifa Sırası: {r[1]}" for r in records])
        await ctx.send(text[:2000])
    else:
        await ctx.send("Hiç Veri Bulunamadı!")

@bot.command()
async def matches(ctx):
    cursor.execute("SELECT home_team, away_team, home_score, away_score FROM matches")
    records = cursor.fetchall()
    if records:
        text = "\n".join([f"{r[0]} {r[2]} - {r[3]} {r[1]}" for r in records])
        await ctx.send(text[:1000])
    else:
        await ctx.send("Hiç Veri Bulunamadı!")

# Yanlış Bir Komut Girersek Alacağımız Mesajları Ekliyoruz!
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Lütfen gerekli tüm argümanları sağlayın")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Komut bulunamadı!")
    else:
        await ctx.send(f"Komut çalıştırılırken bir hata oluştu: {error}")

# Botumuzu Çalışır Hale Getiriyoruz!
bot.run(TOKEN)
