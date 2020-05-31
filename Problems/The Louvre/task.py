class Painting:
    museum = 'Louvre'

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def print_sentence(self):
        print('"{title}" by {artist} ({year}) hangs in the {museum}.'.format(title=self.title,
                                                                             artist=self.artist,
                                                                             year=self.year,
                                                                             museum=Painting.museum))


title_, artist_, year_ = input(), input(), input()
painting = Painting(title_, artist_, year_)
painting.print_sentence()
