<h1 align="center">#1 - Installation, importation et création du Bot</h1>

<br>

Dans ce premier volet de "**Créer un bot Discord avec `Python`**", nous allons voir les prérequis pour faire un bot. Nous allons ensuite installer tous les composants indispensables au développement de notre bot. Nous finirons ce tutoriel par initialiser notre Bot et apprendre à le démarrer.

<br>

## ⚠️Prérequis

Pour développer des bots discord via `Python`, vous avez besoin de télécharger :

Obligatoire : <br>
• `Python` : https://www.python.org/downloads/ <br>
• ` Editeur de texte` : https://www.jetbrains.com/fr-fr/pycharm/ (ou celui de votre choix)

Recommandé : <br>
• `Mon serveur discord d'aide` : https://discord.gg/EHbdMS9

Lorsque vous installez `Python`, n'oubliez pas de cochez la case "**Add Python to PATH**"
<br>
<img src="https://miro.medium.com/max/1344/0*7nOyowsPsGI19pZT.png" alt="MathieuLePuil" width="400px"/>

<br>

## 💽 Installation de discord.py

Pour installer `discord.py`, vous allez devoir ouvrir votre **Invites de commande** sur Windows et Linux ou **Terminal** sur Mac. Entrez ensuite la commande suivante selon votre système d'exploitation.

#### 🪟 Windows 

```commandline
py -3 -m pip install -U git+https://github.com/Rapptz/discord.py
```

#### 💻 MacOS / 🐧 Linux

```commandline
python3 -m pip install -U discord.py
```

<br>

## ⚙ Création du Bot

Pour créer le bot, rendez-vous sur votre portail développeur discord.

• `Portail développeur` : https://discord.com/developers/applications <br><br>

###Étapes de création d'un bot :

• Cliquez sur le bouton `New Application` <br>
<img src="https://poshbot.readthedocs.io/en/latest/guides/backends/discord-new-application.png" alt="MathieuLePuil" width="400px"/> <br>
• Donner un nom à votre bot puis cliquez sur `Create` <br>
• Vous pouvez ensuite lui ajouter une image (optionnel) dans le rectangle `APP ICON` <br>
• Rendez-vous ensuite dans l'onglet `Bot` sur la gauche <br>
• Cliquez sur `Add Bot` puis `Yes, do it !` <br>
<img src="https://images.ctfassets.net/a364c9khexw9/3mNda83bysuztw0cWp2lQr/ad952489adb2cab6716efedfc3326c0b/Screen_Shot_2020-09-12_at_2.35.29_AM.png" alt="MathieuLePuil" width="400px"/> <br>
• Cliquez sur `Reset Token` et gardez-le de côté pour le moment <br>
• Descendez sur la page et cochez le bouton `Presence Intent` <br>

Vous pouvez ensuite désactiver la case `Public Bot` afin que personne ne puisse l'ajouter sur son serveur sans votre autorisation.

Maintenant il vous reste simplement à suivre le code présent dans `main.py`. "Main" signifie "principal". Cela montre le fichier qui contient la racine du bot. Vous pouver le nommer comme vous le souhaitez. Le nom "*main*" est tout de même fortement recommandé.

## ❓ Besoin d'aide ?

Vous n'avez pas compris un point dans l'installation, la création du bot ou dans le code ? N'hésitez pas à faire un tour sur mon serveur Discord puis de vous rendre dans `#❓〡aide-discordpy` et ouvrez un ticket gâce au bouton.

Vous pouvez également me suggérer des fonctionnalités de Discord afin que j'agrémente le GitHub.

• `Mon discord` : https://discord.gg/EHbdMS9

### 👏 Bravo, vous venez de créer votre Bot Discord. Nous verrons dans la prochaine leçon comment créer notre première commande.

*Prochain cours le jeudi 7 Avril.*

---

Crédits: [Mathieu Le Puil](https://github.com/MathieuLePuil) <br>
Patreon: [MathieuLP](https://www.patreon.com/mathieulp)
