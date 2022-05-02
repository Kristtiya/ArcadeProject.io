from matplotlib.pyplot import text
import pygame
import random

pygame.init()
pygame.font.init()

# -- Window and game border
p_height, p_width = 20,20 #Pixel dimensions
width,height = 800, 800  # Window Dimensions
window = pygame.display.set_mode([width,height+ 100]) #Create Window
active_vert = height - p_height
active_hoz = width - p_width
paddleheight = 100
border = (0,0,p_width,p_height)


white = (255, 255, 255) #color white

paddle_speed = 5


bottom_flag = 0
top_flag = 0





def main():
    running = True

    player1 = Player(width/2 - paddleheight/2, 60, 20, paddleheight) #instantiate player 1
    player2 = Player(width/2 - paddleheight/2, 720, 20, paddleheight) #instantiate player 2


    
    while running:
        window.fill((0,0,0))

        player1_graphics = (player1.x_pos,player1.y_pos,player1.plwidth,player1.plheight)
        player2_graphics = (player2.x_pos, player2.y_pos,player2.plwidth,player2.plheight)

        generate_graphics(height, width, p_height, p_width,player1_graphics,player2_graphics)

        collision(player1.y_pos, player1.plheight)


        # --- Keyboard controls ---
        for event in pygame.event.get(): # Escape game when window is closed
            pygame.key.set_repeat(1,10)
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE:# End game when ESC is pressed
                    running = False


                if event.key == pygame.K_w and top_flag == 0:# End game when ESC is pressed
                    pygame.key.set_repeat(10)
                    player1.y_pos -= 1*paddle_speed

                if event.key == pygame.K_s and bottom_flag == 0:# End game when ESC is pressed
                    player1.y_pos += 1 * paddle_speed







        pygame.display.update() # refresh graphics



def collision(yposition, player_height):
    global height
    global width
    global bottom_flag
    global paddle_speed
    global top_flag
    

    if yposition + paddle_speed >= height - player_height - 100:
        bottom_flag = 1
        top_flag = 0
    if yposition - paddle_speed <= 20:
        bottom_flag = 0
        top_flag  = 1
    else:
        bottom_flag = 0
        top_flag = 0






def generate_graphics(border_height, border_width, pixel_height, pixel_width, p1, p2): 
    for i in range(border_width): #Draw game border
        for j in range (border_height):
            if i == (active_hoz) or i == 0 or j == (active_vert) or j == 0:
                border = (i,j,pixel_width,pixel_height)
                pygame.draw.rect(window,white,border) 
                pygame.draw.rect(window,white,p1) 
                pygame.draw.rect(window,white,p2) 
                




class Player:
    def __init__(self, y_pos,x_pos, plwidth, plheight):
        self.y_pos = y_pos
        self.x_pos = x_pos
        self.plwidth = plwidth
        self.plheight = plheight
    


if __name__ == "__main__":
        main()