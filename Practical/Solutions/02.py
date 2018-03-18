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


def suma_smart (List):
    any_list: []
    for year in List:
        if (year not in any_list):
            any_list.append (year)

    for i in any_list:
        sum= 0

        for e in List:
            if (e ==year):
                sum= sum + e
        print("En el año se debe:", sum)

    return



def compare_lists(list1,list2):


    for item1 in list1:
        total_sum = 0
        for item2 in list2:
            if (item1 == item2[0]):
                total_sum = total_sum + float(item2[1])

        print("the territory:", item1 ," has penalty amount of:", total_sum)











#########Solutions##########
file= open("E:\\Sources\\Multas_y_Sanciones_COL\\Multas_y_Sanciones_SECOP_I.csv", 'r', encoding='cp437')
territory= []
new_list= []
zona= []
multas_transmilenio= []
multas_bosa= []
year=[]
penalty_terrlist = []


next(file)
for i in file:
    z= i.split(",")
    #print(z[0])
    territory.append(z[3])
    new_list.append(z[3])
    if ("TRANSMILENIO" in z[0]):
        multas_transmilenio.append (int(z[9]))
    if ("ALCALDAìA LOCAL DE BOSA" in z[0]):
        multas_bosa.append(int(z[9]))
    penalty_terr = z[3],z[9]
    penalty_terrlist.append(penalty_terr)

"""
   
    zona.append(z[0])
    multa.append(z[9])


print(multa)
"""
'''
conteo_smaterter(territory)

for e in file:
    z= i.split(",")
    new_list.append(z[3])
'''

#print(conteo_smaterter(territory)) # Point 1

#print("El numero de filas es:", conteo_filas(new_list)) # Point 3
#print("Transmilenio pago una multa de: ", suma_lista(multas_transmilenio)) # Point 4
#print("Bosa pago una multa de: ", suma_lista(multas_bosa)) # Point 5
print(compare_lists(territory,penalty_terrlist))
