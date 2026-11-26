class Movie:
    def __init__(self, movie_name, rating, ticket_price):
        self.movie_name = movie_name
        self.rating = rating
        self.ticket_price = ticket_price

    def category(self):
        if self.rating >= 8:
            return "Hit"
        elif self.rating >= 5:
            return "Average"
        else:
            return "Flop"

    def display(self):
        print("Movie Name  :", self.movie_name)
        print("Rating      :", self.rating)
        print("Ticket Price:", self.ticket_price)
        print("Category    :", self.category())
        print()


class Cinema:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def show_movies(self):
        print("\n------ Movie Details ------\n")
        for movie in self.movies:
            movie.display()


# Main Program

cinema = Cinema()

n = int(input("Enter number of movies: "))

for i in range(n):
    print("\nEnter details of Movie", i + 1)

    name = input("Movie Name: ")
    rating = float(input("Rating (out of 10): "))
    price = int(input("Ticket Price: "))

    m = Movie(name, rating, price)
    cinema.add_movie(m)

cinema.show_movies()


"""
Enter number of movies: 3

Enter details of Movie 1
Movie Name: Dhurandhar
Rating (out of 10): 9.8
Ticket Price: 300

Enter details of Movie 2
Movie Name: Toxic
Rating (out of 10): 9.5
Ticket Price: 250

Enter details of Movie 3
Movie Name: War
Rating (out of 10): 9.2
Ticket Price: 350

------ Movie Details ------

Movie Name  : Dhurandhar
Rating      : 9.8
Ticket Price: 300
Category    : Hit

Movie Name  : Toxic
Rating      : 9.5
Ticket Price: 250
Category    : Hit

Movie Name  : War
Rating      : 9.2
Ticket Price: 350
Category    : Hit
"""
