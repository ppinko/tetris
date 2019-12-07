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

        # Game window
        self.game_window_w = 400
        self.game_window_h = 500
        self.game_window_color = (255, 255, 255)
        self.game_window_bottom_offset = 50
        self.game_window_left = (self.screen_width - self.game_window_w) / 2
        self.game_window_top = self.screen_height - self.game_window_bottom_offset - self.game_window_h
