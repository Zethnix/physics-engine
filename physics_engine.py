import sys
import pygame
import time
pygame.init()

# Game options
size = (500, 500)
target_fps = 60
prev_time = time.time()

win = pygame.display.set_mode(size)
pygame.display.set_caption("First game")

# Object properties
x = 400
y = 400
width = 40
height = 60
x_vel = 0
y_vel = 0

# Acceleration
initial_burst_momentum = 0.4
de_acceleration = 0.1
min_acceleration = 0.1
friction = 1.05

# Object atributes
speed = 4

run = True
while run:
    # Event quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Physics engine
    if not x_vel == 0:
        x += x_vel
    if not y_vel == 0:
        y -= y_vel

    # Fricton delay
    if x_vel < 0 and not keys[pygame.K_d]:
        x_vel -= (friction ** x_vel) - 1
    if x_vel > 0 and not keys[pygame.K_a]:
        x_vel += (friction ** (-1 * x_vel)) - 1

    # Hitbox within perimeter
    if x < 0:
        x = 0
    if x > size[1]-50:
        x = size[1]-50

    # Register key presses
    keys = pygame.key.get_pressed()

    # Move left
    if keys[pygame.K_a] and not keys[pygame.K_d]:
        if x_vel > -speed:
            if x_vel >= 0:
                acceleration = (initial_burst_momentum *
                                de_acceleration ** (x_vel)) + min_acceleration
                x_vel -= acceleration
            else:
                acceleration = (initial_burst_momentum *
                                de_acceleration ** (-1 * x_vel)) + min_acceleration
                x_vel -= acceleration
            # print(acceleration)
            print(x_vel)
    # Move right
    if keys[pygame.K_d] and not keys[pygame.K_a]:
        if x_vel < speed:
            if x_vel <= 0:
                acceleration = (initial_burst_momentum *
                                de_acceleration ** (-1 * x_vel)) + min_acceleration
                x_vel += acceleration
            else:
                acceleration = (initial_burst_momentum *
                                de_acceleration ** (x_vel)) + min_acceleration
                x_vel += acceleration
            # print(acceleration)
            print(x_vel)

    # Render screen
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

    # Timing code at the END!d
    curr_time = time.time()  # so now we have time after processing
    diff = curr_time - prev_time  # frame took this much time to process and render
    # if we finished early, wait the remaining time to desired fps, else wait 0 ms!
    delay = max(1.0/target_fps - diff, 0)
    time.sleep(delay)
    # fps is based on total time ("processing" diff time + "wasted" delay time)
    fps = 1.0/(delay + diff)
    prev_time = curr_time
pygame.quit()
