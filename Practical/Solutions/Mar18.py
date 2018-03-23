############## Methodes ###########
def conteo_filas (fila):
    counter= 0
    for e in fila:
        counter = counter + 1


    return counter









########### Solotions #####
file= open('C:\\Users\\Hewlett Packard\\Documents\\Documentos Python\\Salaries\\rawdata.csv', "r")
new_file= []
for e in file:
   z= e.split(",")
   new_file.append(z)

## 1
print(conteo_filas(new_file))

## 2