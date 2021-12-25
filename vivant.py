from Inerte.dechet import dechet
from UI import *
import random
from objet import*

listeDesCarnivores = []
listeDesHerbivores=[]
listeDesPlantes = []

listeDesBebeCarnivores = []
listeDesBebeHerbivores = []
listeDesGraines = []

listeDesObjets=listeDesDechets+listeDesViandes
listeDesAnimaux=listeDesCarnivores+listeDesHerbivores

class Vivant:
    def __init__(self,energie,vie,sexe):
        self.energie=energie
        self.vie=vie
        self.sexe=sexe

    def reproduire(self):#tout les être vivants savent se reproduire
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

    def energieUpdate(self,index):
        if self.energie>=1:
            self.energie -=1
        else:
            if self.vie>=20:
                self.energie+=20
                self.vie-=20
            else:
                self.vie=0
    
    def accouchement(self,addListe,bebeListe,animal,energie,vie,rayonVision,rayonContact):
        if animal.enceinte == 0:
            try:
                position=[0,0]
                position[0] = animal.position[0]
                position[1] = animal.position[1]
                addListe.append(animal.__class__(energie,vie,random.choice(['male',"femelle"]),rayonVision,rayonContact,position))
                bebeListe.remove(animal)
            except:
                bebeListe.remove(animal)
        else:
            animal.enceinte -= 1

    def digerer(self):
        if self.digestion==0:
            position=[0,0]
            position[0] = self.position[0]
            position[1] = self.position[1]
            excrement=dechet(300,position)
            listeDesDechets.append(excrement)
            listeDesObjets.append(excrement)
            self.digestion=50
        else:
            self.digestion-=1


