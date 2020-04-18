# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Aaron'
age = 44

# Concat

print('Hello, my name is ' + name + 'and I am ' + str(age))

# String Formatting
# Arguments by position

print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-strings
print(f'Hello, my name is {name} and I am {age}')

# String Methods

s = 'hello world'

#Capitalize
print(s.capitalize())
