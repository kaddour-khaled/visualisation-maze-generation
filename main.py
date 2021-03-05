import pygame

BLACK = (0, 0, 0)
MAZE_WIDTH = MAZE_HEIGHT = 600
CELL_SIZE = 60
MAZE_BACKGROUND_COLOR = (43, 43, 43)

class App:
    def __init__(self, width=900, height=700):
        self.width, self.height = width, height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.maze_space = pygame.Surface((MAZE_WIDTH, MAZE_HEIGHT))
        self.maze_space.fill(MAZE_BACKGROUND_COLOR)

    def on_init(self):
        self.is_running = True

    def on_loop(self):
        pass

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.is_running = False

    def on_render(self):
        # clean the window
        self.window.fill(BLACK)

        # render the maze space
        maze_space_pos = ((self.width - MAZE_WIDTH) // 2, (self.height - MAZE_HEIGHT) // 2) 
        self.window.blit(self.maze_space, maze_space_pos)
        
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