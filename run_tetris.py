"""Main script for running tetris"""

import pygame
import sys

from pygame.sprite import Sprite, Group

from settings import Settings
from shapes import Shapes
from basic_block import Basic_block
from square import Square
from i_shape import I_shape
from l_shape import L_shape

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
    
    # TEST 
    # element = Square(ts)
    # pygame.draw.rect(screen, (255, 255, 0), element.rect)

    element = L_shape(screen, ts)
    element.blint(screen, ts)


    while True:
        gf.check_events()
        gf.blit_game_window(screen, ts)
        pygame.display.flip()

run_tetris()
