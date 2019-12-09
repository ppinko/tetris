"""Script containing all main game functions"""

import pygame
import sys

def check_events(element):
    """Checking events and acts accordingly"""
    
    # Collecting all events
    events = pygame.event.get()
    
    # Checking event types
    for event in events:
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        check_key_downs(event, element)
        rotate_key(event, element)

def check_key_downs(event, element):
    """Checking key downs"""

    if event.type == pygame.KEYDOWN:
        # Moving block down, left and right
        if event.key == pygame.K_DOWN:
            element.move_down = True
        if event.key == pygame.K_LEFT:
            element.move_left = True
        if event.key == pygame.K_RIGHT:
            element.move_right = True

def rotate_key(event, element):
    """Rotating shape"""

    if event.key == pygame.K_a:
        element.rotate('left')
    if even.key == pygame.K_d:
        element.rotate('right')


def blit_game_window(screen, ts):
    """Bliting game window - it does not change during the game"""
    
    top_left_corner = (ts.game_window_left, ts.game_window_top)
    gw_size = (ts.game_window_w, ts.game_window_h)
    gw_rect = pygame.Rect(top_left_corner, gw_size)
    pygame.draw.rect(screen, ts.game_window_color, gw_rect, 5)
