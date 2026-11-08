class MediaError(Exception):
    """Custom exception for media-related errors."""
    def __init__(self, *args, message, obj):
        super().__init__(*args,message)
        self.obj = obj
    

class Movie:
    """Represent a movie in the media catalogue."""
    
    def __init__ (self, title, year, director, duration):
        if not title.strip():
            raise ValueError("Title cannot be empty")
        if year < 1895:
            raise ValueError("Year must be 1895 or later")
        if not director.strip():
            raise ValueError("Director cannot be empty")
        if not duration > 0:
            raise ValueError("Duration must be positive")
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration
    def __str__(self):
        return f"{self.title} ({self.year}) - {self.duration} min, {self.director}"
class TVSeries(Movie):
    """Child class representing an entire TV series."""
    def __init__ (self, title, year, director, duration, seasons, total_episodes):
        super().__init__(title, year, director, duration)
        if seasons < 1:
            raise ValueError("Seasons must be 1 or greater")
        if total_episodes < 1:
            raise ValueError("Total episodes must be 1 or greater")
        self.seasons = seasons
        self.total_episodes = total_episodes
    def __str__(self):
        return f"{self.title} ({self.year}) - {self.seasons} seasons, {self.total_episodes} episodes, {self.duration} min avg, {self.director}"

class MediaCatalogue:
    """A catalogue that can store different types of media items."""
    def __init__(self):
        self.items = []

    def add(self, media_item):
        if not isinstance(media_item, Movie):
            raise MediaError(message="Only Movie or TVSeries instances can be added", obj=media_item)
        self.items.append(media_item)
    def get_movies(self):
        return [item for item in self.items if type(item) is Movie]
    
    def get_tv_series(self):
        return [item for item in self.items if isinstance(item, TVSeries)]
    
    
    def __str__(self):
        if not self.items:
            return "Media Catalogue (empty)"
        result = f"Media Catalogue ({len(self.items)} items):\n\n"

        movies = self.get_movies()
        series = self.get_tv_series()
        if movies:
            result += '=== MOVIES ===\n'

        for index, item in enumerate(self.items):
            result += f"{index + 1}. {item}\n"

        if series:
            result += '=== TV SERIES ===\n'

        for index, item in enumerate(series, start=1):
            result += f"{index}. {item}\n"

        return result
catalogue = MediaCatalogue()
try:
    movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
    print(movie1)
    catalogue.add(movie1)
    movie2 = Movie('Inception', 2010, 'Christopher Nolan', 148)
    catalogue.add(movie2)
    series1 = TVSeries('Breaking Bad', 2008, 'Vince Gilligan', 47, 5, 62)
    catalogue.add(series1)
    series2 = TVSeries('The Office', 2005, 'Greg Daniels', 22, 9, 201)
    catalogue.add(series2)
    
    print(series1)
    print(catalogue)
except ValueError as e:
    print(f"Validation Error: {e}")
except MediaError as e:
    print(f"Media Error: {e}")
    print(f"Unable to add {e.obj}: {type(e.obj)}")

movies = catalogue.get_movies()
series = catalogue.get_tv_series()

print(movie1.__doc__)
print(series1.__doc__)