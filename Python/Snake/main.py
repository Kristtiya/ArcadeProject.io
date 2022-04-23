import pygame
import random

pygame.init()

width,height = 800, 800 # Window Dimensions
p_height, p_width = 20,20 #Pixel size
color = (255, 255, 255) #color white
window = pygame.display.set_mode([width,height]) #Create Window

snake_step = p_height #snake step size
object_direction = 1 # 1 pos direction, -1 neg direction
object_h_v = 0 # 0 is horizontal, 1 is vertical
border = (0,0,p_width,p_height)
game_over = 0
food_present = 0



# Main Function
def main():
    running = True

    snake = SNAKE(400, 400, [],[]) #instantiate player snake
    dot = Food(random.randrange(0,height, snake_step),random.randrange(0,width,snake_step))

    global object_direction
    global object_h_v
   
    #Run until user quits
    
    while running:
    
        window.fill((0,0,0))
        if food_present == 0:
            del dot
            dot = generate_food()

        # move_snake(object_direction, object_h_v, snake.head_x, snake.head_y)
        if object_h_v == 0:
            snake.head_x += (object_direction * snake_step)
        else:
            snake.head_y += (object_direction * snake_step)
        
        food_object = (dot.x, dot.y,p_width,p_height)
        snake_object = (snake.head_x, snake.head_y,p_width,p_height)
        collision(snake.head_x, snake.head_y,dot.x, dot.y)
        
        
        generate_graphics(height, width, p_height,p_width,snake_object,food_object)
        
        
        pygame.display.update() # refresh graphics
        

        for event in pygame.event.get(): # Escape game when window is closed
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE:# End game when ESC is pressed
                    running = False
                elif event.key == pygame.K_w:
                    object_direction = -1
                    object_h_v = 1
                elif event.key == pygame.K_s:
                    object_direction = 1
                    object_h_v = 1
                elif event.key == pygame.K_a:
                    object_direction = -1
                    object_h_v = 0
                elif event.key == pygame.K_d:
                    object_direction = 1
                    object_h_v = 0

def printparty():
    print("Begin Ssslithering!")


def generate_graphics(border_height, border_width, pixel_height, pixel_width,player,food_obj):
    pygame.draw.rect(window, color, player) #draw_head
    for i in range(border_width):
        for j in range (border_height):
            ## Generate border
            if i == (border_width - pixel_width) or i == 0 or j == (border_height - pixel_height) or j == 0:
                border = (i,j,pixel_width,pixel_height)
                pygame.draw.rect(window,color,border) 
                pygame.draw.rect(window,color,food_obj)

def generate_food():
    global p_height
    global p_width
    global height
    global width
    global food_present
    global snake_step

    food = Food(random.randrange(0,height-p_height, snake_step),random.randrange(0,width-p_width,snake_step))
    food_present = 1
    return food

def collision(object_x, object_y, food_x, food_y):
    global height
    global width
    global p_height
    global p_width
    global snake_step
    global game_over 
    global food_present

    #need to figure out how to allow snake to slither along border
    if object_x == p_width  or ((object_x + p_width) == (width - p_width) or
        object_y == p_height or (object_y + p_height) == (height - p_height)):
        snake_step = 0
        game_over = 1

    if object_x == food_x and object_y == food_y:
        food_present = 0





#Classes

#Create Snake class to allow for the spawning of the snake object
class SNAKE:
    """define snake class to support more snakes in the future"""
    def __init__(self, head_x,head_y, body_x,body_y):
        self.head_x = head_x
        self.head_y = head_y
        self.body_x = body_x
        self.body_y = body_y

class Food:
    """define snake class to support more snakes in the future"""
    def __init__(self, x, y):
        self.x = x
        self.y = y



if __name__ == "__main__":
    printparty()
    main()