import discord # importation du module de discord
from discord.ext import commands # importation des commandes via le module "discord.ext"

bot = commands.Bot(command_prefix=">") # Définir le bot et son prefix | Vous pouvez choisir le prefix que vous souhaitez. Il suffit de remplacer le ">"

@bot.event #on créer un évènement qui va se dérouler lors d'une certaine action
async def on_ready(): #on définit que cette action est "on_ready", ce qui s'activera lors du démarrage du bot
    print("Le bot est démarré!") #On envoie un message de confirmation dans la console

bot.run("TOKEN") #Collez votre token à la place de "TOKEN" (les guillemets sont indispensables)