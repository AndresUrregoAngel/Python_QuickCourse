input_f = open("C:\\Users\\P928260\\Downloads\\ssa-pop3-eng.csv","r")
output_f = open("C:\\Users\\P928260\\Downloads\\output.txt","w")
next(input_f)


##  First point

for line in input_f:
    item = line.split(',') 
    if(int(item[3]) > 1000):
        new_line = "{},{},{}".format(str(item[0]),str(item[1]),str(item[3]))
        output_f.write(new_line + '\n')

   

output_f.close()
input_f.close()
 

##  Second point

employ_veterans = []
sum_empl = 0

for line in input_f:
    item = line.split(',')
    year_file = item[0][:4]
    #print(item[1].lower())
    if ( "veterans" in item[1].lower() and int(year_file) == 2010 ):
        employ_veterans.append(int(item[3]))

 
controler = False
while (controler != True):
       
    for item in employ_veterans:
        sum_empl +=item

    avg_emplo = sum_empl / len(employ_veterans)
    #print(sum_empl , len(employ_veterans))
    print('the avarage employee is: {}'.format(round(float(avg_emplo),2)))

    controler = True




##  Third Point

line_counter = 0
for line in input_f:
    line_counter += 1
 

print("the file has {} rows".format(int(line_counter)))


### Plus

years_unique = []
controler = False

while(controler != True):

        #Get a list with the read years
        for line in input_f:
            item = line.split(',')
            year_f = item[0][:4]

            if (year_f not in years_unique):
                years_unique.append(year_f)

           
        for year in years_unique:
            print(year)

       controler = True
