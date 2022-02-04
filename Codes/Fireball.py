import pygame
from Codes.Settings import *

RED = (255, 0, 0)
YELLOW = (0, 255, 255)

class Fireball(pygame.sprite.Sprite):
    def __init__(self, posX, posY, direction, shootFrom):
        super().__init__()
        self.size = (fireballSize, fireballSize)
        self.posX = posX
        self.posY = posY
        self.direction = direction
        self.shootFrom = shootFrom
        self.image = pygame.Surface(self.size)
        if shootFrom == "Player":
            self.image.fill(RED)
        else:
            self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (self.posX, self.posY)

    def fly(self, fireBallGroup):
        if self.direction == 0:  # right
            self.posX += 15
        if self.direction == 1:  # up
            self.posY -= 15
        if self.direction == 2:  # left
            self.posX -= 15
        if self.direction == 3:  # down
            self.posY += 15
        self.rect.center = (self.posX, self.posY)
        return self.distroy(fireBallGroup)

    def distroy(self, fireBallGroup):
        if self.posX > SCREEN_WIDTH or self.posX < 0:
            fireBallGroup.remove(self)
            self.kill()
        elif self.posY > SCREEN_HEIGHT or self.posY < 0:
            fireBallGroup.remove(self)
            self.kill()

        return fireBallGroup
