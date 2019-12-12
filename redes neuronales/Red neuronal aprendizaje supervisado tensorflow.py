
import numpy as np
import tensorflow as tf
from tkinter import *
from tkinter import ttk
#autor:erwin laura cuisara

class Interfaz():
	def __init__(self):
		self.igual=False
		ventana=Tk()
		ventana.title("Calcu_Niwre")
		ventana.config(bg="black")
		frame1=Frame(ventana,bg="black")
		frame1.grid(row=0,column=0)
		frame2=Frame(ventana,bg="black")
		frame2.grid(row=1,column=0)
		frame3=Frame(ventana,bg="black")
		frame3.grid(row=2,column=0)
		self.texto=StringVar()
		label=Label(frame1,fg="black",font=("comic sans ms",50),textvariable=self.texto)
		label.grid(row=0,column=0)

		boton1=Button(frame2,text="P",command=lambda:self.cambiarNum("P"),font=('Bauhaus 93',50))
		boton1.grid(row=0,column=0,padx=1,pady=1)
		boton1.config(width=4,height=1)

		boton2=Button(frame2,text="Q",command=lambda:self.cambiarNum("Q"),font=('Bauhaus 93',50))
		boton2.grid(row=0,column=1,padx=1,pady=1)
		boton2.config(width=4,height=1)

		boton3=Button(frame2,text="R",command=lambda:self.cambiarNum("R"),font=('Bauhaus 93',50))
		boton3.grid(row=0,column=2,padx=5,pady=5)
		boton3.config(width=4,height=1)

		boton4=Button(frame2,text="W",command=lambda:self.cambiarNum("W"),font=('Bauhaus 93',50))
		boton4.grid(row=1,column=0,padx=5,pady=5)
		boton4.config(width=4,height=1)

		boton5=Button(frame2,text="X",command=lambda:self.cambiarNum("X"),font=('Bauhaus 93',50))
		boton5.grid(row=1,column=1,padx=5,pady=5)
		boton5.config(width=4,height=1)

		boton6=Button(frame2,text="Y",command=lambda:self.cambiarNum("Y"),font=('Bauhaus 93',50))
		boton6.grid(row=1,column=2,padx=5,pady=5)
		boton6.config(width=4,height=1)

		boton7=Button(frame2,text="Z",command=lambda:self.cambiarNum("Z"),font=('Bauhaus 93',50))
		boton7.grid(row=2,column=0,padx=5,pady=5)
		boton7.config(width=4,height=1)

		boton8=Button(frame2,text="A",command=lambda:self.cambiarNum("A"),font=('Bauhaus 93',50))
		boton8.grid(row=2,column=1,padx=5,pady=5)
		boton8.config(width=4,height=1)
	
			
		boton9=Button(frame2,text="B",command=lambda:self.cambiarNum("B"),font=('Bauhaus 93',50))
		boton9.grid(row=2,column=2,padx=5,pady=5)
		boton9.config(width=4,height=1)

		botonRes=Button(frame2,text="=",command=self.res,font=('Bauhaus 93',50))
		botonRes.grid(row=3,column=2,columnspan=3,padx=5,pady=5)
		botonRes.config(width=10,height=1)

		botonX=Button(frame2,text="Ↄ",command=lambda:self.cambiarNum("Ↄ"),font=('Bauhaus 93',50))
		botonX.grid(row=0,column=3,padx=5,pady=5)
		botonX.config(width=4,height=1)

		botonD=Button(frame2,text="^",command=lambda:self.cambiarNum("^"),font=('Bauhaus 93',50))
		botonD.grid(row=1,column=3,padx=5,pady=5)
		botonD.config(width=4,height=1)

		botonMas=Button(frame2,text="v",command=lambda:self.cambiarNum("v"),font=('Bauhaus 93',50))
		botonMas.grid(row=2,column=3,padx=5,pady=5)
		botonMas.config(width=4,height=1)

		botonCero=Button(frame2,text=")",command=lambda:self.cambiarNum(")"),font=('Bauhaus 93',50))
		botonCero.grid(row=3,column=1,padx=5,pady=5)
		botonCero.config(width=4,height=1)

		botonMenos=Button(frame2,text="~",command=lambda:self.cambiarNum("~"),font=('Bauhaus 93',50))
		botonMenos.grid(row=2,column=4,padx=5,pady=5)
		botonMenos.config(width=4,height=1)

		botonPunto=Button(frame2,text="(",command=lambda:self.cambiarNum("("),font=('Bauhaus 93',50))
		botonPunto.grid(row=3,column=0,padx=5,pady=5)
		botonPunto.config(width=4,height=1)

		botonC=Button(frame2,text="Limpiar",command=self.clear,font=('Bauhaus 93',50))
		botonC.grid(row=0,column=4,padx=5,pady=5)
		botonC.config(width=6,height=1)

		botonDelete=Button(frame2,text="Del",command=self.borrar,font=('Bauhaus 93',50))
		botonDelete.grid(row=1,column=4,padx=5,pady=5)
		botonDelete.config(width=4,height=1)

		#Seleccionables creacion de combobox 
		
		Label(frame3,fg="black",font=("comic sans ms",30),text="P:").grid(row=0,column=0)
		self.P=ttk.Combobox(frame3,state="readonly",font=("comic sans ms",20),width=4,height=3,values=["V","F","I"])
		self.P.grid(row=0,column=1,padx=5,pady=5)
		self.P.set("I")

		#Q
		Label(frame3,fg="black",font=("comic sans ms",30),text="Q:").grid(row=0,column=2)
		self.Q=ttk.Combobox(frame3,state="readonly",font=("comic sans ms",20),width=4,height=3,values=["V","F","I"])
		self.Q.grid(row=0,column=3,padx=5,pady=5)
		self.Q.set("I")

		Label(frame3,fg="black",font=("comic sans ms",30),text="R:").grid(row=0,column=4)
		self.R=ttk.Combobox(frame3,state="readonly",font=("comic sans ms",20),width=4,height=3,values=["V","F","I"])
		self.R.grid(row=0,column=5,padx=5,pady=5)
		self.R.set("I")

		Label(frame3,fg="black",font=("comic sans ms",30),text="S:").grid(row=0,column=6)
		self.S=ttk.Combobox(frame3,state="readonly",font=("comic sans ms",20),width=4,height=3,values=["V","F","I"])
		self.S.grid(row=0,column=7,padx=5,pady=5)
		self.S.set("I")

		Label(frame3,fg="black",font=("comic sans ms",30),text="T:").grid(row=0,column=8)
		self.T=ttk.Combobox(frame3,state="readonly",font=("comic sans ms",20),width=4,height=3,values=["V","F","I"])
		self.T.grid(row=0,column=9,padx=5,pady=5)
		self.T.set("I")

		Label(frame3,fg="black",font=("comic sans ms",30),text="W:").grid(row=0,column=10)
		self.W=ttk.Combobox(frame3,state="readonly",font=("comic sans ms",20),width=4,height=3,values=["V","F","I"])
		self.W.grid(row=0,column=11,padx=5,pady=5)
		self.W.set("I")
		#EEEEE
		Label(frame3,fg="black",font=("comic sans ms",30),text="X:").grid(row=1,column=0)
		self.X=ttk.Combobox(frame3,state="readonly",font=("comic sans ms",20),width=4,height=3,values=["V","F","I"])
		self.X.grid(row=1,column=1,padx=5,pady=5)
		self.X.set("I")

		#Q
		Label(frame3,fg="black",font=("comic sans ms",30),text="Y:").grid(row=1,column=2)
		self.Y=ttk.Combobox(frame3,state="readonly",font=("comic sans ms",20),width=4,height=3,values=["V","F","I"])
		self.Y.grid(row=1,column=3,padx=5,pady=5)
		self.Y.set("I")

		Label(frame3,fg="black",font=("comic sans ms",30),text="Z:").grid(row=1,column=4)
		self.Z=ttk.Combobox(frame3,state="readonly",font=("comic sans ms",20),width=4,height=3,values=["V","F","I"])
		self.Z.grid(row=1,column=5,padx=5,pady=5)
		self.Z.set("I")
        
		self.negacion=negacion()
		self.conjuncion=conjuncion()
		self.disyuncion=disyuncion()
		self.implicacion=implicacion()
		ventana.mainloop()
            #autor:erwin laura cuisara
	def cambiarNum(self,caracter):
		if self.igual and caracter.isdigit():
			self.texto.set("")
		self.texto.set(self.texto.get()+caracter)
		self.igual=False
	def evaluar(self,texto):
		contador=0
		textoAux=""
		posA=0
		posB=0
		indeterminado=False
		while(True):
			try:
				print(texto)
				t=texto[contador]
				if t=="I":
					indeterminado==True
				if t=="~":
					if texto[contador+1]!="I":
						texto=texto.replace(texto[contador:contador+2],self.negacion.analizar(float(texto[contador+1])))
						contador=-1
				elif t=="(":
					posA=contador
					indeterminado==False
				elif t==")" and indeterminado==False:
					posB=contador
					textoAux=texto[posA:posB+1]
					if textoAux[2]=="v":
						texto=texto.replace(textoAux,self.disyuncion.analizar(float(textoAux[1]),float(textoAux[3])))
					elif textoAux[2]=="^":
						texto=texto.replace(textoAux,self.conjuncion.analizar(float(textoAux[1]),float(textoAux[3])))
					elif textoAux[2]=="Ↄ":
						texto=texto.replace(textoAux,self.implicacion.analizar(float(textoAux[1]),float(textoAux[3])))
					contador=-1
				contador+=1
			except IndexError:
				break
		return texto            
	def res(self):
		#try:
            textoaux=self.texto.get()
            valores=self.P.get()
            if valores=="F":
                textoaux=textoaux.replace("P","0")
            elif valores=="V":
                textoaux=textoaux.replace("P","1")
            elif valores=="I":
                textoaux=textoaux.replace("P","I")
            
            valores=self.Q.get()
            if valores=="F":
                textoaux=textoaux.replace("Q","0")
            elif valores=="V":
                textoaux=textoaux.replace("Q","1")
            elif valores=="I":
                textoaux=textoaux.replace("Q","I")       
                
            valores=self.R.get()
            if valores=="F":
                textoaux=textoaux.replace("R","0")
            elif valores=="V":
                textoaux=textoaux.replace("R","1")
            elif valores=="I":
                textoaux=textoaux.replace("R","I")
            
            valores=self.S.get()
            if valores=="F":
                textoaux=textoaux.replace("S","0")
            elif valores=="V":
                textoaux=textoaux.replace("S","1")
            elif valores=="I":
                textoaux=textoaux.replace("S","I")
                
            valores=self.T.get()
            if valores=="F":
                textoaux=textoaux.replace("T","0")
            elif valores=="V":
                textoaux=textoaux.replace("T","1")
            elif valores=="I":
                textoaux=textoaux.replace("T","I")
            
            valores=self.W.get()
            if valores=="F":
                textoaux=textoaux.replace("W","0")
            elif valores=="V":
                textoaux=textoaux.replace("W","1")
            elif valores=="I":
                textoaux=textoaux.replace("W","I")
        
            valores=self.X.get()
            if valores=="F":
                textoaux=textoaux.replace("X","0")
            elif valores=="V":
                textoaux=textoaux.replace("X","1")
            elif valores=="I":
                textoaux=textoaux.replace("X","I")
                
            valores=self.Y.get()
            if valores=="F":
                textoaux=textoaux.replace("Y","0")
            elif valores=="V":
                textoaux=textoaux.replace("Y","1")
            elif valores=="I":
                textoaux=textoaux.replace("Y","I")
            
            valores=self.Z.get()
            if valores=="F":
                textoaux=textoaux.replace("Z","0")
            elif valores=="V":
                textoaux=textoaux.replace("Z","1")
            elif valores=="I":
                textoaux=textoaux.replace("Z","I")
            self.texto.set(self.evaluar(textoaux))
		#except ZeroDivisionError:
		#	self.texto.set("Math ERROR")
		#except:
		#	self.texto.set("Syntax ERROR")
		#finally:
			
            self.igual=True
	def clear(self):
		self.texto.set("")
	def borrar(self):
		self.texto.set(self.texto.get()[:-1])

