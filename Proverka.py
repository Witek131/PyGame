# coding: utf-8
import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * height for _ in range(width)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 50
        self.n = 0
        print(self.board)

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        color = [pygame.Color(0, 0, 0), pygame.Color(255, 255, 255)]
        for x in range(self.width):
            for y in range(self.height):
                pygame.draw.rect(screen, color[self.board[x][y]],
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                                  self.cell_size))
                pygame.draw.rect(screen, pygame.Color("white"),
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                                  self.cell_size), 1)



    def get_cell(self, mouse_pos):
        # print(mouse_pos[0])
        coor_x = (mouse_pos[0] - self.left) // self.cell_size
        coor_y = (mouse_pos[1] - self.top) // self.cell_size
        if coor_x < 0 or coor_y < 0 or coor_x >= self.width or coor_y >= self.height:
            return None
        return (coor_x, coor_y)


    def on_click(self, cell):
        print(cell)
        for i in range(self.height):
            if self.board[cell[0]][i] == 1:
                self.board[cell[0]][i] = 0
            else:
                self.board[cell[0]][i] = 1
        for i in range(self.width):
            if self.board[i][cell[1]] == 1:
                self.board[i][cell[1]] = 0
            else:
                self.board[i][cell[1]] = 1
        self.board[cell[0]][cell[1]] = (self.board[cell[0]][cell[1]] + 1) % 2
        for i in self.board:
            print(i)

    def get_click(self, mouse_pos):
        """
        вызывает методы получения координат от мышки
        и запуск действий по этим координатам
        :param mouse_pos:
        """
        cell = self.get_cell(mouse_pos)
        if cell:
            print(cell)
            self.n = 1
            self.on_click(cell)


pygame.init()
size = width, height = 400, 400
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
board = Board(5, 7)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
pygame.quit()
