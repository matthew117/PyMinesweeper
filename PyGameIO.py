'''Defines a 2D UI through pygame for use with a given minesweeper board'''

import pygame
import sys

MINESWEEPER_COLOURS = {
    1 : (0, 0, 170), # Blue
    2 : (0, 170, 0), # Green
    3 : (170, 0, 0), # Red
    4 : (0, 0, 128), # Dark Blue
    5 : (170, 85, 0), # Brown
    6 : (0, 170, 170), # Cyan
    7 : (0, 0, 0), # Black
    8 : (128, 128, 128),  # Gray
    0 : (255, 255, 255)
}

class PyGameIO:
    
    def __init__(self, board):
        self.board = board
        
    def start(self):
        pygame.init()
        self.flag_texture = pygame.image.load("flag.png")
        self.font = pygame.font.Font(None, 50)
        pygame.display.set_caption("Minesweeper")
        self.width = 600
        self.height= 600
        self.window = pygame.display.set_mode((self.width, self.height))
        self.render()
        while not self.board.gameOver and not self.board.gameWin:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    x += 2
                    y += 2
                    tx = (self.width - 4) / self.board.width
                    ty = (self.height - 4) / self.board.height
                    if event.button == 1:
                        if pygame.key.get_mods() & pygame.KMOD_CTRL:
                            self.board.rightClick(x // tx, y // tx)
                        else:
                            self.board.leftClick(x // tx, y // ty)
                    if event.button == 3:
                        self.board.rightClick(x // tx, y // tx)
            self.render()
            pygame.display.flip()


    def render(self):
        tileWidth = (self.width - 4) / self.board.width
        tileHeight = (self.height - 4) / self.board.height
        for x in range(0, self.board.width):
            for y in range(0, self.board.height):
                tile = self.board.tiles[y][x]
                if tile.flagged:
                    self.window.blit(pygame.transform.scale(self.flag_texture, (tileWidth - 10, tileHeight - 10)), pygame.Rect(x*tileWidth + 7, y*tileHeight + 7, tileWidth, tileHeight))
                elif tile.hidden:
                    pygame.draw.rect(self.window, (90, 90, 90), pygame.Rect(x*tileWidth + 2, y*tileHeight + 2, tileWidth, tileHeight))
                elif tile.isBomb:
                    pygame.draw.rect(self.window, (255, 0, 0), pygame.Rect(x*tileWidth + 2, y*tileHeight + 2, tileWidth, tileHeight))
                else:
                    pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(x*tileWidth + 2, y*tileHeight + 2, tileWidth, tileHeight))
                    self.window.blit(self.font.render(str(tile.number), 1, MINESWEEPER_COLOURS[tile.number]), (x*tileWidth + tileWidth * 0.4, y*tileHeight + tileHeight * 0.35))
                    #pygame.draw.rect(self.window, MINESWEEPER_COLOURS[tile.number], pygame.Rect(x*tileWidth + 2, y*tileHeight + 2, tileWidth, tileHeight))
                pygame.draw.rect(self.window, (0, 0, 0), pygame.Rect(x*tileWidth + 2, y*tileHeight + 2, tileWidth, tileHeight), 4)