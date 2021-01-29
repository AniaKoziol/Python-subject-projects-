# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 17:15:43 2019

@author: Ania
"""
import pandas as pd 
import gc
import matplotlib.pyplot as plt
import datetime


sty19 = pd.read_csv("file:///D:/Python/pd3/dane/201901-citibike-tripdata.csv", sep = ',')
lut19 = pd.read_csv("file:///D:/Python/pd3/dane/201902-citibike-tripdata.csv", sep = ',')
mar19 = pd.read_csv("file:///D:/Python/pd3/dane/201903-citibike-tripdata.csv", sep = ',')
kwie19 = pd.read_csv("file:///D:/Python/pd3/dane/201904-citibike-tripdata.csv", sep = ',')
maj19 = pd.read_csv("file:///D:/Python/pd3/dane/201905-citibike-tripdata.csv", sep = ',')
czer19 = pd.read_csv("file:///D:/Python/pd3/dane/201906-citibike-tripdata.csv", sep = ',')
lip19 = pd.read_csv("file:///D:/Python/pd3/dane/201907-citibike-tripdata.csv", sep = ',')
sie19 = pd.read_csv("file:///D:/Python/pd3/dane/201908-citibike-tripdata.csv", sep = ',')
wrze19 = pd.read_csv("file:///D:/Python/pd3/dane/201909-citibike-tripdata.csv", sep = ',')
paz19 = pd.read_csv("file:///D:/Python/pd3/dane/201910-citibike-tripdata.csv", sep = ',')
lis19 = pd.read_csv("file:///D:/Python/pd3/dane/201911-citibike-tripdata.csv", sep = ',')
sty19['miesiac']=1 
lut19['miesiac']=2
mar19['miesiac']=3
kwie19['miesiac']=4
maj19['miesiac']=5
czer19['miesiac']=6
lip19['miesiac']=7      
sie19['miesiac']=8
wrze19['miesiac']=9
paz19['miesiac']=10
lis19['miesiac']=11   

sty19.drop_duplicates(keep=False, inplace=True)
lut19.drop_duplicates(keep=False, inplace=True)
mar19.drop_duplicates(keep=False, inplace=True)
kwie19.drop_duplicates(keep=False, inplace=True)
maj19.drop_duplicates(keep=False, inplace=True)
czer19.drop_duplicates(keep=False, inplace=True)
lip19.drop_duplicates(keep=False, inplace=True)
sie19.drop_duplicates(keep=False, inplace=True)
wrze19.drop_duplicates(keep=False, inplace=True)
paz19.drop_duplicates(keep=False, inplace=True)
lis19.drop_duplicates(keep=False, inplace=True)

dane2019 = pd.concat([sty19,lut19,mar19,kwie19,maj19,czer19,lip19,sie19,wrze19,paz19,lis19]) #19596487 

# jakis histogram 
ax = dane2019.plot(kind='bar', title ="V comp", figsize=(15, 10), legend=True, fontsize=12)
ax.set_xlabel("miesiac", fontsize=12)
ax.set_ylabel("tripduration", fontsize=12)
plt.show()


miesiace = list(dane2019.miesiac)
d = {x:miesiace.count(x) for x in miesiace}
print d


# histogram ile bylo osob z roznej plci 

list(sty19[['gender', 'bikeid']].groupby('gender').count()['bikeid'])


# rozkminka na podstawie daty jaki to dzien tygodnia
import datetime
sty19["starttime"] = pd.to_datetime(sty19["starttime"])
sty19["dzien_startu"] = sty19["starttime"].dt.day_name()
dni =[ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sty19[['gender', 'dzien_startu']].groupby('dzien_startu').count().reindex(dni) 

# obliczenie wieku osoby na rowerze 

sty19['wiek'] = 2020 - sty19['birth year']
sty19['wiek_bin'] = sty19['wiek'].apply(lambda x: (1 if x <= 25 else ( 2 if (x>25 and x <=50) else 3 )))

sty19[['wiek_bin','gender']].groupby('wiek_bin').count().gender.tolist()




#
#sty19 = pd.read_csv("file:///D:/Python/pd3/dane/201901-citibike-tripdata.csv", sep = ',')
#lip19 = pd.read_csv("file:///D:/Python/pd3/dane/201907-citibike-tripdata.csv", sep = ',')
#
#sty19["starttime"] = pd.to_datetime(sty19["starttime"])
#sty19["dzien_startu"] = sty19["starttime"].dt.day_name()
#
#lip19["starttime"] = pd.to_datetime(lip19["starttime"])
#lip19["dzien_startu"] = lip19["starttime"].dt.day_name()
#
#
#sty19['wiek'] = 2020 - sty19['birth year']
#sty19['wiek_bin'] = sty19['wiek'].apply(lambda x: (1 if x <= 25 else ( 2 if (x>25 and x <=50) else 3 )))
#lip19['wiek'] = 2020 - lip19['birth year']
#lip19['wiek_bin'] = lip19['wiek'].apply(lambda x: (1 if x <= 25 else ( 2 if (x>25 and x <=50) else 3 )))
#
#
#bike_data = sty19
#bike_data["starttime"] = pd.to_datetime(bike_data["starttime"])
#bike_data["stoptime"] = pd.to_datetime(bike_data["stoptime"])
#bike_data["hour"] = bike_data["starttime"].map(lambda x: x.hour)



