import subprocess
import requests

def check_discord_update():
    # Get current installed version
    process = subprocess.Popen(["pacman", "-Qi", "discord"], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    current_version = None
    for line in output.decode().split('\n'):
        if line.startswith("Version"):
            current_version = line.split(": ")[1]
            break

    # Get latest version from Discord API
    latest_version = requests.get("https://discord.com/api/updates/stable/0/latest").json()["name"]

    # Compare versions
    if current_version != latest_version:
        print(f"New version available: {latest_version}")
        subprocess.run(["sudo", "pacman", "-Syu", "--noconfirm", "discord"])
        print(f"Discord updated to {latest_version}")
    else:
        print("Discord is up to date")

if __name__ == "__main__":
    check_discord_update()
