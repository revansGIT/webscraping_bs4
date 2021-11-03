from bs4 import BeautifulSoup as bs4
import pandas as pd
import lxml

uniqe_id = []
nickname = []

file = open("tik.html", encoding="utf8")     
soup = bs4(file, 'lxml')

tik = soup.find('div', class_="jsx-2021749678 user-list").find_all('a')
for tiktok in tik:
	id123 = tiktok.find('span', class_="jsx-2021749678 unique-id").text
	uniqe_id.append(id123)
	
	nick = tiktok.find('span', class_="jsx-2021749678 nickname").text
	nickname.append(nick)

data = {"username": uniqe_id, "Nickname": nickname}
df = pd.DataFrame.from_dict(data, orient='index')
df = df.transpose()
df.index +=1
df.to_excel('test_username.xlsx')