#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter
import math
from commbot import Commande
from time import sleep

"""
	Initialisation de l'interface graphique
"""
def InitGui():
	global gui # La fenêtre de l'interface
	gui = Tkinter.Tk()

	DessineGui() # Dessin de l'interface graphique

	global listMvt	# Tableau d'entiers des saisies de mouvements par l'utilisateur
	listMvt = []	# 0 : haute, 1 : droite, 2 : bas, 3 gauche

	global nombre	# Compteur pour l'affichage des choix de mouvement
	nombre = 0		# permet de changer de ligne tous les 10 mvts

	global listImg 		# Liste des images réduite
	listImg = []		#
	global listLabel	# Liste des "labels" placé dans "cadre" contenant chacun une image
	listLabel = []		#

	
	global nbParLig # Nombre d'image par ligne dansns l'affichage des images
	nbParLig = 6	#
	global nbMaxLig # Nombre maximum de lignes de mouvements
	nbMaxLig = 9	# 6*9=54 mvts max


	# Boucle d'attente des évènements : clic de bouton
	gui.mainloop()

"""
	Dessin de l'interface : boutons, panel, ...
"""
def DessineGui():
	gui.title('BabyBot')

	global boutons 	# Tableau des 4 boutons de direction
					# 0,1,2,3 dans le sens des aiguilles d'une montre en partant de midi
					# [0] : image grand format
					# [1] : numéro de colonne sur la grille
					# [2] : numéro de ligne sur la grille
					# [3] : image petit format
	boutons = [["images/fhaute.gif",1,0,"images/fhautep.gif"],["images/fdroite.gif",0,1,"images/fdroitep.gif"],["images/fbasse.gif",1,2,"images/fbassep.gif"],["images/fgauche.gif",2,1,"images/fgauchep.gif"]]
	gui.grid() # On utilise le mode grille de Tkinter

	bouton = []		# Les quatres boutons de direction
	global image 	# Permet d'éviter la destruction de la variable
	image = []		# et donc de l'image à la fin de la procédure
	# Dessin des boutons et association de la fonction OnButtonClick
	# 
	for i in range(4):
		image.append(Tkinter.PhotoImage(file=boutons[i][0]))
		bouton.append(Tkinter.Button(gui,image=image[i],bd=0,command=lambda i=i: OnButtonClick(i)))
		bouton[i].grid(column=boutons[i][1],row=boutons[i][2])

	global pad 		# marge de 30px entre les boutons et le parcours
	global cadre  	# cadre pour l'affichage du parcours
	# Dessin du cadre
	pad = Tkinter.Frame(gui,height=450,width=30)
	pad.grid(column=3,row=0,rowspan=3)
	cadre = Tkinter.Frame(gui,height=450,width=350)
	cadre.grid_propagate(False)
	cadre.grid(column=4,row=0,rowspan=3)
	
	# bouton d'exécution du parcours par le robot
	boutonOk = Tkinter.Button(gui,text="OK",bd=0,command=OnButtonOkClick,height=1,width=35)
	boutonOk.grid(column=4,row=3)

	# bouton de correction des mouvements
	boutonOk = Tkinter.Button(gui,text="Effacer dernier mouvement",bd=0,command=OnButtonCorClick,height=1,width=35)
	boutonOk.grid(column=4,row=4)

	# bouton de remise à zéro de la liste des mouvements
	boutonOk = Tkinter.Button(gui,text="Tout Effacer",bd=0,command=OnButtonEffClick,height=1,width=35)
	boutonOk.grid(column=4,row=5)

"""
	Suppresion du dernier mouvement
"""
def OnButtonCorClick():
	if nombre != 0:
		global listMvt
		listMvt.pop
		DelMvt()

"""
	Effacement des mouvements
"""
def OnButtonEffClick():
	if nombre != 0:
		global listMvt
		listMvt[:] = []
		DelAllMvt()

"""
	Procédure d'appel du module de commande du robot
"""
def OnButtonOkClick():
	for mvt in listMvt:
		Commande(mvt)
		sleep(0.1)

"""
	Ajout d'un entier [0..3] à listMvt lors du clic d'un bouton de direction
"""
def OnButtonClick(nb):
	if nombre <= nbMaxLig * nbParLig:
		global listMvt
		listMvt.append(nb) 
		PrintMvt(nb)
	else:
		print "Maximum de mouvement atteint"

"""
	Affichage de l'image réduite du bouton cliqué dans le cadre de droite
"""	
def PrintMvt(nb):
	global nombre
	global listImg
	global listLabel

	# Ajout de la nouvelle image de mouvement
	listImg.append(Tkinter.PhotoImage(file=boutons[nb][3]))
	listLabel.append(Tkinter.Label(cadre,image=listImg[nombre]))
	# Calcul de la postion de la nouvelle image, à droite de la précédente
	# dans la limite de nbParLig par ligne
	ligne = math.ceil((nombre + 1) / float(nbParLig)) - 1
	col = nombre - int(ligne) * nbParLig

	# Positionnent du label et donc de l'image sur la grille
	listLabel[nombre].grid(column=col,row=int(ligne))

	nombre += 1

"""
	Suppression du dernier label et de son image
"""	
def DelMvt():
	global nombre
	global listImg
	global listLabel
	nombre -= 1
	listImg.pop
	listLabel[nombre].grid_forget()
	listLabel.pop

"""
	Suppression de tous les labels et images
"""	
def DelAllMvt():
	global listImg
	global listLabel
	listImg[:] = []
	listLabel[:] = []
	global nombre
	nombre = 0
