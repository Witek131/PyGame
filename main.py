# coding: utf-8
import pygame
import random

pygame.init()
size = width, height = 800, 400
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
c_r = 10
cir = False
cir_col = pygame.Color('white')
gro =[1,-1]
running = True
circle = []
screen2 = pygame.Surface(screen.get_size())
sr = []
while running:
    for event in pygame.event.get():
        screen2 = pygame.Surface(screen.get_size())
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            circle.append(list(event.pos))
            print(1)
            sr.append([random.choice(gro), random.choice(gro)])
    screen2.fill(pygame.Color((0, 0, 0)))

    for i in range(len(circle)):
        if 0 + 10> circle[i][0]:
            sr[i][0] = -sr[i][0]
        if 0 + 10> circle[i][1]:
            sr[i][1] = -sr[i][1]
        if 800 < circle[i][0]:
            sr[i][0] = -sr[i][0]
        if 400 <  circle[i][1]:
            sr[i][1] = -sr[i][1]
        circle[i][0] -= 10*sr[i][0]
        circle[i][1] -= 10*sr[i][1]

        pygame.draw.circle(screen2, cir_col, circle[i], 10, 0)
    screen.blit(screen2, (0, 0))
    pygame.display.flip()
    clock.tick(50)
pygame.quit()
