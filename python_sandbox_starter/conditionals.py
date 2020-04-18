# If/ Else conditions are used to decide to do something based on something being true or false

x = 50
y = 50



# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# if x > y:
#   print(f'{x} is greater than {y}')
# else:
#   print(f'{y} is greater than {x}')

if x > y:
  print(f'{x} is greater than {y}')
elif x == y:
  print(f'{x} is equal to {y}')
else:
  print(f'{y} is greater than {x}')

if x > 2:
  if x <= 10:
    print(f'{x} is greater than 2 and less than 10')

if x > 2 and x <= 10:
  print(f'probably better way to evaluate two conditions')

if not(x == y):
  print(f'{x} does not equal {y}')

# Logical operators (and, or, not) - Used to combine conditional statements




# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1, 2, 3, 4, 5]

if x in numbers:
  print(x in numbers)

if x not in numbers:
  print('not there')



# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

if x is y:
  print('x is y')