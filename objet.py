listeDesViandes=[]
listeDesDechets=[]

import pygame, random
SCREENWIDTH=800
SCREENHEIGHT=600
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

class Objet:
    def __init__(self,energie,vie,sexe):
        self.energie=energie
        self.vie=vie
        self.sexe=sexe

    def reproduire(self):#tout les être vivants savent reproduire
        pass

    def inZone(self,rayon,objectPosition):#check si la distance entre 2 objets est inférieur à une rayon donné 
        distance= ((self.position[0]-objectPosition[0])**2+(self.position[1]-objectPosition[1])**2)**0.5#pygame.sprit.collide_cercle
        if distance==0.0:
            return False
        if distance<=rayon:
            return True
        return False

    def manger(self,proie):#tout les être vivants mangent
        pass
    

class beef(Objet):
    def __init__(self,energie,vie,sexe,rayonVision,rayonContact,position=[100,100]):
        Objet.__init__(self,energie,vie,sexe)
        self.vitesse=0 #vitesse en fonction de l'énergie
        self.name = "plante"
        self.position=position
        self.attaque = self.energie
    
    #sprite du bled
    def draw(self, position, i):
        if i == 0:
            image = pygame.image.load("./sprite/pug/frame-1.gif")
            screen.blit(image, position)
        if i == 1:
            image = pygame.image.load("./sprite/pug/frame-2.gif")
            screen.blit(image, position)
        if i == 2:
            image = pygame.image.load("./sprite/pug/frame-3.gif")
            screen.blit(image, position)
        if i == 3:
            image = pygame.image.load("./sprite/pug/frame-4.gif")
            screen.blit(image, position)


class caca(Objet):
    def __init__(self,energie,vie,sexe,rayonVision,rayonContact,position=[100,100]):
        Objet.__init__(self,energie,vie,sexe)
        self.vitesse=0 #vitesse en fonction de l'énergie
        self.name = "plante"
        self.position=position
        self.attaque = self.energie
    
    #sprite du bled
    def draw(self, position, i):
        if i == 0:
            image = pygame.image.load("./sprite/pug/frame-1.gif")
            screen.blit(image, position)
        if i == 1:
            image = pygame.image.load("./sprite/pug/frame-2.gif")
            screen.blit(image, position)
        if i == 2:
            image = pygame.image.load("./sprite/pug/frame-3.gif")
            screen.blit(image, position)
        if i == 3:
            image = pygame.image.load("./sprite/pug/frame-4.gif")
            screen.blit(image, position)
p=0
while p < 1:
    enfant=beef(100,100,random.choice(['male',"femelle"]),750,100,position=[random.randrange(0,400),random.randrange(0,300)])#self.__class__ permet de récupérer la classe de 'self'
    listeDesViandes.append(enfant)
    p+=1 

