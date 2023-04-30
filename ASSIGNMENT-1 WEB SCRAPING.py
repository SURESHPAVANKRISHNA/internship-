#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. python program to display all the header tags from wikipedia.org and make data frame


# In[2]:


import requests
from bs4 import BeautifulSoup


# In[5]:


page = requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[6]:


page


# In[7]:


soup = BeautifulSoup(page.content)
soup


# In[15]:


header = soup.find_all('h2',class_="mp-h2")
header


# In[43]:


import pandas as pd
df_1 = pd.DataFrame({'header_tags':header})
df_1


# In[17]:


# 2.python program to display IMDB’s Top rated 50 movies’ data (i.e. name, rating, year of release) and make data frame.


# In[18]:


response=requests.get('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc')
response


# In[19]:


Soup=BeautifulSoup(response.content)
Soup


# In[20]:


MoviesName=[]

movies=Soup.find_all("div",class_='lister-item mode-advanced')[:50]
for m in movies:
    name=m.h3.a.text
    MoviesName.append(name)
    
MoviesName


# In[21]:


Year=[]

movies=Soup.find_all("div",class_='lister-item mode-advanced')[:50]
for m in movies:
    year=m.h3.find('span',class_='lister-item-year text-muted unbold').text
    Year.append(year)

Year


# In[22]:


Rating=[]

movies=Soup.find_all("div",class_='lister-item mode-advanced')[:50]
for m in movies:
    rate=m.strong.text
    Rating.append(rate)
    
Rating


# In[23]:


Movies=pd.DataFrame({'Movie':MoviesName[:50],'Rating':Rating[:50],'Year of Release':Year[:50]},index=range(1,51))
Movies.head(50)


# In[24]:


# 3.python program to display IMDB’s Top rated 50 Indian movies’ data (i.e. name, rating, year of release) and make data frame


# In[25]:


response_1=requests.get('https://www.imdb.com/india/top-rated-indian-movies/')
response_1


# In[26]:


soup_1=BeautifulSoup(response_1.content)
soup_1


# In[32]:


movies1=soup_1.find_all('td', class_='titleColumn')

movies_Name = []

for i in movies1:
    name1=i.a.text
    movies_Name.append(name1)
    
movies_Name
    


# In[28]:


Year1=[]

for i in movies1:
    year1=i.span.text
    Year1.append(year1)
    
Year


# In[33]:


rate=soup_1.find_all('td',class_='ratingColumn imdbRating')

Rating_IMDB=[]
for r in rate:
    imdb=r.strong.text
    Rating_IMDB.append(imdb)

Rating_IMDB


# In[34]:


Data_frame2=pd.DataFrame({'Name':movies_Name[0:50],'Rating':Rating_IMDB[0:50],'Year of Release':Year[0:50]})
Data_frame2


# In[35]:


# 4. python program to display list of respected former presidents of India(i.e. Name , Term ofoffice)from https://presidentofindia.nic.in/former-presidents.htm and make data frame.


# In[36]:


request=requests.get('https://presidentofindia.nic.in/former-presidents.htm')
request


# In[37]:


soup_2=BeautifulSoup(request.content)
soup_2


# In[38]:


Presidents_of_india=[]
for i in soup_2.find_all('h3'):
    Presidents_of_india.append(i.text)
Presidents_of_india


# In[39]:


Term=[]
for i in soup_2.find_all('p')[0:14]:
    Term.append(i.text)
Term


# In[40]:


print(len(Term), len(Presidents_of_india))


# In[44]:


df_4=pd.DataFrame({'NAMES':Presidents_of_india,'Term of Office':Term})
df_4


# In[45]:


#5 Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame-
#a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
#b) Top 10 ODI Batsmen along with the records of their team andrating.
#c) Top 10 ODI bowlers along with the records of their team andrating.


# In[46]:


#a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating
info=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')


# In[47]:


soup_3=BeautifulSoup(info.content)
soup_3


# In[48]:


team=soup_3.find_all('tr',class_=('rankings-block__banner','table-body'))


# In[49]:


top10=team[0:10]


# In[50]:


data = {'Team_Name':[],'Matches': [],'Points': [],'Rating':[]}


# In[51]:


