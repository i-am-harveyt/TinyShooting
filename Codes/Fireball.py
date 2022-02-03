import pygame

RED = (255, 0, 0)
YELLOW = (0, 255, 255)

class Fireball(pygame.sprite.Sprite):
    def __init__(self, posX, posY, direction, shootFrom, fireballSize):
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

    def fly(self, fireBallGroup, WIDTH, HEIGHT):
        if self.direction == 0:  # right
            self.posX += 40
        if self.direction == 1:  # up
            self.posY -= 40
        if self.direction == 2:  # left
            self.posX -= 40
        if self.direction == 3:  # down
            self.posY += 40
        self.rect.center = (self.posX, self.posY)
        return self.distroy(fireBallGroup, WIDTH, HEIGHT)

    def distroy(self, fireBallGroup, WIDTH, HEIGHT):
        if self.posX > WIDTH or self.posX < 0:
            fireBallGroup.remove(self)
            self.kill()
        elif self.posY > HEIGHT or self.posY < 0:
            fireBallGroup.remove(self)
            self.kill()

        return fireBallGroup
