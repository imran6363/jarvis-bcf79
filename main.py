from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from mic import listen
from voice import speak
from brain import process
import threading

class JarvisApp(App):
    def build(self):
        layout = BoxLayout()
        threading.Thread(target=self.run_jarvis).start()
        return layout

    def run_jarvis(self):
        speak("Bangladesh Cyber Force 79 system online")

        while True:
            cmd = listen()

            if cmd:
                print("You:", cmd)
                res = process(cmd)

                if res == "exit":
                    speak("Shutting down")
                    break

                speak(res)

JarvisApp().run()
