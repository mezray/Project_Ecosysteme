import pygame
from win32api import GetSystemMetrics


#définir taille écran:
SCREENWIDTH=800
SCREENHEIGHT=600
SCREENWIDTH=GetSystemMetrics(0)
SCREENHEIGHT=GetSystemMetrics(1)
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Environnement")