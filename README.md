# ANGM2305_Final-Project: Generating Maps with WFC

## Demo
Demo Video: <https://youtu.be/wgKraT8uNvA>

## GitHub Repository
GitHub Repo: <https://github.com/Julileeheehee/ANGM2305_Final-Project>

## Description
For this project, I had three main key things I needed to accomplish:
1. Establish the algorithm with my tiles and their constraint rules
2. Turn my text-based grid into a visual one with images in Pygame
3. Polish the program with user-friendly UI elements

This project took several weeks to make, and because of my very limited Python knowledge, I had to learn a TON of things to be able to achieve these key things. The algorithm was a beast to figure out and I had multiple files to try out different ways of organizing things. After, connecting my algorithm to Pygame was confusing at first, but I eventually figured it out. The third key thing was just for myself. I am a firm believer that the level of polish makes or breaks how a user views a project, so I wanted to make it presentable for a user.

## Breakdown of the files in the src folder
The project.py file runs the whole program on its own, but it would be easy to separate the different parts into their own separate python files. The images file contain all the different images I used. The tiles (blank, coastline, grass, water) were all 64x64 tiles where as the buttons were 128x64. Also included in the src file is a .ttf font file of my own handwritting! That was fun to make.

## Big things I learned during this project
- **Enums** -- and what they do. Turns out, they're super useful. I think the name is just scary
- **Sets** -- Also useful because they're like lists, but can't be indexed and don't have duplicates. I needed it for my Tile class.
- **Specifying data types in function parameters** -- I learned it was good practice to include the type of the parameters to be able to read the code more easily. Also it prevents errors during runtime. Cool!
- **How to make a 2D list** -- I knew I needed to make a grid, but I only knew how to make an array. A nested list or a 2D list was basically the same thing. It was confusing at first, but honestly, it's not too difficult to use once you figure it out
- **The | operator** -- I learned it basically means or. Like this or this. In my case, when I made the Tile objects, they had two states: a type or NONE. So I had to type them like `self.tile_type: TileType | None`
- **Threading** -- I wanted to have the program display step-by-step/frame-by-frame, but it kept completing the grid super fast. I had to learn about threading and how to connect it to the Pygame buttons to be able to handle long parts of the code with delays. TBH I still don't quite understand it
- **Getting mouse inputs in Pygame** -- There were a couple of tutorials I used to help me convert mouse positions into grid locations! That was pretty cool to do, but then I realized I kept mixing up x and y
- **How to import fonts and use them** -- I made my own font!

## Main Resources
- My wonderful partner, Seth Gaglione, who happens to be a software engineer at Boeing. He helped me organize my code and come up with the algorithm structure when I finally swallowed my pride to actually ask for help
- CodingTrain and his WFC livestream video <https://www.youtube.com/watch?v=rI_y2GAlQFM>. Even though he's coding in javascript, it was still refreshing and insightful to see how he worked through the problems. He's definitely the Bob Ross of coding!
- CodingQuest and his WFC video <https://www.youtube.com/watch?v=qRtrj6Pua2A>. In this, he's using Python and Pygame for his demonstration, but I was super determined NOT to use his code. The only thing I really used was how he implemented the weights of the tiles.
- <https://www.pygame.org/docs/> I think I had YouTube and the Pygame documentation page up at all times while working on my project haha.

## What I would do if I had more time
The scope in my proposal was WAY larger than I could realistically accomplish. Not to mention, I had other final projects to complete as well. Here are the things I would do in the future if I ever come back to this project:
- **More Tiles** -- Include more tiles than just 3. There are more things to consider with more complex tiles like having different neighbors on each direction.
- **Weighted Tiles** -- Fix up the weights/probablities of the tiles. Right now, I can skew the map to generate more water tiles than grass and vise versa, but in actual practice, the maps are not consistently showing this. 
- **Animation** -- I think it would be cool for the tiles to have an animation, though, I'm not sure how that will apply when the map is printing every frame.
- **Adjustable grid** -- I originally planned for the user to be able to choose a grid size between 2x2 and 10x10. I even planned out my calculations for the scaling and such, but I just ran out of time to implement it. 
- **No hardcoding locations** Ideally, I want this program to have a scalable window, which means the locations of the text and images need to scale as well. Because of how I organized my window and the panels, I had strange offsets and paddings, but I ran out of time to properly put in the calculations for everything
- **Upload the program to itch.io** -- I want to be able to share this with everyone! I know how to do this from a game engine like Unity and Godot, but I'm not sure with Pygame. 
- **Import tiles** -- Give the user the ability to import their own tiles/tileset, pick the rules between the tiles, and have the program generate the map
- **Analyze the tiles** -- Another idea is to have the program analyze a tileset and produce a map from it. This is similar to the overlapping model of the WFC tile-based model
- **3D models** -- Try this out with 3D models since I want to be a prop modeler or an environmental artist
- **Building a game** -- Try building a game similar to Tiny Glade or Townscaper!
- **Try different programming languages** -- If I wanted to make a game in Unity, I'll need to learn how to create this in C#. C++ for Unreal, and GDscript for Godot (it's Python-inspired, but can't use Python without a plugin)