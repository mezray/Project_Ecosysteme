from objet import *
from vivant import *
import random


class Plante(Vivant):
    def __init__(self,rayonRacine,rayonSemis):
        self.rayonSemis=rayonSemis# une plante quoi
        self.rayonRacine=rayonRacine
        
    
    def manger(self,dechet): 
        if self.energie > 0 and dechet.energie > 0:
            self.energie += dechet.energie
            dechet.energie = 0
            return
       
                
    def reproduire(self,x,y):
        enfant=self.__class__(300,300,100,100,position=[x,y])
        listeDesPlantes.append(enfant)

    def inZoneRacine(self,elem):#il faut apeller cette méthode mais sais pas quand ah x)
        if self.inZone(self.rayonRacine,elem.position)==True:
            if type(elem).__name__=='Dechet':
                return self.manger(elem)
    
    def inZoneSemis(self):
        # a completer possiblement supprimer et fusionner avec celui de dessus ==> ! main prblm
        x=self.position[0]+random.randrange(-self.rayonSemis,self.rayonSemis)
        y=self.position[1]+random.randrange(-self.rayonSemis,self.rayonSemis)
        if x<0 or x>800 or y<0 or y>600 :
            return self.inZoneSemis()
        else:
            return self.reproduire(x,y)
        
