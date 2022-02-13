# create counties found
counties = {
    'NA': 'Nairobi',
    'MS': 'Mombasa',
    'UG': 'Uasin Gishu',
    'KS': 'Kisumu',
    'KI': 'Kiambu',
}

# create a few towns within counties
towns = {
    'NA': 'Nairobi',
    'UG': 'Eldoret',
    'MS':'Voi',
    'KS':'Kisumu',
}

#add a few more towns

towns['KI'] = 'Juja'
towns['UG'] = 'Eldoret'
print('\n\n')
# print out locations of towns found in specific county
print(f"In {counties['KI']} we can find: {towns['KI']}")
print(f"In {counties['MS']} we can find: {towns['MS']}")
print('\n\n')
# print every town in every county
for abbrev, county in counties.items():
    print(f"We can find {towns[abbrev]} in {county}")
