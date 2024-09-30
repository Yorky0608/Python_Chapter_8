def car_specs(manu, model, **specs):
    specs["Manufacturer"] = manu
    specs["Model"] = model
    return specs

print(car_specs('Honda', 'Civic', Milage = 33, Doors = 4))