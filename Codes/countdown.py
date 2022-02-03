import pygame


def countDown():
    countDownCLOCK = pygame.time.Clock()
    currentCountDown = 0
    while True:
        currentCountDown += 1
        if currentCountDown >= 360:
            break
        countDownCLOCK.tick(120)
    del countDownCLOCK, currentCountDown