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

# Let's write a function to filter out only items that meet the condition
# Hint: condition will be associated with an anonymous function, e.x., lamdbda x: max(x)
def filter(condition, dict_list):
    temps = []
    for item in dict_list:
        if condition(item):
            temps.append(item)
    return temps


# Let's write a function to do aggregation given an aggregation function and an aggregation key
def aggregate(aggregation_key, aggregation_function, dict_list):
    temps = []
    for item in dict_list:
        try:
            value = float(item[aggregation_key])
            temps.append(value)
        except ValueError:
            temps.append(item[aggregation_key])
    return aggregation_function(temps)


# Print all cities in Germany

filter_list = filter(lambda x: x['country'] == 'Germany', cities)
print("All cities in Germany:")
for item in filter_list:
    print(item['city'])
print()

# Print all cities in Spain with a temperature above 12°C

print("All cities in Spain with a temperature above 12°C:")
filter_country = filter(lambda x: x['country'] == 'Spain' and float(x['temperature']) > 12, cities)
for item in filter_country:
    print(item['city'])
print()

# Count the number of unique countries

unique_country = aggregate('country', set, cities)
print(f"Number of unique countries: {len(unique_country)}")
print()

# Print the average temperature for all the cities in Germany

filter_temperature = filter(lambda x: x['country'] == 'Germany', cities)
sum_temperature = aggregate('temperature', sum, filter_temperature)
avg_temperature = sum_temperature / len(filter_temperature)
print(f"The average temperature for all the cities in Germany: {avg_temperature}")
print()

# Print the max temperature for all the cities in Italy
filter_temperature = filter(lambda x: x['country'] == 'Italy', cities)
max_temperature = aggregate('temperature', max, filter_temperature)
print(f"The max temperature for all the cities in Italy: {max_temperature}")