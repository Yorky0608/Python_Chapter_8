def car_specs(manu, model, **specs):
    specs["Manufacturer"] = manu
    specs["Model"] = model
    return specs

print(car_specs('Honda', 'Civic', Milage=33, Doors=4))


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Caleb', 'York',
                            location='New Haven',
                            field='Software Development',
                             sports=['Tennis', 'Baseball'])

print(user_profile)


def make_album(a_n, a_t):
    album = {"Artist's Name" : a_n, "Album's Title" : a_t}
    return album

while True:
    print(f"\nEnter the Artist's Name and the Album's Title. \n(Enter q to exit)")
    artist = input("Artist's Name  ")
    if artist == 'q':
        break
    title = input("Album's Name  ")
    if title == 'q':
        break
    print(make_album(artist, title))