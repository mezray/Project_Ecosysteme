from living import *
import random
directions = [(-1,0),(0,1),(1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]

class Herbivorous(Living):
    def __init__(self,radiusView,radiusContact):
        self.radiusView=radiusView
        self.radiusContact=radiusContact
        
    def eat(self,grass):
        if self.energy > 0 and grass.energy > 0 and self.energy <= 50:
            self.energy+=grass.energy
            grass.energy = 0
            return
                
    def reproduce(self):
        if len(listeDesHerbivores) < 50 and len(listeDesBebeHerbivores) < 10 and self.strength >= 1 and self.sex == "female":
            listeDesBebeHerbivores.append(self)
            self.strength-=1

    def inRadiusContact(self,target):
        if target.name == self.name :
            if self.sex != target.sex:
                return self.reproduce()
        if str(target.__class__.__bases__[0]) == "<class 'plant.Plant'>" :
            return self.eat(target)
    
    def inRadiusVision(self,target):
        distance = (self.position[0]-target.position[0])**2+(self.position[1]-target.position[1])**2
        direct = (0,0)
        for direction in directions:
            newX = self.position[0]+direction[0]*self.speed
            newY = self.position[1]+direction[1]*self.speed
            if (10<newX<(SCREENWIDTH-50)) and (10<newY<(SCREENHEIGHT-50)):
                near = (newX-target.position[0])**2 + (newY-target.position[1])**2 
                if str(target.__class__.__bases__[0]) == "<class 'plant.Plant'>" and near <= distance:
                    direct = direction
                    distance = near
                if str(target.__class__.__bases__[0]) == "<class 'carnivorous.Carnivorous'>" and near >= distance:
                    direct = direction
                    distance = near
        self.position[0]+=direct[0]*self.speed

        self.position[1]+=direct[1]*self.speed

        return (self.position[0],self.position[1])

        
    def move(self,directionNumber):
        newX = self.position[0] + directions[directionNumber][0]*self.speed
        newY = self.position[1] + directions[directionNumber][1]*self.speed
        if newX < 10 or newX > (SCREENWIDTH-50) or newY < 10 or newY > (SCREENHEIGHT-50) :
            return self.move(random.randrange(0,8))
        else:
            self.position[0] = newX 
            self.position[1] = newY 
            
        self.digest()
        liste = listeDesPlantes + listeDesCarnivores + listeDesHerbivores
        random.shuffle(liste)
        
        i=0
        while i<len(liste):
            if self.inZone(self.radiusContact,liste[i].position) == True:
                self.inRadiusContact(liste[i])
            if self.inZone(self.radiusView,liste[i].position) == True:
                return self.inRadiusVision(liste[i])
            i+=1
        return self.position
    
