import pygame

class Cell:
    CELL_SIZE = 10
    BORDER_COLOR = (70, 140, 160)
    BACKGROUND_COLOR = (200, 100, 50)
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.top, self.right, self.bottom, self.left = True, True, True, True
        self.visited = False
    
    def set_visited(self):
        self.visited = True

    
    def is_visited(self):
        return self.visited

    def render_cell(self, surface):
        
        size = Cell.CELL_SIZE
        x = self.column * size
        y = self.row * size

        # debuging
        if(self.visited):
            r = pygame.rect.Rect(x, y, size, size)
            pygame.draw.rect(surface, Cell.BACKGROUND_COLOR, r)

        if self.top:
            # top border
            Cell.draw_stroke(surface, x,      y,      x + size, y)
        if self.right:
            # right border
            Cell.draw_stroke(surface, x+size, y,      x + size, y+size)
        if self.bottom:
            # bottom border
            Cell.draw_stroke(surface, x,      y+size, x + size, y+size)
        if self.left:
            # left border
            Cell.draw_stroke(surface, x,      y,      x,        y+size)
        
       

    def draw_stroke(surface, x_start, y_start, x_end, y_end):
        pygame.draw.line(surface, Cell.BORDER_COLOR, (x_start, y_start), (x_end, y_end), 3)

    def create_list_cells(nbr_rows, nbr_cols):
        cells = []   
        for row in range(nbr_rows):
            for col in range(nbr_cols):
                cell = Cell(row, col)
                cells.append(cell)
        return cells

    def index(self, i, j, nbr_cols, nbr_rows):
        if i < 0 or i > nbr_rows-1 or j < 0 or j > nbr_cols-1:
            return None
        return j + i * nbr_cols

    def check_neighbors(self, cells, nbr_cols, nbr_rows):
        neighbors = []
        
        index_top_neighbor = self.index(self.row - 1, self.column, nbr_cols, nbr_rows)

        if  index_top_neighbor != None and  not cells[index_top_neighbor].is_visited():
            neighbors.append(cells[index_top_neighbor])

        index_right_neighbor = self.index(self.row, self.column + 1, nbr_cols, nbr_rows)

        if  index_right_neighbor != None and not cells[index_right_neighbor].is_visited():
            neighbors.append(cells[index_right_neighbor])
        
        index_bottom_neighbor = self.index(self.row + 1, self.column, nbr_cols, nbr_rows)
        
        if  index_bottom_neighbor != None and not cells[index_bottom_neighbor].is_visited():
            neighbors.append(cells[index_bottom_neighbor])

        index_left_neighbor = self.index(self.row, self.column - 1, nbr_cols, nbr_rows)
        
        if  index_left_neighbor != None and not cells[index_left_neighbor].is_visited():
            neighbors.append(cells[index_left_neighbor])
        
        if len(neighbors) > 0:
            import random
            i = random.randrange(0, len(neighbors))
            return neighbors[i]
        else:
            return None
    def remove_border(self, next):
        x = self.column - next.column
        y = self.row - next.row
        if x == -1:
            self.right = False
            next.left = False
        elif x == 1:
            self.left = False
            next.right = False

        if y == -1:
            self.bottom = False
            next.top = False 
        elif y== 1:
            self.top = False
            next.bottom = False 