import pygame
from Fireball import Fireball

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Foe(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.size = (30, 30)
        self.health = 10
        self.posX = posX
        self.posY = posY
        self.image = pygame.Surface(self.size)
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (self.posX, self.posY)
        self.hurtTime = 0


    def move(self, player):
        # if player.posX > self.posX:
        #     self.posX += 8
        # elif player.posX < self.posX:
        #     self.posX -= 8
        if player.posY > self.posY:
            self.posY += 3
        elif player.posY < self.posY:
            self.posY -= 3

        self.rect.center = (self.posX, self.posY)

    def attack(self, keyPressed, fireBallGroup):
        if keyPressed == pygame.K_RIGHT:
            fireBallGroup.add(Fireball(self.posX, self.posY, 0, "Foe"))
        elif keyPressed == pygame.K_UP:
            fireBallGroup.add(Fireball(self.posX, self.posY, 1, "Foe"))
        elif keyPressed == pygame.K_LEFT:
            fireBallGroup.add(Fireball(self.posX, self.posY, 2, "Foe"))
        elif keyPressed == pygame.K_DOWN:
            fireBallGroup.add(Fireball(self.posX, self.posY, 3, "Foe"))
        return fireBallGroup

    def detectAttack(self, fireBallGroup, selfCurrent, player):
        # basic foe attack mode
        selfDetectRange = 30
        selfCurrent += 1
        if abs(player.posY - self.posY) < selfDetectRange or\
            abs(player.posX - self.posX) < selfDetectRange:
            if selfCurrent > 30:
                selfCurrent = 0
                if player.posX < self.posX:
                    fireBallGroup = self.attack(keyPressed=pygame.K_LEFT, fireBallGroup=fireBallGroup)
                elif player.posX > self.posX:
                    fireBallGroup = self.attack(keyPressed=pygame.K_RIGHT, fireBallGroup=fireBallGroup)
                elif player.posY < self.posY:
                    fireBallGroup = self.attack(keyPressed=pygame.K_DOWN, fireBallGroup=fireBallGroup)
                elif player.posY > self.posY:
                    fireBallGroup = self.attack(keyPressed=pygame.K_UP, fireBallGroup=fireBallGroup)
    

        return fireBallGroup, selfCurrent

    def hurt(self):
        self.image = pygame.Surface(self.size)
        self.image.fill(RED)
        self.health -= 1

    def renew(self):
        self.image = pygame.Surface(self.size)
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (self.posX, self.posY)

    def die(self, selfGroup):
        selfGroup.remove(self)
        self.kill()
        del self

        return selfGroup

