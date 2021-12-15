import pygame, sys,random
from pygame.locals import *

from vivant import *
from Entite.animauxC import *
from Entite.animauxH import *
from Entite.animauxP import *

from objet import *

#listeDesObjets=listeDesDechets+listeDesViandes
listeDesAnimaux=listeDesCarnivores+listeDesHerbivores

pygame.init()

#définir taille écran:
SCREENWIDTH=800
SCREENHEIGHT=600
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Environnement")

#vitesse du jeu en fps
FPS = 20

frames=0
while 1:
    for event in pygame.event.get():
        if event.type== QUIT: #if pressing the X, quit the progra
            pygame.quit() #stop pygame
            sys.exit() #stop the program
    screen.fill((0,0,0)) #clear the screen;
    
    i=0
    toKill = []
    toAdd = []
    
    """Je verrais pour les sprites cb d'images seront nécessaires"""
    frames+=1
    if frames>6:
        frames=0
    while i<len(listeDesAnimaux): #update all animals
        newPosition=listeDesAnimaux[i].deplacer(random.randrange(0,8))
        listeDesAnimaux[i].draw(newPosition, frames)
        
        if listeDesAnimaux[i].energie>=1:
            listeDesAnimaux[i].energie -=1
            #print(listeDesVivants[i].energie)
        else:
            """Pourra être changer en fonction de points de vies des différents animaux"""
            if listeDesAnimaux[i].vie>=20:
                listeDesAnimaux[i].energie+=20
                listeDesAnimaux[i].vie-=20
            else:
                listeDesAnimaux[i].vie=0

                
        if listeDesAnimaux[i].vie <=0 and listeDesAnimaux[i].energie<=0:
            toKill.append(i)
            """toAdd.append(i.position)"""
        i+=1

    for dead in reversed(toKill):
        try:
            listeDesCarnivores.remove(listeDesAnimaux[dead])
        except:
            listeDesHerbivores.remove(listeDesAnimaux[dead])
        listeDesAnimaux.remove(listeDesAnimaux[dead])
    
    toKill=[]
    plante=0
    while plante<len(listeDesPlantes):
        listeDesPlantes[plante].draw(listeDesPlantes[plante].position, frames)

        if listeDesPlantes[plante].energie<=0:
            toKill.append(plante)
        plante+=1

    for dead in reversed(toKill):
        """Ajouter ici un moyen d'ajouter un objet viande à la position du mort"""
        #listeDesVivants.append()
        listeDesPlantes.remove(listeDesPlantes[dead])
    #for i in toAdd:    
      #  listeDesObjets.append(i)
    
        
        
    pygame.display.update() #update display
    pygame.time.Clock().tick(FPS) #limit FPS



