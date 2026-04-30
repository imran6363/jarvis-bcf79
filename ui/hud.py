from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.clock import Clock

class HUD(Widget):
    angle = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.animate, 0.05)

    def animate(self, dt):
        self.canvas.clear()

        with self.canvas:
            Color(0, 1, 1)
            self.angle += 4

            Line(circle=(300, 400, 150, 0, self.angle), width=2)
            Line(circle=(300, 400, 100, self.angle, self.angle+120), width=1)

class JarvisUI(App):
    def build(self):
        return HUD()
