def make_album(a_n, a_t):
    album = {"Artist's Name" : a_n, "Album's Title" : a_t}
    return album

brek = ''

while True:
    print(f"\nEnter the Artist's Name and the Album's Title. \n(Enter q to exit)")
    artist = input("Artist's Name  ")
    if artist == 'q':
        break
    title = input("Album's Name  ")
    if title == 'q':
        break
    print(make_album(artist, title))