for i in top10:
    pnt=i.find_all('td',recursive=True)
    data['Team_Name'].append(i.find('span',class_='u-hide-phablet').text)
    data['Matches'].append(pnt[2].text)
    data['Points'].append(pnt[3].text)
    data['Rating'].append(pnt[4].text.replace('\n',''))


# In[52]:


MenTeam=pd.DataFrame(data,index=range(1,11))
MenTeam


# In[53]:


#b) Top 10 ODI Batsmen along with the records of their team andrating.


# In[54]:


req=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')


# In[55]:


soup_4=BeautifulSoup(req.content)
soup_4


# In[56]:


player=soup_4.find_all('tr',class_=('rankings-block__banner','table-body'))


# In[57]:


top10=player[0:10]


# In[58]:


data={'Player_Name':[],'Team_Name': [], 'Rating':[]}


# In[59]:


for i in top10:
    bat=i.find_all('td',recursive=True)
    data['Player_Name'].append(bat[1].text.replace('\n',''))
    data['Team_Name'].append(bat[2].text.replace('\n',''))
    data['Rating'].append(bat[3].text.replace('\n',''))


# In[60]:


ODIBATSMAN=pd.DataFrame(data,index=range(1,11))
ODIBATSMAN


# In[61]:


#c) Top 10 ODI bowlers along with the records of their team andrating.


# In[63]:


req_1=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')


# In[65]:


soup_5=BeautifulSoup(req.content)
soup_5


# In[66]:


bowler=soup_5.find_all('tr',class_=('rankings-block__banner','table-body'))


# In[67]:


Top10=bowler[0:10]


# In[68]:


bdata={'Player_Name':[],'Team_Name': [], 'Rating':[]}


# In[69]:


for i in Top10:
    bat=i.find_all('td',recursive=True)
    bdata['Player_Name'].append(bat[1].text.replace('\n',''))
    bdata['Team_Name'].append(bat[2].text.replace('\n',''))
    bdata['Rating'].append(bat[3].text.replace('\n',''))


# In[70]:


ODIBOWL=pd.DataFrame(bdata,index=range(1,11))
ODIBOWL


# In[72]:


#6.Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame-
#a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
#b) Top 10 women’s ODI Batting players along with the records of their team and rating.
#c) Top 10 women’s ODI all-rounder along with the records of their team and rating. 


# In[73]:


req_2=requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')


# In[74]:


soup_6=BeautifulSoup(req.content)
soup_6


# In[75]:


team=soup_6.find_all('tr',class_=('rankings-block__banner','table-body'))
top10=team[0:10]


# In[76]:


data = {'Team_Name':[],'Matches': [],'Points': [],'Rating':[]}


# In[78]:


for i in top10:
    pnt=i.find_all('td',recursive=True)
    data['Team_Name'].append(i.find('span',class_='u-hide-phablet'))
    data['Matches'].append(pnt[2].text)
    data['Points'].append(pnt[3].text)
    data['Rating'].append(pnt[4].text.strip().replace('\n',''))


# In[79]:


WomenTeam=pd.DataFrame(data,index=range(1,11))
WomenTeam


# In[80]:


# b) Top 10 women’s ODI Batting players along with the records of their team and rating.


# In[81]:


req_3=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')


# In[82]:


soup_7=BeautifulSoup(req.content)
soup_7


# In[83]:


player=soup_7.find_all('tr',class_=('rankings-block__banner','table-body'))
top10=player[0:10]


# In[84]:


data={'Player_Name':[],'Team_Name': [], 'Rating':[]}


# In[85]:


for i in top10:
    bat=i.find_all('td',recursive=True)
    data['Player_Name'].append(bat[1].text.replace('\n',''))
    data['Team_Name'].append(bat[2].text.replace('\n',''))
    data['Rating'].append(bat[3].text.replace('\n',''))


# In[86]:


womens_batting=pd.DataFrame(data,index=range(1,11))  
womens_batting


# In[87]:


#c) Top 10 women’s ODI all-rounder along with the records of their team and rating.


# In[88]:


req_4=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')


# In[89]:


soup_8=BeautifulSoup(req.content)
soup_8


# In[90]:


player=soup_8.find_all('tr',class_=('rankings-block__banner','table-body'))
top10=player[0:10]


