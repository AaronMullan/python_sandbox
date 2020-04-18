# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

class User:
  #constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
  
  def greeting(self):
    return f'My name is {self.name} and I am {self.age}'
  
  def has_birthday(self):
    self.age += 1

#extend class
class Customer(User):
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    self.balance = 0

  def set_balance(self, balance):
    self.balance = balance
  
  def greeting(self):
    return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

#init object

aaron = User('Aaron Mullan', 'brad@gmail.com', 42)

karen = Customer('Karen Griswold', 'karen@gmail.com', 44)
karen.set_balance(500)

aaron.has_birthday()
print(aaron.greeting())
print(karen.greeting())