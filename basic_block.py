import pygame
from pygame.sprite import Sprite
from settings import Settings

class Basic_block(Sprite):
    """Basic game element"""

    def __init__self(self, ts):
        """Initilize instance"""
        super(Basic_block, self).__init__()
    
    def block_rect(self, ts):
        """Creates surface for the basic block"""
        rect = pygame.Rect((0, 0), (ts.shape_size, ts.shape_size))
        return rect

