from Inerte.waste import waste
from UI import *
import random
from object import *

listeDesCarnivores = []
listeDesHerbivores=[]
listeDesPlantes = []

listeDesBebeCarnivores = []
listeDesBebeHerbivores = []
listeDesGraines = []

listeDesObjets=listeDesDechets+listeDesViandes
listeDesAnimaux=listeDesCarnivores+listeDesHerbivores

class Living:
    def __init__(self,energy,health,sex):
        self.energy=energy
        self.health=health
        self.sex=sex

    def reproduce(self):
        pass

    def inZone(self,radius,objectPosition):
        distance= ((self.position[0]-objectPosition[0])**2+(self.position[1]-objectPosition[1])**2)**0.5
        if distance == 0.0:
            return False
        if distance<=radius:
            return True
        return False

    def eat(self,prey):
        pass

    def energyUpdate(self,index):
        if self.energy >= 1:
            self.energy-=1
        else:
            if self.health >= 20:
                self.energy+=20
                self.health-=20
            else:
                self.health = 0
    
    def childBirth(self,addListe,bebeListe,animal,energy,health,radiusView,radiusContact):
        if animal.pregnant == 0:
            try:
                position=[0,0]
                position[0] = animal.position[0]
                position[1] = animal.position[1]
                addListe.append(animal.__class__(energy,health,random.choice(['male',"female"]),radiusView,radiusContact,position))
                bebeListe.remove(animal)
            except:
                bebeListe.remove(animal)
        else:
            animal.pregnant-=1

    def digest(self):
        if self.digestion == 0:
            position = [0,0]
            position[0] = self.position[0]
            position[1] = self.position[1]
            excrement = waste(300,position)
            listeDesDechets.append(excrement)
            listeDesObjets.append(excrement)
            self.digestion = 50
        else:
            self.digestion-=1