#neurona negacion

class negacion():
    def __init__(self):
        self.NUM_FEATURES = 1
        self.NUM_ITER = 2000
        self.learning_rate = 0.01
        self.entrenar()
    def entrenar(self):
        x = np.array([[0], [1]], np.float32) 
        y = np.array([1,0], np.float32)
        
        y = np.reshape(y, [2,1])
        X = tf.placeholder(tf.float32, shape=[2, 1])
        Y = tf.placeholder(tf.float32, shape=[2, 1]) 
        self.W = tf.Variable(tf.zeros([self.NUM_FEATURES, 1]), tf.float32)
        B = tf.Variable(tf.zeros([1, 1]), tf.float32) 
        yHat = tf.sigmoid( tf.add(tf.matmul(X,self.W), B) )
        err = Y - yHat
        deltaW = tf.matmul(tf.transpose(X), err )
        deltaB = tf.reduce_sum(err, 0) 
        W_ = self.W + self.learning_rate * deltaW
        B_ = B + self.learning_rate * deltaB
        step = tf.group(self.W.assign(W_), B.assign(B_)) 
        sess = tf.Session()
        init = tf.global_variables_initializer()
        sess.run(init)
        for k in range(self.NUM_ITER):
            sess.run([step], feed_dict={X: x, Y: y})
 
        self.W = np.squeeze(sess.run(self.W))
        self.b = np.squeeze(sess.run(B))
        print('W: ' + str(self.W))
        print('b: ' + str(self.b))
    def analizar(self,dato):
        entradas = tf.placeholder("float", name='Entradas')
        datos = np.array([dato])
        uno = lambda: tf.constant(1.0)
        cero = lambda: tf.constant(0.0)

        with tf.name_scope('Pesos'):
            pesos = tf.placeholder("float", name='Pesos')
            sesgo = tf.placeholder("float", name='Sesgo')

        with tf.name_scope('Activacion'):
            activacion = tf.reduce_sum(tf.add(tf.matmul(entradas, pesos), sesgo))

        with tf.name_scope('Neurona'):
            def neurona():
                return tf.case([(tf.less(activacion, 0.0), cero)], default=uno)
    
        a = neurona()


        with tf.Session() as sess:
            x_1 = []
            out = []
            act = []
            for i in datos:
                print(i)
                j=np.array([[i]])
                print(j)
                salida, activ = sess.run([a, activacion], feed_dict={entradas:j,
                                        pesos:np.array([[self.W]]),
                                        sesgo:self.b})      
                out.append(salida)
                act.append(activ)
                print(out)
                print(act)
            x_1.append(datos[0])
            tabla_info = np.array([x_1, act, out]).transpose()
            tabla = pd.DataFrame(tabla_info, 
                         columns=['x1', 'f(x)', '~ x1'])
            print(tabla)
            return str(int(out[0]))        
            
