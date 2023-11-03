import sys
from time import sleep
from functools import reduce

movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spider-Man: No Way Home", "year": 2021,"rating": 7.6, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020,"rating": 7.4, "genre": "Horror"},
    {"title": "No Time to Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]


class MovieList:
    def __init__(self, movies):
        self.movies = movies

    def show_movie(self, title):
        movie = list(filter(lambda x: x['title'] == title, self.movies))
        if not movie:
            print("Film not found.")
        else:
            movie = movie[0]
            print(f"Info Film\t: {movie['title']}")
            print(f"Rating\t: {movie['rating']}")
            print(f"Release\t: {movie['year']}")
            print(f"Genre\t: {movie['genre']}\n")

    def total_film_by_genres(self):
        genre_count = reduce(lambda count, movie: {
                             **count, movie['genre']: count.get(movie['genre'], 0) + 1}, self.movies, {})
        self.typewriter("Jumlah Film Berdasarkan Genre:")
        print(genre_count)

    def avg_by_year(self):
        data = reduce(lambda film, movie: {
            **film, movie['year']: (
                film.get(movie['year'], (0, 0))[0] + movie['rating'],
                film.get(movie['year'], (0, 0))[1] + 1)}, self.movies, {})
        
        avg_rating = {year: total_rating / count for year, (total_rating, count) in data.items()}
        print(avg_rating)

    def highest_rated(self):
        highest = max(list(map(lambda x: x['rating'], self.movies)))
        detail_film = list(filter(lambda x: x['rating'] == highest, self.movies))[0]

        self.typewriter("Film dengan Rating Tertinggi:")
        print(f"Informasi Film: {detail_film['title']}")
        print(f"Rating: {detail_film['rating']}")
        print(f"Tahun Rilis: {detail_film['year']}")
        print(f"Genre: {detail_film['genre']}")

    def typewriter(self, text):
        for char in text:
            sys.stdout.write(char)
            sleep(0.05)
            sys.stdout.flush()


if __name__ == '__main__':
    movie_info = MovieList(movies)
    awe = "\nPilih tugas yang ingin dilakukan:"

    while True:
        movie_info.typewriter(awe)
        print("""
1. Jumlah film berdasarkan genre
2. Average rating film berdasarkan tahun rilis
3. Film dengan rating tertinggi
4. Cari judul film
0. exit
            """)

        choice = input(">> ")

        if choice == '1':
            movie_info.total_film_by_genres()
        elif choice == '2':
            movie_info.avg_by_year()
        elif choice == '3':
            movie_info.highest_rated()
        elif choice == '4':
            title = input("Masukkan judul film yang ingin dicari: ")
            movie_info.show_movie(title)
        elif choice == '0':
            break
        else:
            print("Invalid input.")
