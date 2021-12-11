from vivant import *
import random
directions = [(-1,0),(0,1),(1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]


class Plante(Vivant):
    def __init__(self,rayonVision,rayonContact):
        self.rayonVision=0 # une plante quoi
        self.rayonContact=rayonContact
        
    
    def manger(self,proie):#le prédateur récupère tout l'énergie de la proie, la proie perd sa vie et il est retirer de la listeDesCarnivores
        # a completer
        return
                
    def reproduire(self):#créer un enfant à partir de la classe de ses parents et ajouter à la listeDesCarnivores
        enfant=self.__class__(300,300,random.choice(['male',"femelle"]),750,100,position=[random.randrange(0,800),random.randrange(0,600)])#self.__class__ permet de récupérer la classe de 'self'
        listeDesHerbivores.append(enfant)

    def inRayonContact(self,cible):#si une cible est dans le rayon de contact
        if len(listeDesPlantes) > 7500:
            oui = random.randrange(0,2)
        else:
            oui = 0
        print(cible.__class__.__bases__[0])
        if str(cible.__class__.__bases__[0])=="<class 'objet.dechet'>" and oui == 0:
            return self.manger(cible)
    
    def inRayonVision(self,cible):
        # a completer possiblement supprimer et fusionner avec celui de dessus ==> ! main prblm
        return

        
    def deplacer(self,directionNumber):#fonction permet de se déplacer suivant une direction: ("S","SW","W","NW","N","NE","E","SE")
        #plutot a supprimer ==> ! main problem
        newX=self.position[0]+directions[directionNumber][0]*self.vitesse
        newY=self.position[1]+directions[directionNumber][1]*self.vitesse
        if newX<0 or newX>800 or newY<0 or newY>600 :
            return self.deplacer(random.randrange(0,8))
        else:
            self.position[0]=newX
            self.position[1]=newY
        i=0
        while i<len(listeDesPlantes):
            if self.inZone(self.rayonContact,listeDesPlantes[i].position)==True:#regarde s'il y a qqch dans le rayon de contact
                self.inRayonContact(listeDesPlantes[i])
            if self.inZone(self.rayonVision,listeDesPlantes[i].position)==True:#regarde s'il y a qqch dans le rayon de vision
                return self.inRayonVision(listeDesPlantes[i])
            i+=1
        return self.position
    
    
