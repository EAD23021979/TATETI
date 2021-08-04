
# *************************************************
# * PROGRAMACION DE LAS MATRICES*
# *************************************************
# PARA DEBUGUERA REEPLAZA POR NADA "#DEBUGMODE 	|"

 
import datetime as dt # Para importar el modulo que maneja fecjas
import string #importo funciones para tener el abecedario en una lista.
from datetime import datetime
import random

class Tateti:
	def ficha (self,VL_numero_de_jugador):

		if VL_numero_de_jugador == "1":
			ficha = "X"
		elif VL_numero_de_jugador == "2":
			ficha = "0"
		else:
			ficha = "="
		return ficha

	def random (self,litaOpciones):
		import random
		self.lista_robot_ran = []

		#print ("ListaOpciones =",litaOpciones)

			
		for i in litaOpciones:
			if i == 'X':
				continue
			elif i == '0':
				continue
			self.lista_robot_ran.append(i)

		n = random.randint(0,int(len(self.lista_robot_ran)-1))

		self.Jugadar_Robot_Ran=self.lista_robot_ran[n]

		print ("Jugada Robot: ", self.Jugadar_Robot_Ran)
		return self.Jugadar_Robot_Ran

	def random_inteligencia_B2 (self,litaOpciones):
		
		import random
		#print ("ListaOpciones =",litaOpciones)

		self.lista_robot_ran = []

		
		
		if 'B2' in litaOpciones:
			self.Jugadar_Robot_Ran = 'B2'
			print ("Jugada Robot:", self.Jugadar_Robot_Ran)
			return self.Jugadar_Robot_Ran

		for i in litaOpciones:
			if i == 'X':
				continue
			elif i == '0':
				continue 
			elif i == '=':
				continue 
			elif '2' in i :
				continue	
			elif 'B' in i :
				continue

			self.lista_robot_ran.append(i)

		if len(self.lista_robot_ran)<=0:
			for i in litaOpciones:
			
				if i == 'X':
					continue
				elif i == '0':
					continue 
				elif i == '=':
					continue 
				self.lista_robot_ran.append(i)
		
		n = random.randint(0,int(len(self.lista_robot_ran)-1))

		self.Jugadar_Robot_Ran=self.lista_robot_ran[n]

		print ("Jugada Robot: ", self.Jugadar_Robot_Ran)
		return self.Jugadar_Robot_Ran


	def Jugar_solo_ATAQUE_J2_DEFENSA_J1 (self,ListaGanadoraf,ListaJugadorf,listaOpciones):

		Resultado = []
		if len(ListaJugadorf) == 0:
			Resultado = "RANDOM"
			#print (Resultado)
			return Resultado	


		#print ("ListaJugadorf 54", ListaJugadorf)
		#print ("len(ListaJugadorf [0] 55)", len(ListaJugadorf [0]))
		#print ("ListaJugadorf [0] 56", ListaJugadorf [0])
		#print (len(ListaJugadorf))
		if len(ListaJugadorf[0]) <= 1:
			Resultado = "RANDOM"
		#	print (Resultado)
			return Resultado
			quit ()	

		# for i in ListaJugadorf:
		# 	print ("ListaJugadorf_Random", ListaJugadorf)
		# 	a = 0
		# 	a = len(i)+a
		# 	print (a)
		# 	if a == 1:
		# 		#print ("RANDOM")
		# 		Resultado = "RANDOM"
		# 		print ("Resultado1", Resultado) 
		# 		return Resultado
		# 		quit ()

		for elemLG in ListaGanadoraf:#['A1', 'A2', 'A3']
		#	print ("Pase por aca")
			dif = []
			#Hola=[]
			#ListaJugaro2=tuple(ListaJugaro) ('A1','B1','C2')
			for elemLJ in ListaJugadorf: #A1 ('A1','B1','C2')
				if elemLJ in elemLG:
		#			print ("elemLJ_A 83" , elemLJ)
		#			print ("elemLG_A 84" , elemLG)
					dif.append(elemLJ)
		#			print ("Dif_antes de Len 86", dif)
				
					if len(dif)>=2:
						for a in elemLG:
							dif2=[]
							if a in dif:
		#						print("a", a)
								continue
		#					print ("DIF_after_1 94", dif2)	
							dif2.append(a)
		#					print("DIF2_LISTA 96", dif2)
		#					print("DIF2_1ER_ELEMENTO 97",dif2[0]) #hasta acá Perfecto

							if dif2[0] not in listaOpciones:
								Resultado = "RANDOM"
								#print ("Sale del If dif2 q no está en la lista 101", Resultado)
								continue
							
							Resultado = dif2[0]
							print("Jugada Robot: ", Resultado)
							return Resultado
				
				# Resultado = "RANDOM"
				# print ("Resultado 109, "Resultado)
				# return Resultado
		# 					print ("DIF_2",dif2)
		# 					print ("Robot_Log:", dif2[0])
		# 					quit ()
		
		Resultado = "RANDOM"
		#print ("Resultado 116", Resultado)# #print("RANDOM")
		return Resultado

	def sumar( self, a, b):
		self.c = a + b
		return self.c,a,b

	def reuperar_archivo_partida_guardada(self, archivo_x):

		from io import open
		import csv

		try:
			with open(archivo_x, newline='') as f:
				reader = csv.reader(f)
				data = list(reader)
		except Exception:
			print ("ERROR: Partida Inexistente")
			self.archivo_guardado = input("Con qué nombre grabó su partida anterior?")
			self.reuperar_archivo_partida_guardada(self.archivo_guardado)
		#print(data)

		self.Lista_user1 = list(data[0])
		self.Lista_user2 = list(data[1])
		self.lista_de_opciones_matriz = list(data[2])
		
		turno_vl = open (archivo_x, "r")
		Turno= turno_vl.readlines()[4]
		self.turno2 = int(Turno) #data[4]

		turno_vl = open (archivo_x, "r")
		VL= turno_vl.readlines()[5]
		self.VL= int(VL) #int(data[5])


		return

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

		input_user3 = input("Desea Guardar la partida? (Y/N) ").upper()

		if input_user3 == "Y":
			name= input("Con qué nombre desea grabar el archivo? ")
			nombre_archivo= self.time_stamp_file_generator (name)
			
			archivo_texto = open(nombre_archivo, "w+")

			LJ1 = self.Lista_user1
			LJ2 = self.Lista_user2
			MFE = self.lista_de_opciones_matriz
			LG = self.winall_auto_step2
			Turno = int(self.turno) # no está recuperando correctamente el valor
			VL=self.VL # no está recuperando correctamente el valor

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
		self.JV = 1
		self.partida_single_player = 2
		self.ListaJugadorf =[]
		self.ListaGanadoraf =[]
		self.Li =[]
		self.litaOpciones=[]
		self.Jugadar_Robot_Ran = []

	def input_usuario(self, msg, test_value=""):
		if self.origen == "consola":
			return input(msg)
		elif self.origen == "test":
			return test_value

	def definir_matriz(self, tamanio=3):
		if self.partida_guardada == 'Y':
		 	return
		try:
			self.VL = int(self.input_usuario("\n\nDe qué tamaño requerimos la matriz: " ))
		except Exception:
			self.VL = tamanio
		if self.VL < 3:
			self.VL = tamanio
		return

	def input_jugador(self, numero_jugador, jugada=None):
		if numero_jugador == "1":
			ficha = "X"
		elif numero_jugador == "2":
			ficha = "0"
		else:
			ficha = "="

		if self.origen == "test":
			input_user = jugada
		
		if numero_jugador == 'R':
			input_userR = self.Jugar_solo_ATAQUE_J2_DEFENSA_J1 (self.winall_auto_step2,self.Lista_user2,self.lista_de_opciones_matriz)
			#print ("ListaUser_ATAQUE 356", input_userR)
			#print ("ListaUser1 357", self.Lista_user1)
			#print ("self.lista_de_opciones_matriz 358", self.lista_de_opciones_matriz)
			#print ("ListaGanadora 359", self.winall_auto_step2)
			#print ("Input_User_1 284", input_userR)
			if input_userR == "RANDOM":
				input_userR = self.Jugar_solo_ATAQUE_J2_DEFENSA_J1 (self.winall_auto_step2,self.Lista_user1,self.lista_de_opciones_matriz)
			#	print("input_user_DEFENSA 363", input_userR)
				
				if input_userR == "RANDOM":
					input_userR = self.random_inteligencia_B2 (self.lista_de_opciones_matriz)
					#print("PC Juega RANDOM 367", input_userR)
					self.Lista_user2.append(input_userR)
					self.lista_de_opciones_matriz = [ficha if i == input_userR else i for i in self.lista_de_opciones_matriz]
					self.print_matriz(self.lista_de_opciones_matriz)
					return
				
				self.Lista_user2.append(input_userR)
				self.lista_de_opciones_matriz = [ficha if i == input_userR else i for i in self.lista_de_opciones_matriz]
				self.print_matriz(self.lista_de_opciones_matriz)
				#return input_userR
			#	print("Estoy por aca 300")

					
				termino_el_partido = self.validacion_ganadores(self.Lista_user2)
				
				if termino_el_partido == 1:
					print("GANO EL JUGADOR R [0]")
					#print (self.turno)
					#print (self.Lista_user2)
					#self.lista_de_opciones_matriz = [ficha if i == input_userR else i for i in self.lista_de_opciones_matriz]
					#self.print_matriz(self.lista_de_opciones_matriz)
				return



			else:
			#	print ("Input_User_1_dos 316", input_userR)
				#print ("Ficha", ficha)
				#ficha = "="
				#print ("Ficha", ficha)
			#	print ("Lista_user2 320", self.Lista_user2)
			#	print ("lista_de_opciones_matriz 321", self.lista_de_opciones_matriz)
				print("PC Juega: ATAQUE 322", input_userR)
				
				self.Lista_user2.append(input_userR)
				#print (self.Lista_user2)
				#print (self.Lista_user2 [0])
				#print (self.Lista_user2 [1])
				self.lista_de_opciones_matriz = ["=" if i == input_userR else i for i in self.lista_de_opciones_matriz]
				#print ("lista_de_opciones_matriz", self.lista_de_opciones_matriz)
				#print("Matriz", self.lista_de_opciones_matriz)
				#print (self.lista_de_opciones_matriz)
				self.print_matriz(self.lista_de_opciones_matriz)
				return

			


		input_user = self.input_usuario(" (s)Salvar (q) Salir  \n Elija un opción Jugador %s [%s]: " % (numero_jugador, ficha)).upper()
		
		if self.origen == "test":
			input_user = jugada
		else:
			if input_user =='S':
				self.guardar_partida()
				quit()
		pass
		

		while input_user not in self.lista_de_opciones_matriz or input_user in ("X", "0", "R"):

			input_user = self.input_usuario(" (s)Salvar (q) Salir  \n Elija un opción Válida Jugador %s [%s]: " % (numero_jugador, ficha)).upper()
			if self.origen == "test":
				input_user = jugada
			else:
				if input_user =='S':
					self.guardar_partida()
					quit()

		if input_user in self.lista_de_opciones_matriz:			
			if numero_jugador == "1":
				self.Lista_user1.append(input_user)
				termino_el_partido = self.validacion_ganadores(self.Lista_user1)
				if termino_el_partido == 1:
					print("GANO EL JUGADOR 1 [X]")
					self.lista_de_opciones_matriz = [ficha if i == input_user else i for i in self.lista_de_opciones_matriz]
					self.print_matriz(self.lista_de_opciones_matriz)
					#quit() #
					return
			elif numero_jugador == "2":
				self.Lista_user2.append(input_user)
				termino_el_partido = self.validacion_ganadores(self.Lista_user2)
				if termino_el_partido == 1:
					print("GANO EL JUGADOR 2 [0]")
					#print (self.turno)
					#print (self.Lista_user2)
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
			self.cantida_de_jugadores = 2
		else:
			self.cantida_de_jugadores = input("HOLA!! BIENVENIDO AL JUEGO!! \n\nDesea empezar una partide de ctos jugadores (1 o 2)?: ",).upper()

		# if self.cantida_de_jugadores == 1:
		# 	print ("Nueva logica para el Jugador 2")
		
		if self.origen == "test":
			self.partida_guardada = 'N'
		else:
			self.partida_guardada = input("\n\nTiene alguna partida guardada? (Y/N): ",).upper()

		while self.partida_guardada not in ('Y','N'):
			self.partida_guardada = input("Ingrese un valor valido (Y/N): ",).upper()
			continue
		
		if self.partida_guardada == 'Y':
			self.archivo_guardado = input("Con qué nombre grabó su partida anterior?")
			self.reuperar_archivo_partida_guardada(self.archivo_guardado)
		
		if self.partida_guardada == 'N':
			self.turno = 1
		else:
			self.turno = self.turno2

		
		self.inicializar_tablero()

		if self.origen == "consola":
			pass
		elif self.origen == "test":
			return self.partida_guardada == 'N'

		self.termino_el_juego = 1  # Si teRmino del juego es == 0 se terminó el juego

		while self.termino_el_juego == 1:

			self.turno = self.turno + 1
			# DEBUGMODE print ("Turno:" ,turno)
			# self.winall_auto_step2=Actualizar_lista ()
			# print ("SISMO",self.winall_auto_step2)
			# Contar_X(self.winall_auto_step2)
			# Entrada Jugardor 1
			if self.turno > (self.VL * self.VL)+1:
				print("TABLAS")
				print ("TURNO", self.turno)
				break
		
			#print ("cantida_de_jugadores", self.cantida_de_jugadores)
			if self.turno%2==0:
			  	JV = "1"
			else:
			  	if self.cantida_de_jugadores == 1:
			  		JV = 'R'
			  	else:
			  		JV = '2'
		

			#print ("JV", JV)
			self.input_jugador(JV)

			self.termino_el_partido = self.validacion_ganadores(self.Lista_user1)
			# print (termino_el_partido)
			# print ("Partido_Cerrado After F", Partido_Cerrado)
			if self.termino_el_partido == 1:
				JV=1
				fichas_f=self.ficha(str(JV))
				print("GANO EL JUGADOR %s [%s]"% (JV,fichas_f))
				break
			else:
				pass

			# Entrada Jugardor 2

			self.turno = self.turno + 1
			# DEBUGMODE print ("Turno",turno)
			# Actualizar_lista () # No entiendo porqué si actulizo la lista, cuando la toma para valider en el while lo hace con la antigua.
			# print ("EMi",self.winall_auto_step2) # Acá es donde se envidencia que la liata self.winall_auto_step2 no es la que debería ser luego de correr la función.
			if self.turno > (self.VL * self.VL)+1:
				print("TABLAS")
				print ("TURNO", self.turno)
				break

			#print ("antida_de_jugadores", self.cantida_de_jugadores)
			if self.turno%2==0:
			  	JV = "1"
			else:
			  	if self.cantida_de_jugadores == '1':
			  		JV = 'R'
			  	else:
			  		JV = '2'

			#print ("JV", JV)
			self.input_jugador(JV)

			self.termino_el_partido = self.validacion_ganadores(self.Lista_user2)
			# print (termino_el_partido)
			# print ("Partido_Cerrado After F", Partido_Cerrado)
			if self.termino_el_partido == 1:
				fichas_f=self.ficha (str(JV))
				print("GANO EL JUGADOR %s [%s]"% (JV,fichas_f))
				
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


if __name__=='__main__':
	JUGAR = Tateti()
	JUGAR.empezar()
