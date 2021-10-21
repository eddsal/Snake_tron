import pygame
import sys
from pygame.locals import *
import random

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()


BLACK = (0, 0, 0)
DISPLAYSURF = pygame.display.set_mode((400, 400))
DISPLAYSURF.fill(BLACK)
pygame.display.set_caption("Game")


class Apple(pygame.sprite.Sprite):
    def __init__(self, xpos):
        super().__init__()
        self.image = pygame.image.load("apple.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = [x for x in xpos]

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("apple.png")
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top < 400:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < 400:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 400:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


apples = []
xpos = []

for i in range(15):
    xpos.append([random.randint(0, 500), random.randint(0, 500)])
for i in range(15):
    print(xpos)
    apples.append(Apple(xpos[i]))

print(apples)

E1 = Snake()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(BLACK)
    for a in apples:
        a.draw(DISPLAYSURF)
    E1.update()
    E1.draw(DISPLAYSURF)
    pygame.display.update()
    FramePerSec.tick(FPS)
