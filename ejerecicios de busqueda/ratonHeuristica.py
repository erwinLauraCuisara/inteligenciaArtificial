from tkinter import *
import sys
class llenarLaverinto():

	def __init__(self,laberinto):
		self.laberinto=laberinto
		self.libre=100
		quesoi=len(self.laberinto)-1
		quesoj=len(laberinto[0])-1
		self.llenar(quesoi,quesoj,1)
	def llenar(self,i,j,num):
		#izquierda
		if(j>0):
			izquierda=self.laberinto[i][j-1]
			if(izquierda!='*' and izquierda==self.libre):
				self.laberinto[i][j-1]=num+1
				self.llenar(i,j-1,num+1)
		#arriba
		if(i>0):
			arriba=self.laberinto[i-1][j]
			if(arriba!='*' and arriba==self.libre):
				self.laberinto[i-1][j]=num+1
				self.llenar(i-1,j,num+1)
		
		#derecha
		if(j<len(self.laberinto[0])-1):
			derecha=self.laberinto[i][j+1]
			if(derecha!='*' and derecha==self.libre):
				self.laberinto[i][j+1]=num+1
				self.llenar(i,j+1,num+1)
		#abajo
		if(i<len(self.laberinto)-1):
			abajo=self.laberinto[i+1][j]
			if(abajo!='*' and abajo==self.libre):
				self.laberinto[i+1][j]=num+1
				self.llenar(i+1,j,num+1)
	def mostrar(self):
		print("el olor generado por el queso es: donde el numero mas menor es el que esta mas cerca del queso")
		for i in range(0,len(self.laberinto)):
			print(self.laberinto[i])
		return self.laberinto
class raton():
	def __init__(self,laberinto,interfaz):
		self.interfaz=interfaz
		self.laberinto=llenarLaverinto(laberinto).mostrar()
		self.recorrer(0,0,999)
	def recorrer(self,i,j,menor):
		control=False
		iaux=i
		jaux=j
		#arriba
		if(i>0):
			arriba=self.laberinto[i-1][j]
			if(type(arriba)!=str):
				if(arriba<=menor):
					iaux=i-1
					menor=arriba
					control=True
		#izquierda
		if(j>0):
			izquierda=self.laberinto[i][j-1]
			if(type(izquierda)!=str):
				if(izquierda<=menor):
					jaux=j-1
					iaux=i
					menor=izquierda
					control=True
		#derecha
		if(j<len(self.laberinto[0])-1):
			derecha=self.laberinto[i][j+1]
			if(type(derecha)!=str):
				if(derecha<=menor):
					jaux=j+1
					iaux=i
					menor=derecha
					control=True
		#abajo
		if(i<len(self.laberinto)-1):
			abajo=self.laberinto[i+1][j]
			if(type(abajo)!=str):
				if(abajo<=menor):
					menor=abajo
					iaux=i+1
					jaux=j
					control=True
		try:
			if(control):
				#self.laberinto[iaux][jaux]='R'
				self.interfaz.mover(iaux,jaux)
				self.recorrer(iaux,jaux,menor)
		except:
			print("sin salida")
	def mostrar(self):
		for i in range(0,len(self.laberinto)):
			print(self.laberinto[i])
class interfaz():
	def __init__(self):
		self.ventana=Tk()
		self.ventana.attributes("-fullscreen",True)
		self.ventana.title("RATON HEURISTICO")
		self.botones=[]
		
		self.generarVentanaPrincipal()

		self.ventana.mainloop()
	def generarVentanaPrincipal(self):
		self.frame=Frame(self.ventana)
		self.frame.pack()
		Label(self.frame,text="RATON HEURISTICO \n PORFABOR AGA CLICK EN LOS CUADROS PARA PONER MUROS",font=("comic sans ms",33)).grid(row=0,column=0,columnspan=15,padx=2,pady=2)
		for i in range(0,7):
			self.botones.append([])
			for j in range(0,14):
				self.botones[i].append(Button(self.frame,text="",font=('Helvetica',33),bg="red",width=2,height=-1))
				self.botones[i][j].grid(row=i+1,column=j,padx=2,pady=2)
		self.botones[0][0]['text']='R'
		self.botones[0][1]['command']=lambda:self.modificar(0,1)
		self.botones[0][2]['command']=lambda:self.modificar(0,2)
		self.botones[0][3]['command']=lambda:self.modificar(0,3)
		self.botones[0][4]['command']=lambda:self.modificar(0,4)
		self.botones[0][5]['command']=lambda:self.modificar(0,5)
		self.botones[0][6]['command']=lambda:self.modificar(0,6)
		self.botones[0][7]['command']=lambda:self.modificar(0,7)
		self.botones[0][8]['command']=lambda:self.modificar(0,8)
		self.botones[0][9]['command']=lambda:self.modificar(0,9)		
		self.botones[0][10]['command']=lambda:self.modificar(0,10)
		self.botones[0][11]['command']=lambda:self.modificar(0,11)
		self.botones[0][12]['command']=lambda:self.modificar(0,12)
		self.botones[0][13]['command']=lambda:self.modificar(0,13) 
		
		self.botones[1][0]['command']=lambda:self.modificar(1,0) 
		self.botones[1][1]['command']=lambda:self.modificar(1,1)
		self.botones[1][2]['command']=lambda:self.modificar(1,2)
		self.botones[1][3]['command']=lambda:self.modificar(1,3)
		self.botones[1][4]['command']=lambda:self.modificar(1,4)
		self.botones[1][5]['command']=lambda:self.modificar(1,5)
		self.botones[1][6]['command']=lambda:self.modificar(1,6)
		self.botones[1][7]['command']=lambda:self.modificar(1,7)
		self.botones[1][8]['command']=lambda:self.modificar(1,8)
		self.botones[1][9]['command']=lambda:self.modificar(1,9)		
		self.botones[1][10]['command']=lambda:self.modificar(1,10)
		self.botones[1][11]['command']=lambda:self.modificar(1,11)
		self.botones[1][12]['command']=lambda:self.modificar(1,12)
		self.botones[1][13]['command']=lambda:self.modificar(1,13) 
		self.botones[2][0]['command']=lambda:self.modificar(2,0) 
		self.botones[2][1]['command']=lambda:self.modificar(2,1)
		self.botones[2][2]['command']=lambda:self.modificar(2,2)
		self.botones[2][3]['command']=lambda:self.modificar(2,3)
		self.botones[2][4]['command']=lambda:self.modificar(2,4)
		self.botones[2][5]['command']=lambda:self.modificar(2,5)
		self.botones[2][6]['command']=lambda:self.modificar(2,6)
		self.botones[2][7]['command']=lambda:self.modificar(2,7)
		self.botones[2][8]['command']=lambda:self.modificar(2,8)
		self.botones[2][9]['command']=lambda:self.modificar(2,9)		
		self.botones[2][10]['command']=lambda:self.modificar(2,10)
		self.botones[2][11]['command']=lambda:self.modificar(2,11)
		self.botones[2][12]['command']=lambda:self.modificar(2,12)
		self.botones[2][13]['command']=lambda:self.modificar(2,13) 
		self.botones[3][0]['command']=lambda:self.modificar(3,0)
		self.botones[3][1]['command']=lambda:self.modificar(3,1)
		self.botones[3][2]['command']=lambda:self.modificar(3,2)
		self.botones[3][3]['command']=lambda:self.modificar(3,3)
		self.botones[3][4]['command']=lambda:self.modificar(3,4)
		self.botones[3][5]['command']=lambda:self.modificar(3,5)
		self.botones[3][6]['command']=lambda:self.modificar(3,6)
		self.botones[3][7]['command']=lambda:self.modificar(3,7)
		self.botones[3][8]['command']=lambda:self.modificar(3,8)
		self.botones[3][9]['command']=lambda:self.modificar(3,9)		
		self.botones[3][10]['command']=lambda:self.modificar(3,10)
		self.botones[3][11]['command']=lambda:self.modificar(3,11)
		self.botones[3][12]['command']=lambda:self.modificar(3,12)
		self.botones[3][13]['command']=lambda:self.modificar(3,13) 
		self.botones[4][0]['command']=lambda:self.modificar(4,0)
		self.botones[4][1]['command']=lambda:self.modificar(4,1)
		self.botones[4][2]['command']=lambda:self.modificar(4,2)
		self.botones[4][3]['command']=lambda:self.modificar(4,3)
		self.botones[4][4]['command']=lambda:self.modificar(4,4)
		self.botones[4][5]['command']=lambda:self.modificar(4,5)
		self.botones[4][6]['command']=lambda:self.modificar(4,6)
		self.botones[4][7]['command']=lambda:self.modificar(4,7)
		self.botones[4][8]['command']=lambda:self.modificar(4,8)
		self.botones[4][9]['command']=lambda:self.modificar(4,9)		
		self.botones[4][10]['command']=lambda:self.modificar(4,10)
		self.botones[4][11]['command']=lambda:self.modificar(4,11)
		self.botones[4][12]['command']=lambda:self.modificar(4,12)
		self.botones[4][13]['command']=lambda:self.modificar(4,13) 
		self.botones[5][0]['command']=lambda:self.modificar(5,0)
		self.botones[5][1]['command']=lambda:self.modificar(5,1)
		self.botones[5][2]['command']=lambda:self.modificar(5,2)
		self.botones[5][3]['command']=lambda:self.modificar(5,3)
		self.botones[5][4]['command']=lambda:self.modificar(5,4)
		self.botones[5][5]['command']=lambda:self.modificar(5,5)
		self.botones[5][6]['command']=lambda:self.modificar(5,6)
		self.botones[5][7]['command']=lambda:self.modificar(5,7)
		self.botones[5][8]['command']=lambda:self.modificar(5,8)
		self.botones[5][9]['command']=lambda:self.modificar(5,9)		
		self.botones[5][10]['command']=lambda:self.modificar(5,10)
		self.botones[5][11]['command']=lambda:self.modificar(5,11)
		self.botones[5][12]['command']=lambda:self.modificar(5,12)
		self.botones[5][13]['command']=lambda:self.modificar(5,13) 
		self.botones[6][0]['command']=lambda:self.modificar(6,0)
		self.botones[6][1]['command']=lambda:self.modificar(6,1)
		self.botones[6][2]['command']=lambda:self.modificar(6,2)
		self.botones[6][3]['command']=lambda:self.modificar(6,3)
		self.botones[6][4]['command']=lambda:self.modificar(6,4)
		self.botones[6][5]['command']=lambda:self.modificar(6,5)
		self.botones[6][6]['command']=lambda:self.modificar(6,6)
		self.botones[6][7]['command']=lambda:self.modificar(6,7)
		self.botones[6][8]['command']=lambda:self.modificar(6,8)
		self.botones[6][9]['command']=lambda:self.modificar(6,9)		
		self.botones[6][10]['command']=lambda:self.modificar(6,10)
		self.botones[6][11]['command']=lambda:self.modificar(6,11)
		self.botones[6][12]['command']=lambda:self.modificar(6,12)
		self.botones[6][13]['text']="Q"
		Button(self.frame,text="salir",font=('Helvetica',33),bg="red",width=3,height=-1,command=self.cerrar).grid(row=8,column=14,padx=2,pady=2)
		Button(self.frame,text="empezar",font=('Helvetica',25),bg="red",width=6,height=-1,command=self.generarMatriz).grid(row=7,column=14,padx=2,pady=2)
		Button(self.frame,text="limpiar",font=('Helvetica',25),bg="red",width=5,height=-1,command=self.limpiar).grid(row=6,column=14,padx=2,pady=2)
	def cerrar(self):
		sys.exit()
	def modificar(self,i,j):
		self.botones[i][j]['text']='*'
	def mover(self,i,j):
		self.botones[i][j]['text']='R'
	def limpiar(self):
		for i in range(0,7):
			for j in range(0,14):
				self.botones[i][j]['text']=""
	def generarMatriz(self):
		matriz=[]
		for i in range(0,7):
			matriz.append([])
			for j in range(0,14):
				y=self.botones[i][j]['text']
				if(y==''):
					matriz[i].append(100)
				else:
					matriz[i].append(self.botones[i][j]['text'])
		raton(matriz,self)
r=interfaz()



