from vivant import *
from objet import *
import random
directions = [(-1,0),(0,1),(1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]


class Carnivore(Vivant):
    def __init__(self,rayonVision,rayonContact):
        self.rayonVision=rayonVision
        self.rayonContact=rayonContact

    def manger(self,proie):#le prédateur récupère tout l'énergie de la proie, la proie perd sa vie et il est retirer de la listeDesCarnivores
        if self.energie > 0 and self.energie <=100:
            if self.attaque >= proie.energie and proie.energie > 0: #Si attaque >> energie de la proie ET energie de la proie > 0
                self.energie += proie.energie
                proie.energie = 0 #on retire les dégats à l'energie de la cible --> a revoir pour cas attaque fait que pt energie << 0
                #print("statu attaquant",self.name, self.energie, "et proie", proie.name, proie.energie)
                self.caca +=1
                return
            if self.attaque < proie.energie:
                proie.energie -= self.attaque
                self.energie += self.attaque
                self.caca +=1
                return
                
    def reproduire(self):#créer un enfant à partir de la classe de ses parents et ajouter à la listeDesCarnivores
        if len(listeDesCarnivores)<200 and len(listeDesBebeCarnivores)<75 and self.force >= 1 and self.sexe == "femelle":
            listeDesBebeCarnivores.append(self)
            self.force -= 1


    def inRayonContact(self,cible):#si une cible est dans le rayon de contact
        if cible.name==self.name:#s'ils sont de même espèce animal mais de sexe différent, ils vont reproduire
            if self.sexe != cible.sexe:
                return self.reproduire()
        return self.manger(cible)
    
    def inRayonVision(self,cible):
        distance= (self.position[0]-cible.position[0])**2+(self.position[1]-cible.position[1])**2
        direct=(0,0)
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
        #random.shuffle(liste)
        i=0
        if self.caca >=20:
            return 
        while i<len(liste):
            if self.inZone(self.rayonContact,liste[i].position)==True:#regarde s'il y a qqch dans le rayon de contact
                self.inRayonContact(liste[i])
            if self.inZone(self.rayonVision,liste[i].position)==True:#regarde s'il y a qqch dans le rayon de vision
                return self.inRayonVision(liste[i])
            i+=1
        
        return self.position
    
    
