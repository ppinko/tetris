import pygame
from pygame.sprite import Sprite

class Shapes(Sprite):
    """Representation of all game blocks"""

    def __init__(self, screen, ts):
        """Init method"""

        super(Shapes, self).__init__() # inherit from class Sprite
        #self.form = form
        self.screen = screen
        self.color = (255, 255, 0)
        

    def l_shape(self, ts):
        """Create a surface for L-shape block"""
        # p - stands for point
        p0 = (ts.screen_width / 2, ts.game_window_top + ts.shape_size)
        p1 = (ts.screen_width / 2, ts.game_window_top)
        p2 = (ts.screen_width / 2 - ts.shape_size, ts.game_window_top)
        p3 = (ts.screen_width / 2 - ts.shape_size, 
                ts.game_window_top + 2 * ts.shape_size)
        p4 = (ts.screen_width / 2 + 2*  ts.shape_size, 
                ts.game_window_top + 2 * ts.shape_size)
        p5 = (ts.screen_width / 2 + 2*  ts.shape_size, 
                ts.game_window_top + ts.shape_size)
        points = [p0, p1, p2, p3, p4, p5, p0]
        # color = (255, 255, 0)
        return points

    def draw_shape(self, ts):
        """Creates and draws a surface"""
        points_list = self.l_shape(ts)
        pygame.draw.polygon(self.screen, self.color, points_list, 0)



