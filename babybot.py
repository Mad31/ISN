#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter
import math

class simpleapp_tk(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		
		self.boutons = [["images/fhaute.gif",2,0,"images/fhautep.gif"],["images/fdroite.gif",3,1,"images/fdroitep.gif"],["images/fbasse.gif",2,2,"images/fbassep.gif"],["images/fgauche.gif",1,1,"images/fgauchep.gif"]]
		self.grid()

		self.photoL=Tkinter.PhotoImage(file="images/rect.gif")
		self.forme = Tkinter.Label(self,bd=2,image=self.photoL,anchor="w",fg="blue",bg="white")
		self.forme.grid(column=0,row=1,sticky='NS')
		
		self.pad = Tkinter.Frame(self,height=450,width=30)
		self.pad.grid(column=4,row=0,rowspan=3,sticky='NS')
		self.cadre = Tkinter.Frame(self,height=450,width=300)
		self.cadre.grid_propagate(False)
		self.cadre.grid(column=5,row=0,rowspan=3,sticky='NS')
		
		boutonOk = Tkinter.Button(self,text="OK",bd=0,command=self.OnButtonOkClick,height=1,width=35)
		boutonOk.grid(column=5,row=4,sticky='NS')

		self.bouton = []
		self.image = []
		self.nombre = 0
		for i in range(4):
			self.image.append(Tkinter.PhotoImage(file=self.boutons[i][0]))
			self.bouton.append(Tkinter.Button(self,image=self.image[i],bd=0,command=lambda i=i: self.OnButtonClick(i)))
			self.bouton[i].grid(column=self.boutons[i][1],row=self.boutons[i][2])

		self.grid_columnconfigure(0,weight=1)
		self.resizable(True,False)
		self.update()
		self.geometry(self.geometry())
		
		self.listMvt = []
		self.listImg = []
		self.listLabel = []

	def OnButtonOkClick(self):
		print "OK"

	def OnButtonClick(self,nb):
		self.AddMvt(nb)
		
		self.PrintMvt(nb)
		
	def AddMvt(self,nb):
		self.listMvt.append(nb)
		

	def PrintMvt(self,nb):
		self.listImg.append(Tkinter.PhotoImage(file=self.boutons[nb][3]))
		self.listLabel.append(Tkinter.Label(self.cadre,image=self.listImg[self.nombre]))
		col = math.ceil((self.nombre + 1) / float(9)) - 1
		ligne = self.nombre - int(col)*9
		self.listLabel[self.nombre].grid(column=int(col),row=ligne)
		self.nombre += 1


if __name__ == "__main__":
	app = simpleapp_tk(None)
	app.title('BabyBot')
	app.mainloop()