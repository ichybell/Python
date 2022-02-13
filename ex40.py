class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

my_lyrics = ["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"]
my2nd_lyrics = ["They rally around tha family",
                        "With pockets full of shells"]
happy_bday = Song(my_lyrics)

bulls_on_parade = Song(my2nd_lyrics)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