class conjuncion():
    def __init__(self):
        self.entradas = 2
        self.numero_interaciones = 2000
        self.taza_aprendizaje = 0.01
        self.entrenar()
    def entrenar(self):
        x = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], np.float32) 
        y = np.array([0, 0, 1, 0], np.float32)
        y = np.reshape(y, [4,1])
         
        X = tf.placeholder(tf.float32, shape=[4, 2])
        Y = tf.placeholder(tf.float32, shape=[4, 1])
         
        self.W = tf.Variable(tf.zeros([self.entradas, 1]), tf.float32)
        B = tf.Variable(tf.zeros([1, 1]), tf.float32)
         
        yHat = tf.sigmoid( tf.add(tf.matmul(X,self.W), B) )
        err = Y - yHat
        deltaW = tf.matmul(tf.transpose(X), err ) 
        deltaB = tf.reduce_sum(err, 0)
        W_ = self.W + self.taza_aprendizaje * deltaW
        B_ = B + self.taza_aprendizaje * deltaB
        step = tf.group(self.W.assign(W_), B.assign(B_))
         
        sess = tf.Session()
        init = tf.global_variables_initializer()
        sess.run(init)
        
         
        for k in range(self.numero_interaciones):
         sess.run([step], feed_dict={X: x, Y: y})
         
        self.W = np.squeeze(sess.run(self.W))
        self.b = np.squeeze(sess.run(B))
         
        
        print('W: ' + str(self.W))
        
        print('b: ' + str(self.b))
        
        
    def analizar(self,dato1,dato2):
        entradas = tf.placeholder("float", name='Entradas')
        datos = np.array([[dato1, dato2]])
        
        uno = lambda: tf.constant(1.0)
        cero = lambda: tf.constant(0.0)
        
        with tf.name_scope('Pesos'):
            pesos = tf.placeholder("float", name='Pesos')
            sesgo = tf.placeholder("float", name='Sesgo')
        
        with tf.name_scope('Activacion'):
            activacion = tf.reduce_sum(tf.add(tf.matmul(entradas, pesos), sesgo))
        
        with tf.name_scope('Neurona'):
            def neurona():
                return tf.case([(tf.less(activacion, 0.0), cero)], default=uno)
            
            a = neurona()
        
        
        with tf.Session() as sess:
            x_1 = []
            x_2 = []
            out = []
            act = []
            for i in range(len(datos)):
                t = datos[i].reshape(1, 2)
                salida, activ = sess.run([a, activacion], feed_dict={entradas: t,
                                                pesos:np.array([[self.W[0]],[self.W[1]]]),
                                                sesgo:self.b})
                x_1.append(t[0][0])
                x_2.append(t[0][1])
                out.append(salida)
                act.append(activ)
            tabla_info = np.array([x_1, x_2, act, out]).transpose()
            tabla = pd.DataFrame(tabla_info, 
                                 columns=['x1', 'x2', 'f(x)', 'x1 ^ x2'])
        print(tabla)
        return str(int(out[0]))


