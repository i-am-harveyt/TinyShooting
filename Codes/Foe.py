import pygame
from Codes.Fireball import Fireball

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Foe(pygame.sprite.Sprite):
    def __init__(self, posX, posY, foeSize):
        super().__init__()
        self.size = (foeSize, foeSize)
        self.maxHealth = 5
        self.health = 5
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
            self.posY += 5
        elif player.posY < self.posY:
            self.posY -= 5

        self.rect.center = (self.posX, self.posY)

    def attack(self, keyPressed, fireBallGroup, fireballSize):
        if keyPressed == pygame.K_RIGHT:
            fireBallGroup.add(
                Fireball(self.posX, self.posY, 0, "Foe", fireballSize))
        elif keyPressed == pygame.K_UP:
            fireBallGroup.add(
                Fireball(self.posX, self.posY, 1, "Foe", fireballSize))
        elif keyPressed == pygame.K_LEFT:
            fireBallGroup.add(
                Fireball(self.posX, self.posY, 2, "Foe", fireballSize))
        elif keyPressed == pygame.K_DOWN:
            fireBallGroup.add(
                Fireball(self.posX, self.posY, 3, "Foe", fireballSize))
        return fireBallGroup

    def detectAttack(self, fireBallGroup, selfCurrent, player, fireballSize):
        # basic foe attack mode
        selfDetectRange = 30
        selfCurrent += 1
        if abs(player.posY - self.posY) < selfDetectRange or\
            abs(player.posX - self.posX) < selfDetectRange:
            if selfCurrent > 30:
                selfCurrent = 0
                if player.posX < self.posX:
                    fireBallGroup = self.attack(
                        keyPressed=pygame.K_LEFT, fireBallGroup=fireBallGroup, 
                        fireballSize=fireballSize)
                elif player.posX > self.posX:
                    fireBallGroup = self.attack(
                        keyPressed=pygame.K_RIGHT, fireBallGroup=fireBallGroup, 
                        fireballSize=fireballSize)
                elif player.posY < self.posY:
                    fireBallGroup = self.attack(
                        keyPressed=pygame.K_DOWN, fireBallGroup=fireBallGroup, 
                        fireballSize=fireballSize)
                elif player.posY > self.posY:
                    fireBallGroup = self.attack(
                        keyPressed=pygame.K_UP, fireBallGroup=fireBallGroup, 
                        fireballSize=fireballSize)
    

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

        return selfGroup

