from Practical.Solutions.mtd_march18 import conteo_filas,conteo_smaterter,list_avarage,conteo,smart_avarage


########### Solutions ################
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

Salary_PythonUniversities = smart_avarage(PythonUniver_List)
print("the avarage list is {}".format(round(Salary_PythonUniversities,2)))