# In[91]:


data={'Player_Name':[],'Team_Name': [], 'Rating':[]}


# In[92]:


for i in top10:
    bat=i.find_all('td',recursive=True)
    data['Player_Name'].append(bat[1].text.replace('\n',''))
    data['Team_Name'].append(bat[2].text.replace('\n',''))
    data['Rating'].append(bat[3].text.replace('\n',''))


# In[93]:


women_allrounder=pd.DataFrame(data,index=range(1,11))
women_allrounder


# In[ ]:





# In[140]:


#7. python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world andmake data frame-
#i) Headline
#ii) Time
#iii) News Link


# In[16]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[4]:


page_13 = requests.get('https://www.cnbc.com/world/?region=world')
page_13


# In[5]:


news=BeautifulSoup(page_13.content)
news


# In[18]:


Headline=[]
for i in news.find_all('div',class_='RiverHeadline-headline RiverHeadline-hasThumbnail')[0:2]:
   Headline.append(i.text)
Headline


# In[8]:


Time=news.find('time')
Time


# In[9]:


Time.text


# In[19]:


Time=[]
for i in news.find_all('time')[0:2]:
   Time.append(i.text)
Time


# In[11]:


url_5= "https://www.cnbc.com/world/?region=world"


# In[12]:


webpage_4 = requests.get(url_5) 


# In[21]:


trav = BeautifulSoup(webpage_4.content, "html.parser")

for link in trav.find_all('a')[0:2]:
    print(type(link), " ", link)
trav


# In[22]:


Data_frame=pd.DataFrame({'Headline':Headline,'Time':Time,'trav':trav})
Data_frame


# In[ ]:





# In[95]:


# 8. Write a python program to scrape the details of most downloaded articles from AI in last 90days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articlesScrape below mentioned details and make data frame-
#i) Paper Title
#ii) Authors
#iii) Published Date
#iv) Paper URL


# In[38]:


page_2=requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
page_2


# In[39]:


Books=BeautifulSoup(page_2.content)
Books


# In[40]:


Title=[]
for i in Books.find_all('h2',class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg")[0:50]:
    Title.append(i.text)
    
Title


# In[41]:


Author=[]
for i in Books.find_all('span',class_="sc-1w3fpd7-0 dnCnAO")[0:50]:
   Author.append(i.text)
Author


# In[42]:


Date=[]
for i in Books.find_all('span',class_="sc-1thf9ly-2 dvggWt")[0:50]:
   Date.append(i.text)
Date


# In[ ]:





# In[118]:


df_5=pd.DataFrame({"Title":Title, "Author":Author, "Published Date":Date})
df_5


# In[119]:


#9.Write a python program to scrape mentioned details from dineout.co.in and make data frame-
#i) Restaurant name
#ii) Cuisine
#iii) Location
#iv) Ratings
#v) Image URL


# In[120]:


page_9 = requests.get('https://www.dineout.co.in/bangalore-restaurants/dineout-pay')


# In[121]:


page_9


# In[123]:


soup_9 = BeautifulSoup(page_9.content)
soup_9


# In[125]:


first_title_11 = soup_9.find('a',class_="restnt-name ellipsis")
first_title_11


# In[126]:


first_title_11.text


# In[128]:


loc = soup_9.find('div',class_="restnt-loc ellipsis")
loc.text


# In[129]:


sta = soup_9.find('span',class_="double-line-ellipsis")
sta.text.split('|')[0]


# In[130]:


titles_12 = []

for i in soup_9.find_all('a',class_="restnt-name ellipsis"):
    titles_12.append(i.text)
    
titles_12


# In[132]:


location = []

for i in soup_9.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
    
location


# In[133]:


price = []

for i in soup_9.find_all('span',class_="double-line-ellipsis"):
    price.append(i.text.split('|')[0])
    
price


# In[134]:


images =  []
for i in soup_9.find_all("img",class_="no-img"):
    images.append(i.get('data-src'))
    
images


# In[137]:


print(len(titles_12),len(location),len(price),len(images))


# In[139]:


import pandas as pd
df_6 = pd.DataFrame({'titles':titles_12,'location':location,'price':price,'images':images})
df_6


# In[ ]:


""""""END OF NOTES """"""

