import pygame

pygame.init()
size = width, height = 800, 400
screen = pygame.display.set_mode(size)
running = True
screen2 = pygame.Surface(screen.get_size())
x1, y1, w, h = 0, 0, 0, 0
drawing = False  # режим рисования выключен
x=-1
y=-1
clok= pygame.time.Clock()
cir= []
speed=[]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            cir.append(list(event.pos))
            speed.append([1,-1])
    screen2.fill((0,0,0))
    for i in range(len(cir)):

        pygame.draw.circle(screen2, (255,255,255), cir[i], 10)
        cir[i][0] -=speed[i][0]
        cir[i][1] +=speed[i][1]
        if cir[i][0] > 400 :
            speed[i][1] =-1
        print(cir[i][1],speed[i][1])

    screen.blit(screen2,(0,0))


    pygame.display.flip()
    clok.tick(100)
pygame.quit()