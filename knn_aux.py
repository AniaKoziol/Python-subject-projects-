import numpy as np
from random import seed
from random import randrange
from math import sqrt
import random

#macierze do testów

X = [[2.7810836,2.550537003],
	[1.465489372,2.362125076],
	[3.396561688,4.400293529],
	[1.38807019,1.850220317],
	[3.06407232,3.005305973],
	[7.627531214,2.759262235],
	[5.332441248,2.088626775],
	[6.922596716,1.77106367],
	[8.675418651,-0.242068655],
	[7.673756466,3.508563011]]


Z = [[2,0.56,0],
	[1.4,5.9,1],
	[2.09,3.47,0],
	[4,1,1]]


y = [0,0,0,0,0,1,1,1,1,1]

#--------implementacja odleglosci euklidesowej miedzy dwoma wektorami-------
#--------wyspecyfikowana tak, by użyć w dalszych funkcjach------------------

def odleglosc(punkt1, punkt2):
	'''
	funkcja przyjmuje dwa punty
	oblicza odleglosc euklidesowa 
	nie uwzgledniajac ostatnich wspolrzednych
	(to beda klasy obserwacji)
	'''	
	distance = 0.0
	for i in range(len(punkt1)-1):
		distance += (punkt1[i] - punkt2[i])**2
	return np.sqrt(distance)



## ------------ implementacja znalezienia k sasiadow ------------------------


def znajdz_sasiadow(X, y, z,k):
	'''
	lizymy odleglosc kazdego punktu Xi z z
    sorujemy  wzgl odleglosci
	wybieramy k najblizszych punktow i ich klasy 
	'''
	X = np.hstack((X,list(map(lambda el: [el],y))))
	odleglosci = list()
	for x in X:
		dist = odleglosc(z, x)
		odleglosci.append((x, dist))
	odleglosci.sort(key=lambda tup: tup[1])
	najblizsi = list()
	for i in range(2):
		najblizsi.append(odleglosci[i][0])
	return najblizsi

#------------ wyznaczenie klasy dla danej obserwacji -----------------
		
def wyznacz_klase(X, z, k):
	'''
	dla macierzy najblizszych sasiadow,wyliczamy etykiete 
	moda jesli mozna ja wyznaczyc jednoznacznie 
	losowa wartosc jesli nie
	'''	
	najblizszi_sasiedzi = znajdz_sasiadow(X, y,z, k)
	klasy = [row[-1] for row in najblizszi_sasiedzi]
	if len(set(klasy)) != len(klasy):		
		wi = max(set(klasy), key=klasy.count)
		wi = int(wi)
	else:
		wi = random.choice(klasy)
		wi = int(wi)		
	return wi


#---------- inne przydatne funkcje do obliczania knn -----------------------
	
def str_to_float(dane, x):
	'''
	zamienia str na float
	'''
	for i in dane:
		i[x] = float(i[x].strip())

#------





