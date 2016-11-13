import cocos


class Bullet(cocos.sprite.Sprite):

    def __init__(self, image, position):
        super(Bullet, self).__init__(image, position=position, scale=0.5)
        self.speed = 225
        self.velocity = (0, 0)

    def update(self, dt):
        self.position = (
            self.position[0] + (self.velocity[0]*dt),
            self.position[1] + (self.velocity[1]*dt)
        )


class PlayerBullet(Bullet):

    def __init__(self, position):
        super(PlayerBullet, self).__init__("assets/player_bullet.png", position)
        self.velocity = (self.speed, 0)


class EnemyBullet(Bullet):

    def __init__(self, position):
        super(EnemyBullet, self).__init__("assets/enemy_bullet.png", position)
        self.velocity = (-self.speed, 0)