#clase o
    
class disyuncion():
    def __init__(self):
        self.NUM_FEATURES = 2
        self.NUM_ITER = 2000
        self.learning_rate = 0.01
        self.entrenar()
    def entrenar(self):
        x = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], np.float32)
        y = np.array([0, 1, 1, 1], np.float32) 
        y = np.reshape(y, [4,1])
         
        X = tf.placeholder(tf.float32, shape=[4, 2])
        Y = tf.placeholder(tf.float32, shape=[4, 1])
         
        self.W = tf.Variable(tf.zeros([self.NUM_FEATURES, 1]), tf.float32)
        B = tf.Variable(tf.zeros([1, 1]), tf.float32)
         
        yHat = tf.sigmoid( tf.add(tf.matmul(X,self.W), B) )
        err = Y - yHat
        deltaW = tf.matmul(tf.transpose(X), err )
        deltaB = tf.reduce_sum(err, 0) 
        W_ = self.W + self.learning_rate * deltaW
        B_ = B + self.learning_rate * deltaB
        step = tf.group(self.W.assign(W_), B.assign(B_)) 
         
        sess = tf.Session()
        init = tf.global_variables_initializer()
        sess.run(init)
        
         
        for k in range(self.NUM_ITER):
         sess.run([step], feed_dict={X: x, Y: y})
         
        self.W = np.squeeze(sess.run(self.W))
        self.b = np.squeeze(sess.run(B))
        
        
        
        print('W: ' + str(self.W))
        
        print('b: ' + str(self.b))
        
        
    def analizar(self,dato1,dato2):
        entradas = tf.placeholder("float", name='Entradas')
        datos = np.array([[dato1, dato2]])
        
        uno = lambda: tf.constant(1.0)
        cero = lambda: tf.constant(0.0)
        
        with tf.name_scope('Pesos'):
            pesos = tf.placeholder("float", name='Pesos')
            sesgo = tf.placeholder("float", name='Sesgo')
        
        with tf.name_scope('Activacion'):
            activacion = tf.reduce_sum(tf.add(tf.matmul(entradas, pesos), sesgo))
        
        with tf.name_scope('Neurona'):
            def neurona():
                return tf.case([(tf.less(activacion, 0.0), cero)], default=uno)
            
            a = neurona()
        
        #autor:Erwin Laura cuisara
        with tf.Session() as sess:
            x_1 = []
            x_2 = []
            out = []
            act = []
            for i in range(len(datos)):
                t = datos[i].reshape(1, 2)
                salida, activ = sess.run([a, activacion], feed_dict={entradas: t,
                                                pesos:np.array([[self.W[0]],[self.W[1]]]),
                                                sesgo:self.b})
                x_1.append(t[0][0])
                x_2.append(t[0][1])
                out.append(salida)
                act.append(activ)
            tabla_info = np.array([x_1, x_2, act, out]).transpose()
            tabla = pd.DataFrame(tabla_info, 
                                 columns=['x1', 'x2', 'f(x)', 'x1 v x2'])
        print(tabla)
        return str(int(out[0]))
    
