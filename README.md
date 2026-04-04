# Conway's Game of Life

### Overview
This project implements a cellular automata known as Conway's Game of Life. It consists of two-dimensional grid which cells have one of two states: alive (black) or dead (white). The current state is determined each round by those rules:
- An alive cell with fewer than two or more than three alive neighbours becomes a dead cell
- An alive cell with two or three alive neighbours stays alive
- A dead cell with three alive neighbours becomes an alive cell

### Technologies
Python, libraries: pygame, numpy, random, time

### How to run
python game_of_life.py

### Pipeline
- Creating a grid
- Determining locations of alive cells randomly
- Start of the game - each iteration determining the state of all cells and updating the grid