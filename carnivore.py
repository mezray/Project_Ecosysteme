from vivant import *
import random
directions = [(-1,0),(0,1),(1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
listeDesCarnivores=[]

class Carnivore(Vivant):
    def __init__(self,rayonVision,rayonContact):
        self.rayonVision=rayonVision
        self.rayonContact=rayonContact

    def manger(self,proie):#le prédateur récupère tout l'énergie de la proie, la proie perd sa vie et il est retirer de la listeDesCarnivores
        if self.energie > 0:
            if self.attaque >= proie.energie and proie.energie > 0: #Si attaque >> energie de la proie ET energie de la proie > 0
                self.energie += proie.energie
                proie.energie = 0 #on retire les dégats à l'energie de la cible --> a revoir pour cas attaque fait que pt energie << 0
                #print("statu attaquant",self.name, self.energie, "et proie", proie.name, proie.energie)
                return
            if self.attaque < proie.energie:
                proie.energie -= self.attaque
                self.energie += self.attaque
                return
                
    def reproduire(self):#créer un enfant à partir de la classe de ses parents et ajouter à la listeDesCarnivores
        enfant=self.__class__(300,300,random.choice(['male',"femelle"]),750,100,position=[random.randrange(0,800),random.randrange(0,600)])#self.__class__ permet de récupérer la classe de 'self'
        listeDesCarnivores.append(enfant)

    def inRayonContact(self,cible):#si une cible est dans le rayon de contact
        if len(listeDesCarnivores) < 7500:
            oui = random.randrange(0,2)
        else:
            oui = 0
        #print(cible.__class__.__bases__[0])
        if cible.name==self.name and oui == 3:#s'ils sont de même espèce animal mais de sexe différent, ils vont reproduire
            if self.sexe != cible.sexe:
                return self.reproduire()
        if str(cible.__class__.__bases__[0])=="<class 'carnivore.Carnivore'>" and oui == 0:#si un carnivore croise un herbivore, herbivore sera manger
            return self.manger(cible)
        if str(cible.__class__.__bases__[0])=="<class 'herbivore.Herbivore'>" and oui == 0:#si un carnivore croise un herbivore, herbivore sera manger
            return self.manger(cible)
        if str(cible.__class__.__bases__[0])=="<class 'objet.viande'>" and oui == 0:
            return self.manger(cible)
    
    def inRayonVision(self,cible):
        distance= (self.position[0]-cible.position[0])**2+(self.position[1]-cible.position[1])**2
        direct=directions[0]
        for direction in directions:
            proche=(self.position[0]+direction[0]-cible.position[0])**2+(self.position[1]+direction[1]-cible.position[1])**2 
            if self.attaque >cible.attaque and proche <= distance:
                direct=direction
                distance=proche
            if self.attaque <cible.attaque and proche >= distance:
                direct=direction
                distance=proche
        self.position[0]+=direct[0]*self.vitesse
        self.position[1]+=direct[1]*self.vitesse
        return (self.position[0],self.position[1])

        
    def deplacer(self,directionNumber):#fonction permet de se déplacer suivant une direction: ("S","SW","W","NW","N","NE","E","SE")
        newX=self.position[0]+directions[directionNumber][0]*self.vitesse
        newY=self.position[1]+directions[directionNumber][1]*self.vitesse
        """if newX and newY == listeDesVivants.position 
            redo"""
        """a changer car ils peuvent sortir de la map"""
        if newX<0 or newX>800 or newY<0 or newY>600 :
            return self.deplacer(random.randrange(0,8))
        else:
            self.position[0]=newX
            self.position[1]=newY
        i=0
        while i<len(listeDesCarnivores):
            if self.inZone(self.rayonContact,listeDesCarnivores[i].position)==True:#regarde s'il y a qqch dans le rayon de contact
                self.inRayonContact(listeDesCarnivores[i])
            if self.inZone(self.rayonVision,listeDesCarnivores[i].position)==True:#regarde s'il y a qqch dans le rayon de vision
                return self.inRayonVision(listeDesCarnivores[i])
            i+=1
        
        return self.position
    
    
