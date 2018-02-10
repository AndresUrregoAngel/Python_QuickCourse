input_f = open("C:\\Users\\Hewlett Packard\Documents\\Ejercicios Python\\pensionados.txt","r")
output_f = open('C:\\Users\\Hewlett Packard\Documents\\Ejercicios Python\\NewFile.txt',"w")
#next(input_f)
'''
for i in input_f:
    x = i.split(',')
    if (int(x[3])>1000):
        new_line = "{},{},{}".format(str(x[0]),str(x[1]),str(x[3]))
        output_f.write(new_line)

#next(input_f)
counter= 0
New_list=[]
for i in input_f:
    x= i.split(',')
    Date= x[0]
    año= Date[:4]
    output_f.write(año)
    #print(año)
    if (x[1] == 'Veterans Affairs Canada' and int(año) == 2010):
        #print(año, x[1], x[3])
        New_list.append(int(x[3]))


suma= 0
for i in New_list:
    suma= suma + i
    counter= counter + 1



print("El promedio de los pensionados en Veterans Affairs Canada es: ", round(suma/counter,1))
'''
counter= 0
for i in input_f:
    x= i.split(',')
    counter= counter + 1
    #len(i + str(counter))


print("The number of rows that are in the files are:", str(counter))

for i in  input_f:
    x= i.split(',')


















