import pygame
from carnivore import *

class loup(Carnivore):
    def __init__(self,energie,vie,sexe,rayonVision,rayonContact,position):
        Carnivore.__init__(self,rayonVision,rayonContact)
        Vivant.__init__(self,energie,vie,sexe)
        self.name= "loup"
        self.enceinte = 100
        self.digestion=500
        self.force = 1
        self.vitesse = 7
        self.position = position
        self.attaque = self.energie
    
    #sprite
    def draw(self, position, i):
        gifNumber='./sprite/pug/frame-'+str(i%4+1)+'.gif'
        image = pygame.image.load(gifNumber)
        screen.blit(image, position)


class chat(Carnivore):
    def __init__(self,energie,vie,sexe,rayonVision,rayonContact,position):
        Carnivore.__init__(self,rayonVision,rayonContact)
        Vivant.__init__(self,energie,vie,sexe)
        self.name= "chat"
        self.enceinte = 50
        self.digestion=300
        self.vitesse = 7
        self.force = 1
        self.position=position
        self.attaque = self.energie
        
    def draw(self, position, i):
        gifNumber='./sprite/cat/frame-'+str(i+1)+'.gif'
        image = pygame.image.load(gifNumber)
        screen.blit(image, position)

p=0
while p < 2:
    enfant1=loup(150,500,'male',300,150,position=[random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)])
    enfant2=loup(150,500,"femelle",300,150,position=[random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)])
    #enfant2=chat(300,300,random.choice(['male',"femelle"]),150,50,position=[random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)])
    
    listeDesCarnivores.append(enfant1)
    listeDesCarnivores.append(enfant2)
    p+=1


