"""Game settings"""

import pygame.image

class Settings():
    """All game settings"""
   
    def __init__(self):
        # Screen settings and game title
        self.screen_width = 1200
        self.screen_height = 600
        self.screen_bg_color = (0, 0, 0)
        self.title = "Tetris for kids"
        self.screen_icon = pygame.image.load('images/tetris.png')

