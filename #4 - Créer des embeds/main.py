import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=">", description="test", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Le bot est démarré !")


@bot.command()
async def embed(ctx, pseudo, age):
    embed = discord.Embed(title = "Titre de l'embed", description = "Description de l'embed", color = 0xFFFFFF) # Définit l'embed sous le nom "embed", on lui ajoute un titre, une description et une couleur
    embed.add_field(name = "Nom de l'utilisateur", value = pseudo, inline = True) # On rajoute un champ de valeur qui sera à la même ligne que les autres champs de valeurs
    embed.add_field(name = "Âge de l'utilisateur", value = age, inline = True)
    embed.set_footer(text = "Ici c'est le footer") # on rajoute un footer à l'embed
    #embed.set_image(url="") # ajoute une image un l'embed
    #embed.set_thumbnail(url="") # ajoute un thumbnail à l'embed
    await ctx.send(embed = embed) # envoie l'embed dans le salon dans lequelle on a fait la commande


bot.run("TOKEN")