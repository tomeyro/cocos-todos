import cocos
import pyglet
from .Bullet import PlayerBullet


class Player(cocos.sprite.Sprite):

    def __init__(self, position=(0, 0)):
        super(Player, self).__init__("assets/player.png", position=position)

        self.speed = 175
        self.velocity = (0, 0)

        self.weapon_cooling_time = 0.3
        self.current_cooling_time = 0.3
        self.bullets = []

        self.pressed_keys = []

    def on_key_press(self, key, modifiers):
        if key not in self.pressed_keys:
            self.pressed_keys.append(key)

    def on_key_release(self, key, modifiers):
        if key in self.pressed_keys:
            self.pressed_keys.remove(key)

    def update(self, dt):
        vx, vy = 0, 0
        if pyglet.window.key.RIGHT in self.pressed_keys or pyglet.window.key.D in self.pressed_keys:
            vx = self.speed
        elif pyglet.window.key.LEFT in self.pressed_keys or pyglet.window.key.A in self.pressed_keys:
            vx = -self.speed
        if pyglet.window.key.UP in self.pressed_keys or pyglet.window.key.W in self.pressed_keys:
            vy = self.speed
        elif pyglet.window.key.DOWN in self.pressed_keys or pyglet.window.key.S in self.pressed_keys:
            vy = -self.speed
        self.velocity = (vx, vy)

        self.position = (
            self.position[0] + (self.velocity[0]*dt),
            self.position[1] + (self.velocity[1]*dt)
        )

        self.current_cooling_time += dt
        if pyglet.window.key.SPACE in self.pressed_keys and self.current_cooling_time >= self.weapon_cooling_time:
            self.current_cooling_time = 0
            bullet = PlayerBullet(self.position)
            self.bullets.append(bullet)
            self.parent.add(bullet)
        for bullet in self.bullets:
            bullet.update(dt)
            if bullet.position[0] > self.parent.get_window_width():
                self.parent.remove(bullet)
                self.bullets.remove(bullet)
