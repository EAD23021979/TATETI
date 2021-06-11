#import datetime as dt
from datetime import datetime
from io import open


time2= datetime.now()
#date1= dt.date.today()
#time1= dt.time(10, 23, 30, 4566)
time_stamp = str(time2.year) + str(time2.month)  + str(time2.day) + str(time2.hour) + str(time2.minute) + str(time2.second)


# print (time1)
# print (time2)
# print (time2.hour)
# print (time2.minute)
# print (time2.second)
print (time_stamp)

archivo_texto = open (str(time_stamp) + ".txt", "w")

#archivo_texto = open(+str(time2.hour)str(time2.minute)+str(time2.minute)+".txt", "w")


def time_stamp_file_generator (name):
	import datetime as dt
	from io import open
	time2= datetime.now()
	time_stamp = str(time2.year) + str(time2.month)  + str(time2.day) + str(time2.hour) + str(time2.minute) + str(time2.second)
	archivo_texto = open (str(name) + str(time_stamp) + ".txt", "w")
	print (archivo_texto)
	return archivo_texto

def guardar_partida ():
	
	input_user = input("Desea Guardar la partida? (Y/N) ").upper()

	if input_user == "Y":
		name= input("Con qué nombre desea grabar el archivo? ")
		time_stamp_file_generator (name)
		print("ok_file generado")
	print("arafue")
	return

guardar_partida()
