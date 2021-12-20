import pygame, sys,random
from pygame.locals import *
from UI import *

from vivant import *
from Entite.animauxC import *
from Entite.animauxH import *
from Entite.animauxP import *

from objet import *
from Inerte.viande import *
from Inerte.dechet import *


listeDesObjets=listeDesDechets+listeDesViandes
listeDesAnimaux=listeDesCarnivores+listeDesHerbivores

pygame.init()

#vitesse du jeu en fps
FPS = 50

#Frame Gif
frames=0

#Initialisation
while 1:
    for event in pygame.event.get():
        if event.type== QUIT: #if pressing the X, quit the program
            pygame.quit() #stop pygame
            sys.exit() #stop the program
    screen.fill((0,0,0)) #clear the screen;
    
    
    
    """Je verrais pour les sprites cb d'images seront nécessaires"""
    frames+=1
    if frames>6:
        frames=0
        
    # 1er = plantes
    toKill = []
    toAdd = []
    plante=0
    while plante<len(listeDesPlantes):
        listeDesPlantes[plante].draw(listeDesPlantes[plante].position, frames)
        """ CHANGEMENT VALEUR A LA FIN DU PROJET"""
        if listeDesPlantes[plante].energie>=1:
            listeDesPlantes[plante].energie -=1
        else:
            if listeDesPlantes[plante].vie>=20:
                listeDesPlantes[plante].energie+=20
                listeDesPlantes[plante].vie-=20
            else:
                listeDesPlantes[plante].vie=0
            
        if listeDesPlantes[plante].vie<=0:
            toKill.append(plante)
            toAdd.append([plante, listeDesPlantes[plante].position])
        plante+=1

    for dead in reversed(toKill):
        listeDesPlantes.remove(listeDesPlantes[dead])
        
    for i, position in toAdd:
        listeDesDechets.append(caca(100, position))
        listeDesObjets+=listeDesDechets

      
    #2eme animaux
    toKill = []
    toAdd = []
    i=0
    while i<len(listeDesAnimaux): #update all animals
        #print(listeDesAnimaux[i])
        newPosition=listeDesAnimaux[i].deplacer(random.randrange(0,8))
        listeDesAnimaux[i].draw(newPosition, frames)
        
        if listeDesAnimaux[i].energie>=1:
            listeDesAnimaux[i].energie -=1

        else:
            """Pourra être changer en fonction de points de vies des différents animaux"""
            if listeDesAnimaux[i].vie>=20:
                listeDesAnimaux[i].energie+=20
                listeDesAnimaux[i].vie-=20
            else:
                listeDesAnimaux[i].vie=0

                
        if listeDesAnimaux[i].vie <=0:
            toKill.append(i)
            toAdd.append([i, listeDesAnimaux[i].position])

        i+=1

    for dead in reversed(toKill):
        try:
            listeDesCarnivores.remove(listeDesAnimaux[dead])
        except:
            listeDesHerbivores.remove(listeDesAnimaux[dead])
        listeDesAnimaux.remove(listeDesAnimaux[dead])

    for i, position in toAdd:
        listeDesViandes.append(beef(100, position))
        listeDesObjets+=listeDesViandes

    
    #3eme objets
    toKill = []
    toAdd = []
    objet = 0
    while objet<len(listeDesObjets): #update all objects
        listeDesObjets[objet].draw(listeDesObjets[objet].position, frames)
        #print(listeDesObjets[i])
        if listeDesObjets[objet].vie>=1:
            listeDesObjets[objet].vie -=1  
            #print(listeDesObjets[objet].vie)
            
        if listeDesObjets[objet].vie <=0:
            toKill.append(objet)
            if (isinstance(listeDesObjets[objet], caca)) == False:
                toAdd.append([objet, listeDesObjets[objet].position])
        objet+=1
        
    for dead in reversed(toKill):
        try:
            listeDesViandes.remove(listeDesObjets[dead])
        except:
            listeDesDechets.remove(listeDesObjets[dead])
        #**



    for i, position in toAdd:
        listeDesDechets.append(caca(1000, position))
        listeDesObjets+=listeDesDechets
    #**  
    listeDesObjets = []
    listeDesObjets=listeDesViandes+listeDesDechets
    pygame.display.update() #update display
    pygame.time.Clock().tick(FPS) #limit FPS



