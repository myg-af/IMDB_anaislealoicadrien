import sqlite3

class Data:
    def __init__(self):
        try:
            self.connexion = sqlite3.connect("IMDB.db")
            self.c = self.connexion.cursor()
        except:
            print("no db connexion")

    def create_table_movies(self):
        with self.connexion:
            self.connexion.execute("""CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                year INTEGER,
                public TEXT,
                runtime INTEGER,
                rating FLOAT,
                total_rating INTEGER,
                value FLOAT,
                synopsis TEXT,
                img TEXT
            );""")

    def create_table_realisators(self):
        self.connexion.execute("""CREATE TABLE IF NOT EXISTS realisators (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            movie_id INTEGER
        );""")

    def insert_into_movies(self,title,year,public,runtime,rating,total_rating,value,synopsis,img):
        with self.connexion:
            self.c.execute("INSERT INTO movies (title, year, public, runtime, rating, total_rating, value, synopsis, img) VALUES (?,?,?,?,?,?,?,?,?)", (title,year,public,runtime,rating,total_rating,value,synopsis,img))

    def insert_into_realisators(self,realisator, movie_id):
        with self.connexion:
            self.c.execute("INSERT INTO realisators (name, movie_id) VALUES (?,?)", (realisator, movie_id))
