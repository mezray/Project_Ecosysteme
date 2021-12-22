import pygame
from herbivore import *

class lapin(Herbivore):
    def __init__(self,energie,vie,sexe,rayonVision,rayonContact,position):
        Herbivore.__init__(self,rayonVision,rayonContact)
        Vivant.__init__(self,energie,vie,sexe)
        self.name= "lapin"
        self.enceinte = 20
        self.force = 1
        self.vitesse = 7 #vitesse en fonction de l'énergie
        self.position = position
        self.attaque = self.energie
    
    #sprite du bled
    def draw(self, position, i):
        gifNumber='./sprite/Lapin/frame-'+str(i%3+1)+'.gif'
        image = pygame.image.load(gifNumber)
        screen.blit(image, position)


p=0
while p < 50:
    enfant1=lapin(100,300,'male',400,150,position=[random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)])#random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)
    enfant2=lapin(100,300,"femelle",400,150,position=[random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)])
    listeDesHerbivores.append(enfant1)
    listeDesHerbivores.append(enfant2)
    p+=1