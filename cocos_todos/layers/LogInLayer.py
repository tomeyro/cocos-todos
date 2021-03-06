import cocos
import requests
import threading
from .BaseLayer import BaseLayer
from .WaveLayer import WaveLayer

token = ""
wave = []


class LogInLayer(BaseLayer):

    is_event_handler = True

    def __init__(self):
        super(LogInLayer, self).__init__(22, 22, 22, 255)

        self.email = cocos.menu.EntryMenuItem("Email:", self.do_nothing, "")

        self.password = cocos.menu.EntryMenuItem("Password:", self.on_password_entered, "")
        self.password_value = ""

        self.log_in = cocos.menu.MenuItem("Log in", self.try_log_in)

        menu = cocos.menu.Menu("TODO DESTROYER")
        menu.create_menu([self.email, self.password, self.log_in])
        self.add(menu)

        self.logging_in = False
        self.warning_message = ""
        self.warning_label = cocos.text.Label(
            self.warning_message,
            (self.get_window_width() / 2, 10),
            anchor_x="center"
        )
        self.add(self.warning_label)

        self.go_to_wave = False

    def on_password_entered(self, text):
        if len(text) > len(self.password_value):
            self.password_value += text[-1:]

        else:
            self.password_value = self.password_value[:-1]

        self.password.value = "*" * len(self.password_value)

    def try_log_in(self):
        if not self.logging_in:
            self.logging_in = True
            self.warning_message = "Trying to log in"
            log_in_thread = threading.Thread(target=self.request_log_in)
            log_in_thread.start()

        else:
            self.warning_message = "Wait please... Trying to log in"

    def request_log_in(self):
        log_in_request = requests.post(
            "http://todo-api.dlavieri.com/login",
            json={
                'email': self.email.value,
                'password': self.password_value
            }, headers={
                'Content-Type': "application/json"
            }
        )

        if log_in_request.status_code == 200:
            self.warning_message = "OK.. Getting first wave"
            global token
            token = log_in_request.json()[u'token']
            wave_request = requests.get(
                "http://todo-api.dlavieri.com/todo?page_size=10&filters=completed:true",
                headers={
                    'Content-Type': "application/json",
                    'Authorization': "Bearer " + token
                }
            )

            if wave_request.status_code == 200:
                global wave
                wave = wave_request.json()[u'todos']
                print("Found " + str(len(wave)))
                self.warning_message = "OK! Found " + str(len(wave)) + "!"
                self.go_to_wave = True

            else:
                self.warning_message = "Wave ERROR"

        else:
            self.warning_message = "Log in ERROR"

        self.logging_in = False

    def update(self, dt):
        super(LogInLayer, self).update(dt)

        self.warning_label.element.text = self.warning_message
        if self.go_to_wave:
            cocos.director.director.replace(WaveLayer.create_scene())
