#!/usr/bin/env python
# coding: utf-8

# # PadPy praca domowa nr 2
# ## Anna Kozioł
# 
# Celem pracy domowej było wykonanie zapytań w języku sql i ich interpretacja oraz wywołania identycznych zapytań przy użyciu pakietu Pandas. 
#  Dla każdego z otrzymanych wyników dokonano sprawdzenia, czy  wyniki są tożsame oraz zapytanie 'pandas' jest on klasy DataFrame. Dodatkowo dokonano porówania czasów wykonania poszczególnych obliczeń. Podsumowanie zawiera wnioski z analizy.
# 
# ### 1. Wczytanie odpowiednich zbiorów danych, metod wyśwetlania oraz utworzenie tymczasowej bazy danych

# In[200]:


import pandas as pd
import numpy as np
from IPython.display import display, HTML
import sqlite3
import tempfile
import os
import timeit

CSS = """
.output {
    flex-direction: row;
}
"""

HTML('<style>{}</style>'.format(CSS))


# In[201]:


#pliki danych

badges = pd.read_csv("file:///D:/Python/pd2/Badges.txt", sep = ",")
comments = pd.read_csv("file:///D:/Python/pd2/Comments.txt", sep = ",")
postLinks = pd.read_csv("file:///D:/Python/pd2/PostLinks.txt", sep = ",")
posts = pd.read_csv("file:///D:/Python/pd2/Posts.txt", sep = ",")
tags = pd.read_csv("file:///D:/Python/pd2/Tags.txt", sep = ",")
users = pd.read_csv("file:///D:/Python/pd2/Users.txt", sep = ",")
votes = pd.read_csv("file:///D:/Python/pd2/Votes.txt", sep = ",")

baza = os.path.join(tempfile.mkdtemp(), "baza.db")
if os.path.isfile(baza):
    os.remove(baza)
conn = sqlite3.connect(baza)

badges.to_sql("badges", conn)
comments.to_sql("comments", conn)
postLinks.to_sql("postLinks", conn)
posts.to_sql("posts", conn)
tags.to_sql("tags", conn)
users.to_sql("users", conn)
votes.to_sql("votes", conn)


# ### Zapytanie 1
# 
# Zapytanie zwraca dla każdego postu otrzymał ile głosów _'UpMod'_ określone jako UpVotes. 

# In[198]:


#sql

start1 = timeit.default_timer()

df_sgl_1 = pd.read_sql_query("SELECT PostId, COUNT(*) AS UpVotes                              FROM Votes WHERE VoteTypeId=2 GROUP BY PostId", conn)

t1_sql = timeit.default_timer() - start1

#pandas 

start2 = timeit.default_timer()

x = votes[votes.VoteTypeId == 2][['PostId']].groupby('PostId').size()
df_pd_1 = x.to_frame().reset_index().rename(columns= {0: 'UpVotes'})

t1_pd = timeit.default_timer() - start2

#wynik

display(df_pd_1.head(10))
display(df_sgl_1.head(10))


# * sprawdzenie poprawności

# In[92]:


df_sgl_1.equals(df_pd_1)


# * sprawdzenie typu
# 

# In[54]:


type(df_pd_1)


# * porównanie czasów

# In[199]:


print('sql: ' + str(t1_sql) + 's')
print('pd:  ' + str(t1_pd) + 's')


# ### Zapytanie 2 
# Zapytanie zwraca Tytuł, Score, licznik wyświetleń (ViewCount),licznik ulubień (FavoriteCount) dla postów,
# które są pytaniami oraz mają ponad 10.000 ViewCount i ponad 25 FavoriteCount.

# In[202]:


#sql

start1 = timeit.default_timer()

df_sgl_2 = pd.read_sql_query("SELECT Title, Score, ViewCount, FavoriteCount                           FROM Posts WHERE PostTypeId=1 AND FavoriteCount >= 25 AND ViewCount>=10000", conn)
t2_sql = timeit.default_timer() - start1

#pandas 
start2 = timeit.default_timer()

df_pd_2 = posts[["Title", "Score", "ViewCount", "FavoriteCount"]][(posts.PostTypeId == 1) & (posts.FavoriteCount >= 25) & (posts.ViewCount>=10000)]         .reset_index(drop= True)

