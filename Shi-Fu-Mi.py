from tkinter import*
from random import*

class Root (Tk):
	def __init__(self) :
		super().__init__() 
		self.points = 0
		self.points2j1 = 0
		self.points2j2 = 0
		self.boutonquitter = Button(self,text ='Quitter', command = self.quit)
		self.boutonquitter.grid(row = 0, column = 1)
		self.messageD=Label(self, text = "Shi-fu-mi : 1 ou 2 joueurs ?")
		self.messageD.grid(row=1, columnspan=3)
		self.bouton1j = Button(self, text = '1 joueur', command = self.interface1j)
		self.bouton1j.grid(row= 2, column = 1)
		self.bouton2j = Button(self, text = '2 joueurs', command = self.interface2j)
		self.bouton2j.grid(row = 3, column = 1)
		
	def interface1j(self):
		self.bouton1j.destroy()
		self.bouton2j.destroy()
		self.messageD.destroy()
		self.message1j = Label(self, text = '1 joueur')
		self.message1j.grid (row = 1, columnspan = 3)
		self.message_point = Label(self, text = 'Nombre de points = ')
		self.message_point.grid(row = 2, column = 0)
		self.message_point2 = Label(self, text = self.points)
		self.message_point2.grid(row = 2, column = 1)
		self.message_point3 = Label(self,text = 'points')
		self.message_point3.grid(row = 2, column = 2)
		self.boutonP= Button(self, text = 'Pierre', command = self.pierre)
		self.boutonP.grid(row = 3, column = 0)
		self.boutonF = Button(self, text = 'Feuille', command = self.feuille)
		self.boutonF.grid(row = 3, column = 1)
		self.boutonC = Button(self, text = 'Ciseaux', command =self.ciseaux)
		self.boutonC.grid(row = 3, column = 2)
		self.boutonswitch1 = Button(self, text = 'jouer à 2', command = self.destroyswitch)
		self.boutonswitch1.grid(row=5, column = 1)
	
	def destroyswitch(self):
		self.boutonP.destroy()
		self.boutonF.destroy()
		self.boutonC.destroy()
		self.boutonswitch1.destroy()
		self.message1j.destroy()
		self.message_point.destroy()
		self.message_point2.destroy()
		self.message_point3.destroy()
		self.points=0
		self.interface2j()
		
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
		self.message_joueur.grid(row = 3, column = 0)
		self.messagevs = Label(self, text = 'vs')
		self.messagevs.grid(row = 3, column = 1)
		self.message_ordi = Label(self, text = self.ordi)
		self.message_ordi.grid(row = 3, column = 2)
		self.message_fin = Label(self,text = '')
		if self.resultat ==0:
			self.message_fin = Label(self, text = 'Egalité')
			self.message_fin.grid(row = 4, columnspan = 3)
		elif self.resultat ==2:
			self.message_fin= Label(self, text = 'Tu as gagné')
			self.message_fin.grid(row = 4, columnspan = 3)
		elif self.resultat ==1:
			self.message_fin = Label(self, text = "l'ia a gagné")
			self.message_fin.grid(row = 4, columnspan = 3)
		self.bouton_replay = Button(self, text = 'Continuer', command = self.destroy)
		self.bouton_replay.grid(row = 5, column = 1)
		
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
		
		
		
		
		
	def interface2j(self):
		self.bouton1j.destroy()
		self.bouton2j.destroy()
		self.messageD.destroy()
		self.message2j = Label(self, text = '2 joueurs')
		self.message2j.grid(row = 1, columnspan = 3)
		self.message_point = Label(self, text = 'Joueur 1 = ')
		self.message_point.grid(row = 2, column = 0)
		self.message_point2 = Label(self, text = self.points2j1)
		self.message_point2.grid(row = 2, column = 1)
		self.message_pointj2 = Label(self, text = 'Joueur 2 = ')
		self.message_pointj2.grid(row = 3, column = 0)
		self.message_point2j2 = Label(self, text = self.points2j2)
		self.message_point2j2.grid(row = 3, column = 1)
		self.message_joueur1 = Label(self, text = 'Joueur 1')
		self.message_joueur1.grid(row = 5, columnspan = 3)	
		self.boutonP= Button(self, text = 'Pierre', command = self.pierre1)
		self.boutonP.grid(row = 6, column = 0)
		self.boutonF = Button(self, text = 'Feuille', command = self.feuille1)
		self.boutonF.grid(row = 6,column = 1)
		self.boutonC = Button(self, text = 'Ciseaux', command =self.ciseaux1)
		self.boutonC.grid(row = 6, column = 2)
		self.boutonswitch2 = Button(self, text = 'jouer seul', command = self.destroyswitch2j)
		self.boutonswitch2.grid(row = 8, column = 1)
	
	def destroyswitch2j(self):
		self.message_joueur1.destroy()
		self.boutonP.destroy()
		self.boutonF.destroy()
		self.boutonC.destroy()
		self.boutonswitch2.destroy()
		self.message2j.destroy()
		self.message_point.destroy()
		self.message_point2.destroy()
		self.message_pointj2.destroy()
		self.message_point2j2.destroy()
		self.points2j1=0
		self.points2j2=0
		self.interface1j()
		
	def pierre1(self):
		self.choixj1 = 'pierre'
		self.joueur2()
		
	def feuille1(self):
		self.choixj1 = 'feuille'
		self.joueur2()
		
	def ciseaux1(self):
		self.choixj1 = 'ciseaux'
		self.joueur2()
		
	def joueur2 (self):
		self.message_joueur1.destroy()
		self.boutonP.destroy()
		self.boutonF.destroy()
		self.boutonC.destroy()
		self.boutonswitch2.destroy()
		self.message_joueur2 = Label(self, text = 'Joueur 2')
		self.message_joueur2.grid(row = 5, columnspan = 3)
		self.boutonP2= Button(self, text = 'Pierre', command = self.pierre2)
		self.boutonP2.grid(row = 6, column = 0)
		self.boutonF2 = Button(self, text = 'Feuille', command = self.feuille2)
		self.boutonF2.grid(row = 6, column = 1)
		self.boutonC2 = Button(self, text = 'Ciseaux', command =self.ciseaux2)
		self.boutonC2.grid(row = 6, column = 2)

	def pierre2(self):
		self.choixj2 = 'pierre'
		self.manche2j()
		
	def feuille2(self):
		self.choixj2 = 'feuille'
		self.manche2j()
		
	def ciseaux2(self):
		self.choixj2 = 'ciseaux'
		self.manche2j()

	def manche2j (self):
		self.message_joueur2.destroy()
		self.boutonP2.destroy()
		self.boutonF2.destroy()
		self.boutonC2.destroy()
		if self.choixj1 == self.choixj2 :
			self.resultat = 0
		elif self.choixj1 == 'pierre':
			if self.choixj2 == 'feuille' :
				self.resultat = 1
			elif self.choixj2 == 'ciseaux':
				self.resultat = 2
		elif self.choixj1 == 'feuille':
			if self.choixj2 == 'pierre':
				self.resultat = 2
			elif self.choixj2 == 'ciseaux':
				self.resultat = 1
		elif self.choixj1 == 'ciseaux':
			if self.choixj2 == 'pierre':
				self.resultat = 1
			elif self.choixj2 == 'feuille':
				self.resultat = 2
		self.point2j()
		
	def point2j(self):
		if self.resultat == 2:
			self.points2j1 = self.points2j1 + 1			
		elif self.resultat == 1:
			self.points2j2 = self.points2j2 + 1
		self.afficher2j()
		
	def afficher2j(self):
		self.message_j1 = Label(self, text = self.choixj1)
		self.message_j1.grid(row = 6, column = 0)
		self.messagevs = Label(self, text = 'vs')
		self.messagevs.grid(row = 6, column = 1)
		self.message_j2= Label(self, text = self.choixj2)
		self.message_j2.grid(row = 6, column = 2)
		if self.resultat ==0:
			self.message_fin = Label(self, text = 'Egalité')
			self.message_fin.grid(row = 7, columnspan = 3)
		elif self.resultat ==2:
			self.message_fin= Label(self, text = 'Le joueur 1 a gagné')
			self.message_fin.grid(row = 7, columnspan = 3)
		elif self.resultat ==1:
			self.message_fin = Label(self, text = "le joueur 2 a gagné")
			self.message_fin.grid(row = 7, columnspan = 3)
		self.bouton_replay = Button(self, text = 'Continuer', command = self.destroy2j)
		self.bouton_replay.grid(row=8, column = 1)
		
	def destroy2j(self):
		self.message_j1.destroy()
		self.messagevs.destroy()
		self.message_j2.destroy()
		self.bouton_replay.destroy()
		self.message_point.destroy()
		self.message_point2.destroy()
		self.message_pointj2.destroy()
		self.message_point2j2.destroy()
		self.message_fin.destroy()
		self.message2j.destroy()
		self.interface2j()
				
		
		
fenetre = Root()
fenetre.mainloop()
