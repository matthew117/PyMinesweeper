import sys
import pygame

from Board import Board
from CommandLineIO import CommandLineIO
from PyGameIO import PyGameIO

def main():
  board = Board(8, 8, 6)
  
  # ui = CommandLineIO(board)
  # ui.start()
  ui = PyGameIO(board)
  ui.start()
  
    
if __name__ == "__main__":
  main()