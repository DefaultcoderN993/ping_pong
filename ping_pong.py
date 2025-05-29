import pygame as pg

window = pg.display.set_mode((700, 500))
clock = pg.time.Clock()
pg.display.set_caption('Ping Pong')

class GameSprite(pg.sprite.Sprite):
    def __init__(self, speed, p_image, x, y, scale_x, scale_y):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(p_image), (scale_x, scale_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = pg.key.get_pressed()
        if keys_pressed[pg.K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[pg.K_s] and self.rect.y < 395:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys_pressed = pg.key.get_pressed()
        if keys_pressed[pg.K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[pg.K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed

player1 = Player(7, 'рокетка.png', 650, 250, 50, 100)
player2 = Player2(7, 'рокетка.png', 5, 250, 50, 100)

game = True
while game:
    player1.draw()
    player2.draw()
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False
    player1.update()
    player2.update()
    clock.tick(40)
    pg.display.update()