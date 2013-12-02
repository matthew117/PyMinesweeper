''' Represents one tile on a Minesweeper board '''
class Tile:
  
  def __init__(self):
    self.isBomb = False
    self.hidden = True
    self.number = 0
    self.flagged = False