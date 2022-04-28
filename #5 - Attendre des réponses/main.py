import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=">", description="test", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Le bot est démarré !")


@bot.command()
async def commander(ctx):
    await ctx.send("Que voulez-vous commander ?")

    def checkMessage(message): # création de la fonction pour vérifier le message
        return message.author == ctx.message.author and ctx.message.channel == message.channel # on vérifie que l'auteur du message de réponse est le même que celui qui a fait la commande et qu'il est dans le même channel que celle-ci

    try:
        commande = await bot.wait_for("message", timeout = 10, check = checkMessage) # on attend le message pendant maximum 10 secondes et on vérifie grâce à la fonction checkMessage si tout est respecté
    except:
        await ctx.send("Vous avez été trop long, veuillez refaire la commande !") # si les 10 secondes sont passées, on envoie ce message
        return # on arrête le processus

    message = await ctx.send(f"Nous préparons votre commande ({commande.content}). Cochez la réaction ✅ pour valider, ou cochez la réaction ❌ pour annuler !") # commande.content = contenu du message de commande
    await message.add_reaction("✅") # ajoute la réaction au message ci-dessus
    await message.add_reaction("❌")

    def checkEmoji(reaction, user): # création de la fonction pour vérifier la réaction
        return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌") # on vérifie que l'auteur de la réaction est le même que celui qui a fait la commande, qu'il est dans le même channel que celle-ci et que la réaction est une des deux proposées et non une rajoutée
    try:
        reaction, user = await bot.wait_for("reaction_add", timeout = 10, check = checkEmoji) # on attend le message pendant maximum 10 secondes et on vérifie grâce à la fonction checkEmoji si tout est respecté
        if reaction.emoji == "✅": # on regarde si la réaction est ✅
            await ctx.send("Votre commandee a été expédiée !")
        else: # si ce n'est pas la réaction ✅, on exécute ce code
            await ctx.send("Nous annulons votre commande !")

    except:
        await ctx.send("Votre temps de réponse est trop long, veuillez recommencer !") # si les 10 secondes sont passées, on envoie ce message
        return  # on arrête le processus


bot.run("TOKEN")