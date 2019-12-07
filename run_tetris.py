"""Main script for running tetris"""

import pygame
import sys

from pygame.sprite import Sprite, Group

from settings import Settings
from shapes import Shapes

import game_functions as gf

def run_tetris():
    # Main game function

    pygame.init()
    
    # Initilize settings
    ts = Settings() # ts - tetris settings
    
    # Setting screen size, caption and icon
    screen = pygame.display.set_mode((ts.screen_width, ts.screen_height))
    pygame.display.set_caption(ts.title)
    pygame.display.set_icon(ts.screen_icon)
    screen.fill(ts.screen_bg_color)
    
    # Test polygon
    l_Shape = Shapes(screen, ts)
    l_Shape.draw_shape(ts)

    while True:
        gf.check_events()
        gf.blit_game_window(screen, ts)
        pygame.display.flip()

run_tetris()
