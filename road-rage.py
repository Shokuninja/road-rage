import pygame

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))

player = pygame.Rect((300, 250, 50, 50))
player_speed = 1
# playerimg = pygame.image.load("src/racecar.png")

# def player (x, y):
#     gameDisplay.blit(playerimg, (x,y))

# x = ()


run = True
while run:

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_w] == True:
        player.y -= player_speed
        # print('left')

    elif key[pygame.K_s] == True:
        player.y += player_speed

    if key[pygame.K_a] == True:
        player.x -= player_speed

    elif key[pygame.K_d] == True:
        player.x += player_speed

    player.x = max(0, min(player.x, screen_width - player.width))
    player.y = max(0, min(player.y, screen_height - player.height))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
