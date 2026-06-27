class RecommendationSystem:

    def __init__(self):

        self.movies = {
            "action": [
                ("Avengers: Endgame", 9.0),
                ("John Wick", 8.8),
                ("Mission Impossible", 8.5)
            ],
            "comedy": [
                ("3 Idiots", 9.2),
                ("Jumanji", 8.1),
                ("Free Guy", 8.0)
            ],
            "sci-fi": [
                ("Interstellar", 9.5),
                ("Inception", 9.3),
                ("The Matrix", 9.0)
            ],
            "horror": [
                ("The Conjuring", 8.7),
                ("Insidious", 8.3),
                ("Annabelle", 7.8)
            ]
        }

    def show_genres(self):
        print("\nAvailable Genres:")
        for genre in self.movies:
            print("-", genre.title())

    def recommend(self, genre):

        genre = genre.lower()

        if genre in self.movies:

            print("\nRecommended Movies:")
            print("-" * 30)

            for movie, rating in self.movies[genre]:
                print(f"{movie} ⭐ {rating}")

        else:
            print("Genre not found!")

    def run(self):

        print("=" * 50)
        print("AI MOVIE RECOMMENDATION SYSTEM")
        print("=" * 50)

        while True:

            self.show_genres()

            choice = input(
                "\nEnter genre (or exit): "
            ).lower()

            if choice == "exit":
                print("Thank you for using the system!")
                break

            self.recommend(choice)


system = RecommendationSystem()
system.run()