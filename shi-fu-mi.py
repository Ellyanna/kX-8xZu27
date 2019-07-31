from tkinter import*
from random import*

class Root (Tk):
	def __init__(self) :
		super().__init__() 
		self.points = 0
		self.points2j = 0
		self.boutonquitter = Button(self,text ='Quitter', command = self.quit)
		self.boutonquitter.pack()
		self.messageD=Label(self, text = "Shi-fu-mi : 1 ou 2 joueurs ?")
		self.messageD.pack()
		self.bouton1j = Button(self, text = '1 joueur', command = self.interface1j)
		self.bouton1j.pack()
		self.bouton2j = Button(self, text = '2 joueurs', command = self.interface2j)
		self.bouton2j.pack()
		
	def interface1j(self):
		self.bouton1j.destroy()
		self.bouton2j.destroy()
		self.messageD.destroy()
		self.message1j = Label(self, text = '1 joueur')
		self.message1j.pack()
		self.message_point = Label(self, text = 'Nombre de points = ')
		self.message_point.pack()
		self.message_point2 = Label(self, text = self.points)
		self.message_point2.pack()
		self.message_point3 = Label(self,text = 'points')
		self.message_point3.pack()
		self.boutonP= Button(self, text = 'Pierre', command = self.pierre)
		self.boutonP.pack()
		self.boutonF = Button(self, text = 'Feuille', command = self.feuille)
		self.boutonF.pack()
		self.boutonC = Button(self, text = 'Ciseaux', command =self.ciseaux)
		self.boutonC.pack()
		self.boutonswitch1 = Button(self, text = 'jouer à 2', command = self.interface2j)
		self.boutonswitch1.pack()
		
		
	def pierre(self):
		self.choix_joueur = 'pierre'
		self.choix()
		
	def feuille(self):
		self.choix_joueur = 'feuille'
		self.choix()
		
	def ciseaux(self):
		self.choix_joueur = 'ciseaux'
		self.choix()
		
	def choix(self):
		self.boutonP.destroy()
		self.boutonF.destroy()
		self.boutonC.destroy()
		self.boutonswitch1.destroy()
		self.ordi = randint(1, 3)
		if self.ordi == 1:
			self.ordi = 'pierre'
		elif self.ordi == 2:
			self.ordi = 'feuille'
		elif self.ordi == 3:
			self.ordi = 'ciseaux'
		self.manche()
	
	def manche (self):
		self.resultat=''
		if self.choix_joueur == self.ordi :
			self.resultat = 0
		elif self.choix_joueur == 'pierre':
			if self.ordi == 'feuille' :
				self.resultat = 1
			elif self.ordi == 'ciseaux':
				self.resultat = 2
		elif self.choix_joueur == 'feuille':
			if self.ordi == 'pierre':
				self.resultat = 2
			elif self.ordi == 'ciseaux':
				self.resultat = 1
		elif self.choix_joueur == 'ciseaux':
			if self.ordi == 'pierre':
				self.resultat = 1
			elif self.ordi == 'feuille':
				self.resultat = 2
		self.point()
		
	def point(self):
		if self.resultat == 2:
			self.points = self.points+ 1			
		elif self.resultat == 1:
			self.points = self.points - 1
		self.afficher()
		
	def afficher(self):
		self.message_joueur = Label(self, text = self.choix_joueur)
		self.message_joueur.pack()
		self.messagevs = Label(self, text = 'vs')
		self.messagevs.pack()
		self.message_ordi = Label(self, text = self.ordi)
		self.message_ordi.pack()
		self.message_fin = Label(self,text = '')
		if self.resultat ==0:
			self.message_fin = Label(self, text = 'Egalité')
			self.message_fin.pack()
		elif self.resultat ==2:
			self.message_fin= Label(self, text = 'Tu as gagné')
			self.message_fin.pack()
		elif self.resultat ==1:
			self.message_fin = Label(self, text = "l'ia a gagné")
			self.message_fin.pack()
		self.bouton_replay = Button(self, text = 'Continuer', command = self.destroy)
		self.bouton_replay.pack()
		
	def destroy(self):
		self.message_joueur.destroy()
		self.messagevs.destroy()
		self.message_ordi.destroy()
		self.bouton_replay.destroy()
		self.message_point.destroy()
		self.message_point2.destroy()
		self.message_point3.destroy()
		self.message_fin.destroy()
		self.message1j.destroy()
		self.interface1j()
		
		
		
		
		
	def interface1j(self):
		self.bouton1j.destroy()
		self.bouton2j.destroy()
		self.messageD.destroy()
		self.message2j = Label(self, text = '2 joueurs')
		self.message2j.pack()
		self.message_point = Label(self, text = 'Nombre de points = ')
		self.message_point.pack()
		self.message_point2 = Label(self, text = self.points2j)
		self.message_point2.pack()
		self.message_point3 = Label(self,text = 'points')
		self.message_point3.pack()
		self.message_joueur1 = Label(self, text = 'Joueur 1')
		self.message_joueur1.pack()
		self.boutonP= Button(self, text = 'Pierre', command = self.pierre1)
		self.boutonP.pack()
		self.boutonF = Button(self, text = 'Feuille', command = self.feuille1)
		self.boutonF.pack()
		self.boutonC = Button(self, text = 'Ciseaux', command =self.ciseaux1)
		self.boutonC.pack()
		self.boutonswitch2 = Button(self, text = 'jouer seul', command = self.interface1j)
		self.boutonswitch2.pack()
		
	def pierre1(self):
		self.choix_j1 = 'pierre'
		self.joueur2()
		
	def feuille1(self):
		self.choix_j1 = 'feuille'
		self.joueur2()
		
	def ciseaux1(self):
		self.choix_j1 = 'ciseaux'
		self.joueur2()
		
	def joueur2 (self):
		self.message_joueur1.destroy()
		self.boutonP.destroy()
		self.boutonF.destroy()
		self.boutonC.destroy()
		self.boutonswitch2.destroy()
		self.message_joueur2 = Label(self, text = 'Joueur 2')
		self.message_joueur2.pack()
		self.boutonP2= Button(self, text = 'Pierre', command = self.pierre2)
		self.boutonP2.pack()
		self.boutonF2 = Button(self, text = 'Feuille', command = self.feuille2)
		self.boutonF2.pack()
		self.boutonC2 = Button(self, text = 'Ciseaux', command =self.ciseaux2)
		self.boutonC2.pack()

		
		
		
fenetre = Root()
fenetre.mainloop()