t2_pd = timeit.default_timer() - start2
#wyniki

display(df_pd_2.head(10))
display(df_sgl_2.head(10))


# * sprawdzenie poprawności

# In[91]:


df_sgl_2.equals(df_pd_2)


# * sprawdzenie typu

# In[53]:


type(df_pd_2)


# * porówanie czasów

# In[203]:


print('sql: ' + str(t2_sql) + 's')
print('pd:  ' + str(t2_pd) + 's')


# ### Zapytanie 3 
# 
# Zapytanie zwraca nazwę Tagu, liczbę występowania (Count), Id autora, lokalizację oraz nick (DisplayName) 
# dla autorów innych niż o Id = -1 w porządku malejącym względem liczby Count.
# 
# 

# In[210]:


#sql

start1 = timeit.default_timer()

df_sgl_3 = pd.read_sql_query("SELECT Tags.TagName, Tags.Count, Posts.OwnerUserId,                             Users.Location, Users.DisplayName                              FROM Tags                              JOIN Posts ON Posts.Id=Tags.WikiPostId                              JOIN Users ON Users.AccountId=Posts.OwnerUserId                              WHERE OwnerUserId != -1                             ORDER BY Count DESC", conn)
t3_sql = timeit.default_timer() - start1

#pandas 
start2 = timeit.default_timer()

temp1 = pd.merge(tags,posts, how = 'inner', left_on = 'WikiPostId', right_on= 'Id' )
temp2=  pd.merge(temp1,users, how = 'inner', left_on = 'OwnerUserId', right_on= 'AccountId' )
df_pd_3 = temp2[temp2.OwnerUserId != -1].sort_values("Count", ascending=[False])[["TagName","Count", "OwnerUserId", "Location", "DisplayName"]]        .reset_index(drop = True)
t3_pd = timeit.default_timer() - start2

#wyniki

display(df_pd_3.head(10))
display(df_sgl_3.head(10))


# * sprawdzenie poprawności

# In[89]:


df_sgl_3.equals(df_pd_3)


# * sprawdzenie typu

# In[65]:


type(df_pd_3)


# * porównanie czasów

# In[211]:


print('sql: ' + str(t3_sql) + 's')
print('pd:  ' + str(t3_pd) + 's')


# ### Zapytanie 4 
# 
# Zapytanie zwraca tytuł postu oraz liczbę powiązanych postów (RelatedPostId) określoną jako NumLinks dla postów które są pytaniem w porządku malejącym względem NumLinks.

# In[ ]:





# In[207]:


#sql
start1 = timeit.default_timer()

df_sgl_4 = pd.read_sql_query("SELECT Posts.Title, RelatedTab.NumLinks FROM                             (SELECT RelatedPostId AS PostId, COUNT(*) AS NumLinks                             FROM PostLinks GROUP BY RelatedPostId) AS RelatedTab                             JOIN Posts ON RelatedTab.PostId=Posts.Id                             WHERE Posts.PostTypeId=1                             ORDER BY NumLinks DESC", conn)
t4_sql = timeit.default_timer() - start1


#pandas

start2 = timeit.default_timer()

RelatedTab_temp = postLinks.groupby('RelatedPostId').size()
RelatedTab_temp = RelatedTab_temp.to_frame().reset_index()
RelatedTab = RelatedTab_temp.rename(columns = {'RelatedPostId': 'PostId', 0: 'NumLinks'})
posts_temp = posts[posts.PostTypeId == 1]
df_pd_4 = pd.merge(RelatedTab, posts_temp, how = 'inner', right_on ='Id', left_on = 'PostId' )         .sort_values("NumLinks", ascending=[False],kind= 'mergesort')[['Title', 'NumLinks']].reset_index(drop = True)
t4_pd = timeit.default_timer() - start2

#wyniki

display(df_pd_4.head(10))
display(df_sgl_4.head(10))


# * poprawność wyników

# In[88]:


df_sgl_5.equals(df_pd_5)


# * sprawdzenie typu

# In[51]:


type(df_pd_4)


# * porównanie czasów

# In[208]:


print('sql: ' + str(t4_sql) + 's')
print('pd:  ' + str(t4_pd) + 's')


