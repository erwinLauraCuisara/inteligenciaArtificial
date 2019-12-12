from tkinter import *
class interfaz():
	def __init__(self):
		self.ventana=Tk()
		self.ventana.attributes("-fullscreen",True)
		self.ventana.title("RATON HEURISTICO")
		self.botones=[]
		self.primerTiro=True
		self.iaux=0
		self.jaux=0
		self.generarVentanaPrincipal()

		self.ventana.mainloop()
	def generarVentanaPrincipal(self):
		self.frame=Frame(self.ventana)
		self.frame.pack()
		Label(self.frame,text="PROBLEMA DE LAS N REINAS, PORFABOR \n LLENE EL TABLERO PARA HACER LA REPARACION",font=("comic sans ms",32)).grid(row=0,column=0,columnspan=15,pady=2)
		for i in range(0,8):
			self.botones.append([])
			for j in range(0,8):
				self.botones[i].append(Button(self.frame,text="",font=('Helvetica',25),bg="red",width=5,height=-1))
				self.botones[i][j].grid(row=i+1,column=j,padx=0,pady=1)
		self.botones[0][0]['command']=lambda:self.modificar(0,0)
		self.botones[0][1]['command']=lambda:self.modificar(0,1)
		self.botones[0][2]['command']=lambda:self.modificar(0,2)
		self.botones[0][3]['command']=lambda:self.modificar(0,3)
		self.botones[0][4]['command']=lambda:self.modificar(0,4)
		self.botones[0][5]['command']=lambda:self.modificar(0,5)
		self.botones[0][6]['command']=lambda:self.modificar(0,6)
		self.botones[0][7]['command']=lambda:self.modificar(0,7)
		
		self.botones[1][0]['command']=lambda:self.modificar(1,0) 
		self.botones[1][1]['command']=lambda:self.modificar(1,1)
		self.botones[1][2]['command']=lambda:self.modificar(1,2)
		self.botones[1][3]['command']=lambda:self.modificar(1,3)
		self.botones[1][4]['command']=lambda:self.modificar(1,4)
		self.botones[1][5]['command']=lambda:self.modificar(1,5)
		self.botones[1][6]['command']=lambda:self.modificar(1,6)
		self.botones[1][7]['command']=lambda:self.modificar(1,7)
		self.botones[2][0]['command']=lambda:self.modificar(2,0) 
		self.botones[2][1]['command']=lambda:self.modificar(2,1)
		self.botones[2][2]['command']=lambda:self.modificar(2,2)
		self.botones[2][3]['command']=lambda:self.modificar(2,3)
		self.botones[2][4]['command']=lambda:self.modificar(2,4)
		self.botones[2][5]['command']=lambda:self.modificar(2,5)
		self.botones[2][6]['command']=lambda:self.modificar(2,6)
		self.botones[2][7]['command']=lambda:self.modificar(2,7)
		self.botones[3][0]['command']=lambda:self.modificar(3,0)
		self.botones[3][1]['command']=lambda:self.modificar(3,1)
		self.botones[3][2]['command']=lambda:self.modificar(3,2)
		self.botones[3][3]['command']=lambda:self.modificar(3,3)
		self.botones[3][4]['command']=lambda:self.modificar(3,4)
		self.botones[3][5]['command']=lambda:self.modificar(3,5)
		self.botones[3][6]['command']=lambda:self.modificar(3,6)
		self.botones[3][7]['command']=lambda:self.modificar(3,7)
		self.botones[4][0]['command']=lambda:self.modificar(4,0)
		self.botones[4][1]['command']=lambda:self.modificar(4,1)
		self.botones[4][2]['command']=lambda:self.modificar(4,2)
		self.botones[4][3]['command']=lambda:self.modificar(4,3)
		self.botones[4][4]['command']=lambda:self.modificar(4,4)
		self.botones[4][5]['command']=lambda:self.modificar(4,5)
		self.botones[4][6]['command']=lambda:self.modificar(4,6)
		self.botones[4][7]['command']=lambda:self.modificar(4,7)
		self.botones[5][0]['command']=lambda:self.modificar(5,0)
		self.botones[5][1]['command']=lambda:self.modificar(5,1)
		self.botones[5][2]['command']=lambda:self.modificar(5,2)
		self.botones[5][3]['command']=lambda:self.modificar(5,3)
		self.botones[5][4]['command']=lambda:self.modificar(5,4)
		self.botones[5][5]['command']=lambda:self.modificar(5,5)
		self.botones[5][6]['command']=lambda:self.modificar(5,6)
		self.botones[5][7]['command']=lambda:self.modificar(5,7)
		self.botones[6][0]['command']=lambda:self.modificar(6,0)
		self.botones[6][1]['command']=lambda:self.modificar(6,1)
		self.botones[6][2]['command']=lambda:self.modificar(6,2)
		self.botones[6][3]['command']=lambda:self.modificar(6,3)
		self.botones[6][4]['command']=lambda:self.modificar(6,4)
		self.botones[6][5]['command']=lambda:self.modificar(6,5)
		self.botones[6][6]['command']=lambda:self.modificar(6,6)
		self.botones[6][7]['command']=lambda:self.modificar(6,7)
		self.botones[7][0]['command']=lambda:self.modificar(7,0)
		self.botones[7][1]['command']=lambda:self.modificar(7,1)
		self.botones[7][2]['command']=lambda:self.modificar(7,2)
		self.botones[7][3]['command']=lambda:self.modificar(7,3)
		self.botones[7][4]['command']=lambda:self.modificar(7,4)
		self.botones[7][5]['command']=lambda:self.modificar(7,5)
		self.botones[7][6]['command']=lambda:self.modificar(7,6)
		self.botones[7][7]['command']=lambda:self.modificar(7,7)
		
		Label(self.frame,text="SE PROCEDE A REPARAR EL TABLERO",font=("comic sans ms",20)).grid(row=9,column=0,columnspan=15,padx=2,pady=2)
		Button(self.frame,text="salir",font=('Helvetica',33),bg="blue",width=3,height=-1,command=self.cerrar).grid(row=9,column=14,padx=1,pady=2)
		Button(self.frame,text="empezar",font=('Helvetica',25),bg="blue",width=6,height=-1,command=self.generarMatriz).grid(row=8,column=14,padx=1,pady=2)
		Button(self.frame,text="limpiar",font=('Helvetica',25),bg="blue",width=5,height=-1,command=self.limpiar).grid(row=7,column=14,padx=1,pady=2)
	def cerrar(self):
		sys.exit()
	def modificar(self,i,j):
		self.botones[i][j]['text']='R'
		self.iaux=i
		self.jaux=j
		self.primerTiro=False

	def mover(self,i,j,dato):
		self.botones[i][j]['text']=dato
	def limpiar(self):
		for i in range(0,8):
			for j in range(0,8):
				self.botones[i][j]['text']=""
		self.primerTiro=True
	def generarMatriz(self):
		matriz=[]
		for i in range(0,8):
			matriz.append([])
			for j in range(0,8):
				y=self.botones[i][j]['text']
				if(y==''):
					matriz[i].append('L')
				else:
					matriz[i].append(y)
x=interfaz()

