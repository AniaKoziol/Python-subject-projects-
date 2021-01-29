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


kols = ["StID","StName","StLat","StLong"]
stat = pd.read_csv("stat.csv.zip",
                   index_col=0)


ramki = "ramki_final"
pliki = os.listdir(os.path.join('.',ramki))
pliki.sort()
# p = pliki[4]

########################3
d = {"Miesiac": [],"Rok": [],"In": [],"Out": [],
     "StName": [],"StLat": [],"StLong": []}
wyniki = pd.DataFrame(d)

# p = pliki[0]
for p in pliki:
    ramka = os.path.join(ramki,p)
    print("Processing", ramka)
    bikes = pd.read_csv(ramka,
                        usecols=[3,7])
    bikes.columns= ["StartID","EndID"]
    wiersz = stat.copy()
    wiersz["In"] = bikes.groupby("EndID").size()
    wiersz.In = wiersz.In.fillna(0)
    wiersz.In = wiersz.In.astype(int)
    wiersz["Out"]= bikes.groupby("StartID").size()
    wiersz.Out = wiersz.Out.fillna(0)
    wiersz.Out = wiersz.Out.astype(int)
    wiersz["Both"] = wiersz.In + wiersz.Out
    
    wiersz["Miesiac"] = int(p[4:6])
    wiersz["Rok"] = int(p[0:4])
    wiersz = wiersz[["Miesiac","Rok","In","Out",
                     "StName","StLat","StLong"]]
    wyniki = wyniki.append(wiersz)

wyniki
wyniki.In = wyniki.In.astype(int)
wyniki.Out = wyniki.Out.astype(int)
wyniki["Both"] = wyniki.In + wyniki.Out
wyniki.Both=wyniki.Both.astype(int)
wyniki.Miesiac=wyniki.Miesiac.astype(int)
wyniki.Rok = wyniki.Rok.astype(int)

wyniki = wyniki[["Miesiac","Rok","In","Out","Both",
                 "StName","StLat","StLong"]]
wyniki.sort_values(by=["Miesiac","Rok"])
wyniki.to_csv("heat_ramka_stacji.csv.zip")


# wczytywanie
wr = pd.read_csv("heat_ramka_stacji.csv.zip",index_col=0)
hed = wr.head()

wr.shape[0]/1095

