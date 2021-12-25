from object import *
from living import *
import random
class Plant(Living):
    def __init__(self,radiusRacine,radiusSemis):
        self.radiusSemis=radiusSemis
        self.radiusRacine=radiusRacine
    
    def eat(self,waste): 
        if self.energy > 0 and waste.energy > 0:
            self.energy += 20
            waste.energy -= 20
            return
       
                
    def reproduce(self,x,y):
        if len(listeDesPlantes)<50 and self.strength >= 1 and self.energy <= 10:
            enfant=self.__class__(150,10,300,100,position=[x,y])
            listeDesGraines.append(enfant)
            self.strength -= 1

    def inZoneRacine(self,elem):
        i=0
        while i<len(elem):
            element = elem[i]
            if self.inZone(self.radiusRacine,element.position)==True:
                if type(element).__name__ == 'Waste':
                    return self.eat(element)
            i+=1
    
    def inZoneSemis(self):
        x = self.position[0] + random.randrange(-self.radiusSemis,self.radiusSemis)
        y = self.position[1] + random.randrange(-self.radiusSemis,self.radiusSemis)
        if x < 10 or x > (SCREENWIDTH-50) or y < 10 or y > (SCREENHEIGHT-50) :
            return self.inZoneSemis()
        else:
            return self.reproduce(x,y)
        
