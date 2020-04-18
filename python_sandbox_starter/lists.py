# A List is a collection which is ordered and changeable. Allows duplicate members.
numbers = [1, 2, 3, 4, 5]

numbers2 = list((1, 2, 3, 4, 5))

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

print(len(fruits))

fruits.append('Mangoes')

fruits.remove('Apples')

fruits.insert(2, 'Strawberries')

fruits.pop(1)

fruits.sort(reverse=True)
print(fruits)
