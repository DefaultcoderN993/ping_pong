import pygame as pg

WIDTH = 700
HEIGHT = 500
window = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption('Ping Pong')

background = pg.transform.scale(
    pg.image.load("forest.jpg"),
    (WIDTH, HEIGHT)
)

BLACK = (0, 0, 0)

class GameSprite(pg.sprite.Sprite):
    def __init__(self, speed, p_image, x, y, width, height, bg_color=BLACK):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(p_image), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.bg_color = bg_color
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def fill(self, color=None):
        if color is None:
            pg.draw.rect(window, self.bg_color, self.rect)
        else:
            pg.draw.rect(window, color, self.rect)

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

class Ball(GameSprite):
    def __init__(self, speed, p_image, x, y, width, height, bg_color=BLACK):
        super().__init__(speed, p_image, x, y, width, height, bg_color)
        self.speed_x = speed
        self.speed_y = speed
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y > HEIGHT - self.rect.height or self.rect.y < 0:
            self.speed_y *= -1
        if self.rect.x > WIDTH - self.rect.width:
            player2_score += 1
        if self.rect.x < self.rect.x < 0:
            player1_score += 1
        if pg.sprite.collide_rect(player1, ball) or pg.sprite.collide_rect(player2, ball):
            self.speed_x *= -1

class Game():
    run = True
    finish = False
    player1_score = 0
    player2_score = 0

player1 = Player(7, 'рокетка.png', 620, 250, 75, 100)
player2 = Player2(7, 'рокетка.png', 0, 250, 75, 100)
ball = Ball(3, 'мяч.png', 350, 250, 50, 50)

game = Game()
while game.run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game.run = False
    if not game.finish:
        window.blit(background, (0, 0))
        player1.fill()
        player2.fill()
        ball.fill()
        player1.draw()
        player2.draw()
        ball.draw()
        player1.update()
        player2.update()
        ball.update()
        clock.tick(40)
        pg.display.update()