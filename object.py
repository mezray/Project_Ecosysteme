from UI import *
listeDesViandes=[]
listeDesDechets=[]

class Object:
    def __init__(self,energy, position):
        self.energy = energy
        self.position = position
        self.attack = 0
