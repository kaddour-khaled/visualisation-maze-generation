import pygame
from cell import Cell

BLACK = (0, 0, 0)
MAZE_WIDTH = MAZE_HEIGHT = 600
MAZE_BACKGROUND_COLOR = (43, 43, 43)

rows = MAZE_HEIGHT // Cell.CELL_SIZE
columns = MAZE_WIDTH // Cell.CELL_SIZE
class App:
    def __init__(self, width=900, height=700):
        self.width, self.height = width, height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.maze_space = pygame.Surface((MAZE_WIDTH, MAZE_HEIGHT))
        self.maze_space.fill(MAZE_BACKGROUND_COLOR)
        # create cells
        self.list_cell = Cell.create_list_cells(rows, columns)
        self.current = self.list_cell[0]
        self.current.set_visited()
        self.stack = []

    def on_init(self):
        self.is_running = True

    def on_loop(self):
        next = self.current.check_neighbors(self.list_cell, columns, rows)
        if next != None:
            next.set_visited()
            self.current.remove_border(next)
            self.stack.append(self.current)
            self.current = next
        else:
            if len(self.stack) > 0:
                self.current = self.stack.pop(len(self.stack)-1)
            

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.is_running = False

    def on_render(self):
        # clean the window
        self.window.fill(BLACK)

        # render the maze space
        maze_space_pos = ((self.width - MAZE_WIDTH) // 2, (self.height - MAZE_HEIGHT) // 2) 
        self.window.blit(self.maze_space, maze_space_pos)
        
        # render all cell
        for cell in self.list_cell:
            cell.render_cell(self.maze_space)
        
        # render current cell
        x = self.current.column * Cell.CELL_SIZE
        y = self.current.row * Cell.CELL_SIZE
        r = pygame.rect.Rect(x, y, Cell.CELL_SIZE, Cell.CELL_SIZE)
        pygame.draw.rect(self.maze_space, (255, 0, 255), r)
        # update window
        pygame.display.update()

    def on_clean(self):
        pass

    def on_execute(self):
        self.on_init()
        while self.is_running:
            for event in pygame.event.get():
                self.on_event(event)
    
            self.on_loop()
            self.on_render()
        self.on_clean()

if __name__ == "__main__":
    app = App()
    app.on_execute()