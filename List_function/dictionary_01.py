# dictionary = A changeable, unordered collection of unique key:value pairs
#              Fast beacause they use hashing, allow us to access a value quickly

capitals = {'India':'New Delhi',
            'China' : 'Beijing',
            'USA' : 'Washington DC',
            'Russia' : 'Mascow',
            }
# capitals.update({'Germany':'Berlin'})
# capitals.update({'India' : 'Gujarat'})
# capitals.pop('China')
# capitals.clear()

# print(capitals['Germany'])
# print(capitals.get('Germany'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

for key, value in capitals.items():
    print(key, value)