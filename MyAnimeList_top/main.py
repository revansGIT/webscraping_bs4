from bs4 import BeautifulSoup as bs4
import pandas as pd
import requests

# to store data
ranks = []
titles = []
airing = []
ratings = []
ep = []
fan = []
urls = []

url = requests.get('https://myanimelist.net/topanime.php?')
soup = bs4(url.text, 'html.parser')

animes = soup.find('div', class_='pb12').findAll('tr')
	for anime in animes:
		for name in anime.find_all('div', class_='di-ib clearfix'):
			ttl = name.find('a').text
			titles.append(ttl)

		for details in anime.find_all('div', class_='information di-ib mt4'):
			episode = details.text.split('        ')[1]
			aire = details.text.split('        ')[2]
			member = details.text.split('        ')[3]
			ep.append(episode)
			airing.append(aire)
			fan.append(member)

		for topranking in anime.find_all('td', class_='rank ac'):
			rank = topranking.find('span').text
			ranks.append(rank)

		for star in anime.find_all('td', class_='score ac fs14'):
			rating = star.find('span').text
			ratings.append(rating)

		image = anime.find_all('img')
		for poster in image:
			url = poster['data-src']
			urls.append(url)

data = {'Title': titles, 'Rank': ranks, 'Episode': ep, 'Airing': airing, 'Fanbase': fan, 'Rating': ratings, 'Poster': urls}

df = pd.DataFrame.from_dict(data, orient='index')
df = df.transpose()
df.index +=1
df.to_excel('toprankanime.xlsx')
