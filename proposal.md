# Generating Maps with WFC

## Repository
https://github.com/Julileeheehee/ANGM2305_Final-Project.git

## Description
This project will explore the Wave Function Collapse algorithm and how to use it to generate maps from implemented tiles. This is the basis of procedurally generated spaces and objects.

## Features
- Choose map size to generate
	- A slider or input boxes will ask the user the size of the map they want to generate. It will be width x height in units.
- Choose the tiles to generate from
	- For this project, 2D Top-Down tiles will be used, but there will be an option to use user-provided tiles instead
- Include weights 
	- This will create a way for land-specific environments to be generated. For example, creating a map that has more water or more forests.

## Challenges
- What is WFC and entropy??
    - I will need to understand the WFC algorithm and how to properly calculate entropy.
- Pygame and grids
    - I need to figure out how to make a grid system in Pygame and how to control the size via either a slider or input box
- Pygame and images
    - A little later in development, I will need to create an input system to choose which tiles to include in the map

## Outcomes
Ideal Outcome:
- Ideally, I would like to be able to have a working "game" where the user can choose the tiles they want to use and generate different maps with.

Minimal Viable Outcome:
- Minimally, I want to create a 5x5 map with 3 tiles. The tiles will be a water tile, coastline tile, and a grass tile. This will ensure that while, yes, the map is "boring", my algorithm does work.

## Milestones

- Week 1 (4/13 - 4/19)
  1. Learn Pygame: grids and images
  2. Start writing out the code to use just two tiles: grass and stone

- Week 2 (4/20 - 4/26)
  1. Put in three tiles: water, coast, grass
  2. Make the grid bigger with just user input

- Week 3 (4/27 - 5/3)
  1. Add corner tiles
  2. Figure out weights for the maps

- Week 4 (5/4 - 5/10)
  1. Add more tiles with the option to choose the tiles
  2. Add UI to make the program look nice
  3. Have friends test out the program

- Final two days (5/11 - 5/12)
  1. Check everything for bugs
  2. Maybe put it on Itch.io for portfolio purposes
  3. Double check project requirements on the rubric
