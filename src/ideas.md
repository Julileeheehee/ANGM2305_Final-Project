# This is a file to map out what I'm doing before I code it

## Different layers to the code:

### Grid
  * Possibly use a 2D list [x][y] for the grid itself
  * 

### Tile
  * The tile needs to know:
    * What it is or what it could be
    * What its neigbors could be
    * What its entropy is if it is not yet collapsed
  * The edges are important to note
  * Dictionary of tiles? Rules?

### Tile Neighbors
  * When the tile object gets made, I'll need to keep track of the neighbors
  * Each neighbor will have its own neighbors and so own...

### Entropy
  * I will need to calculate the lowest entropy of each neighbor
  * Each neighbor will also have a different entropy
  * If two tiles are next to the spot with the lowest entropy, a random tile will be chosen
  * Entropy of 0 means Collapsed

### Collapse
  * After the initial tile is chosen, a random tile in a random direction is chosen
    * This means two tiles will be collapsed
  * Entropy will be constantly evaluated as well as collapsing

---
# What to start with first!!!!!
  * 2x2 grid
  * Make a dictionary of the tiles and their edges
  * Get the entropy of the tile based on the possiblilities of what it could be
    * maybe put the keys into a list and get the length of that?? 
    * Is is possible to get the length of a dictionary??
  * Pick the top tile and have it calculate the entropy of the other tiles
