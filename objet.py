from UI import *
listeDesViandes=[]
listeDesDechets=[]
directions = [(-1,0),(0,1),(1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]

class Objet:
    def __init__(self,vie, position):
        self.vie = vie
        self.position = position