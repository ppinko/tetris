import pygame

from pygame.sprite import Sprite, Group
from basic_block import Basic_block

class I_shape(Basic_block):
    """Representation of square 20x20"""
    def __init__(self, screen, ts):
        """Initilize instance"""
        super(I_shape, self).__init__()
        self.rect_1 = self.block_rect(ts)
        self.rect_1.centerx = ts.screen_width / 2
        self.rect_1.centery = ts.game_window_top + 3 * ts.shape_size / 2
        self.rect_2 = self.block_rect(ts)
        self.rect_2.centerx = ts.screen_width / 2
        self.rect_2.centery = ts.game_window_top + ts.shape_size / 2
        self.rect_list = [self.rect_1, self.rect_2]

    def blint(self, screen, ts):
        """Test"""
        for rect in self.rect_list:
            pygame.draw.rect(screen, (256, 255, 0), rect)
