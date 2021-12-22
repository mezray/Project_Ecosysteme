import pygame
from carnivore import *

class loup(Carnivore):
    def __init__(self,energie,vie,sexe,rayonVision,rayonContact,position):
        Carnivore.__init__(self,rayonVision,rayonContact)
        Vivant.__init__(self,energie,vie,sexe)
        self.name= "loup"
        self.enceinte = 0
        self.force = 1
        self.vitesse = 20 #vitesse en fonction de l'énergie
        self.position = position
        self.attaque = self.energie
    
    #sprite du bled
    def draw(self, position, i):
        gifNumber='./sprite/pug/frame-'+str(i%4+1)+'.gif'
        image = pygame.image.load(gifNumber)
        screen.blit(image, position)


class chat(Carnivore):
    def __init__(self,energie,vie,sexe,rayonVision,rayonContact,position):
        Carnivore.__init__(self,rayonVision,rayonContact)
        Vivant.__init__(self,energie,vie,sexe)
        self.name= "chat"
        self.vitesse = 7
        self.force = 1
        self.position=position
        self.attaque = self.energie
        
    def draw(self, position, i):
        gifNumber='./sprite/cat/frame-'+str(i+1)+'.gif'
        image = pygame.image.load(gifNumber)
        screen.blit(image, position)

p=7
while p < 8:
    enfant1=loup(150,500,'male',1250,50,position=[random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)])#self.__class__ permet de récupérer la classe de 'self'
    enfant2=loup(150,500,"femelle",1250,50,position=[random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)])#self.__class__ permet de récupérer la classe de 'self'
    #enfant2=chat(300,300,random.choice(['male',"femelle"]),150,50,position=[random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)])#self.__class__ permet de récupérer la classe de 'self'
    
    listeDesCarnivores.append(enfant1)
    listeDesCarnivores.append(enfant2)
    p+=1


