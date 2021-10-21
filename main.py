import pygame
import sys
from pygame.locals import *
import random

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()


BLACK = (0, 0, 0)
DISPLAYSURF = pygame.display.set_mode((400, 600))
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


apples = []
xpos = []

for i in range(15):
    xpos.append([random.randint(0, 500), random.randint(0, 500)])
for i in range(15):
    print(xpos)
    apples.append(Apple(xpos[i]))

print(apples)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(BLACK)
    for a in apples:
        a.draw(DISPLAYSURF)
    pygame.display.update()
    FramePerSec.tick(FPS)
