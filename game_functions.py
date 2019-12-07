"""Script containing all main game functions"""

import pygame
import sys

def check_events():
    """Checking events and acts accordingly"""
    
    # Collecting all events
    events = pygame.event.get()
    
    # Checking event types
    for event in events:
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

def blit_game_window(screen, ts):
    """Bliting game window - it does not change during the game"""
    
    top_left_corner = (ts.game_window_left, ts.game_window_top)
    gw_size = (ts.game_window_w, ts.game_window_h)
    gw_rect = pygame.Rect(top_left_corner, gw_size)
    pygame.draw.rect(screen, ts.game_window_color, gw_rect, 5)
