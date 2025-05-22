from pygame import *

window = display.set_mode((700, 500))
clock = time.Clock()
display.set_caption('Ping Pong')
class GameSprite(sprite.Sprite):
    def __init__(self, speed, p_image, x, y, scale_x, scale_y):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (scale_x, scale_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 595:
            self.rect.x += self.speed
game = True
while game:
	for e in event.get():
        	if e.type == QUIT:
            		game = False
	clock.tick(40)
	display.update()