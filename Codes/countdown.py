import pygame


def countDown(SCREEN):
    countDownCLOCK = pygame.time.Clock()
    images = [
        pygame.image.load("Graphics/Countdown3.png").convert(),
        pygame.image.load("Graphics/Countdown2.png").convert(),
        pygame.image.load("Graphics/Countdown1.png").convert()
    ]
    currentImage = 0
    while True:
        if currentImage >= 3:
            break
        SCREEN.blit(images[currentImage], (0, 0))
        pygame.display.flip()
        currentImage += 1

        countDownCLOCK.tick(1)