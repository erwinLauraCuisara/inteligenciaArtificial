from tkinter import *
class pila():
	def __init__(self):
		self.items=[]
	def estaVacia(self):
		return self.items==[]
	def push(self,item):
		self.items.append(item)
	def get(self):
		return self.items.pop()
class ratonCiega():
	def __init__(self,laberinto,interfaz):
		self.interfaz=interfaz
		self.laberinto=laberinto
		self.laberinto[0][0]='*'
		self.pila=pila()
		self.recorrer(0,0,0)
	def recorrer(self,i,j,num):
		control=False
		#arriba
		if(i>0):
			arriba=self.laberinto[i-1][j]
			if(type(arriba)!=int):
				if(arriba=="Q"):
					self.laberinto[i-1][j]="LLEGO"
					self.interfaz.mover(i-1,j,'LLEGO')
				if(arriba!="*"):
					self.pila.push([i-1,j])
					self.laberinto[i-1][j]=num+1
					self.interfaz.mover(i-1,j,num+1)
					control=True
					self.recorrer(i-1,j,num+1)
		#izquierda
		if(j>0):
			izquierda=self.laberinto[i][j-1]
			if(type(izquierda)!=int):
				if(izquierda=="Q"):
					self.laberinto[i][j-1]="LLEGO"
					self.interfaz.mover(i,j-1,"LLEGO")
				if(izquierda!="*"):
					self.pila.push([i,j-1])
					self.laberinto[i][j-1]=num+1
					self.interfaz.mover(i,j-1,num+1)
					control=True
					self.recorrer(i,j-1,num+1)
		#derecha
		if(j<len(self.laberinto[0])-1):
			derecha=self.laberinto[i][j+1]
			if(type(derecha)!=int):
				if(derecha=="Q"):
					self.laberinto[i][j+1]="LLEGO"
					self.interfaz.mover(i,j+1,"LLEGO")
				if(derecha!="*"):
					self.pila.push([i,j+1])
					self.laberinto[i][j+1]=num+1
					self.interfaz.mover(i,j+1,num+1)
					control=True
					self.recorrer(i,j+1,num+1)
		#abajo
		if(i<len(self.laberinto)-1):
			abajo=self.laberinto[i+1][j]
			if(type(abajo)!=int):
				if(abajo=="Q"):
					self.laberinto[i+1][j]="LLEGO"
					self.interfaz.mover(i+1,j,"LLEGO")
					
				if(abajo!="*"):
					self.pila.push([i+1,j])
					self.laberinto[i+1][j]=num+1
					self.interfaz.mover(i+1,j,num+1)
					control=True
					self.recorrer(i+1,j,num+1)
		try:
			if(control==False):
				aux=self.pila.get()
				self.recorrer(aux[0],aux[1],num)
		except IndexError:
			print("se llego al objetivo")
	def mostrar(self):
		return self.laberinto
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
		Label(self.frame,text="RATON POR EL METODO DE PROFUNDIDAD, PORFABOR \n AGA CLICK EN LOS CUADROS ROJOS PARA PONER OBSTACULOS",font=("comic sans ms",32)).grid(row=0,column=0,columnspan=15,padx=2,pady=2)
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
		Label(self.frame,text="NOTAR QUE LOS NUMEROS(ASCENDETE) SON LOS PASOS QUE REALIZO EL RATON \n INCLUYENDO EL RETORNO DEL RATON(SACAR DE LA PILA)",font=("comic sans ms",20)).grid(row=8,column=0,columnspan=15,padx=2,pady=2)
		Button(self.frame,text="salir",font=('Helvetica',33),bg="blue",width=3,height=-1,command=self.cerrar).grid(row=8,column=14,padx=2,pady=2)
		Button(self.frame,text="empezar",font=('Helvetica',25),bg="blue",width=6,height=-1,command=self.generarMatriz).grid(row=7,column=14,padx=2,pady=2)
		Button(self.frame,text="limpiar",font=('Helvetica',25),bg="blue",width=5,height=-1,command=self.limpiar).grid(row=6,column=14,padx=2,pady=2)
	def cerrar(self):
		sys.exit()
	def modificar(self,i,j):
		self.botones[i][j]['text']='*'
	def mover(self,i,j,dato):
		self.botones[i][j]['text']=dato
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
					matriz[i].append('L')
				else:
					matriz[i].append(self.botones[i][j]['text'])
		ratonCiega(matriz,self)
'''print("el laberinto por defecto es el que esta abajo, si desea cambiarlo: \n -L significa que esta LIBRE \n -Q es el queso \n -el raton esta en la pos (0,0) \n -* es el muro ")
laberinto=[[0,'L','L','L'],['L','L','*','*'],['L','*','*','L'],['L','L','L','L'],['L','*','L','Q']]
for i in range(0,len(laberinto)):
			print(laberinto[i])
print("====")
print("el recorrido empieza con 1,2,3,...,n asta llegar al queso (busqueda con profundidad) \n si no encuentra salida vuelve (sacamos de la pila)")
x=ratonCiega(laberinto)
print(x.mostrar())'''
x=interfaz()

