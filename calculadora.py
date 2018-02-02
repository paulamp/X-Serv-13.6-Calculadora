#!/usr/bin/python3
import sys 
operando = sys.argv[1]
if operando == 'sumar':
	sumando = float(sys.argv[2]) + float(sys.argv[3])
	print(sys.argv[2],"+",sys.argv[3],"=",sumando)
elif operando == 'restar':
	restando = float(sys.argv[2]) - float(sys.argv[3])
	print(sys.argv[2],"-",sys.argv[3],"=",restando)
elif operando == 'multiplicar':
	multi = float(sys.argv[2]) * float(sys.argv[3])
	print(sys.argv[2],"x",sys.argv[3],"=",multi)
elif operando == 'dividir':
	try:
		division = float(sys.argv[2]) / float(sys.argv[3])
		print(sys.argv[2],"/",sys.argv[3],"=",division)
	except ZeroDivisionError:
		print("NO ES POSIBLE DIVIDIR ENTRE CERO")
else:
	print("No existe: ",operando, "como operando")


