import pygame, sys,random
from pygame.locals import *

from vivant import *
from Entite.animauxC import *
from Entite.animauxH import *
from Entite.animauxP import *

from objet import *
listeDesVivants= listeDesHerbivores + listeDesCarnivores + listeDesPlantes
listeDesObjets=listeDesDechets+listeDesViandes

pygame.init()

#définir taille écran:
SCREENWIDTH=800
SCREENHEIGHT=600
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Environnement")

#vitesse du jeu en fps
FPS = 2


frames=0
while 1:
    for event in pygame.event.get():
        if event.type== QUIT: #if pressing the X, quit the progra
            pygame.quit() #stop pygame
            sys.exit() #stop the program
    screen.fill((0,0,0)) #clear the screen;
    
    i=0
    toKill = []
    
    """Je verrais pour les sprites cb d'images seront nécessaires"""
    frames+=1
    if frames>7:
        frames=0
    while i<len(listeDesVivants): #update all animals
        newPosition=listeDesVivants[i].deplacer(random.randrange(0,8))
        listeDesVivants[i].draw(newPosition, frames)
        
        if listeDesVivants[i].energie>=1:
            listeDesVivants[i].energie -=1
            print(listeDesVivants[i].energie)
        else:
            """Pourra être changer en fonction de points de vies des différents animaux"""
            if listeDesVivants[i].vie>=20:
                listeDesVivants[i].energie+=20
                listeDesVivants[i].vie-=20
            else:
                listeDesVivants[i].vie=0

                
        if listeDesVivants[i].vie <=0 and listeDesVivants[i].energie<=0:
            toKill.append(i)
        i+=1

    for dead in reversed(toKill):
        """Ajouter ici un moyen d'ajouter un objet viande à la position du mort"""
        #listeDesVivants.append()
        listeDesVivants.remove(listeDesVivants[dead])
 
        
        
    pygame.display.update() #update display
    pygame.time.Clock().tick(FPS) #limit FPS



