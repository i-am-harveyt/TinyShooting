import pygame


def countdown(SCREEN):
    countDownCLOCK = pygame.time.Clock()
    currentImage = 0
    images = [
        pygame.image.load("Graphics/Countdown3.png").convert_alpha(),
        pygame.image.load("Graphics/Countdown2.png").convert_alpha(),
        pygame.image.load("Graphics/Countdown1.png").convert_alpha()
        ]
    while True:
        if currentImage == 3:
            break

        SCREEN.blit(images[currentImage], (0, 0))
        pygame.display.flip()
        currentImage += 1

        countDownCLOCK.tick(1)