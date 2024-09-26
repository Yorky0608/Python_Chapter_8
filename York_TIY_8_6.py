def city_country(city, country = "US"):
    if country == "us" or country == "US" or country == "uS" or country == "Us":
        message = f"{city.title()}, {country.upper()}"
    else:
        message = f"{city.title()}, {country.title()}"
    return message

#test to see if inputs work and how to manipulate them
#print(city_country(input("City  "), input("Country  ")))

city = "new haven"
country = "uS"

print(city_country(city, country))
print(city_country(city = "Milwaukee"))
print(city_country(city = "Sydney", country = "Australia"))