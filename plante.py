from objet import *
from vivant import *
import random




class Plante(Vivant):
    def __init__(self,rayonRacine,rayonSemis):
        self.rayonSemis=rayonSemis
        self.rayonRacine=rayonRacine
        
    
    def manger(self,dechet): 
        if self.energie > 0 and dechet.energie > 0:
            self.energie += 20
            dechet.energie -= 20
            return
       
                
    def reproduire(self,x,y):
        if len(listeDesPlantes)<50 and self.force >= 1 and self.energie <= 10:
            enfant=self.__class__(150,10,300,100,position=[x,y])
            listeDesGraines.append(enfant)
            self.force -= 1

    def inZoneRacine(self,elem):
        i=0
        while i<len(elem):
            element = elem[i]
            if self.inZone(self.rayonRacine,element.position)==True:
                if type(element).__name__=='dechet':
                    return self.manger(element)
            i+=1
    
    def inZoneSemis(self):
        x=self.position[0]+random.randrange(-self.rayonSemis,self.rayonSemis)
        y=self.position[1]+random.randrange(-self.rayonSemis,self.rayonSemis)
        if x<10 or x>(SCREENWIDTH-50) or y<10 or y>(SCREENHEIGHT-50) :
            return self.inZoneSemis()
        else:
            return self.reproduire(x,y)
        
