Algoritmo INICIO_VELOCIDADES
	Escribir "Ingrese velocidad vehiculo 1 en km/h"
	Leer v1
	Escribir "Ingrese velocidad vehiculo 2 en km/h"
	Leer v2
	Escribir "Ingrese ditancia entre los coches en km"
	Leer d1
	si v1>v2 Entonces
		tiempo<-d1/v1
	SiNo
		tiempo<-d1/v2
	FinSi
	Escribir "El tiempo (min) que tardara en alcanzar al coche es de: ", tiempo*60 
FinAlgoritmo
