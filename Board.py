''' Represents a Minesweeper game board '''
from Tile import Tile
from random import shuffle
import sys

class Board:
  
  def __init__(self, width, height, numOfBombs):
    self.width = width
    self.height = height
    self.tiles = []
    self.bombs = []
    self.gameOver = False
    self.gameWin = False
    
    # initialize a 2D array of size width x height with blank tiles
    possibleCoordinates = []
    for y in range(0, height):
      row = []
      for x in range(0, width):
        t = Tile()
        row.append(t)
        possibleCoordinates.append((x,y))
      self.tiles.append(row)
      
    # add some bombs to random locations    
    for i in range(numOfBombs):
      shuffle(possibleCoordinates)
      x, y = possibleCoordinates.pop()
      self.tiles[x][y].isBomb = True
      self.bombs.append((x, y))
      
    self.calculateAdjacentBombs()
  
  # perform a convolution to sum adjacency info for each tile
  def calculateAdjacentBombs(self):
    for y in range(0, self.height):
      for x in range(0, self.width):
        for dy in range(-1,2):
          for dx in range(-1,2):
            if y + dy >= 0 and y + dy < self.height:
              if x + dx >= 0 and x + dx < self.width:
                if self.tiles[y + dy][x + dx].isBomb:
                  self.tiles[y][x].number += 1
  
  def recurseBlanks(self, x, y):
    tile = self.tiles[y][x]
    if tile.isBomb:
      return
    if tile.flagged:
      return
    if tile.number > 0:
      tile.hidden = False
      return
    if tile.number == 0:
      tile.hidden = False
      for dy in range(-1,2):
        for dx in range(-1,2):
          if y + dy >= 0 and y + dy < self.height:
            if x + dx >= 0 and x + dx < self.width:
              if self.tiles[y + dy][x + dx].hidden:
                self.recurseBlanks(x + dx, y + dy)
  
  def leftClick(self, x, y):
    if x < 0 or x >= self.width or y < 0 or y >= self.height:
      return
    tile = self.tiles[y][x]
    if tile.flagged:
      return
    if tile.isBomb:
      self.gameOver = True
    elif tile.number == 0:
      self.recurseBlanks(x, y)
    else:
      tile.hidden = False
      
  def rightClick(self, x, y):
    if x < 0 or x >= self.width or y < 0 or y >= self.height:
      return
    tile = self.tiles[y][x]
    if tile.flagged:
      tile.flagged = False
    else:
      tile.flagged = True
      # temporarily assume this is the last bomb
      foundAllBombs = True
      for i, j in self.bombs:
        bombTile = self.tiles[i][j]
        if not bombTile.flagged:
          foundAllBombs = False
      self.gameWin = foundAllBombs
  
  def __str__(self):
    s = ""
    for row in self.tiles:
      for tile in row:
        if tile.flagged:
          s += "F "
        elif tile.hidden:
            s += "? "
        elif tile.number == 0:
          s += "  "
        elif tile.isBomb:
          s += "* "
        else:
          s += "{0} ".format(tile.number)
      s += "\n"
    return s