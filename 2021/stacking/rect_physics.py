"""
https://stackoverflow.com/questions/67063822/why-is-only-one-of-my-rects-working-when-i-applied-physics-to-both
"""
import pygame

pygame.init()

screen = pygame.display.set_mode((226, 318))
player_pos = [95, 292]
door_list = []
door_pos = 95,0
open_door_pos = 95, 0
column_pos = 100,100

pygame.display.set_icon(pygame.image.load('Sprites/Icon.png'))
pygame.display.set_caption("Knock Knight")

column = pygame.image.load('Sprites/Column.png').convert()
column.set_colorkey((255, 255, 255))

door = pygame.image.load('Sprites/Door.png').convert()#if you dont convert it colorkey wont work
door.set_colorkey((255, 255, 255))

open_door = pygame.image.load('Sprites/Open door.png').convert()

player1 = pygame.image.load('Sprites/Player.png').convert()
player1.set_colorkey((255, 255, 255))

moving_right = False
moving_left = False
moving_up = False
moving_down = False


def check_collision(player, door):
    for player in door:
        if player_rect.colliderect(door_rect):
            screen.blit(open_door, (open_door_pos))

def check_collision(player, column):
    global moving_up, moving_down, moving_left, moving_right
    collision_tolerance = 15
    for player in column:
        if player_rect.colliderect(column_rect):
            if abs(player_rect.top - column_rect.bottom) < collision_tolerance:
                moving_up = False
            if abs(player_rect.bottom - column_rect.top) < collision_tolerance:
                moving_down = False
            if abs(player_rect.left - column_rect.right) < collision_tolerance:
                moving_left = False
            if abs(player_rect.right - column_rect.left) < collision_tolerance:
                moving_right = False

clock = pygame.time.Clock()
while True:
    screen.fill((15, 15, 15))

    door_list.clear()

    column_rect = screen.blit(column, column_pos)
    door_rect = screen.blit(door, door_pos)
    door_list.append(door_rect)
    player_rect = screen.blit(player1, player_pos)

    if moving_right == True:
        player_pos[0] += 2
    if moving_left == True:
        player_pos[0] -= 2
    if moving_up == True:
        player_pos[1] -= 2
    if moving_down == True:
        player_pos[1] += 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
            if event.key == K_UP:
                moving_up = True
            if event.key == K_DOWN:
                moving_down = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
            if event.key == K_UP:
                moving_up = False
            if event.key == K_DOWN:
                moving_down = False

    if player_pos[1] > 290:
        moving_down = False #This will be changed later so you die
    if player_pos[1] < 4:
        moving_up = False
    if player_pos[0] < 4:
        moving_left = False
    if player_pos[0] > 212:
        moving_right = False

    check_collision(column_rect, player_rect)
    check_collision(door_rect, player_rect)

    pygame.display.update()
    clock.tick(120)

pygame.quit()