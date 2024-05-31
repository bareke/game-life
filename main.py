import time
import pygame
import numpy as np

COLOR_BACKGROUND = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
COLOR_DIE_NEXT = (170, 170, 170)
COLOR_ALIVE_NEXT = (255, 255, 255)

pygame.init()
pygame.display.set_caption("Conway's Game of Life")


class GameOfLife:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen = pygame.display.set_mode((width, height))
        self.cells = np.zeros((height // cell_size, width // cell_size))
        self.running = False

    def draw_grid(self):
        self.screen.fill(COLOR_GRID)
        for x in range(0, self.width, self.cell_size):
            for y in range(0, self.height, self.cell_size):
                rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, COLOR_BACKGROUND, rect, 1)

    def update_cells(self, with_progress=False):
        updated_cells = np.zeros((self.cells.shape[0], self.cells.shape[1]))

        for row, col in np.ndindex(self.cells.shape):
            alive = np.sum(self.cells[row-1:row+2, col-1:col+2]) - self.cells[row, col]
            color = COLOR_BACKGROUND if self.cells[row, col] == 0 else COLOR_ALIVE_NEXT

            if self.cells[row, col] == 1:
                if alive < 2 or alive > 3:
                    if with_progress:
                        color = COLOR_DIE_NEXT
                elif 2 <= alive <= 3:
                    updated_cells[row, col] = 1
                    if with_progress:
                        color = COLOR_ALIVE_NEXT
            else:
                if alive == 3:
                    updated_cells[row, col] = 1
                    if with_progress:
                        color = COLOR_ALIVE_NEXT

            pygame.draw.rect(self.screen, color, (col * self.cell_size, row * self.cell_size, self.cell_size - 1, self.cell_size - 1))

        self.cells = updated_cells

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.running = not self.running
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                self.cells[pos[1] // self.cell_size, pos[0] // self.cell_size] = 1

    def run(self):
        self.draw_grid()
        self.update_cells()
        pygame.display.flip()

        while True:
            self.handle_events()
            self.screen.fill(COLOR_GRID)
            self.draw_grid()

            if self.running:
                self.update_cells(with_progress=True)

            pygame.display.update()
            time.sleep(0.001)


if __name__ == "__main__":
    game = GameOfLife(800, 600, 10)
    game.run()
