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
