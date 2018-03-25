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







########### Solotions ################
file= open('E:\\Sources\\Salaries\\rawdata.csv','r')#open ('C:\\Users\\Hewlett Packard\\Documents\\Documentos Python\\Salaries\\Salaries\\rawdata.csv', "r")
new_file= []
lengu_file= []
Pythonsalary_list = []
PythonUniver_List = []
studies_list= []
year_list= []
#next(file)
for e in file:
   z= e.split(",")
   new_file.append(z)
   lengu_file.append(z[11]) # saving all programming languages in a list
   studies_list.append(z[13])
   #year_list.append(z[27])
   if (z[11].lower() == "python"):
        #if (z[13] == "universitario"):
        Pythonsalary_list.append(z[19])
   if (z[11].lower() == "python" and "universitario" in z[13].lower()):
       PythonUniver_List.append(int(z[19]))


   if (z[11] == "Python"): # If programming language is python
       year_list.append(z[27])









#print(year_list)
#print(studies_list)
## 1
#print(conteo_filas(new_file))

## 2
#print(conteo_smaterter(lengu_file))

## 3
#print("The average salary for people who program in python is:", suma/ counter)
## 4
#print("There are ", conteo(studies_list,"UNIVERSITARIO"), "university students")
#print("There are ", conteo(studies_list, "TÃ©CNICO"), "technicians")

## 6
"""
for e in file:
z= e.split(",")
if (z[11]== "Python"):
   year_list.append(z[27])
print(year_list)

suma= 0
counter= 0
avarage = 0
for i in year_list:
suma = suma + int(i)
counter = counter + 1
avarage = suma / counter
print("The average age for Python programmers is: ",avarage)
"""


### example avarage method

def smart_avarage (elements_list): # This list must to contain only numeric variables
    counter =0
    accomulative_sum = 0
    for item in elements_list:
        counter += 1  # this variable will count how many elements are in the list
        accomulative_sum = accomulative_sum + item # this variable will contain the accumulative sum amount

    avarage_list = accomulative_sum / counter

    return avarage_list


example_list = ['3',2,1,5,6]

Salary_PythonUniversities = smart_avarage(PythonUniver_List)
print("the avarage list is {}".format(round(Salary_PythonUniversities,2)))


