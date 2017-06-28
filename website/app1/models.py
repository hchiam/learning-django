from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.album_title + ' - ' + self.artist


# a song needs to be a part of an album
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    # ForeignKey: to link mulitple songs to the same album
    # on_delete=models.CASCADE: when album deleted. delete all linked songs
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    
    def __str__(self):
        return self.song_title
