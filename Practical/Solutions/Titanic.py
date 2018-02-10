#with open("C:\\Users\\Hewlett Packard\\Documents\\Ejercicios Python\\titanic1.csv", 'r') as f:
    #print (f.read())

#new_file= open("C:\\Users\\Hewlett Packard\Documents\\Ejercicios Python\\titanic_2.txt", 'w')
'''
next(titanic)
sex= []
counter= 0
for e in titanic:
    x= e.split(',')
    if (x[2]== "Female" and "Masculine"):
        sex.append(int(x[4]))
        print(sex)
'''
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



