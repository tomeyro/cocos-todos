import cocos
import threading
import requests
import pyglet


class BaseLayer(cocos.layer.ColorLayer):

    def __init__(self, r, g, b, a, width=None, height=None):
        super(BaseLayer, self).__init__(r, g, b, a, width=width, height=height)

        self.schedule(self.update)

    def update(self, dt):
        pass

    def get_window_width(self):
        return cocos.director.director.get_window_size()[0]

    def get_window_height(self):
        return cocos.director.director.get_window_size()[1]

    @classmethod
    def create_scene(cls):
        return cocos.scene.Scene(cls())


class MainLayer(BaseLayer):

    is_event_handler = True

    def __init__(self):
        super(MainLayer, self).__init__(22, 22, 22, 255)

        email_label = cocos.text.Label(
            text='Email',
            position=((self.get_window_width() / 2) - 100, (self.get_window_height() / 2)- 100)
        )
        self.email_value = ''
        self.email_input = cocos.text.Label(
            position=((self.get_window_width() / 2), (self.get_window_height() / 2) - 100),
            color=(200, 200, 200, 255)
        )
        self.add(email_label)
        self.add(self.email_input)

    def on_text(self, text):
        self.email_value += text

    def on_key_press(self, key, modifiers):
        if key == pyglet.window.key.BACKSPACE:
            self.email_value = self.email_value[:-1]
        if key == pyglet.window.key.RETURN:
            pass

    def the_thread(self):
        pass
        # r = requests.get('http://www.tomas.com.ve')
        # self.text = r.text

    def update(self, dt):
        super(MainLayer, self).update(dt)

        self.email_input.element.text = self.email_value


cocos.director.director.init(width=800, height=480, caption="Todo Destroyer")
cocos.director.director.run(MainLayer.create_scene())
