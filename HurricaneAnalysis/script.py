# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def clean_damages(damages):
  r = []
  for damage in damages:
    if damage[-1] == 'B':
      r.append(float(damage[:-1]) * 1000000000)
    elif damage[-1] == 'M':
      r.append(float(damage[:-1]) * 1000000)
    else:
      r.append('Damages not recorded')
  return r

damages = clean_damages(damages)

# write your construct hurricane dictionary function here:
dict_property_names = ['name', 'month', 'year', 'max sustained wind', 'area affected', 'damage', 'deaths']
hurricanes_properties = list(zip(names, months, years, max_sustained_winds, areas_affected, damages, deaths))
hurricanes_by_name_dict = {hurricane[0]: {k: v for k, v in zip(dict_property_names, hurricane)} for hurricane in hurricanes_properties}

# write your construct hurricane by year dictionary function here:
hurricanes_by_year_dict = {item['year']: item for item in hurricanes_by_name_dict.values()}

# write your count affected areas function here:
total_list_of_areas = [area for list_areas in [elem['area affected'] for elem in hurricanes_by_name_dict.values()] for area in list_areas]
list_of_areas = list(set(total_list_of_areas))
affected_areas_count = {area: total_list_of_areas.count(area) for area in list_of_areas}

# write your find most affected area function here:
most_affected_area = sorted(affected_areas_count.items(), key=lambda x: x[1], reverse=True)[0]

# write your greatest number of deaths function here:
# print(hurricanes_by_year_dict)
list_of_hurricane_deaths = [tuple((hurricane['name'], hurricane['deaths'])) for hurricane in hurricanes_by_year_dict.values()]
greatest_number_of_deaths = sorted(list_of_hurricane_deaths, key=lambda x: x[1], reverse=True)[0]

# write your catgeorize by mortality function here:
def set_mortality(deaths):
  if deaths == 0:
    return 0
  elif deaths < 100:
    return 1
  elif deaths < 500:
    return 2
  elif deaths < 1000:
    return 3
  elif deaths < 10000:
    return 4
  else:
    return 5

list_of_hurricane_deaths_incl_scale = [tuple((hurricane[0], set_mortality(hurricane[1]))) for hurricane in list_of_hurricane_deaths]
hurricane_mort_dict = {s: [] for s in range(6)}
for hurricane in list_of_hurricane_deaths_incl_scale:
  hurricane_mort_dict[hurricane[1]].append(hurricanes_by_name_dict[hurricane[0]])

# write your greatest damage function here:
list_of_hurricane_damage = [tuple((hurricane['name'], hurricane['damage'])) for hurricane in hurricanes_by_year_dict.values() if type(hurricane['damage']) != str]
greatest_damage = sorted(list_of_hurricane_damage, key=lambda x: x[1], reverse=True)[0]

# write your catgeorize by damage function here:
def set_damage(damage):
  if damage == 'Damages not recorded':
    return 0
  elif damage < 100000000:
    return 1
  elif damage < 1000000000:
    return 2
  elif damage < 10000000000:
    return 3
  elif damage < 50000000000:
    return 4
  else:
    return 5

list_of_hurricane_damage_incl_scale = [tuple((hurricane['name'], set_damage(hurricane['damage']))) for hurricane in hurricanes_by_year_dict.values()]

hurricane_damage_dict = {s: [] for s in range(6)}
for hurricane in list_of_hurricane_damage_incl_scale:
  hurricane_damage_dict[hurricane[1]].append(hurricanes_by_name_dict[hurricane[0]])



