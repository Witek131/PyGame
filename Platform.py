# coding: utf-8
import pygame



class Platform(pygame.sprite.Sprite):
    size = (100, 10)

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.add(platform)
        self.image = pygame.Surface(Platform.size)
        self.image.fill(pygame.Color(255, 0, 0))
        self.rect = pygame.Rect(pos,(Platform.size))


class Hero(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = pygame.Surface((20, 20))
        self.image.fill(pygame.Color(0, 255, 0))
        self.rect = pygame.Rect(pos, (20, 20))

    def update(self):
        if pygame.sprite.spritecollideany(self, platform) is None:
            self.rect.top += 1


pygame.init()
all_sprites = pygame.sprite.Group()
platform = pygame.sprite.Group()
size = width, height = 400, 400
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
hero = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                if hero == 0:
                    hero = Hero(event.pos)
                else:
                    hero.rect.topleft = event.pos
            if event.button == 1:
                Platform(event.pos)
        if hero !=0:
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    hero.rect.left -=10
                if event.key == pygame.K_RIGHT:
                    hero.rect.left += 10

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(50)
pygame.quit()
