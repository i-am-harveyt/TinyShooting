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
        pygame.time.wait(1000)
        currentImage += 1

        countDownCLOCK.tick(120)