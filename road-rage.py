import pygame
import time
import random


pygame.init()

# crash_sound = pygame.mixer.Sound("/Users/bobby/Downloads/Tokyo_Drift_Fast__Furious (1).mp3")
# pygame.mixer.music.load("/Users/bobby/Downloads/Car_Crash_Sound_Effect.mp3")
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Road Rage")

clock = pygame.time.Clock()

# carImg = pygame.image.load("src/cars/9.png")
# car_width = 73
# car_height = 200

background_photos = [
    pygame.image.load("src/background/18.png"),
]

current_photo_index = 0
background_img = background_photos[current_photo_index]
background_img = pygame.transform.scale(background_img, (display_width, display_height))

bomb_img = pygame.image.load("src/cars/car_sport_01.svg")
bomb_width = 150
bomb_height = 200
bomb_img = pygame.transform.scale(bomb_img, (bomb_width, bomb_height))

current_photo_index = 0
background_img = background_photos[current_photo_index]
background_img = pygame.transform.scale(background_img, (display_width, display_height))

playerimg = pygame.image.load("src/cars/4.png")
player_width = 250
player_height = 200
playerimg = pygame.transform.scale(playerimg, (player_width, player_height))

# player = playerimg.get_rect(center=(500, 500))



white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

car_speed = 5
pause = False

heart_img = pygame.image.load("src/Pixel Heart Animation GIFs & Spritesheets, 32x32 and 16x16/Pixel Heart Animation 32x32.gif")
heart_img = pygame.transform.scale(heart_img, (30, 30))
hearts = 3

crash_sound = pygame.mixer.Sound("/Users/bobby/Downloads/Car_Crash_Sound_Effect.mp3")
pygame.mixer.music.load("/Users/bobby/Downloads/Tokyo_Drift_Fast__Furious.mp3")

def enemys(enemyx, enemyy, enemyw, enemyh):
    gameDisplay.blit(bomb_img, (enemyx, enemyy, enemyw, enemyh))


def car(x,y):
    gameDisplay.blit(playerimg, (x, y))

def enemys_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))

def crash():
    pygame.message_display("You Crashed") 
    pygame.mixer.music.stop(crash_sound)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    large_text = pygame.font.SysFont(None, 115)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(text_surf, text_rect)

    pygame.display.update()

    pygame.time.wait(2000)

