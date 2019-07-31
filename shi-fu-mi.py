from tkinter import*
from random import*

class Root (Tk):
	def __init__(self) :
		super().__init__() 
		self.boutonquitter = Button(self,text ='Quitter', command = self.quit)
		self.boutonquitter.pack()
		self.messageD=Label(self, text = "Shi-fu-mi : 1 ou 2 joueurs ?")
		self.messageD.pack()
		self.bouton1j = Button(self, text = '1 joueur', command = self.interface1j)
		self.bouton1j.pack()
		self.bouton2j = Button(self, text = '2 joueurs')
		self.bouton2j.pack()
		self.bouton3 = Button(self, text ='')
		self.bouton3.pack()

		
	def interface1j(self):
		self.bouton1j.destroy()
		self.bouton2j.destroy()
		self.bouton3.destroy()
		self.messageD.destroy()
		self.message1j = Label(self, text = '1 joueur')
		self.message1j.pack()
		self.boutonP= Button(self, text = 'Pierre', command = self.pierre)
		self.boutonP.pack()
		self.boutonF = Button(self, text = 'Feuille', command = self.feuille)
		self.boutonF.pack()
		self.boutonC = Button(self, text = 'Ciseaux', command =self.ciseaux)
		self.boutonC.pack()
		
	def pierre(self):
		choix_joueur = 1
		
	def feuille(self):
		choix_joueur = 2
		
	def ciseaux(self):
		choix_joueur = 3
		
		
	

fenetre = Root()
fenetre.mainloop()