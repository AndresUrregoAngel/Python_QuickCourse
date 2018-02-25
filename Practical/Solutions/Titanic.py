#with open("C:\\Users\\Hewlett Packard\\Documents\\Ejercicios Python\\titanic1.csv", 'r') as f:
    #print (f.read())

#new_file= open("C:\\Users\\Hewlett Packard\Documents\\Ejercicios Python\\titanic_2.txt", 'w')

#next(titanic)
sex= []
counter= 0
for e in titanic:
    x= e.split(',')
    if (x[2]== "Female" and "Masculine"):
        sex.append(int(x[4]))
        print(sex)

f= open("C:\\Users\\Hewlett Packard\\Documents\\Ejercicios Python\\titanic1.csv", 'r')
c= open("C:\\Users\\Hewlett Packard\Documents\\Ejercicios Python\\titanic_2.txt", 'w')
new= []
counter= 0
male= 0
female= 0
next(f)
for i in f:
    x= i.split(',')
    if (x[5] == str ("male")):
        male= male + 1
    else:
        female= female + 1

print( male, female)
        #new.append(x[5])
f.close()
f= open("C:\\Users\\Hewlett Packard\\Documents\\Ejercicios Python\\titanic1.csv", 'r')
survived= 0
next(f)
for i in f:
    x= i.split(',')
    if (int(x[1]) == 1):
        survived = survived + 1
print(survived)

f.close()

f= open("C:\\Users\\Hewlett Packard\\Documents\\Ejercicios Python\\titanic1.csv", 'r')
#f = open("E:\\Sources\\titanic.csv","r")
next(f)
age_list = []
for e in f:
    x= e.split(',')
    if (x[6] == ''):
        age_list.append(0)
    else:
        age_list.append(float(x[6]))

    #if (int (x[6]) < 30):
     #   print(x[6])
young= 0
mature= 0
old= 0
young_list= []
mature_list= []
old_list= []
for age in age_list:
    if (age < 30 ):
        young= age + 1
        young_list.append(young)
    if (age <= 31 and 51):
            mature+= 1
            mature_list.append(mature)
    if (age > 51 ):
        old =old + 1
        old_list.append(old)

print("the number of young people who climbed the Titanic was",young)
print("the number of mature people who climbed the Titanic was",mature)
print("the number of old people who climbed the Titanic was",old)
print("List Young",young_list)
print("List Mature",mature_list)
print("List Old",old_list)











