sandwich_items = ['Bacon',  'Lettuce', 'Tomato']

def make_sandwich(*items):
    print("\nHere is what you ordered on your sandwich: ")
    for i in items:
        for items in i:
            print(f"- {items}")

make_sandwich(sandwich_items)

sandwich_items = ['Bacon',  'Lettuce', 'Tomato', "Onion"]
make_sandwich(sandwich_items)

sandwich_items = ["Only a bun. I do not like sandwiches!"]
make_sandwich(sandwich_items)