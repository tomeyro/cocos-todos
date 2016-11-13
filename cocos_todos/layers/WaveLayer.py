from .BaseLayer import BaseLayer
from ..sprites.Player import Player


class WaveLayer(BaseLayer):

    is_event_handler = True

    def __init__(self):
        super(WaveLayer, self).__init__(0, 100, 200, 125)

        self.player = Player(
            position=(self.get_window_width() / 2, self.get_window_height() / 2)
        )
        self.add(self.player)

    def on_key_press(self, key, modifiers):
        self.player.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.player.on_key_release(key, modifiers)

    def update(self, dt):
        super(WaveLayer, self).update(dt)
        self.player.update(dt)
