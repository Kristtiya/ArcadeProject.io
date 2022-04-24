from matplotlib.pyplot import text
import pygame
import random

pygame.init()
pygame.font.init()



def printparty():
    print("Begin Ssslithering!")

p_height, p_width = 20,20 #Pixel dimensions
width,height = 800, 800  # Window Dimensions

color = (255, 255, 255) #color white
window = pygame.display.set_mode([width,height+ 100]) #Create Window

snake_step = p_height #snake step size
object_direction = 1 # 1 pos direction, -1 neg direction
object_h_v = 0 # 0 is horizontal, 1 is vertical
border = (0,0,p_width,p_height)
game_over = 0
food_present = 1
POKEFONT = pygame.font.Font("PokemonGBfont.ttf", 32)
score_position = [60, 800+20]
points = 0
active_vert = height - p_height
active_hoz = width - p_width




# Main Function
def main():
    prev_x = 20
    prev_y = 20
    global object_direction
    global object_h_v
    snake_len = 1 #snake starts with length of 1 unit

    running = True
    snake = SNAKE(400, 400, [100],[100]) #instantiate player snake
    dot = Food(random.randrange(0,height, snake_step),random.randrange(0,width,snake_step))
    snake_object = [(snake.body_x[0], snake.body_y[0],p_width,p_height)]
    

    while running:
        window.fill((0,0,0)) #Clear Screen
        collision(snake.body_x[0], snake.body_y[0],dot.x, dot.y)
        snake.body_x = [snake.body_x[0]] + snake.body_x
        snake.body_y = [snake.body_y[0]] + snake.body_y
        


        ## --- Snake Movement ---
        
        if object_h_v == 0:
            snake.body_x[0 ]+= (object_direction * snake_step)
        else:
           snake.body_y[0] += (object_direction * snake_step)
        
        prev_x = snake.body_x[0] #Previous head position
        prev_y = snake.body_y[0] #Previous head position
        
        #

        
        ## --- Food object ---
        food_object = (dot.x, dot.y,p_width,p_height)
        if food_present == 0:
            snake_len += 1
            snake.body_x.insert(prev_x,1)
            snake.body_y.insert(prev_y,1)
            #snake.body_y.append(prev_y)
            del dot
            dot = generate_food()
        snake.body_x.pop() #remove last object
        snake.body_y.pop() #remove last object
        print(snake.body_x)


        snake_object = (snake.body_x[0], snake.body_y[0], p_width, p_height)
        
        

            
        
        # --- Graphics ---
        for i in range(snake_len):
            pygame.draw.rect(window, color, (snake.body_x[i], snake.body_y[i], p_width, p_height)) #draw snake head

        generate_graphics(height, width, p_height,p_width,food_object) #generate border, snake, and food
        
            

        # --- Generate Text ---
        text_surface =  POKEFONT.render(str(points),False,color)
        window.blit(text_surface, score_position)
        pygame.display.update() # refresh graphics
        
        
        # --- Keyboard controls ---
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


def generate_graphics(border_height, border_width, pixel_height, pixel_width,food_obj): 
    for i in range(border_width): #Draw game border
        for j in range (border_height):
            if i == (active_hoz) or i == 0 or j == (active_vert) or j == 0:
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


    food = Food(random.randrange(p_height,active_vert, snake_step),random.randrange(p_width,active_hoz,snake_step))
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
    global object_direction
    global object_h_v
    global points

    if (object_x == p_width) and object_direction == -1 and object_h_v == 0: # left border
        snake_step = 0
        game_over = 1
    
    elif ((object_x + p_width) == (width - p_width)) and object_direction == 1 and object_h_v == 0: # right border
        snake_step = 0
        game_over = 1

    elif (object_y == p_height) and object_direction == -1 and object_h_v == 1: # upper border
        snake_step = 0
        game_over = 1
    
    elif ((object_y + p_height) == (height - p_height)) and object_direction == 1 and object_h_v == 1: # lower border
        snake_step = 0
        game_over = 1

    elif object_y == food_y and (object_x == food_x + p_width) and object_direction == -1 and object_h_v == 0:
        points += 10
        food_present = 0
    elif object_y == food_y and (object_x == food_x - p_width) and object_direction == 1 and object_h_v == 0:
        points += 10
        food_present = 0
    elif object_x == food_x and (object_y == food_y + p_height) and object_direction == -1 and object_h_v == 1:
        points += 10
        food_present = 0
    elif object_x == food_x and (object_y == food_y - p_height) and object_direction == 1 and object_h_v == 1:
        points += 10
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