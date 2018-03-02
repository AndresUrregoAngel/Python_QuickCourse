#############Methodes#######
def conteo (Plist,Pverificacion):
    counter = 0
    for e in Plist:
        if (e.lower() == Pverificacion):
            counter= counter + 1

    return counter


def conteo_smaterter (Plist):
    item_unique = []
    #counter_list= []

    for item in Plist:
        if (item not in item_unique):
            item_unique.append(item)


    for item in item_unique:

        counter = 0
        for line in Plist:
            if(line == item):
                counter = counter + 1
        print("En el territorio",item , "hay:",counter)
        #counter_list.append(counter)

    return #counter_list
def conteo_filas (fila):
    counter= 0
    for e in new_list:
        counter = counter + 1


    return counter

def suma_lista (l): # Es un metodo con el fin de hacer una suma
    suma= 0
    for e in l:
        suma = suma + e

    return suma








#########Solutions##########
file= open("C:\\Users\\Hewlett Packard\\Documents\\Ejercicios Python\\Multas_y_Sanciones_SECOP_I.csv", 'r', encoding='cp437')
territory= []
new_list= []
zona= []
multas_transmilenio= []
multas_bosa= []


next(file)
for i in file:
    z= i.split(",")
    #print(z[0])
    if ("TRANSMILENIO" in z[0]):
        multas_transmilenio.append (int(z[9]))
    if ("ALCALDAìA LOCAL DE BOSA" in z[0]):
        multas_bosa.append(int(z[9]))

#for i in multas_bosa:
  #  print(i)



"""
    territory.append(z[3])
    new_list.append(z[3])
    zona.append(z[0])
    multa.append(z[9])


print(multa)
"""
'''
print('En el territorio Distrito Capital hay:',conteo(territory,'distrito capital'))
print("En el territorio Nacional hay:", conteo(territory,'nacional'))
print("En el Territorio Nacional Centralizado hay:", conteo(territory,'nacional centralizado'))
print("En el Territorio Departamental Centralizado hay:", conteo(territory,'territorial departamental centralizado'))
print("En el Territorio Departamental Descentralizado hay:", conteo(territory,'territorial departamental descentralizado'))
print("En el Territorio Distrital Municipal Nivel 1 hay:", conteo(territory,'territorial distrital municipal nivel 1'))
print("En el Territorio Distrital Municipal Nivel 2 hay:", conteo(territory,'territorial distrital municipal nivel 2'))
print("En el Territorio Distrital Municipal Nivel 3 hay:", conteo(territory,'territorial distrital municipal nivel 3'))
print("En el Territorio Distrital Municipal Nivel 4 hay:", conteo(territory,'territorial distrital municipal nivel 4'))
print("En el Territorio Distrital Municipal Nivel 5 hay:", conteo(territory,'territorial distrital municipal nivel 5'))
print("En el Territorio Distrital Municipal Nivel 6 hay:", conteo(territory,'territorial distrital municipal nivel 6'))

conteo_smaterter(territory)

for e in file:
    z= i.split(",")
    new_list.append(z[3])
'''
conteo_smaterter(territory)
#print("El numero de filas es:", conteo_filas(new_list))
#print("Hya:", suma(zona,'BOGOTAü D.C. - TRANSMILENIO', multa))
print("Transmilnio pago una multa de: ", suma_lista(multas_transmilenio))
print("Bosa pago una multa de: ", suma_lista(multas_bosa))
