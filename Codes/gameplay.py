import pygame
from Codes.Player import Player
from Codes.Foe import Foe


def game_play(SCREEN, WIDTH, HEIGHT):

    # use this to block events
    events = pygame.event.get()
    del events

    BLACK = (25, 25, 25)

    player = Player(posX=50, posY=20+HEIGHT//2)
    playerGroup = pygame.sprite.Group()
    playerGroup.add(player)

    foe = Foe(posX=WIDTH-50, posY=20+HEIGHT//2)
    foeGroup = pygame.sprite.Group()
    foeGroup.add(foe)

    heart = pygame.image.load("Graphics/Heart.png").convert_alpha()
    emptyHeart = pygame.image.load("Graphics/EmptyHeart.png").convert_alpha()

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
                        keyPressed=event.key, fireBallGroup=fireBallGroup)

        # detect player's movement
        keyPressed = pygame.key.get_pressed()
        player.move(keyPressed, WIDTH, HEIGHT)

        # detect valid attack
        if len(fireBallGroup) > 0:
            for fireball in fireBallGroup:
                fireBallGroup = fireball.fly(fireBallGroup, WIDTH, HEIGHT)
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
        if currentTime - player.hurtTime >= 0.2:
            player.renew()
        for enemy in foeGroup:
            if currentTime - enemy.hurtTime >= 0.2:
                enemy.renew()

        # deal with the rendering
        pygame.display.flip()
        SCREEN.fill(BLACK)
        # render the heart(s)
        for i in range(player.maxHealth):
            if i <= player.health-1:
                SCREEN.blit(heart, (0+20*i, 0))
            else:
                SCREEN.blit(emptyHeart, (0+20*i, 0))
        for i in range(foe.maxHealth):
            if i <= foe.health-1:
                SCREEN.blit(heart, (WIDTH-20*foe.maxHealth+20*i, 0))
            else:
                SCREEN.blit(emptyHeart, (WIDTH-20*foe.maxHealth+20*i, 0))
        playerGroup.draw(SCREEN)
        foeGroup.draw(SCREEN)
        fireBallGroup.draw(SCREEN)
        gameCLOCK.tick(120)

    if player.health <= 0:
        return False
    else:
        return True

