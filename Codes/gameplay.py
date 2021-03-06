import pygame
from Codes.Settings import *
from Codes.Player import Player
from Codes.Foe import Foe


def game_play(WINDOW, SCREEN):

    # use this to block events
    events = pygame.event.get()
    del events

    playerSize, foeSize, fireballSize = 50, 50, 30
    healthBarWidth = 200
    healthBarHeight = 50

    player = Player(posX=50, posY=50+SCREEN_HEIGHT//2)
    playerGroup = pygame.sprite.Group()
    playerGroup.add(player)

    foe = Foe(posX=SCREEN_WIDTH-50, posY=50+SCREEN_HEIGHT//2)
    foeGroup = pygame.sprite.Group()
    foeGroup.add(foe)

    fireBallGroup = pygame.sprite.Group()

    shootingKey = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]

    gameCLOCK = pygame.time.Clock()
    currentTime = gameCLOCK.get_time()
    foeCurrent = 0

    running = True
    while running:

        # detect event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key in shootingKey:
                    fireBallGroup = player.attack(
                        keyPressed=event.key, 
                        fireBallGroup=fireBallGroup)

        # detect player's movement
        keyPressed = pygame.key.get_pressed()
        player.move(keyPressed)

        # detect valid attack
        if len(fireBallGroup) > 0:
            for fireball in fireBallGroup:
                fireBallGroup = fireball.fly(fireBallGroup)
                if pygame.sprite.collide_rect(fireball, player) and\
                    fireball.shootFrom != "Player":
                    player.hurtTime = gameCLOCK.get_time()
                    player.hurt()
                    if player.health == 0:
                        playerGroup = player.die(playerGroup)
                    fireball.kill()
                    del fireball
                    continue

                for enemy in foeGroup:
                    if pygame.sprite.collide_rect(fireball, enemy) and\
                        fireball.shootFrom == "Player":
                        enemy.hurtTime = gameCLOCK.get_time()
                        enemy.hurt()
                        if enemy.health == 0:
                            foeGroup = enemy.die(foeGroup)
                        fireball.kill()
                        del fireball
                        break

        if len(playerGroup) == 0 or len(foeGroup) == 0:
                running = False

        # for foes' move and attack
        for enemy in foeGroup:
            enemy.move(player)
            fireBallGroup, foeCurrent = enemy.detectAttack(
                fireBallGroup, foeCurrent, player)


        # get time
        currentTime = gameCLOCK.get_time()
        if currentTime - player.hurtTime >= 1:
            player.renew()
        for enemy in foeGroup:
            if currentTime - enemy.hurtTime >= 1:
                enemy.renew()

        # deal with the rendering
        pygame.display.flip()
        SCREEN.fill(BLACK)

        # render the health bar
        pygame.draw.rect(SCREEN, WHITE, pygame.Rect(50, 0, healthBarWidth, healthBarHeight), 0)
        pygame.draw.rect(SCREEN, RED, pygame.Rect(
            50, 0, healthBarWidth*player.health/player.maxHealth, healthBarHeight), 0)

        pygame.draw.rect(SCREEN, WHITE, pygame.Rect(
            SCREEN_WIDTH-healthBarWidth-50, 0, healthBarWidth, healthBarHeight), 0)
        pygame.draw.rect(SCREEN, RED, pygame.Rect(
            SCREEN_WIDTH-healthBarWidth-50, 0, 
            healthBarWidth*foe.health/foe.maxHealth, healthBarHeight), 0)

        playerGroup.draw(SCREEN)
        foeGroup.draw(SCREEN)
        fireBallGroup.draw(SCREEN)
        WINDOW.blit(
            pygame.transform.scale(SCREEN, WINDOW.get_rect().size),
            (0, 0)
        )
        gameCLOCK.tick(120)

    if player.health <= 0:
        return False
    else:
        return True

