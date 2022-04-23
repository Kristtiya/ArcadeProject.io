#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ncurses.h>

#include "header.h"
//#include "KeyboardInput.h"


// to run: gcc Main.c -o Main

// Defining Variable
bool game_run = true;


int bound_height = 30;
int bound_width = 30;
int i;
int j;
int fruit_x;
int fruit_y;

int snake_x = 20;
int snake_y = 20;

int key;
int prev_x;
int prev_y;


	

char str[3];

void draw_boundary();
void user_control();
void food_generator();
void snake_movement();

void main() //Main function
{   
    while(game_run = true){
        int in = getchar( );

        if( in != ERR )
            key = in;
        switch( key )
        {
            // case KEY_DOWN:
            //         snake_y++;
            //         break;
            // case KEY_RIGHT:
            //         snake_x++;
            //         break;
            // case KEY_UP:
            //     snake_y--;
            //     break;
            // case KEY_LEFT:
            //     snake_x--;
            //     break;
            case 'x':
                game_run = false;
                break;

        }
        
        if(snake_x == bound_width || snake_y == bound_height){
            game_run = false;
            }
        else{
            //helloworldtest();
            //food_generator();
            draw_boundary();
            snake_movement();
            }

    }
}


// Functions

// Draws the boundary of the game.
void draw_boundary(){
    //system("cls");
    printf("\n");
    for (i = 0; i < bound_height; i++) {
        for (j = 0; j < bound_width; j++) {
            if (i == 0 || i == bound_width - 1 || j == 0 || j == bound_height - 1){
                printf("#");
            }
            else if(i == fruit_y && j == fruit_x){
                 printf("O");}
            else if(snake_y==i && snake_x==j){
                 printf("S");}
            else {
                printf(" ");
            }
        }
        printf("\n");
    }
}

// Determines position of food
void food_generator(){
        
            fruit_x = (rand() % (bound_width - 1));
            fruit_y = (rand() % (bound_height - 1));
        }

void snake_movement(){
        snake_x = snake_x;
            
        }




