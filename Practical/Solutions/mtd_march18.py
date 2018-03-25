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

def list_avarage (a_list,b_list):
    c_list= []
    counter= 0
    sum= 0
    average = 0
    for e in a_list:
        if (e == "Python" ):
            c_list.append(z[27])
            for i in c_list:
                counter = counter + 1
                sum = sum + int(i)
                average = sum / counter
    #print(c_list)
    return average

def conteo (Plist,name):
    counter = 0
    for e in Plist:
        if (e.upper() == name):
            counter= counter + 1

    return counter


### example avarage method
def smart_avarage (elements_list): # This list must to contain only numeric variables
    counter =0
    accomulative_sum = 0
    for item in elements_list:
        counter += 1  # this variable will count how many elements are in the list
        accomulative_sum = accomulative_sum + item # this variable will contain the accumulative sum amount

    avarage_list = accomulative_sum / counter

    return avarage_list


