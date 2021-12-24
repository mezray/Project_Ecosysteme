import pygame
from win32api import GetSystemMetrics


#définir taille écran:
SCREENWIDTH=1500  
SCREENHEIGHT=800
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Environnement")