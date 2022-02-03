import pygame


def win_or_lose(SCREEN, win):
    remain = True
    winScreen = pygame.image.load("Graphics/Win.png").convert_alpha()
    loseScreen = pygame.image.load("Graphics/Lose.png").convert_alpha()
    screenClock = pygame.time.Clock()
    while remain:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    remain = False
                elif event.key == pygame.K_ESCAPE:
                    remain = False

        if win:
            SCREEN.blit(winScreen, (0, 0))
        else:
            SCREEN.blit(loseScreen, (0, 0))

        pygame.display.flip()
        screenClock.tick(120)
