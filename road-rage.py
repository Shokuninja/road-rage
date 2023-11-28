import pygame

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))

playerimg = pygame.image.load("src/racecar.png")

player = playerimg.get_rect(center=(300, 250))
player_speed = 1



run = True
while run:

    screen.fill((255, 255, 255))
    screen.blit(playerimg, player)
    #pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_UP] == True:
        player.y -= player_speed
        # print('left')

    elif key[pygame.K_DOWN] == True:
        player.y += player_speed

    if key[pygame.K_LEFT] == True:
        player.x -= player_speed

    elif key[pygame.K_RIGHT] == True:
        player.x += player_speed

    player.x = max(0, min(player.x, screen_width - player.width))
    player.y = max(0, min(player.y, screen_height - player.height))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
