# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
person = {
  'first_name': 'John',
  'last_name': 'Doe',
}

# print (person, type(person))

# person2 = dict(first_name='Sarah', last_name='Williams')

# print(person['first_name'])
# print(person.get('last_name'))

person['phone'] = '555-555-55555'

# print(person)
# print(person.keys())
# print(person.items())

person2 = person.copy()
person2['city'] = 'Boston'
print(person2)

person.pop('phone')
person['home'] = 'here'
print(person)

print(len(person2))

people = [
  {'name': 'Martha', 'age': 30},
  {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])