class implicacion():
    def __init__(self):
        self.NUM_FEATURES = 2
        self.NUM_ITER = 2000
        self.learning_rate = 0.01
        self.entrenar()
    def entrenar(self):
        x = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], np.float32)
        y = np.array([1, 0, 1, 1], np.float32) 
        y = np.reshape(y, [4,1]) 
         
        X = tf.placeholder(tf.float32, shape=[4, 2])
        Y = tf.placeholder(tf.float32, shape=[4, 1])
         
        self.W = tf.Variable(tf.zeros([self.NUM_FEATURES, 1]), tf.float32)
        B = tf.Variable(tf.zeros([1, 1]), tf.float32)
         
        yHat = tf.sigmoid( tf.add(tf.matmul(X,self.W), B) )
        err = Y - yHat
        deltaW = tf.matmul(tf.transpose(X), err )
        deltaB = tf.reduce_sum(err, 0) 
        W_ = self.W + self.learning_rate * deltaW
        B_ = B + self.learning_rate * deltaB
        step = tf.group(self.W.assign(W_), B.assign(B_))
         
        sess = tf.Session()
        init = tf.global_variables_initializer()
        sess.run(init)
        
         
        for k in range(self.NUM_ITER):
         sess.run([step], feed_dict={X: x, Y: y})
         
        self.W = np.squeeze(sess.run(self.W))
        self.b = np.squeeze(sess.run(B))
        
        
        
        print('W: ' + str(self.W))
        
        print('b: ' + str(self.b))
        
        
    def analizar(self,dato1,dato2):
        entradas = tf.placeholder("float", name='Entradas')
        datos = np.array([[dato1, dato2]])
        
        uno = lambda: tf.constant(1.0)
        cero = lambda: tf.constant(0.0)
        
        with tf.name_scope('Pesos'):
            pesos = tf.placeholder("float", name='Pesos')
            sesgo = tf.placeholder("float", name='Sesgo')
        
        with tf.name_scope('Activacion'):
            activacion = tf.reduce_sum(tf.add(tf.matmul(entradas, pesos), sesgo))
        
        with tf.name_scope('Neurona'):
            def neurona():
                return tf.case([(tf.less(activacion, 0.0), cero)], default=uno)
            
            a = neurona()
        
        
        with tf.Session() as sess:
            
            x_1 = []
            x_2 = []
            out = []
            act = []
            for i in range(len(datos)):
                t = datos[i].reshape(1, 2)
                salida, activ = sess.run([a, activacion], feed_dict={entradas: t,
                                                pesos:np.array([[self.W[0]],[self.W[1]]]),
                                                sesgo:self.b})
                x_1.append(t[0][0])
                x_2.append(t[0][1])
                out.append(salida)
                act.append(activ)
            tabla_info = np.array([x_1, x_2, act, out]).transpose()
            tabla = pd.DataFrame(tabla_info, 
                                 columns=['x1', 'x2', 'f(x)', 'x1 Ↄ x2'])
        print(tabla)
        return str(int(out[0]))
x=Interfaz()
#print(x.evaluar("((1^0)v~1)"))
