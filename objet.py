from UI import *
listeDesViandes=[]
listeDesDechets=[]

class Objet:
    def __init__(self,energie, position):
        self.energie = energie
        self.position = position
        self.attaque=0
