from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
import random

class HackerUI(App):
    text = "Initializing JARVIS..."

    def build(self):
        self.label = Label(text=self.text, font_size=18)
        Clock.schedule_interval(self.animate, 0.2)
        return self.label

    def animate(self, dt):
        chars = "01#@$%"
        self.label.text = "".join(random.choice(chars) for _ in range(40))
