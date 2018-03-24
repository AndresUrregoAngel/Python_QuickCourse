############## Methodes ###########
def conteo_filas (fila):
    counter= 0
    for e in fila:
        counter = counter + 1


    return counter


def conteo_smaterter (Plist):
    item_unique = []

    for item in Plist:
        if (item not in item_unique):
            item_unique.append(item)


    for item in item_unique:

        counter = 0
        for line in Plist:
            if(line == item):
                counter = counter + 1
        print("- language of Programing: ",item , "were surveyed:",counter)

    return

def average_rows (any_list,name,list_cost):
    counter= 0
    sum= 0
    average = 0
    for e in any_list:

        for i in list_cost:
        if (e == name ):
            counter = counter + 1
            for i in list_cost:
                sum = sum + int(i)
                average = sum / counter
             # print(sum)
    return counter, average, sum













########### Solotions ################
file= open ('C:\\Users\\Hewlett Packard\\Documents\\Documentos Python\\Salaries\\Salaries\\rawdata.csv', "r")
new_file= []
lengu_file= []
cost_list= []
for e in file:
   z= e.split(",")
   new_file.append(z)
   lengu_file.append(z[11])
   cost_list.append(z[19])
#print(cost_list)

#print(lengu_file)

## 1
#print(conteo_filas(new_file))

## 2
#print(conteo_smaterter(lengu_file))

## 3
print(average_rows(lengu_file,"Python", cost_list))
print(cost_list)
## 4

for e in cost_list