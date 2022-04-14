import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=">", description="test", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Le bot est démarré !")


@bot.command()
async def coucou(ctx, *, pseudo): # on rajoute entre parenthèse le(s) paramètre(s) qu'on souhaite. Ici, uniquement "pseudo". L'astérisque sert uniquement à indiquer que le paramètre pseudo peut contenir des espaces
    await ctx.send(f"Coucou {pseudo} !") # envoie le message avec le pseudo indiqué das la commandes


@bot.command()
@commands.has_permissions(kick_members = True) # donne la permission de faire la commande à toutes les personnes qui peuvent expulser des utilisateurs du serveur
async def modo(ctx):
    await ctx.send("Vous avez la permission !")


@bot.event
async def on_command_error(ctx, error): # on définit un event qui réagira lorsqu'il y aura une erreur dans une commande
    if isinstance(error, commands.MissingPermissions): # Si l'erreur est une permission manquante (comme dans >modo) il exécutera le script ci-dessous
        await ctx.send("Vous n'avez pas la permission !")


bot.run("TOKEN")