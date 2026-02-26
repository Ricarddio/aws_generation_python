import re

#ABRIMOS EL ARCHIVO de texto

with open("preproinsulin-seq.txt" , "r") as f:
    
    #leemos el contenido del texto
    raw_data=f.read()
    

#eliminamos la palabra ORIGIN
clean_data = re.sub(r"\bORIGIN\b", "", raw_data, flags= re.IGNORECASE)


#Eliminamos el terminador de registro
clean_data = clean_data.replace("//","")

#Eliminar cualquier cosa que no sea letra.
clean_data = re.sub(r"[^A-Za-z]", "", clean_data)

#convertimos a minúsculas
clean_data = clean_data.lower() 

#abrir nuevamente el archivo prepoinsulin

with open("prepoinsulin-seq.txt", "w") as f:
    
    #limpiamos el archivo
    f.write(clean_data)
    


#calculñamos la longitud de prepoinsulina    
print ("Longitud prepoinsulina = ", len(clean_data))

if len(clean_data) != 110:
    print("Error, la secuencia no tiene 110 caractéres")
    exit()
    
lsinsulin = clean_data[0:24]
binsulin = clean_data[24:54]
cinsulin = clean_data[54:89]
ainsulin = clean_data[89:110]

with open("lsinsulin-seq-cleant.txt","w") as f:
    f.write(lsinsulin)

with open("binsulin-seq-cleant.txt","w") as f:
    f.write(binsulin)

with open("cinsulin-seq-cleant.txt","w") as f:
    f.write(cinsulin)
    
with open("ainsulin-seq-cleant.txt","w") as f:
    f.write(ainsulin)

#verificamos el tamano de caracteres
print("lsinsulin = ", len(lsinsulin))
print("binsulin = ", len(binsulin))
print("cinsulin = ", len(cinsulin))
print("ainsulin = ", len(ainsulin))

insulin = binsulin + ainsulin
#total de insulina
print("insulina procesada= ", len(insulin))

#secuencia d ela insulina
print("secuencia de la insulina = ", insulin )

    