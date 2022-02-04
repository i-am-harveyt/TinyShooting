import pygame
from Codes.Settings import *
from Codes.gameplay import game_play
from Codes.countdown import countdown
from Codes.win_or_lose import win_or_lose

pygame.init()
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
SCREEN = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("TinyShooting!")
CLOCK = pygame.time.Clock()
TOPIC = pygame.image.load("Graphics/TOPIC.png").convert_alpha()
win = False

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    countdown(WINDOW)
                    win = game_play(WINDOW, SCREEN)
                    pygame.time.delay(2000)
                    win_or_lose(WINDOW, win)
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        pygame.display.flip()
        WINDOW.blit(
            TOPIC, 
            (0, 0)
            )
        CLOCK.tick(120)

