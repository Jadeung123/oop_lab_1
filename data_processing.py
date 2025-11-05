import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany

germany_city = []
for city in cities:
    if city['country'] == 'Germany':
        germany_city.append(city['city'])
for city in germany_city:
    print(city)
print()

# Print all cities in Spain with a temperature above 12°C

spain_city_with_temp_above_12 = []
for city in cities:
    if city['country'] == 'Spain' and float(city['temperature']) > 12:
        spain_city_with_temp_above_12.append(city['city'])
for city in spain_city_with_temp_above_12:
    print(city)
print()

# Count the number of unique countries

unique_contries = []
for city in cities:
    if city['country'] not in unique_contries:
        unique_contries.append(city['country'])
print(len(unique_contries))
print()

# Print the average temperature for all the cities in Germany

germany_temp = []
for city in cities:
    if city['country'] == 'Germany':
        germany_temp.append(float(city['temperature']))
avg_germany_temp = sum(germany_temp) / len(germany_temp)
print(avg_germany_temp)
print()

# Print the max temperature for all the cities in Italy

italy_temp = []
for city in cities:
    if city['country'] == 'Italy':
        italy_temp.append(city['temperature'])
max_italy_temp = max(italy_temp)
print(max_italy_temp)
