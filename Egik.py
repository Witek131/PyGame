import pygame

eg = open("eg", "r")
eg1 = [tuple(map(float, i[1:-1].replace(',', '.').split(';'))) for i in eg.read().split(', ')]
print(eg1)
pygame.init()
pygame.display.set_caption('EGIK')
sizi = width, height = 501, 501
screen = pygame.display.set_mode(sizi)
running = True
kof = 5

def zoom(eg,kof):
    s = []
    for i in range(len(eg)):
        s.append([])
        s[i].append(eg[i][0] * kof + 100)
        s[i].append(eg[i][1] * kof + 100)
    pygame.draw.polygon(screen, (255, 250, 255), s, 2)
    pygame.display.flip()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            kof += 1
            zoom(eg1[:], kof)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            kof -= 1
            zoom(eg1[:], kof)
        screen.fill((0,0,0))