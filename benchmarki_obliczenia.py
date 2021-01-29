
import pandas as pd
import os
import psutil
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier


path = "D:/Python/pd4/zbiory_benchmarkowe/"	
pliki = os.listdir(path)	
	
#------------ DRZEWA ---------------------
AUC = list()
i=1
for p in pliki[ : : 2]:
	ramka = pd.read_csv(path + "{}".format(p), header = None)	
	ramka_label = pd.read_csv(path + "{}".format(pliki[i]), header = None)
	i = i+2
	ramka = pd.DataFrame(ramka)
	X=ramka[ramka.columns]  # Features
	y=ramka_label 
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% test
	clf=RandomForestClassifier(n_estimators=10)
	clf.fit(X_train,y_train)
	y_pred=clf.predict(X_test)
	auc = metrics.accuracy_score(y_test, y_pred)
	AUC.append(auc)
		

AUC_drzewa = pd.DataFrame(AUC)
nazwy = pd.DataFrame([p[:-9] for p in pliki[ : : 2]])
AUC_drzewa['nazwy'] = nazwy
AUC_drzewa = AUC_drzewa.rename(columns = {0: 'AUC_drzewa'})

AUC_drzewa.to_csv("D:/Python/pd4/wyniki/AUC_drzewa.csv")

#--------- LDA -----------------------------------
	
AUC_lda = list()
i=1
for p in pliki[ : : 2]:
	ramka = pd.read_csv(path + "{}".format(p), header = None)	
	ramka_label = pd.read_csv(path + "{}".format(pliki[i]), header = None)
	i = i+2
	ramka = pd.DataFrame(ramka)
	X=ramka[ramka.columns]  # Features
	y=ramka_label 
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% test
	lda = LinearDiscriminantAnalysis()
	X_lda = lda.fit_transform(X_train, y_train)	
	y_pred=lda.predict(X_test)
	auc = metrics.accuracy_score(y_test, y_pred)
	AUC_lda.append(auc)
	
	
AUC_lda = pd.DataFrame(AUC_lda)
nazwy = pd.DataFrame([p[:-9] for p in pliki[ : : 2]])
AUC_lda['nazwy'] = nazwy
AUC_lda = AUC_lda.rename(columns = {0: 'AUC_lda'})

AUC_lda.to_csv("D:/Python/pd4/wyniki/AUC_lda.csv")
	


#--------- KNN sclearn-----------------------------------
	
AUC_knn = list()
i=1
for p in pliki[ : : 2]:
	ramka = pd.read_csv(path + "{}".format(p), header = None)	
	ramka_label = pd.read_csv(path + "{}".format(pliki[i]), header = None)
	i = i+2
	ramka = pd.DataFrame(ramka)
	X=ramka[ramka.columns]  # Features
	y=ramka_label 
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% test
	knn = KNeighborsClassifier(n_neighbors= len(np.unique(ramka_label)))
	X_lda = knn.fit(X_train,y_train)
	y_pred=knn.predict(X_test)
	auc = metrics.accuracy_score(y_test, y_pred)
	AUC_knn.append(auc)
	
	
AUC_knn = pd.DataFrame(AUC_knn)
nazwy = pd.DataFrame([p[:-9] for p in pliki[ : : 2]])
AUC_knn['nazwy'] = nazwy
AUC_knn = AUC_knn.rename(columns = {0: 'AUC_knn'})

AUC_knn.to_csv("D:/Python/pd4/wyniki/AUC_knn.csv")
	

	
#-- połączenie ramek do zrobienia wykresów 

result = pd.merge(AUC_drzewa, AUC_lda, on='nazwy')
result2 = pd.merge(result, AUC_knn, on='nazwy')	

polaczone = result2[['nazwy','AUC_drzewa','AUC_lda','AUC_knn']]


polaczone.to_csv("D:/Python/pd4/wyniki/polaczone.csv")



	