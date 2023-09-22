countries = ['Croatia',
 'USA',
 'Argentina',
 'Mexico',
 'USA',
 'Morocco',
 'New Mexico',
 'Finland',
 'Argentina',
 'Italy',
 'Canada',
 'South Korea']

italy = countries[-3]
mexico = countries[3]
kindof_neighbors = countries[1:5]

countries.append('Malta')
countries.append('Thailand')
countries[6] = 'USA'
countries.pop()

unique_countries = set(countries)

num_of_repeats = len(countries) - len(unique_countries)
print(num_of_repeats)