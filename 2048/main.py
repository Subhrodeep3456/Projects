import pygame 
import random
import math

pygame.init()

#Defining constants
FPS = 60


WIDTH, HEIGHT = 800, 800
ROWS = 4
COLS = 4

RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS

OUTLINE_COLOR = (187, 173, 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192, 180)
FONT_COLOR = (119, 110, 101)

#Create PyGame Window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

FONT = pygame.font.SysFont("comicsans", 60, bold=True)

MOVE_VEL = 20

#Defining Tiles
class Tile:
    COLORS = [     #Colors used in 2048
        (237, 229, 218), #2
        (238, 225, 201), #4
        (243, 178, 122), #8
        (246, 150, 101), #16
        (247, 124, 95),  #32
        (247, 95, 59),   #64
        (237, 208, 115), #128
        (237, 204, 99),  #256
        (236, 202, 80),  #512

    ]

    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.x = col * RECT_WIDTH
        self.y = row * RECT_HEIGHT

    def get_color(self):
        color_index = int(math.log2(self.value)) - 1
        color = self.COLORS[color_index]
        return color

    def draw(self, window):
        color = self.get_color()
        pygame.draw.rect(window, color, (self.x, self.y, RECT_WIDTH, RECT_HEIGHT))

        text = FONT.render(str(self.value), 1, FONT_COLOR)
        window.blit(text, )

    def set_pos(self):
        pass

    def move(self, delta):
        pass



def draw_grid(window):   #Draw grid
    for row in range(1,ROWS):
        y = row * RECT_HEIGHT
        pygame.draw.line(window, OUTLINE_COLOR, (0, y), (WIDTH, y), OUTLINE_THICKNESS)
        
    for col in range(1,COLS):
        x = col * RECT_WIDTH
        pygame.draw.line(window, OUTLINE_COLOR, (x, 0), (x, HEIGHT), OUTLINE_THICKNESS)  
    
    
    
    
    pygame.draw.rect(window, OUTLINE_COLOR, (0, 0, WIDTH, HEIGHT), OUTLINE_THICKNESS)

    



#Do graphics
def draw(window):
    window.fill(BACKGROUND_COLOR)
    

    draw_grid(window)


    pygame.display.update()  #Always fill screen first then other operations take place



#Creating game loop
def main(window):
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If exit button then break
                run = False
                break

        draw(window)   

    pygame.quit()

if __name__ == "__main__": #Only exec function when running file DIRECTLY
    main(WINDOW)





