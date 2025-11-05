import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

url= requests.get(f'https://www.scrapethissite.com/pages/forms/').text
soup =BeautifulSoup(url,'lxml')
# players= soup.find_all('tr')
players=soup.find_all('tr')[1:]
# print(players)
# st.write(players)
team_name=[]
year=[]
wins=[]
for i in players:
    name=i.find_all('td')[0].text.strip()
    yr=i.find_all('td')[1].text.strip()
    win=i.find_all('td')[2].text.strip()
    team_name.append(name)
    year.append(yr)
    wins.append(win)
data=pd.DataFrame({'Team name':team_name,"year":year,"wins":wins})
st.dataframe(data)