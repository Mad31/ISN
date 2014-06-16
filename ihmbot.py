#!/usr/bin/python

import Tkinter
import math
from commbot import Commande
from time import sleep

def InitGui():
	global gui
	gui = Tkinter.Tk()
	DessineGui()
	gui.title('BabyBot')
	gui.mainloop()

def DessineGui():
	global boutons
	boutons = [["images/fhaute.gif",1,0,"images/fhautep.gif"],["images/fdroite.gif",0,1,"images/fdroitep.gif"],["images/fbasse.gif",1,2,"images/fbassep.gif"],["images/fgauche.gif",2,1,"images/fgauchep.gif"]]
	gui.grid()

	"""global photoL
	photoL=Tkinter.PhotoImage(file="images/rect.gif")
	forme = Tkinter.Label(gui,bd=2,image=photoL,anchor="w",fg="blue",bg="white")
	forme.grid(column=0,row=1,sticky='NS')"""
	
	global pad
	global cadre
	pad = Tkinter.Frame(gui,height=450,width=30)
	pad.grid(column=3,row=0,rowspan=3,sticky='NS')
	cadre = Tkinter.Frame(gui,height=450,width=300)
	cadre.grid_propagate(False)
	cadre.grid(column=4,row=0,rowspan=3,sticky='NS')
	
	boutonOk = Tkinter.Button(gui,text="OK",bd=0,command=OnButtonOkClick,height=1,width=35)
	boutonOk.grid(column=3,row=2,sticky='NS')

	bouton = []
	global image
	image = []
	global nombre
	nombre = 0
	for i in range(4):
		image.append(Tkinter.PhotoImage(file=boutons[i][0]))
		bouton.append(Tkinter.Button(gui,image=image[i],bd=0,command=lambda i=i: OnButtonClick(i)))
		bouton[i].grid(column=boutons[i][1],row=boutons[i][2])

	global listMvt
	global listImg
	global listLabel
	listMvt = []
	listImg = []
	listLabel = []

def OnButtonOkClick():
	print "OK"
	for mvt in listMvt:
		Commande(mvt)
		sleep(0.1)


def OnButtonClick(nb):
	AddMvt(nb)
	PrintMvt(nb)
	
def AddMvt(nb):
	global listMvt
	listMvt.append(nb)
	
def PrintMvt(nb):
	global nombre
	global listImg
	global listLabel
	listImg.append(Tkinter.PhotoImage(file=boutons[nb][3]))
	listLabel.append(Tkinter.Label(cadre,image=listImg[nombre]))
	col = math.ceil((nombre + 1) / float(9)) - 1
	ligne = nombre - int(col)*9
	listLabel[nombre].grid(column=int(col),row=ligne)
	nombre += 1
