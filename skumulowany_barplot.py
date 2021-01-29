import pandas as pd
import os
import psutil
import numpy as np
import seaborn as sns
def usage():
    process = psutil.Process(os.getpid())
    return process.memory_info()[0] / float(2 ** 20)


usage()


print(os.getcwd())
os.chdir("/home/pawelwicherek/Py/pd3")
stat = pd.read_csv("stat.csv.zip")

ramki = "ramki_final"
pliki = os.listdir(os.path.join('.',ramki))
pliki.sort()


############################
przejazdy = pd.DataFrame(columns=["Miesiac","Rok",
                       "LpK","LpM",
                       "LpN"])

print(usage())
for p in pliki:
    ramka = os.path.join(".",ramki,p)
    print("Processing",ramka)
    bikes = pd.read_csv(ramka,usecols=[14])
    bikes.columns = ["Gender"]
    print("> Current memory used:  ", usage())
    (Miesiac,Rok) = (p[4:6],p[0:4])    
    (LpN,LpM,LpK) = tuple(bikes.groupby("Gender").size())
    wiersz = pd.DataFrame({"Miesiac": Miesiac,
                           "Rok": [Rok], 
                           "LpK": [LpK], 
                           "LpM": [LpM], 
                           "LpN": [LpN]})
    przejazdy = przejazdy.append(wiersz)
    del bikes
    del wiersz
print("Done!")


print(przejazdy)
przejazdy = przejazdy.sort_values(by=["Rok","Miesiac"],
                ascending=[True,True])\
    .reset_index(drop=True)

przejazdy.to_csv("skumulowany_barplot.csv.zip",index=False)


przejazdy_read = pd.read_csv("skumulowany_barplot.csv.zip")
przejazdy_read




