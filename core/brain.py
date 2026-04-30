from datetime import datetime
import os

def process(cmd):
    cmd = cmd.lower()

    if "hello" in cmd:
        return "Hello Imran, system online."

    elif "time" in cmd:
        return datetime.now().strftime("%H:%M")

    elif "youtube" in cmd:
        os.system("xdg-open https://youtube.com")
        return "Opening YouTube"

    elif "exit" in cmd:
        return "exit"

    return "Command not recognized"
