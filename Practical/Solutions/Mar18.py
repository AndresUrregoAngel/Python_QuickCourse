from Python_QuickCourse.Practical.Solutions.mtd_march18 import conteo_filas,conteo_smaterter,list_avarage,conteo,smart_avarage,mayor_list
#import conteo_filas,conteo_smaterter,list_avarage,conteo,smart_avarage from Python_QuickCourse.Practical.Solutions.mtd_march18

########### Solutions ################
file= open ("C:\\Users\\Todos\\Documents\\Salaries\\Salaries\\rawdata.csv", "r")
new_file= []
lengu_file= []
Pythonsalary_list = []
PythonUniver_List = []
studies_list= []
year_list= []
city= []
bogota_list= []
#next(file)
for e in file:
   z= e.split(",")
   new_file.append(z)
   lengu_file.append(z[11]) # saving all programming languages in a list
   studies_list.append(z[13])
   city.append(z[32])
   #year_list.append(z[27])
   if (z[11].lower() == "python"):
        #if (z[13] == "universitario"):
        Pythonsalary_list.append(z[19])
   if (z[11].lower() == "python" and "universitario" in z[13].lower()):
       PythonUniver_List.append(int(z[19]))


   if (z[11] == "Python"): # If programming language is python
       year_list.append(z[27])

   if ("bogota" in z[32].lower()):
       bogota_list.append(z[32])

print(city)
print(bogota_list)



"""
#print(year_list)
#print(studies_list)
## 1
print(conteo_filas(new_file))

## 2
print(conteo_smaterter(lengu_file))

## 3
Salary_PythonUniversities = smart_avarage(PythonUniver_List)
print("the avarage list is {}".format(round(Salary_PythonUniversities,2)))
## 4
print("There are ", conteo(studies_list,"UNIVERSITARIO"), "university students")
print("There are ", conteo(studies_list, "TÃ©CNICO"), "technicians")
"""
## 5
"""
counter = 0
for e in lengu_file:
    counter = counter + 1
    if (int(e) < 315):
        print(e)
"""

## 6
#print("The avarage age for Programmers in Python is: ", smart_avarage(year_list))


## 7
#
#print(conteo_smaterter(lengu_file))
print(mayor_list(lengu_file))




