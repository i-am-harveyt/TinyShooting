import pygame
from Codes.gameplay import game_play

WIDTH, HEIGHT = 800, 600
BLACK = (25, 25, 25)

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Game!")
CLOCK = pygame.time.Clock()

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_play(SCREEN, WIDTH, HEIGHT)
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        SCREEN.fill(BLACK)
        pygame.display.flip()
        CLOCK.tick(120)

