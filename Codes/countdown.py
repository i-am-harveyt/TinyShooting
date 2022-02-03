import pygame


def countDown(SCREEN):
    countDownCLOCK = pygame.time.Clock()
    currentImage = 3
    while True:
        if currentImage <= 0:
            break
        SCREEN.blit(
            pygame.image.load(
                f"Graphics/Countdown{currentImage}.png").convert(), 
                (0, 0)
                )
        pygame.display.flip()
        currentImage -= 1

        countDownCLOCK.tick(1)
