import pygame
from Codes.Fireball import Fireball

WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.size = (30, 30)
        self.maxHealth = 5
        self.health = 5
        self.posX = posX
        self.posY = posY
        self.image = pygame.Surface(self.size)
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.posX, self.posY)
        self.hurtTime = 0


    def move(self, keyPressed, WIDTH, HEIGHT):
        if keyPressed[pygame.K_w]:
            if self.posY > 20 + 15:
                self.posY -= 3
        if keyPressed[pygame.K_s]:
            if self.posY < HEIGHT - 15:
                self.posY += 3
        if keyPressed[pygame.K_a]:
            if self.posX > 15:
                self.posX -= 3
        if keyPressed[pygame.K_d]:
            if self.posX < WIDTH - 15:
                self.posX += 3

        self.rect.center = (self.posX, self.posY)

    def attack(self, keyPressed, fireBallGroup):
        if keyPressed == pygame.K_RIGHT:
            fireBallGroup.add(Fireball(self.posX, self.posY, 0, "Player"))
        elif keyPressed == pygame.K_UP:
            fireBallGroup.add(Fireball(self.posX, self.posY, 1, "Player"))
        elif keyPressed == pygame.K_LEFT:
            fireBallGroup.add(Fireball(self.posX, self.posY, 2, "Player"))
        elif keyPressed == pygame.K_DOWN:
            fireBallGroup.add(Fireball(self.posX, self.posY, 3, "Player"))
        return fireBallGroup

    def hurt(self):
        self.image = pygame.Surface(self.size)
        self.image.fill(RED)
        self.health -= 1

    def renew(self):
        self.image = pygame.Surface(self.size)
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.posX, self.posY)

    def die(self, playerGroup):
        playerGroup.remove(self)
        self.kill()
        self.posX = -100
        self.posY = -100
        del self

        return playerGroup

