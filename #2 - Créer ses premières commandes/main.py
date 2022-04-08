import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=">", description="test", intents=discord.Intents.all()) # on autorise ici toutes les intents (plus d'informations ici : https://discordpy.readthedocs.io/en/stable/intents.html)


@bot.event
async def on_ready():
    print("Le bot est démarré !")


@bot.command()  # créer une commande dans le bot
async def test(ctx):  # on définit dans une fonction asynchrone la commande (ici test) et on ajoute en paramètre le contexte (obligatoire dans les commandes)
    await ctx.send("Le test est validé !")  # on envoie "test" dans le salon où on a exécuté la commande


@bot.command()
async def latence(ctx):
    await ctx.send(f"**La latence du bot est de `{round(bot.latency * 1000)}ms`.**")  # on envoie le ping (ici en ms et arrondi) dans le salon où on a exécuté la commande. Le f avant les guillemets est indispensable pour entrer des valeurs entre accolades (ici la latence)


bot.run("TOKEN")
