from vivant import *
from objet import *
import random
directions = [(-1,0),(0,1),(1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]


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
        if len(listeDesCarnivores)<50:
            enfant=self.__class__(300,300,random.choice(['male',"femelle"]),750,100,position=[random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)])#self.__class__ permet de récupérer la classe de 'self'
            listeDesBebeCarnivores.append(enfant)


    def inRayonContact(self,cible):#si une cible est dans le rayon de contact
        if len(listeDesCarnivores) < 7500:
            #oui = random.randrange(0,2)
            oui = 1
        else:
            oui = 0
        if cible.name==self.name and oui == 1:#s'ils sont de même espèce animal mais de sexe différent, ils vont reproduire
            if self.sexe != cible.sexe:
                return self.reproduire()
        #print(cible.__class__.__bases__[0])
        if str(cible.__class__.__bases__[0])=="<class 'carnivore.Carniveore'>" and oui == 0:#si un carnivore croise un carnivore, carnivore sera manger
            return self.manger(cible)
        if str(cible.__class__.__bases__[0])=="<class 'herbivore.Herbivore'>" and oui == 0:#si un carnivore croise un herbivore, herbivore sera manger
            return self.manger(cible) 
        if str(cible.__class__.__bases__[0])=="<class 'objet.Objet'>" and oui == 0: #si un carnivore croise un objet viande, viande sera manger
            return self.manger(cible)
    
    def inRayonVision(self,cible):
        distance= (self.position[0]-cible.position[0])**2+(self.position[1]-cible.position[1])**2
        direct=directions[0]
        for direction in directions:
            newX=self.position[0]+direction[0]*self.vitesse
            newY=self.position[1]+direction[1]*self.vitesse
            if (10<newX<(SCREENWIDTH-50)) and (10<newY<(SCREENHEIGHT-50)):
                proche=(newX-cible.position[0])**2+(newY-cible.position[1])**2 
                if self.attaque >=cible.attaque and proche <= distance:
                    direct=direction
                    distance=proche
                if self.attaque <=cible.attaque and proche >= distance:
                    direct=direction
                    distance=proche
        self.position[0]+=direct[0]*self.vitesse
        self.position[1]+=direct[1]*self.vitesse
        return (self.position[0],self.position[1])

        
    def deplacer(self,directionNumber):#fonction permet de se déplacer suivant une direction: ("S","SW","W","NW","N","NE","E","SE")
        newX=self.position[0]+directions[directionNumber][0]*self.vitesse
        newY=self.position[1]+directions[directionNumber][1]*self.vitesse
        if newX<10 or newX>(SCREENWIDTH-50) or newY<10 or newY>(SCREENHEIGHT-50) :
            return self.deplacer(random.randrange(0,8))
        else:
            self.position[0]=newX
            self.position[1]=newY

        liste=listeDesHerbivores+listeDesViandes+listeDesCarnivores
        random.shuffle(liste)
        i=0
        while i<len(liste):
            if self.inZone(self.rayonContact,liste[i].position)==True:#regarde s'il y a qqch dans le rayon de contact
                self.inRayonContact(liste[i])
            if self.inZone(self.rayonVision,liste[i].position)==True:#regarde s'il y a qqch dans le rayon de vision
                return self.inRayonVision(liste[i])
            i+=1
        
        return self.position
    
    
