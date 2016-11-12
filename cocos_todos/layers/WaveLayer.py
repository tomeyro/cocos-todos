import cocos
from os.path import join
from .BaseLayer import BaseLayer


class WaveLayer(BaseLayer):

    def __init__(self):
        super(WaveLayer, self).__init__(0, 100, 200, 125)

        self.sprite = cocos.sprite.Sprite(
            join("assets", "ships.png"),
            position=(self.get_window_width()/2, self.get_window_height()/2)
        )
        self.add(self.sprite)

    def update(self, dt):
        super(WaveLayer, self).update(dt)
