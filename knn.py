
from knn_aux import odleglosc, znajdz_sasiadow, wyznacz_klase,str_to_float

#do testowania 
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



# -------- KNN() -----------------------------------------------------

def knn(X,y, Z, k):
	'''
	oblicza klase dla zadanej macierzy bedacej zbiorem testowym
	na postawie funkcji zawartych w pliku knn_aux.py
	'''
	W = list()
	for z in Z:
		wi = wyznacz_klase(X, z, k)
		W.append(wi)
	return(W)
	

	
#----- Ocena jakoci podziału ----------------------------------------
	
def kroswalidacja(benchmark, k):
	'''
	algorytm dzieli zbior benchmak na k czesci
	-liczy jaki rozmoar powinien miec pojedynczy zbior dla zadeklarowanej liczby podzialow
	-losuje indeksy obserwacji ktore wpadną do pojedynczego zbioru
	-dodaje te obserwacje do jednej z czescii blokuje mozliwosc dodania jej do innej	
	'''
	dataset_final = list()
	benchmark_copy = list(benchmark)
	size = int(len(benchmark) / k) #ile elementow bedzie mial zbior
	for _ in range(k):
		fold = list()
		while len(fold) < size:
			index = randrange(len(benchmark_copy)) #losuje indeks obserwacji
			fold.append(benchmark_copy.pop(index)) #dodaje obserwacje o indeksie index do zbioru 
		dataset_final.append(fold)
	return dataset_final


print(kroswalidacja(X, 2))
len(kroswalidacja(X, 2))

print(kroswalidacja(X, 5))
len(kroswalidacja(X, 5))

#--- Accuracy 

def accuracy_metric(prawdziwe, przewidywane):
	poprawne = 0
	for i in range(len(prawdziwe)):
		if prawdziwe[i] == przewidywane[i]:
			poprawne = poprawne + 1
	return poprawne / float(len(prawdziwe)) * 100.0





