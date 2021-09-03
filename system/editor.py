# Codigo desenvolvido por Luiz Flores 22/03/2021 as 15:05
import math
import os
import subprocess

main_path = "./NACA0012_18DEGREES"

for root, subFolder, filename in os.walk(main_path):

	for folder in subFolder:
	
		print(folder)

def angulo(a, element):
	pi = 3.14159265

	param = a

	aux1 = math.cos((param*pi)/180.0)
	aux2 = math.sin((param*pi)/180.0)

	if element == 1:
		return aux2

	else:
		return aux1

#def abrir():



with open('controlDict', 'r+') as f:
	lines = [x.strip() for x in f.readlines()]
        
	liftDir = []
        
	dragDir = []
        
	s = 1
        
	c = 2

	ang = int(input("Alpha in degrees: "))
        
	aux1 = angulo(ang,s)
        
	aux2 = angulo(ang,c)
        
	l = ('liftDir ({} {} 0);'.format(-aux1, aux2))
        
	d = ('dragDir ({} {} 0);'.format(aux2, aux1))

	lines[80] = l

	lines[81] = d

	u = lines[0]

	print("Completed")

	if lines[0] == str(u):

		with open('controlDict', 'w') as f:
                        
			f.write('')

	#print(lines)

	with open('controlDict', 'r+') as f:

		for i in range(0,len(lines)):
			f.write(lines[i]+"\n")
			
#abrir()
