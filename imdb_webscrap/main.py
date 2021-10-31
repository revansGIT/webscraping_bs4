from bs4 import BeautifulSoup as bs4
import pandas as pd
import requests

# to store data
ranks = []
titles = []
releases = []
ratings = []
urls = []

try:
	# main sites url
	html = requests.get('https://www.imdb.com/chart/toptv/')
	html.raise_for_status()
	soup = bs4(html.text, 'html.parser')
	
	imdbs = soup.find('tbody', class_='lister-list').find_all('tr')
	for imdb in imdbs:
		name = imdb.find('td', class_='titleColumn').a.text
		titles.append(name)
		rank = imdb.find('td', class_='titleColumn').get_text(strip=True).split('.')[0]
		ranks.append(rank)
		year = imdb.find('td', class_='titleColumn').span.text.strip('()')
		releases.append(year)
		rating = imdb.find('td', class_='ratingColumn imdbRating').strong.text
		ratings.append(rating)
		
		# to get the image or poster in url form!
		image = imdb.find_all('img')
		for img in image:
			url = img['src']
			urls.append(url)
except Exception as e:
	print(e)

data = {'Title': titles, 'Rank': ranks, 'Release': releases, 'Rating': ratings, 'Poster': urls}

# using pandas module to sort all data in dataframe
df = pd.DataFrame(data = data)
df.index+=1

# give your location to put xl file
df.to_excel('../imdb_toprated_series.xlsx')