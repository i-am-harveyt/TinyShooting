import pygame
from Codes.gameplay import game_play

WIDTH, HEIGHT = 800, 620
BLACK = (25, 25, 25)

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Game!")
CLOCK = pygame.time.Clock()
TOPIC = pygame.image.load("Graphics/TOPIC.png").convert_alpha()

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

        pygame.display.flip()
        SCREEN.blit(TOPIC, (0, 0))
        CLOCK.tick(120)

