import pygame
pygame.init()

width,height = 800, 800
p_height, p_width = 10,10
color = (255, 255, 255)
window = pygame.display.set_mode([width,height]) #Create Window

snake_step = 10


#Hello World Test function

# Main Function

def main():

    snake = SNAKE(400, 400, [],[])
   

    #Run until user quits
    running = True
    while running:
        
        generate_graphics(height, width, p_height,p_width)
        pygame.draw.rect(window, color, (snake.head_x, snake.head_y,p_width,p_height) ) #draw_head
        pygame.display.update()
        for event in pygame.event.get(): # Escape game when window is closed
            if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE:# End game when ESC is pressed
                running = False
            if event.key == pygame.K_w:
                snake.head_y += snake_step
            if event.key == pygame.K_a:
                snake.head_x -= snake_step
            if event.key == pygame.K_s:
                snake.head_y -= snake_step
            if event.key == pygame.K_d:
                snake.head_y += snake_step
                
    


def printparty():
    print("Hello World")


def generate_graphics(border_height, border_width, pixel_height, pixel_width):
    for i in range(border_width):
        for j in range (border_height):
            ## Generate border
            if i == (border_width - pixel_width) or i == 0 or j == (border_height - pixel_height) or j == 0:
                pygame.draw.rect(window,color,(i,j,pixel_width,pixel_height)) 

def move_snake(head_x, head_y, body_x, body_y):
    print("*Slither**")



#Classes

#Create Snake class to allow for the spawning of the snake object
class SNAKE:
    """define snake class to support more snakes in the future"""
    def __init__(self, head_x,head_y, body_x,body_y):
        self.head_x = head_x
        self.head_y = head_y
        self.body_x = body_x
        self.body_y = body_y





if __name__ == "__main__":
    printparty()
    main()