import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=">", description="test", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Le bot est démarré !")


@bot.event
async def on_message(message):  # On exécute le script lorsqu'un message est envoyé dans un salon
    if message.author == bot.user:  # On vérifie si le message a été envoyé par le bot
        return  # Si oui, on arrête le processus
    await message.channel.send(f"> {message.content}\n{message.author}")  # Si non, on envoie les informations du message dans le salon où il a été envoyé


@bot.event
async def on_message_delete(message):  # On exécute le script lorsqu'un message est supprimé
    await message.channel.send(f"Le message de {message.author} a été supprimé \n> {message.content}")  # On envoie l'auteur et le contenu du message dans le channel où il a été supprimé


@bot.event
async def on_message_edit(before, after):  # On exécute le script lorsqu'un message est modifié
    await before.channel.send(f"{before.author} a édité son message :\nAvant -> {before.content}\nAprès -> {after.content}")  # On envoie le contenu du message avant et après dans le channel où il a été modifié


@bot.event
async def on_member_join(member):  # On exécute le script un utilisateur rejoint le serveur
    channel = member.guild.get_channel("ID du channel de bienvenue")  # Séléction du channel de bienvenue où envoyer le message
    await channel.send(f"Acceuillons a bras ouvert {member.mention} ! Bienvenue dans ce magnifique serveur :)")  # Envoie du message de bienvenue dans le channel paramétré


@bot.event
async def on_member_remove(member):  # On exécute le script un utilisateur quitte le serveur
    channel = member.guild.get_channel(714786510238384532)  # Séléction du channel de départ où envoyer le message
    await channel.send(f"En cette belle journée nous déplorons la perte d'un membre bien aimé, {member.mention}.")  # Envoie du message de départ dans le channel paramétré


@bot.event
async def on_reaction_add(reaction, user):  # On exécute le script lorsqu'une réaction est ajouté sur un message
    await reaction.message.add_reaction(reaction.emoji)  # Le bot ajoute lui-même une deuxième réaction à la première mise par l'utilisateur


@bot.event
async def on_typing(channel, user, when):  # On exécute le script lorsqu'un utilisateur commence à taper dans le salon
    await channel.send(f"{user.name} a commencé à écrire dans ce channel le {when}.") # Envoie d'un message informant de la personne qui est en train d'écrire et à quelle date/heure


bot.run("NzM2MjE5Njg1MTQxNjEwNTE2.G6JQQ0.JAlZKL63UpYDcdj5phBTii31GJ2F6UE0GerG4Q")