# ### Zapytanie 5 
# 
# Zapytanie zwraca Id Postu liczbę głosów 'za' _(UpMod)_ określonych jako _'UpVotes'_ dla postów będących pytaniem w porządku malejącym względem UpVotes. 

# In[212]:


#sql
start1 = timeit.default_timer()
df_sgl_5 = pd.read_sql_query("SELECT UpVotesTab.*, Posts.Title FROM                             (                             SELECT PostId, COUNT(*) AS UpVotes FROM Votes WHERE VoteTypeId=2 GROUP BY PostId                             ) AS UpVotesTab                             JOIN Posts ON UpVotesTab.PostId=Posts.Id                             WHERE Posts.PostTypeId=1                             ORDER BY UpVotesTab.UpVotes DESC", conn)
t5_sql = timeit.default_timer() - start1

#pandas

start2 = timeit.default_timer()

UpVotesTab = votes[votes.VoteTypeId == 2 ].groupby('PostId').size()
UpVotesTab = UpVotesTab.to_frame().reset_index().rename(columns = { 0: 'UpVotes'})
posts_temp = posts[posts.PostTypeId == 1][['Title', 'Id']]
df_pd_5 = pd.merge(UpVotesTab, posts_temp, right_on = 'Id', left_on = 'PostId', how = 'inner' )          .sort_values('UpVotes', ascending=False,kind= 'mergesort').drop('Id', axis='columns').reset_index(drop = True)

t5_pd = timeit.default_timer() - start2
#wyniki

display(df_pd_5.head(10))
display(df_sgl_5.head(10))


# * porównanie wyników 

# In[84]:


df_sgl_5.equals(df_pd_5)


# * sprawdzenie typu

# In[85]:


type(df_pd_5)


# * porównanie czasów 

# In[214]:


print('sql: ' + str(t5_sql) + 's')
print('pd:  ' + str(t5_pd) + 's')


# In[ ]:





# In[ ]:





# ### Zapytanie 6 
# 
# Zapytanie dla każdego Id postu który otrzymał głos 'za' ('UpMod') zwraca liczbę tych głosów oraz liczbę głosów 'przeciw' (DownMod). Gdy nie ma informacji o głosach 'DownMod', zwracane jest 0.
# 

# In[229]:


#sql

start1 = timeit.default_timer()
df_sgl_6 = pd.read_sql_query("SELECT UpVotesTab.PostId, UpVotesTab.UpVotes, IFNULL(DownVotesTab.DownVotes, 0) AS DownVotes                             FROM                             (                            SELECT PostId, COUNT(*) AS UpVotes FROM Votes                            WHERE VoteTypeId=2 GROUP BY PostId                            ) AS UpVotesTab                            LEFT JOIN                            (                            SELECT PostId, COUNT(*) AS DownVotes FROM Votes                            WHERE VoteTypeId=3 GROUP BY PostId                            ) AS DownVotesTab                            ON UpVotesTab.PostId=DownVotesTab.PostId", conn)
                            
t6_sql = timeit.default_timer() - start1

#pandas

start2 = timeit.default_timer()

UpVotesTab_temp = votes[votes.VoteTypeId == 2].groupby('PostId').size()
UpVotesTab = UpVotesTab_temp.to_frame().reset_index().rename(columns = { 0: 'UpVotes'})

DownVotesTab_temp = votes[votes.VoteTypeId == 3].groupby('PostId').size()
DownVotesTab = DownVotesTab_temp.to_frame().reset_index().rename(columns = { 0: 'DownVotes'})

df_pd_6 = pd.merge(UpVotesTab,DownVotesTab, how = 'left', on = 'PostId')
df_pd_6['DownVotes'] = df_pd_6['DownVotes'].replace(np.nan, 0)
df_pd_6['DownVotes'] = df_pd_6['DownVotes'].astype(np.int64)

t6_pd = timeit.default_timer() - start2

# wyniki 

display(df_pd_6.head(10))
display(df_sgl_6.head(10))


# * porównanie wyników

# In[224]:



df_sgl_6.equals(df_pd_6) 


# * sprawdzenie typu

# In[182]:


type(df_pd_6)


# * porównanie czasów

# In[225]:


print('sql: ' + str(t6_sql) + 's')
print('pd:  ' + str(t6_pd) + 's')


# ### Zapytanie 7
# 
# Zapytanie zwraca Id postu oraz różnicę w ilości głosów 'za' (UpMod) i 'przeciw' (DownMod).
# 

# In[226]:


#sql

start1 = timeit.default_timer()
df_sgl_7 = pd.read_sql_query("SELECT PostId, UpVotes-DownVotes AS Votes FROM (                             SELECT UpVotesTab.PostId, UpVotesTab.UpVotes, IFNULL(DownVotesTab.DownVotes, 0) AS DownVotes                            FROM                            (                            SELECT PostId, COUNT(*) AS UpVotes FROM Votes                            WHERE VoteTypeId=2 GROUP BY PostId                            ) AS UpVotesTab                            LEFT JOIN                            (                            SELECT PostId, COUNT(*) AS DownVotes                            FROM Votes WHERE VoteTypeId=3 GROUP BY PostId                            ) AS DownVotesTab                            ON UpVotesTab.PostId=DownVotesTab.PostId                            UNION                            SELECT DownVotesTab.PostId, IFNULL(UpVotesTab.UpVotes, 0) AS UpVotes, DownVotesTab.DownVotes                            FROM                            (                            SELECT PostId, COUNT(*) AS DownVotes FROM Votes                            WHERE VoteTypeId=3 GROUP BY PostId                            ) AS DownVotesTab                            LEFT JOIN                            (                            SELECT PostId, COUNT(*) AS UpVotes FROM Votes                            WHERE VoteTypeId=2 GROUP BY PostId                            ) AS UpVotesTab                            ON DownVotesTab.PostId=UpVotesTab.PostId                            )", conn)
t7_sql = timeit.default_timer() - start1
                            
#pandas

start2 = timeit.default_timer()

UpVotesTab_temp = votes[votes.VoteTypeId == 2].groupby('PostId').size()
UpVotesTab = UpVotesTab_temp.to_frame().reset_index().rename(columns = { 0: 'UpVotes'}) 
DownVotesTab_temp = votes[votes.VoteTypeId == 3].groupby('PostId').size()
DownVotesTab = DownVotesTab_temp.to_frame().reset_index().rename(columns = { 0: 'DownVotes'}) 

left = pd.merge(UpVotesTab,DownVotesTab, how = 'left', on = 'PostId' )
left2 = pd.merge(DownVotesTab,UpVotesTab, how = 'left', on = 'PostId' )
left2['UpVotes'] = left2['UpVotes'].replace(np.nan, 0)
left2['UpVotes'] = left2['UpVotes'].astype(int)


df_pd_7 = pd.concat([left,left2],sort=False).drop_duplicates()
df_pd_7['DownVotes'] = df_pd_7['DownVotes'].replace(np.nan, 0)
df_pd_7['DownVotes'] = df_pd_7['DownVotes'].astype(int)
df_pd_7['Votes'] = df_pd_7['UpVotes'] - df_pd_7['DownVotes']
df_pd_7 = df_pd_7[['PostId','Votes']].sort_values('PostId', ascending=True, kind= 'mergesort').reset_index(drop = True)

t7_pd = timeit.default_timer() - start2

#wyniki

display(df_pd_7.head(11))
display(df_sgl_7.head(11))


# * porówanie wyników

# In[179]:


df_sgl_7.equals(df_pd_7)


# * sprawdzenie typu 

# In[138]:


type(df_pd_7)


# * porównanie czasów

# In[227]:


print('sql: ' + str(t7_sql) + 's')
print('pd:  ' + str(t7_pd) + 's')


# ### Podsumowanie 
# We wszystkich przypadkach udało się uzyskać te same wyniki przy pomocy pd.read_sql_query oraz funkcji pakietu pandas.
# Wszystkie zwracane wyniki są klasy DataFrame.
# Porównanie czasów prowadzi do wniosku, iż zazwyczaj funkcje pakietu 'Pandas' są wiele szybsze, w szczególności w przypadku bardzo złożonych zapytań.
# Tylko w przypadku 4 funkcja read_sql_query okazała się minimalnie szybsza. 

# In[ ]:




