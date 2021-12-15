from vivant import *
import random
directions = [(-1,0),(0,1),(1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]

class Herbivore(Vivant):
    def __init__(self,rayonVision,rayonContact):
        self.rayonVision=rayonVision
        self.rayonContact=rayonContact
        
    
    def manger(self,herbe):
        if self.energie > 0 and herbe.energie > 0:
            self.energie += herbe.energie
            herbe.energie = 0
            return
                
    def reproduire(self):#créer un enfant à partir de la classe de ses parents et ajouter à la listeDesCarnivores
        enfant=self.__class__(300,300,random.choice(['male',"femelle"]),750,100,position=[random.randrange(0,800),random.randrange(0,600)])#self.__class__ permet de récupérer la classe de 'self'
        listeDesHerbivores.append(enfant)

    def inRayonContact(self,cible):#si une cible est dans le rayon de contact
        if cible.name==self.name :#s'ils sont de même espèce animal mais de sexe différent, ils vont reproduire
            if self.sexe != cible.sexe:
                return self.reproduire()
        if str(cible.__class__.__bases__[0])=="<class 'plante.Plante'>" :#si un carnivore croise un herbivore, herbivore sera manger
            return self.manger(cible)
    
    def inRayonVision(self,cible):
        distance= (self.position[0]-cible.position[0])**2+(self.position[1]-cible.position[1])**2
        direct=directions[0]
        for direction in directions:
            newX=self.position[0]+direction[0]*self.vitesse
            newY=self.position[1]+direction[1]*self.vitesse
            if 10<newX<750 and 10<newY<550:
                proche=(newX-cible.position[0])**2+(newY-cible.position[1])**2 
                if str(cible.__class__.__bases__[0])=="<class 'plante.Plante'>" and proche <= distance:
                    direct=direction
                    distance=proche
                if str(cible.__class__.__bases__[0])=="<class 'carnivore.Carnivore'>" and proche >= distance:
                    direct=direction
                    distance=proche
        self.position[0]+=direct[0]*self.vitesse
        self.position[1]+=direct[1]*self.vitesse
        return (self.position[0],self.position[1])

        
    def deplacer(self,directionNumber):#fonction permet de se déplacer suivant une direction: ("S","SW","W","NW","N","NE","E","SE")
        newX=self.position[0]+directions[directionNumber][0]*self.vitesse
        newY=self.position[1]+directions[directionNumber][1]*self.vitesse
        if newX<10 or newX>750 or newY<10 or newY>550 :
            return self.deplacer(random.randrange(0,8))
        else:
            self.position[0]=newX
            self.position[1]=newY
        
        liste=listeDesPlantes+listeDesCarnivores
        i=0
        while i<len(liste):
            if self.inZone(self.rayonContact,liste[i].position)==True:#regarde s'il y a qqch dans le rayon de contact
                self.inRayonContact(liste[i])
            if self.inZone(self.rayonVision,liste[i].position)==True:#regarde s'il y a qqch dans le rayon de vision
                return self.inRayonVision(liste[i])
            i+=1
        
        return self.position
    
    
