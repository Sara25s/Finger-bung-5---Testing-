import subprocess
import sys

def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "../requirements.txt"])
        print("Alle Anforderungen wurden erfolgreich installiert.")
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Installieren der Anforderungen: {e}")

if __name__ == "__main__":
    install_requirements()
