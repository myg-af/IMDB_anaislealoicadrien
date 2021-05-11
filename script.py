from scraping import *
import time
from database import Data

movie_id = 0

data = Data()
data.create_table_movies()
data.create_table_realisators()

links = get_list_urls()

for link in links:
    pagelink = urllib.request.urlopen(link)
    soup = BeautifulSoup(pagelink, 'html.parser')

    movies = get_list_movies(soup)

    for i in list(movies):
        i = list(i)
        movie_id += 1

        title = get_title(i)
        img = get_img(i)
        year = get_year(i)
        public = get_public(i)
        runtime = get_runtime(i)
        genre = get_genre(i)
        rating = get_rating(i)
        total_rating = get_total_rating(i)
        synopsis = get_synopsis(i)
        value = get_value(i)

        data.insert_into_movies(title,year,public,runtime,rating,total_rating,value,synopsis,img)
        
        realisators(i,data,movie_id)

        

