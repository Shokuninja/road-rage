import pygame
import random

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))

background_photos = [
    pygame.image.load("src/background/18.png"),
]

current_photo_index = 0
background_img = background_photos[current_photo_index]
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))

playerimg = pygame.image.load("src/cars/cars_race1.png")
playerimg = pygame.transform.scale(playerimg, (300, 300))
player = playerimg.get_rect(center=(300, 250))
player_speed = 5

# Step 1: Create bomb image
bomb_img = pygame.image.load("src/missles/bomb.png")
bomb_img = pygame.transform.scale(bomb_img, (50, 50))

# Step 2: Set bomb properties
bombs = []
bomb_speed = 5
spawn_interval = 2000  # milliseconds
spawn_timer = 0
last_frame_time = pygame.time.get_ticks()

# Step 3: Spawn bombs at regular intervals
def spawn_bomb():
    x = random.randint(0, screen_width - bomb_img.get_width())
    y = 0
    bombs.append(pygame.Rect(x, y, bomb_img.get_width(), bomb_img.get_height()))

# Step 4: Move bombs down
def move_bombs():
    for bomb in bombs:
        bomb.y += bomb_speed

# Step 5: Check for collision
def check_collision():
    for bomb in bombs:
        if bomb.colliderect(player):
            bombs.remove(bomb)

run = True
while run:
    screen.blit(background_img, (0, 0))
    screen.blit(playerimg, player)

    key = pygame.key.get_pressed()
    if key[pygame.K_UP] == True:
        player.y -= player_speed
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

    # Step 6: Spawn bombs at regular intervals
    spawn_timer += pygame.time.get_ticks() - last_frame_time
    last_frame_time = pygame.time.get_ticks()
    if spawn_timer >= spawn_interval:
        spawn_bomb()
        spawn_timer = 0

    # Step 7: Move bombs down
    move_bombs()

    for bomb in bombs:
        screen.blit(bomb_img, bomb)

    # Step 8: Check for collision
    check_collision()

    pygame.display.update()

pygame.quit()
