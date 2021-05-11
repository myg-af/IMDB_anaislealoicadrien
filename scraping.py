from bs4 import BeautifulSoup
import urllib.request

def get_list_urls():
    links = []
    for i in range(1,1001,50):
        #links.append(f"https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start={i}&ref_=adv_nxt")
        links.append(f"https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&start={i}&ref_=adv_nxt")
    return links

def get_list_movies(soup):
    return soup.find_all('div', attrs={'class': 'lister-item mode-advanced'})

def get_title(i):
    return i[3].find('img', attrs={'class': 'loadlate'})['alt'].strip()

def get_img(i):
    return i[3].find('img', attrs={'class': 'loadlate'})['loadlate'].strip()

def get_runtime(i):
    return i[5].find('span', attrs={'class': 'runtime'}).text.strip()[:-4]

def get_genre(i):
    return i[5].find('span', attrs={'class': 'genre'}).text.strip()

def get_rating(i):
    return i[5].find('meta', attrs={'itemprop': 'ratingValue'})['content'].strip()

def get_total_rating(i):
    return i[5].find('meta', attrs={'itemprop': 'ratingCount'})['content'].strip()

def get_synopsis(i):
    synopsis = list(i[5].find_all('p', attrs={'class': 'text-muted'}))
    synopsis = synopsis[1].text.strip()
    return synopsis
    
def get_year(i):
    year = i[5].find('span', attrs={'class': 'lister-item-year text-muted unbold'}).text[1:5].strip()
    try:
        year = int(year)
    except:
        year = -1
    return year

def get_public(i):
    try:
        public = i[5].find('span', attrs={'class': 'certificate'}).text.strip()
    except:
        public = "NaN"
    return public

def realisators(i,data,movie_id):
    realisator = i[5].find_all('p', attrs={'class': ''})
    realisator = str(realisator[0]).split('|')[0]
    realisator = BeautifulSoup(realisator, 'html.parser')
    try:
        for i in range(0,1000):
            realisator1 = realisator.find_all('a')[i].text
            data.insert_into_realisators(realisator1,movie_id)
    except:
        pass

def get_value(i):
    value = i[5].find_all('span')
    value = value[-1:][0].text
    value = value[1:][:-1]
    value = value.replace(",", ".")
    return value
