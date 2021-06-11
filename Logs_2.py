from io import open
from datetime import datetime
#Listas a capturar


def time_stamp_file_generator (name):
	import datetime as dt
	from io import open
	time2= datetime.now()
	time_stamp = str(time2.year) + str(time2.month)  + str(time2.day) + str(time2.hour) + str(time2.minute) + str(time2.second)
	nombre_archivo = str(name) + str(time_stamp) + ".txt"
	archivo_texto = open (nombre_archivo, "w")
	print (nombre_archivo)
	return nombre_archivo


Turno = 9
Lista_Jugador_1 = ('A1','A3','B2','C1','E2')
Lista_Jugador_2 = ('A2','B1','B3','B2')
Matriz_Front_End = ('A1','A2','A3','B1','B2','B3','C1','C2')
Lista_Ganadora  = ('Ganar','Ganar','Ganar','pila')

nombre_archivo = time_stamp_file_generator('EAD')
print(nombre_archivo)

archivo_texto = open(nombre_archivo, "w+")

LJ1 = Lista_Jugador_1
LJ2 = Lista_Jugador_2 
MFE = Matriz_Front_End
LG = Lista_Ganadora
Turno = Turno

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


archivo_texto.close()

print("Partida Guardada")