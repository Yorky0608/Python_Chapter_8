def make_album(album_title, artist_name = "TheFatRat", num_songs = None):
    if num_songs:
        album = {"Name": artist_name, "Title": album_title, "Songs" : num_songs}
    else:
        album = {"Name" : artist_name, "Title" : album_title}
    return album

I = 0
name = "Marshmellow"
album = "Joytime"

print(make_album(album, name))
print(make_album(artist_name = "TheFatRat", album_title = "Warrior Songs"))
print(make_album(album_title = "Parallax"))
print(make_album(album_title = "Parallax", num_songs = 10))