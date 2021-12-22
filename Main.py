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

from plante import *

listeDesObjets=listeDesDechets+listeDesViandes
listeDesAnimaux=listeDesCarnivores+listeDesHerbivores



pygame.init()

#vitesse du jeu en fps
FPS = 200

#Frame Gif
frames=0

def energieUpdate(etreVivant,index):
    if etreVivant.energie>=1:
        etreVivant.energie -=1
    else:
        if etreVivant.vie>=20:
            etreVivant.energie+=20
            etreVivant.vie-=20
        else:
            etreVivant.vie=0
            
    if etreVivant.vie<=0:
        toKill.append(index)
        toAdd.append([index, etreVivant.position])

#Initialisation
while 1:
    for event in pygame.event.get():
        if event.type== QUIT: #if pressing the X, quit the program
            pygame.quit() #stop pygame
            sys.exit() #stop the program
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
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
        energieUpdate(listeDesPlantes[plante],plante)
        #listeDesPlantes[plante].inZoneRacine(listeDesDechets)
        listeDesPlantes[plante].inZoneSemis()
        

        plante+=1

    for dead in reversed(toKill):
        listeDesPlantes.remove(listeDesPlantes[dead])
        
    for i, position in toAdd:#sert à quoi 'i'?
        listeDesDechets.append(dechet(300, position))
        listeDesObjets=listeDesDechets+listeDesViandes

      
    #2eme animaux
    toKill = []
    toAdd = []
    i=0
    while i<len(listeDesAnimaux): #update all animals
        newPosition=listeDesAnimaux[i].deplacer(random.randrange(0,8))
        listeDesAnimaux[i].draw(newPosition, frames)
        energieUpdate(listeDesAnimaux[i],i)
        i+=1

    for dead in reversed(toKill):
        try:
            listeDesCarnivores.remove(listeDesAnimaux[dead])
        except:
            listeDesHerbivores.remove(listeDesAnimaux[dead])
        listeDesAnimaux.remove(listeDesAnimaux[dead])

    for i, position in toAdd:
        viande=beef(300, position)
        listeDesViandes.append(viande)
        listeDesObjets.append(viande)


    #3eme objets
    toKill = []
    toAdd = []
    objet = 0
    while objet<len(listeDesObjets): #update all objects
        listeDesObjets[objet].draw(listeDesObjets[objet].position, frames)
        if listeDesObjets[objet].energie>=1:
            listeDesObjets[objet].energie -=1  
            
        else:
            toKill.append(objet)
            if (isinstance(listeDesObjets[objet], dechet)) == False:
                toAdd.append([objet, listeDesObjets[objet].position])
        objet+=1
        
    for dead in reversed(toKill):
        try:
            listeDesViandes.remove(listeDesObjets[dead])
        except:
            listeDesDechets.remove(listeDesObjets[dead])
        listeDesObjets.remove(listeDesObjets[dead])
        

    for i, position in toAdd:
        listeDesDechets.append(dechet(300, position))
        listeDesObjets=listeDesDechets+listeDesViandes
        

    listeDesCarnivores += listeDesBebeCarnivores
    listeDesHerbivores += listeDesBebeHerbivores
    listeDesAnimaux=listeDesCarnivores+listeDesHerbivores
    listeDesPlantes += listeDesGraines
    
    listeDesGraines.clear()
    listeDesBebeCarnivores.clear()
    listeDesBebeHerbivores.clear()

       
    #print(listeDesGraines)
    pygame.display.update() #update display
    pygame.time.Clock().tick(FPS) #limit FPS