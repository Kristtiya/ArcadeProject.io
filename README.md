## Welcome to the Arcade Project!

You can access the repository here [on GitHub](https://github.com/Kristtiya/Games-in-Verilog) to view current progress on the different games we are working on!

Prior to this course, I did not have a lot of knowledge about computers so a lot of my knowledge is limited to Computer Architecture. This project has allowed me to better understand how a lot of concepts work. I also have been able to implement a few and see them in action.

### What is this project about?
The purpose of this project is to understand how hardware-based games were developed through research, examples, and trying to develop my own game.

### The Process
A lot of the initial 2 weeks have been focused on researching and understanding the different components that are necessary for developing a game. My main source has been the tutorial book **Designing Games Hardware in Verilog** by Steven Hugg. Through that, different concepts would come up that I would do external research on.

Due to lack of physical resources (FPGA board and CRT Television) I used an [emulator](https://8bitworkshop.com/v3.4.2/?file=clock_divider.v&platform=verilog) provided by the author. It simulates a CRT television so that I can experiment with programming and developing the hardware for games and components.

I followed tutorials provided by the book in order to understand how different pieces of hardware can be applied to designing a video game such as:
  * Counters
  * Single Cycle CPUs
  * ROM vs RAM
  * Flip-Flops



```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Brick Breaking Game


### Mistakes and how we will be Moving Forward
After spending countless hours trying to follow the tutorials provided, I realized the methodology of teaching was not for me. It was similar to ModSim where we would be sort of walked into realizing the answers, while also be provided a lot of example code at once. It made it difficult for me to process what I was trying to learn, and it was hard to debug and complete the unfinished portions of the codes provided. 

**December 5th, 2019**
I ended up pivoting by reviewing the provided code, and starting building from the simplest game - the Tank Game. It does not have a CPU, a scoreboard, or animation implemented. I stripped it from its mechanics such as rotation, multiple sprites, and collision and mainly kept the input modules, the background graphics, and the ROM layout for the sprites. I have now been working on building an environment and developing a testing room rather than a game. The version that is currently in progress is focusing on user input and in-game physics.


### Game Progress
Currently, I am working on a simple Demo game that implements in-game gravity, user input, and jumping.


Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/Kristtiya/ArcadeProject.io/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
