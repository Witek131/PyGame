# coding: utf-8
import pygame
import random

class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randint(-5, 5)
        self.vy = random.randrange(-5, 5)

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx
class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)

horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
pygame.init()
size = width, height = 800, 400
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
c_r = 10
cir = False
cir_col = pygame.Color('white')
gro = [1, -1]
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
        if 0 + 10 > circle[i][0]:
            sr[i][0] = -sr[i][0]
        if 0 + 10 > circle[i][1]:
            sr[i][1] = -sr[i][1]
        if 800 < circle[i][0]:
            sr[i][0] = -sr[i][0]
        if 400 < circle[i][1]:
            sr[i][1] = -sr[i][1]
        circle[i][0] -= 10 * sr[i][0]
        circle[i][1] -= 10 * sr[i][1]

        pygame.draw.circle(screen2, cir_col, circle[i], 10, 0)
    screen.blit(screen2, (0, 0))
    pygame.display.flip()
    clock.tick(50)
pygame.quit()
