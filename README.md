## Welcome to the Arcade Project!

You can access the repository here [on GitHub](https://github.com/Kristtiya/Games-in-Verilog) to view current progress on the different games we are working on!

Prior to this course, I did not have a lot of knowledge about computers so a lot of my knowledge is limited to Computer Architecture. This project has allowed me to better understand how a lot of concepts work. I also have been able to implement a few and see them in action.

### Our Mission
The purpose of this project is to understand how hardware-based games were developed through research, examples, and trying to develop my own game.

### The Process
A lot of the initial 2 weeks have been focused on researching and understanding the different components that are necessary for developing a game. My main source has been the tutorial book **Designing Games Hardware in Verilog** by Steven Hugg. Through that, different concepts would come up that I would do external research on.

Due to lack of physical resources (FPGA board and CRT Television) I used an [emulator](https://8bitworkshop.com/v3.4.2/?file=clock_divider.v&platform=verilog) provided by the author. It simulates a CRT television so that I can experiment with programming and developing the hardware for games and components.

I followed tutorials provided by the book in order to understand how different pieces of hardware can be applied to designing a video game such as:
  * Counters
  * Single Cycle CPUs
  * ROM vs RAM
  * Flip-Flops

### Components and some of their Possible Implementations
What has been fun about this project is seeing the different creative ways different components can be used to create features for the game. For example, logic gates such as AND, OR, or XOR are very useful in determining different flags in games such as collision. 

#### Counters and Flip-Flops
One interesting implementation that I have seen before, and that is also used in game development is debouncing. Buttons, when pressed, can produce sound which mess with the signal. In order to combat this, the process of debouncing is applied. 
This way this works is by using 2 flip flops that are enabled at the positive edge of the system's clock. One takes in the input, the other takes the output of that flip-flop, and then sends it to anothe flip-flop that is enabled at the positive edge of the clock and also by a counter. The counter can be created using different types of components, but a simple method could be using more flip-flops. The amount of time the designer believes the button needs to be pressed for it to be considered a valid input signal then affects the amount of ticks the counter will count up to. Debouncing is super important for hardware games as the inputs all come from buttons. The games have to have responsive controls or else the users will not be compelled to play anymore.

Another implementation of a counter that I learned in this project has been for trying to implement in-game physics. In the DaikonDemo module, I used it when programming the jump function of the game. When the user gives the jump command the sprite moves vertically for a set amount of time rather than the user holding the jump button.

#### Single Cycle CPU
The size (bits) of the single cycle CPU determines the capabilities of the games. It can either limit or enhance the capabilities of the game such as affecting color, graphics, sound, and even control. The more the bits, the more the opcodes that can be used, numbers that can be handled, colors that can be presented, etc. 

What I found interesting, though I did not have too much time to become fully fluent in this topic, was creating an assembly language dedicated for the games. Different game consoles have their own assembly code. A whole new language can be made for each individual game. For one of the example programs that implemented a single cycle cpu, the author had their own assembly language they used that was dedicated to the game they designed.

#### ROM vs RAM
I did have trouble differentiating the two initally as their names are very similar. Both are also forms of memory which made it even more difficult. After looking at examples, however, it is very clear what they do and how they can be used.

RAM, or Random Access Memory, is memory that is only available when the device is running. In the case of video games- it can keep track of states of objects such as if an object should be visible or not. It stores temporary values for games which do not need to be saves. RAM must have power in order to hold its data, so once it loses power, it loses its data.

ROM, or Read-Only Memory, stores instructions or data that is usually essential for a device to run. In PCs it holds the boot-up software. It can vary, but in games it can hold features such as the graphics for the games and for some older game consoles such as the gameboy, ROMS were used to store a lot of the game's features.

### Brick Breaking Game Demo
The brick breaking game is just like [Breakout](https://en.wikipedia.org/wiki/Breakout_(video_game)) though it is less polished than the actual game. The layout was already developed for this game so my goal for this demo was to implement the health-down system and keeping the paddle within the borders.

This demo further cemented the concept of hardware programming compared to software programming. Collision is not the same as in when programming a game on python. It involves flags or focusing on bits, such as checking if 2 signals that are entering the same section. I was stuck on that concept for a bit as I kept focusing on the collision of graphics and not the collision of data in-game.

I was able to update the game with a health down system that resets the ball and brings the life down by 1 value when the ball goes past the paddle. I also was able to get the paddle to stay within the left border of the game field, but the right border is still unstable so further development will have to be made. 

The code for the updated demo can be found in the repository under BrickSmash. 
### Mistakes and how we will be Moving Forward
After spending countless hours trying to follow the tutorials provided, I realized the methodology of teaching was not for me. It was similar to ModSim where we would be sort of walked into realizing the answers, while also be provided a lot of example code at once. It made it difficult for me to process what I was trying to learn, and it was hard to debug and complete the unfinished portions of the codes provided. 

**December 5th, 2019**
I ended up pivoting by reviewing the provided code, and starting building from the simplest game - the Tank Game. It does not have a CPU, a scoreboard, or animation implemented. I stripped it from its mechanics such as rotation, multiple sprites, and collision and mainly kept the input modules, the background graphics, and the ROM layout for the sprites. I have now been working on building an environment and developing a testing room rather than a game. The version that is currently in progress is focusing on user input and in-game physics.

### Game Progress
Currently, I am working on a simple Demo game that implements in-game gravity, user input, and jumping. At the moment, it does not contain any of the detailed graphics. It also does not implement a more detailed RAM, bitmap, or a single cycle CPU. 

The image below shows the planned layout for the demo.
![Layout](https://github.com/Kristtiya/ArcadeProject/blob/master/Screenshot%20from%202019-12-04%2016-44-29.png "Game Layout")

As of now, I have complete the MVP of this 2 week sprint as the game takes in user input and can control an object on the screen. My goal for the next week is to polish the game even more



Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/Kristtiya/ArcadeProject.io/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

