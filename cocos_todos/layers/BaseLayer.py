import cocos


class BaseLayer(cocos.layer.ColorLayer):

    def __init__(self, r, g, b, a, width=None, height=None):
        super(BaseLayer, self).__init__(r, g, b, a, width=width, height=height)

        self.schedule(self.update)

    def update(self, dt):
        pass

    @staticmethod
    def get_window_width():
        return cocos.director.director.get_window_size()[0]

    @staticmethod
    def get_window_height():
        return cocos.director.director.get_window_size()[1]

    def do_nothing(self, *args, **kwargs):
        pass

    @classmethod
    def create_scene(cls):
        return cocos.scene.Scene(cls())
