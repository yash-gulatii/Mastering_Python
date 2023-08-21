"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

# Initial dictionary with one city
city_data = {
    'USA': {'North America': ['Mountain View']}
}

# Cities to add
cities_to_add = {
    'India': {'Asia': ['Bangalore']},
    'USA': {'North America': ['Atlanta']},
    'Egypt': {'Africa': ['Cairo']},
    'China': {'Asia': ['Shanghai']}
}

# Add cities to the dictionary
for country, continent_city_data in cities_to_add.items():
    for continent, cities in continent_city_data.items():
        if country not in city_data:
            city_data[country] = {}
        if continent not in city_data[country]:
            city_data[country][continent] = []
        city_data[country][continent].extend(cities)

# Print cities in the USA in alphabetical order
print("1")
for city in sorted(city_data['USA']['North America']):
    print(city)

# Print cities in Asia with their respective countries
print("2")
for country, continent_city_data in city_data.items():
    for continent, cities in continent_city_data.items():
        if continent == 'Asia':
            for city in sorted(cities):
                print("{} - {}".format(city, country))


"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""