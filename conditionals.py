#se va a crear un vañidador para saber si podemos o no entrar a una fiesta
#es importante agregar que para entrar a la fiesta debes ser mayor de edad
#se crea la variable edad y en ella se va a guardar lo que escriba el ususario

edad=input("Escriba su edad_: ")
dinero=input("Escriba su dinero_: ")

#convertimos la varibale de entrada a entero debido a que cuando se escribe por consola el valor 
#guardado es texto (str)
edad=int(edad)
dinero=int(dinero)

#vamos a comparar si la edad es mayor
#aqui se imprime si la edad es mayor o igual a los 18 años
#si no se cuumple la condicióm de er mayor de 18 años, imprime "no puede entrar"

if edad >= 18 :

    if dinero >= 600 :
        print("Puede entrar")
    else:
        print("no puede entrar")
        
else:
    print("no puede entrar")
    
    
if edad >=18 and dinero >=600:
    print ("v2 puede entrar")
    
else: 
    print("v2 no puede entrar")
    
    
dinero =input("escriba el dinero en su cuenta")
dinero=int(dinero)

"""
laboratorio

creamos una variable ussrreply y en ella guardamos lo que describa el ususario
si lo que hay en la variable es exactamente yes ==yes entonces se imprime la ayuda
de lo contrario dice que no
"""
userReply = input("Do you need to ship a package? (Enter yes or no) ")
if userReply == "yes":
    print("We can help you ship that package!")
    
else:
    print("Please come back when you need to ship a package. Thank you.")
    
    """
    en la variable userReply guardamos una de estas opciones stamps, envelope o copy
    si la variable == stamps imrpimimos stamps
    si la variable == envelope imrpimimos envelope
    si la variable == copues imrpimimos copies


    
    
    """
    
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
    
    



    




    