import pygame


def countdown(SCREEN):
    countDownCLOCK = pygame.time.Clock()
    currentImage = -479
    while True:
        if currentImage >= -120:
            break
        SCREEN.blit(
            pygame.image.load(
                f"Graphics/Countdown{abs(currentImage)//120}.png").convert(), 
                (0, 0)
                )
        pygame.display.flip()
        currentImage += 1

        countDownCLOCK.tick(120)
