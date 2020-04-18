# Python has functions for creating, reading, updating, and deleting files.
myFile = open('myfile.txt', 'w')

print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

myFile.write('I love Python')
myFile.write(' and Javascript')
myFile.close()

myFile = open('myFile.txt','a')
myFile.write('I also like PHP')
myFile.close()

myFile = open('myFile.txt','r+')
text = myFile.read(100)
print(text)