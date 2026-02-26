#ejercicio1
#creamos una varibalemyString y dentro de ella se guarda el texto ""this is a string
myString = "This is a string."

print(myString)

print(type(myString))

print(myString + " is of the data type " + str(type(myString)))

#ejercicio 2
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString


print(thirdString)

#ejercicio 3
name = input("What is your name? ")
print(name)

#ejercicio 4
#sustituye los corchetes por las variables que pongas en format
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))
