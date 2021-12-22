import pygame, random
from objet import *

class dechet(Objet):
    def __init__(self,energie,position):
        Objet.__init__(self, energie, position)
        self.name = "dechet"
        self.position=position
        
    
    #sprite du bled
    def draw(self, position, i):
        gifNumber='./sprite/Cacs/frame-'+str(i%5+1)+'.gif'
        image = pygame.image.load(gifNumber)
        screen.blit(image, position)
        
p=10
while p < 10:
    enfant=dechet(15000, position=[random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)])#self.__class__ permet de récupérer la classe de 'self'
    listeDesDechets.append(enfant)
    p+=1
