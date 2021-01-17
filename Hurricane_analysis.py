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

# damages in actual Nos
updated_damages = []
for damage in damages:
  if '' in damage.split('M'):
    updated_damages.append(float(damage.split('M')[0]) * 10**6)
  elif '' in damage.split('B'):
    updated_damages.append(float(damage.split('B')[0]) * 10**9)
  else:
    updated_damages.append('Damages not recorded')

#print(updated_damages)

# modified hurricane dictionary
def hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  hurricanes = {}
  for index in range(len(names)):
    hurricanes[names[index]] = {"Name": names[index], "Month": months[index], "Year": years[index], "Max Sustained Wind": max_sustained_winds[index], "Areas Affected": areas_affected[index], "Damage": updated_damages[index], "Deaths": deaths[index]}
  return hurricanes

hurricanes_data = hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
#print(hurricanes_data)

# hurricane dictionary in years
def hurricane_dict_years(hurricanes_dict):
  dict_years ={}
  for i in range(len(names)):
    dict_years[years[i]] = hurricanes_dict[names[i]]
  return dict_years

hurricane_data_years = hurricane_dict_years(hurricanes_data)

# Areas affected by count
def count_affected_areas(area_affected):
  count = 0
  for i in range(len(names)):
    for list in hurricanes_data[names[i]]["Areas Affected"]:
      if list == area_affected:
        count += 1
  return count

# areawise affected count
def affected_areas_count(hurricanes_data):
  affect_list = []
  count_affect = []
  areawise_count ={}
  for i in range(len(names)):
    for a in hurricanes_data[names[i]]["Areas Affected"]:
      if not (a in affect_list):
        affect_list.append(a)
  for count in affect_list:
    areawise_count[count] = count_affected_areas(count)
  return areawise_count

# Mortality by Hurricane
def count_deaths_hurricane(names):
  hurricane_death = {}
  for i in range(len(names)):
    hurricane_death[names[i]] = deaths[i]
  return hurricane_death

#print(count_deaths_hurricane(names))

maximum_death = max(count_deaths_hurricane(names), key = count_deaths_hurricane(names).get)

# Hurricane Mortality rating
def hurricane_rating_mortality(dictio):
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  new_dic = {0:[], 1:[], 2:[], 3:[], 4:[]}
  for hurricane in dictio:
    mortality = dictio[hurricane]['Deaths']
    for i in range(len(mortality_scale)-1,0,-1):
      if mortality >= mortality_scale[i]:
        new_dic[i].append(dictio[hurricane]['Name'])
  return new_dic

mortality_rating = hurricane_rating_mortality(hurricanes_data)
#print(mortality_rating)


# greatest damage function :
def greatest_damage(dic):
  most_damage = 0.0
  most_hurricane = ''

  for hurricane in dic:
    damage = dic[hurricane]['Damage']
    if damage != 'Damages not recorded':
      if damage > most_damage:
        most_damage = damage
        most_hurricane = hurricane
  return (most_hurricane, most_damage)

most_damaging_hurricane = greatest_damage(hurricanes_data)
print(most_damaging_hurricane)

# catgeorize by damage function :
def damage_order(dic):
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  new_dic = {0:[],1:[],2:[],3:[],4:[]}
  
  for hurricane in dic:
    curr_damage = dic[hurricane]['Damage']
    current_cane = dic[hurricane]['Name']
    if curr_damage == 'Damages not recorded':
      new_dic[0].append(current_cane)
    else:
      for i in range(len(damage_scale)-1,0,-1):
        if curr_damage > damage_scale[i-1] and curr_damage <= damage_scale[i] :
          new_dic[i].append(current_cane)
  return new_dic

hurricane_by_damage = damage_order(hurricanes_data)
print(hurricane_by_damage)












  
  



    
