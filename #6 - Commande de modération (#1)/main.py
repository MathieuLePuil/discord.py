import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=">", description="test", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Le bot est démarré !")


@bot.command()
@commands.has_permissions(ban_members=True)  # ajoute la permission de faire la commande uniquement aux personnes qui peuvent bannir
async def ban(ctx, user: discord.User, *, reason):  # user : discord.User signifie que nous allons devoir mentionner quelqu'un dans la commande
    await ctx.guild.ban(user, reason=reason)  # cette fonction va bannir "user" et la raison affichée dans discord sera "reason"
    await ctx.send(f"{user} a été ban pour {reason}")


@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, user, *, reason):  # ici, on ne met pas "user : discord.User" car l'utilisateur ne peut pas être mentionné, car il n'est pas sur le serveur
    userName, userId = user.split("#")  # Lorsque nous allons entrer un pseudo (ex: Dr3Xt3r#0001), cette partie de code va permettre de le couper en deux à partir du #. Dr3Xt3r sera l'"userName" et 0001 l'"userId"
    bannedUsers = await ctx.guild.bans()  # on récupère ici la liste des utilisateurs bannis sur le serveur
    for i in bannedUsers:  # on vérifie dans la liste de toutes les personnes bannies
        if i.user.name == userName and i.user.discriminator == userId:  # on regarde si un utilisateur a le même pseudo et ID dans la liste des bannis que celui qu'on avait mis dans la commande
            await ctx.guild.unban(i.user, reason=reason)  # on dé-banni l'utilisateur du serveur
            await ctx.send(f"{user} a été unban")
        else:  # si aucun pseudo / ID ne correspond, on exécute le code suivant
            await ctx.send(f"L'utilisateur {user} ne figure pas dans la liste des bannis")


@bot.command()
@commands.has_permissions(kick_members=True)  # ajoute la permission de faire la commande uniquement aux personnes qui peuvent kick
async def kick(ctx, user: discord.User, *, reason):
    await ctx.guild.kick(user, reason=reason)
    await ctx.send(f"{user} a été kick pour {reason}")


@bot.command()
@commands.has_permissions(kick_members=True)
async def clear(ctx, nombre: int):  # On précise que le paramètre nombre sera forcément une integer (suite de nombre)
    messages = await ctx.channel.history(limit=nombre + 1).flatten()  # on récupère le nombre de messages indiqué dans la commande + le message de la commande dans le channel où elle a été faite
    for message in messages:  # pour tous les messages qui sont dans la liste
        await message.delete()  # on les supprime


bot.run("NzM2MjE5Njg1MTQxNjEwNTE2.G6JQQ0.JAlZKL63UpYDcdj5phBTii31GJ2F6UE0GerG4Q")
