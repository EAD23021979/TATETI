
# *************************************************
# * PROGRAMACION DE LAS MATRICES*
# *************************************************
# PARA DEBUGUERA REEPLAZA POR NADA "#DEBUGMODE 	|"

 
import datetime as dt # Para importar el modulo que maneja fecjas
import string #importo funciones para tener el abecedario en una lista.
from datetime import datetime


class Tateti:

	def sumar( self, a, b):
		self.c = a + b
		return self.c,a,b

	def reuperar_archivo_partida_guardada(self, archivo_x):

		from io import open
		import csv


		with open(archivo_x, newline='') as f:
		    reader = csv.reader(f)
		    data = list(reader)

		#print(data)

		self.Lista_user1 = list(data[0])

		self.Lista_user2 = list(data[1])
		self.lista_de_opciones_matriz = list(data[2])
		
		

		turno_vl = open (archivo_x, "r")
		Turno= turno_vl.readlines()[4]
		self.turno = int(Turno) #data[4]

		turno_vl = open (archivo_x, "r")
		VL= turno_vl.readlines()[5]
		self.VL= int(VL) #int(data[5])


		return

		# print ("Lista_Jugador_1=",Lista_Jugador_1)
		# print ("Lista_Jugador_2=",Lista_Jugador_2)
		# print ("Matriz_Front_End=",Matriz_Front_End)
		# print ("Turno",Turno)
		# print ("VL",Turno)

		# LJ1 = self.Lista_user1
		# LJ2 = self.Lista_user2
		# MFE = self.lista_de_opciones_matriz
		# LG = self.winall_auto_step2
		# Turno = self.turno
		# VL=self.VL

	def time_stamp_file_generator (self, name):
		import datetime as dt
		from io import open
		time2= datetime.now()
		time_stamp = str(time2.year) + str(time2.month)  + str(time2.day) + str(time2.hour) + str(time2.minute) + str(time2.second)
		nombre_archivo = str(name) + str(time_stamp) + ".txt"
		archivo_texto = open (nombre_archivo, "w")
		#print ("Tu Partida se guardó con el sigueinte Nombre", nombre_archivo)
		return nombre_archivo


	def guardar_partida (self):

		input_user = input("Desea Guardar la partida? (Y/N) ").upper()

		if input_user == "Y":
			name= input("Con qué nombre desea grabar el archivo? ")
			nombre_archivo= self.time_stamp_file_generator (name)
			
			archivo_texto = open(nombre_archivo, "w+")

			LJ1 = self.Lista_user1
			LJ2 = self.Lista_user2
			MFE = self.lista_de_opciones_matriz
			LG = self.winall_auto_step2
			Turno = self.turno
			VL=self.VL

			archivo_texto.truncate()
			#archivo_texto.write("Lista_Jugador_1=(")

			for item in LJ1:
				archivo_texto.write("%s," % str(item))

			archivo_texto = open(nombre_archivo, "r+")
			archivo_texto.seek(len(archivo_texto.read())-1)
			archivo_texto.truncate()


			#archivo_texto.write("\nLista_Jugador_2=(")
			archivo_texto.write("\n")
			for item in LJ2:
			 	archivo_texto.write("%s," % str(item))

			archivo_texto = open(nombre_archivo, "r+")
			archivo_texto.seek(len(archivo_texto.read()))
			archivo_texto.truncate()


			#archivo_texto.write("\nMatriz_Front_End=(")
			archivo_texto.write("\n")
			for item in MFE:
				archivo_texto.write("%s," % str(item))

			archivo_texto = open(nombre_archivo, "r+")
			archivo_texto.seek(len(archivo_texto.read())+1) # No entiendo porque tengo que sumarle 2 si sería el fianl del file!!!
			archivo_texto.truncate()

			#archivo_texto.write("\nLista_Ganadora=(")
			archivo_texto.write("\n")
			for item in LG:
				archivo_texto.write("%s," % str(item))

			archivo_texto = open(nombre_archivo, "r+")
			archivo_texto.seek(len(archivo_texto.read())+2) # No entiendo porque tengo que sumarle 2 si sería el fianl del file!!!
			archivo_texto.truncate()

			archivo_texto.write("\n%s" % str(Turno))
			archivo_texto.write("\n%s" % str(VL))

			archivo_texto.close()

			print ("Tu Partida se guardó con el sigueinte Nombre", nombre_archivo)
			#print("Partida Guardada")
			return
		
		else:
			print ("CHAU")
			return

	def __init__(self, origen="consola"):
		self.Lista_user1 = []
		self.Lista_user2 = []
		self.Partido_Cerrado = 0
		self.VL = 0
		self.lista_de_opciones_matriz = []
		self.winall_auto_step2 = []
		self.origen = origen
		self.turno = 1
		self.partida_guardada = 'N'

	def input_usuario(self, msg, test_value=""):
		if self.origen == "consola":
			return input(msg)
		elif self.origen == "test":
			return test_value

	def definir_matriz(self, tamanio=3):
		if self.partida_guardada == 'Y':
		 	return
		try:
			self.VL = int(self.input_usuario("De qué tamaño requerimos la matriz: " ))
		except Exception:
			self.VL = tamanio
		if self.VL < 3:
			self.VL = tamanio
		return

	def input_jugador(self, numero_jugador, jugada=None):
		if numero_jugador == "1":
			ficha = "X"
		else:
			ficha = "0"
		if self.origen == "test":
			input_user = jugada
		
		if self.turno%2==0:
		 	numero_jugador = "1"
		 	ficha = "X"
		else:
		 	numero_jugador= "2"
		 	ficha = "0"

		input_user = self.input_usuario(" (s) para salvar el juego \n Elija un opción Jugador %s [%s]: " % (numero_jugador, ficha)).upper()
		#Ver dónde poner este IF para Guardar y cerrar el juego	
		if input_user =='S':
			self.guardar_partida()
			quit()
		pass
		

		while input_user not in self.lista_de_opciones_matriz or input_user in ("X", "0"):

			input_user = self.input_usuario(" (s) para salvar el juego \n Elija un opción Válida Jugador %s [%s]: " % (numero_jugador, ficha)).upper()
			if input_user =='S':
				self.guardar_partida()
				quit()
			pass

		if input_user in self.lista_de_opciones_matriz:			
			if numero_jugador == "1":
				self.Lista_user1.append(input_user)
				termino_el_partido = self.validacion_ganadores(self.Lista_user1)
				if termino_el_partido == 1:
					print("GANO EL JUGADOR 1 [X]")
					self.lista_de_opciones_matriz = [ficha if i == input_user else i for i in self.lista_de_opciones_matriz]
					self.print_matriz(self.lista_de_opciones_matriz)
					quit() #
					return
			else:
				self.Lista_user2.append(input_user)
				termino_el_partido = self.validacion_ganadores(self.Lista_user2)
				if termino_el_partido == 1:
					print("GANO EL JUGADOR 2 [0]")
					print (self.turno)
					print (self.Lista_user2)
					self.lista_de_opciones_matriz = [ficha if i == input_user else i for i in self.lista_de_opciones_matriz]
					self.print_matriz(self.lista_de_opciones_matriz)	
					return
			
			self.lista_de_opciones_matriz = [ficha if i == input_user else i for i in self.lista_de_opciones_matriz]
			# print(self.lista_de_opciones_matriz)
			self.print_matriz(self.lista_de_opciones_matriz)
		# DEBUGMODE print ("Lista_user1: ", Lista_user1)
		# DEBUGMODE print ("Lista_user2:", Lista_user2)

		else:
			print("Crap")

	def inicializar_tablero(self):
		self.definir_matriz()
		list_count = []
		for i in range (self.VL):
			list_count.append(i)

		self.VL1 = self.VL
		# Genera la Lista ganadora, que es una lista de listas.
		WinAll_Auto_Step1 = [] #Genera la lista de items ganadores sin agruparlos, pero en orden del 1 al n -> Ejemplo A1,A2,A3


		#Letra_ABC(0)
		for a in list_count:

			for i in range(self.VL):
				#print ("I", i)
				#print ("self.VL", self.VL)
				letra = self.Letra_ABC(a)
				WinAll_Auto_Step1.append(letra + str(i+1)) #saco la A y le meto la función. WinAll_Auto_Step1.append("A"+str(i+1))
		# for i in range(self.VL):
		# 	WinAll_Auto_Step1.append(Letra_ABC(1)+str(i+1))
		# for i in range(self.VL):
		# 	WinAll_Auto_Step1.append(Letra_ABC(2)+str(i+1))
		for a in list_count:

			for i in range(self.VL):
				#print ("I", i)
				#print ("self.VL", self.VL)
				WinAll_Auto_Step1.append(self.Letra_ABC(i)+str(a+1))


		# for i in range(self.VL):
		# 	WinAll_Auto_Step1.append(Letra_ABC(i)+str())

		for i in range(self.VL):
			WinAll_Auto_Step1.append(self.Letra_ABC(i)+str(i+1)) # Diagonal
		for i in range(self.VL):
			WinAll_Auto_Step1.append(self.Letra_ABC(2-i)+str(i+1)) # Diagonal
		# for i in range(self.VL):

		# 	WinAll_Auto_Step1.append(Letra_ABC(0+i)+str(1))
		# for i in range(self.VL):
		# 	WinAll_Auto_Step1.append(Letra_ABC(0+i)+str(2))
		# for i in range(self.VL):
		# 	WinAll_Auto_Step1.append(Letra_ABC(0+i)+str(3))

		self.winall_auto_step2=[] #Agrupa los resultados en elemento de 3 componentes -> ['A1','A2','A3'],['B1','B2','B3']
		#print (len(WinAll_Auto_Step1))

		# Go -Este paso es el que genera los Segmentos de elementos agrupados de a 3 o 4 o lo que defina self.VL. Que en resumen serán los segmentos que si algun jugador agruapa lo hace ganar
		for i in range (0,len(WinAll_Auto_Step1),self.VL):
			#print(i)
			self.winall_auto_step2.append(list(WinAll_Auto_Step1[i:i+self.VL]))


		# ******************************************************************************************
		# Generar la lista de  opciones a elegir para generar la matriz
		# ******************************************************************************************

		

		if self.partida_guardada == 'Y':
			self.lista_de_opciones_matriz = self.lista_de_opciones_matriz
	
		else:
			self.lista_de_opciones_matriz = []
			for a in list_count:
				for i in range(self.VL):
					#print ("I", i)
					#print ("self.VL", self.VL)
					self.lista_de_opciones_matriz.append(self.Letra_ABC(a)+str(i+1))


		#print("Lista_de_Opciones_matri", self.lista_de_opciones_matriz)




		#*********** PRINTS PARA CONTROLAR LOS RESULTADOS ******************************
		#print(WinAll_Auto_Step1)

		#print("Lista de elementos previos a la ganadora", WinAll_Auto_Step1)
		#DEBUGMODE print("Lista de Segmentos Ganadora", self.winall_auto_step2)

		#DEBUGMODE print("Cantidad de combinaciones pata ganar", len(self.winall_auto_step2))

		# Con las siguiente 4 Linea se genera  la matriz a presentar en el front End

		self.print_matriz(self.lista_de_opciones_matriz)

		# print(" ")
		# print ("Lista Jugador 1" , Lista_user1)
		# print ("Lista Jugador 2" , Lista_user2)
		# print (" ")
		# print(len(winall))
		# print_matriz()
		# print (" ")

	def empezar(self):
		if self.origen == "test":
			self.partida_guardada = 'N'
		else:
			self.partida_guardada = input("HOLA!! BIENVENIDO AL JUEGO!! --> tiene alguna partida gudardada? (Y/N)",).upper()
		
		if self.partida_guardada == 'Y':
			self.archivo_guardado = input("Con qué nombre grabó su partida anterior?")
			self.reuperar_archivo_partida_guardada(self.archivo_guardado)

		
		self.inicializar_tablero()

		if self.origen == "consola":
			pass
		elif self.origen == "test":
			return self.partida_guardada == 'N'


		if self.partida_guardada == 'N':
			self.turno = 1

		self.termino_el_juego = 1  # Si teRmino del juego es == 0 se terminó el juego

		while self.termino_el_juego == 1:

			self.turno = self.turno + 1
			# DEBUGMODE print ("Turno:" ,turno)
			# self.winall_auto_step2=Actualizar_lista ()
			# print ("SISMO",self.winall_auto_step2)
			# Contar_X(self.winall_auto_step2)
			# Entrada Jugardor 1
			if self.turno > (self.VL * self.VL):
				print("TABLAS")
				print ("TURNO", self.turno)
				break

			self.input_jugador("1")

			self.termino_el_partido = self.validacion_ganadores(self.Lista_user1)
			# print (termino_el_partido)
			# print ("Partido_Cerrado After F", Partido_Cerrado)
			if self.termino_el_partido == 1:
				#print("GANO EL JUGADOR 1 [A]")
				break
			else:
				pass

			# Entrada Jugardor 2

			self.turno = self.turno + 1
			# DEBUGMODE print ("Turno",turno)
			# Actualizar_lista () # No entiendo porqué si actulizo la lista, cuando la toma para valider en el while lo hace con la antigua.
			# print ("EMi",self.winall_auto_step2) # Acá es donde se envidencia que la liata self.winall_auto_step2 no es la que debería ser luego de correr la función.
			if self.turno > (self.VL * self.VL):
				print("TABLAS")
				print ("TURNO", self.turno)
				break

			self.input_jugador("2")

			self.termino_el_partido = self.validacion_ganadores(self.Lista_user2)
			# print (termino_el_partido)
			# print ("Partido_Cerrado After F", Partido_Cerrado)
			if self.termino_el_partido == 1:
				#print("GANO EL JUGADOR 2 [0]")
				break

		print("FIN DEL JUEGO")

	@staticmethod
	def Letra_ABC(posicion):
		abecedario = list(string.ascii_uppercase)
		letra = abecedario[posicion]
		return letra

	def print_matriz(self, lista):
		
		

		print ("******"*self.VL)
		
		Matriz_front_end= []

		for i in range (0,len(lista),self.VL):
			Matriz_front_end.append(list(lista[i:i+self.VL]))
		
		# if self.partida_guardada == 'Y':

		# 	Matriz_front_end = self.lista_de_opciones_matriz
		
		
		for i in Matriz_front_end:
			print (i)

		print ("******"*self.VL)
		print (self.turno)
		return Matriz_front_end

	def validacion_ganadores(self, listaPlayer): #Esta función valida si la lista de alguno de los ganadore es GANADORA

		Partido_Cerrado = 0

		for a in self.winall_auto_step2:
			comparando = []
			#DEBUGMODE print ("Fun_self.winall_auto_step2", self.winall_auto_step2)
			#DEBUGMODE print ("FunC(a)", a)
			if len(comparando) <= self.VL:

				for i in listaPlayer:
					if i in a:
						#DEBUGMODE print ("ListaJugador a comparar",listaPlayer)# Lista_user1:  ['B2', 'A2', 'B1']
						#DEBUGMODE print ("Lista que compara", a) #a=['A2', 'B2', 'C2']
						comparando.append(i)
						if len(comparando) >= self.VL:
							#DEBUGMODE print ("HAY GANADOR querido")
							#DEBUGMODE print ("Partido_Cerrado Func", Partido_Cerrado)
							return 1

					else:
						if len(comparando) >= self.VL:
							break

			else:
				break

		#print ("out of loop")


#JUGAR = Tateti()

#JUGAR.empezar()