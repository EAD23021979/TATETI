from io import open
import csv


with open('asdf2021610225153.txt', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)

Lista_Jugador_1 = list(data[0])

Lista_Jugador_2 = list(data[1])
Matriz_Front_End= list(data[2])

turno_vl = open ('asdf2021610225153.txt', "r")
Turno= turno_vl.readlines()[4]

turno_vl = open ('asdf2021610225153.txt', "r")
VL= turno_vl.readlines()[5]


print ("Lista_Jugador_1=",Lista_Jugador_1)
print ("Lista_Jugador_2=",Lista_Jugador_2)
print ("Matriz_Front_End=",Matriz_Front_End)
print ("Turno",Turno)
print ("VL",VL)


# import numpy as np
# data = np.genfromtxt ('mark.txt', delimiter=',')
# print( data)
# for i in data:
# 	print()


# Try this, using the csv module and its reader() method:

# import csv

# f = open('file.csv')

# the_data = list(csv.reader(f, delimiter r'\t'))[1:]