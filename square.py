import pygame

from pygame.sprite import Sprite, Group
from basic_block import Basic_block

class Square(Basic_block):
    """Representation of square 20x20"""
    def __init__(self, ts):
        """Initilize instance"""
        super(Square, self).__init__()
        self.rect = self.block_rect(ts)
        self.rect.centerx = ts.screen_width / 2
        self.rect.centery = ts.game_window_top + ts.shape_size / 2
    
