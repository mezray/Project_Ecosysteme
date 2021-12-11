from objet import *
import random
directions = [(-1,0),(0,1),(1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]


class Viande(Objet):
    def __init__(self,rayonVision,rayonContact):
        self.rayonVision=rayonVision
        self.rayonContact=rayonContact
        

    
    def manger(self,proie):#le prédateur récupère tout l'énergie de la proie, la proie perd sa vie et il est retirer de la listeDesCarnivores
        return
                
    def reproduire(self):#créer un enfant à partir de la classe de ses parents et ajouter à la listeDesCarnivores
        return

    def inRayonContact(self,cible):#si une cible est dans le rayon de contact
        return
    def inRayonVision(self,cible):
        return

        
    def deplacer(self,directionNumber):#fonction permet de se déplacer suivant une direction: ("S","SW","W","NW","N","NE","E","SE")
        newX=self.position[0]+directions[directionNumber][0]*self.vitesse
        newY=self.position[1]+directions[directionNumber][1]*self.vitesse
        if newX<0 or newX>800 or newY<0 or newY>600 :
            return self.deplacer(random.randrange(0,8))
        else:
            self.position[0]=newX
            self.position[1]=newY
        i=0
        while i<len(listeDesViandes):
            if self.inZone(self.rayonContact,listeDesViandes[i].position)==True:#regarde s'il y a qqch dans le rayon de contact
                self.inRayonContact(listeDesViandes[i])
            if self.inZone(self.rayonVision,listeDesViandes[i].position)==True:#regarde s'il y a qqch dans le rayon de vision
                return self.inRayonVision(listeDesViandes[i])
            i+=1
        
        return self.position
    
    
