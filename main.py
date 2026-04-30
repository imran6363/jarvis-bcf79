import threading
from voice.wake import detect
from voice.stt import listen
from voice.tts import speak
from core.router import process
from ui.hud import JarvisUI

def jarvis_loop():
    speak("System ready")

    while True:
        detect()
        speak("Yes?")

        cmd = listen()

        if cmd:
            print("You:", cmd)

            if "exit" in cmd:
                speak("Shutting down")
                break

            res = process(cmd)
            speak(res)

threading.Thread(target=jarvis_loop).start()
JarvisUI().run()