def crash():

    global hearts
    hearts -= 1
    # Flash the colors for a certain duration
    flash_duration = 2
    flash_start_time = time.time()

    while time.time() - flash_start_time < flash_duration:
        # Change the color of the bomb randomly between red, orange, and yellow
        color = random.choice(['red', 'orange', 'yellow'])
        gameDisplay.fill(color=color)
        # bomb_img.fill(pygame.Color(color))

        pygame.display.update()
        clock.tick(10)

    if hearts <= 0:
        message_display("You're DEAD")
        game_intro()
    else:
        message_display("You're Injured")
        game_loop()

    
    pygame.mixer.music.stop()
    # pygame.mixer.Sound.play(crash_sound) 
    
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("YOU DIED", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    

    game_loop()

   

    game_intro()
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(background_img, (0, 0))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again", 150, 450, 100, 50, green, bright_green, game_loop)
        button("RESET", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False

def paused():

    pygame.mixer.music.pause()

    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue", 150, 450, 100, 50, green, bright_green, unpause)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

def game_intro():
    intro = True
    global hearts
    hearts = 3

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(background_img, (0, 0))  # Display the background image

        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("Road Rage", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause, hearts

    pygame.mixer.music.play(-1)

    x = (display_width * 0.45)
    y = (display_height * 0.6)

    x_change = 0
    y_change = 0

    enemy_startx = random.randrange(0, display_width)
    enemy_starty = -600
    # Track enemy position throughout game state
    enemy_current_position_x, enemy_current_position_y = enemy_startx, enemy_starty
    enemy_speed = 4
    enemy_width = 100
    enemy_height = 100

    # enemys(enemy_startx, enemy_starty, enemy_width, enemy_height)
    # enemy_starty += enemy_speed

    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_change = -5
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_change = 5
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    y_change = -5
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                    y_change = 0


        x += x_change
        y += y_change
        gameDisplay.blit(background_img, (0, 0))  # Display the background image

        enemys(enemy_current_position_x, enemy_current_position_y, enemy_width, enemy_height)
        enemy_current_position_y += enemy_speed
        car(x, y)
        enemys_dodged(dodged)

        # Checks if car has gone off screen
        if x > display_width - player_width or x < -200:
            crash()
            enemys(enemy_current_position_x, enemy_current_position_y, enemy_width, enemy_height)

        if enemy_current_position_y > display_height:
            enemy_current_position_y = 0 - enemy_height
            enemy_current_position_x = random.randrange(0, display_width)
            dodged += 1
            enemy_speed += 1

            # TODO: Increase sprite size while increasing enemy width.
            # enemy_width += (dodged * 1.2)

        # Checks if car has collided with enemy.
        # HORIZONTAL_CHECKS = x > enemy_startx and x < enemy_startx + enemy_width or x + car_width > enemy_startx and x + car_width < enemy_startx + enemy_width
        # VERTICAL_CHECKS = y > enemy_starty and y < enemy_starty + enemy_height
        # COLLISION_CHECKS_X = x > enemy_current_position_x and x < enemy_current_position_x + enemy_width or x + car_width > enemy_current_position_x and x + car_width < enemy_current_position_x + enemy_width
        # COLLISION_CHECKS_Y = y > enemy_current_position_y and y < enemy_current_position_y + enemy_height
        COLLISION_CHECK_X_GOING_LEFT = abs(x - enemy_current_position_x) <= 10
        COLLISION_CHECK_X_GOING_RIGHT = abs(enemy_current_position_x - x) <= 40
        COLLISION_CHECK_X = COLLISION_CHECK_X_GOING_LEFT or COLLISION_CHECK_X_GOING_RIGHT
        COLLISION_CHECK_Y = abs(y - enemy_current_position_y) <= 85
        # playerrect, bombrect = playerimg.get_rect(), bomb_img.get_rect()
        # print(playerrect.width, playerrect.height)
        # print(bombrect.width, bombrect.height)
        # if playerrect.colliderect(bombrect):
        if COLLISION_CHECK_X and COLLISION_CHECK_Y:
            print(f"Collision detected.")
            print(f"\n\tCAR POSITION: ({x}, {y})\n\tENEMY POSITION: ({enemy_current_position_x}, {enemy_current_position_y})")
            print(f"Difference in Positions: \n\tdX: {abs(x - enemy_current_position_x)}. \n\tdY: {abs(y - enemy_current_position_y)}")
            print(f"Triggering event to crash player with health loss.")
            crash()
            print(f"Respawning enemy.")
            enemys(enemy_startx, enemy_starty, enemy_width, enemy_height)

        # if COLLISION_CHECKS_X:
        #     # TODO: Ensure enemy car image is drawn right. Right now,
        #     #       enemy image is a little to the left of the "hitbox" 
        #     #       or area that collides with the player. 
        #     print('y crossover')

        #     if COLLISION_CHECKS_Y:
        #         print('x crossover')
        #         crash()
        #         enemys(enemy_startx, enemy_starty, enemy_width, enemy_height)


        for i in range(hearts):
            gameDisplay.blit(heart_img, (display_width - 30 * (i + 1), 10))
        pygame.display.update()
        clock.tick(60)

# Updated image paths and sizes 
heart_img = pygame.image.load("src/Pixel Heart Animation GIFs & Spritesheets, 32x32 and 16x16/Pixel Heart Animation 32x32.gif")
heart_img = pygame.transform.scale(heart_img, (30, 30))


game_intro()
game_loop()
pygame.quit()
quit()