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
        print("-In ",item.lower(), "There are:",counter)

    return


def list_avarage (a_list,b_list):
    c_list= []
    counter= 0
    sum= 0
    average = 0
    for e in a_list:
        if (e == "Python" ):
       #     c_list.append(z[27])
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
        accomulative_sum = accomulative_sum + int(item) # this variable will contain the accumulative sum amount

    avarage_list = accomulative_sum / counter

    return round(avarage_list,1)



def mayor_list (Plist):
    item_unique = []
    counter_file = []

    """This for is used to create a list with a unique language programming"""
    for item in Plist:
        if (item not in item_unique):
            item_unique.append(item)

    """This for is used to create a list with the counter of language programming
        from the original list"""
    for item in item_unique:
        counter = 0
        for line in Plist:
            if (line == item):
                counter = counter + 1
        counter_file.append((item,counter)) # I leave this line at the same level of the for by item

    maximo= 0 # variable used to store the maximum value

    """This loop is used to find out the maximum value of counter by 
        language programming and save it in a variable"""
    for languages in counter_file:
        if (languages[1] > maximo):
            maximo = languages[1]

    """Looking for the language within the list that match the 
        value of the variable maximum"""
    for languages in counter_file:
        if(languages[1]== maximo):
            print('the most popular language programming is:',languages)



def mayor_list_dictionary (Plist):
    counter_file = {}  # This is a dictionary structure

    """This for is used to create a key with a unique language programming"""
    for item in Plist:
        if (item not in counter_file):
            key = item # define for every language programming a key for my dictionary
            counter_file.setdefault(key, []) # Add the key to a dictionary with a default value of  zero

    """This loop is used to find out the maximum value of counter by 
        language programming and save it the key and value that match with the key"""
    for key in counter_file.keys():  # I need to go thru the entire list looking for the key in the dictionary
        counter = 0                  # by every key I use the counter to count the new line
        for line in Plist:
            if (line == key):
                counter = counter + 1
        counter_file.setdefault(key, []).append(counter) # finally I update the valu of my key with the last
                                                         # value of counter by key

    maximum_key = max(counter_file, key=counter_file.get)  # I get the key with the maximum value

    for k, v in counter_file.items(): # I look for the key equals to maximum and print it
        if (k == maximum_key):
            print('the most popular language programing is {} with {} number of developers'.format(k,v))


def mayor_list_avg (Plist,listSalary):
    item_unique = []
    counter_file = []
    lengu_file= []
    item_file = []

    """This for is used to create a list with a unique language programming"""
    for item in Plist:
        if (item not in item_unique):
            item_unique.append(item)

    """This for is used to create a list with the counter of language programming
        from the original list"""
    for item in item_unique:
        counter = 0
        for line in Plist:
            if (line == item):
                counter = counter + 1
        counter_file.append((item,counter)) # I leave this line at the same level of the for by item
        item_file.append(item)

    maximo= 0 # variable used to store the maximum value

    """This loop is used to find out the maximum value of counter by 
        language programming and save it in a variable"""
    for languages in counter_file:
        if (languages[1] > maximo):
            maximo = languages[1]

    """Looking for the language within the list that match the 
        value of the variable maximum"""
    for languages in counter_file:
        if(languages[1]== maximo):
            lengu_file.append(maximo)
            print('the most popular language programming is:',languages)
    maximo= 0
    counter= 0
    for max in item_file:
        counter = counter + 1
        if (counter[1]> maximo):
            maximo = counter


"""
    for max in item_file:
       # if (max [1] == maximo):)
 """
def Avg_smaterter (Plist, Salary):
    item_unique = []

    for item in Plist:
        if (item not in item_unique):
            item_unique.append(item)


    for item in item_unique:

        counter = 0
        for line in Plist:
            if(line == item):
                counter = counter + 1
        print("-In ",item.lower(), "There are:",counter)
