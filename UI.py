import pygame
from win32api import GetSystemMetrics


#définir taille écran:

SCREENWIDTH=1920  
SCREENHEIGHT=1080
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Environnement")