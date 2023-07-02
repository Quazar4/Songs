class SongService:
    def __init__(self):
        self.songs = []

    def add_song(self, title, artist, duration):
        song = {
            "title": title,
            "artist": artist,
            "duration": duration
        }
        self.songs.append(song)
        print(f"Added '{song['title']}' by {song['artist']}")

    def delete_song(self, title):
        for song in self.songs:
            if song['title'] == title:
                self.songs.remove(song)
                print(f"Deleted '{song['title']}' by {song['artist']}")
                return
        print(f"Song '{title}' not found.")

    def update_song(self, title, new_title=None, new_artist=None, new_duration=None):
        for song in self.songs:
            if song['title'] == title:
                if new_title:
                    song['title'] = new_title
                if new_artist:
                    song['artist'] = new_artist
                if new_duration:
                    song['duration'] = new_duration
                print(f"Updated '{song['title']}' by {song['artist']}")
                return
        print(f"Song '{title}' not found.")

    def display_songs(self):
        if len(self.songs) == 0:
            print("No songs found.")
        else:
            print("Song List:")
            for song in self.songs:
                print(f"'{song['title']}' by {song['artist']} [{song['duration']}]")

song_service = SongService()

song_service.add_song("Song 1", "Artist 1", "3:45")
song_service.add_song("Song 2", "Artist 2", "4:20")
song_service.add_song("Song 3", "Artist 3", "5:10")

song_service.display_songs()

song_service.update_song("Song 2", new_title="Updated Song", new_artist="Updated Artist", new_duration="6:30")
song_service.display_songs()

song_service.delete_song("Song 1")
song_service.display_songs()
