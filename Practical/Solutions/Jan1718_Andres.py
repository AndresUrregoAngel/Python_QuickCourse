#################### methodes ####################

def open_file(file_name):
        input_file = open(file_name,'r')
        return input_file

def generic_counter(info_list,parameter_req):
    counter = 0
    for item in info_list:
        if(item == parameter_req):
            counter += 1
    
    return counter

def ages_counter(ages_list,min_age,limit_age):
        counter_age = 0
        for item in ages_list:
            if (item >= min_age and item <= limit_age):
                counter_age += 1
        
        return counter_age

    
def  classes_counter (class_list):
    validation = False
    class_counter = []
    
    while( validation != True):
        class_unique = []
        
        for item in class_list:
            if (item not in class_unique):
                class_unique.append(item)
                
        
        for item_unique in class_unique:
            counter_byclass = 0
            for item_class in class_list:
                if (item_class == item_unique):
                    counter_byclass +=1
            
            class_counter.append((item_unique,counter_byclass))
        
        validation = True
    
    return class_counter
    


###################### Solutions  ###################    

file_name = 'titanic.csv' ## file path
info = open_file(file_name) ## Open the file
gender_list = [] ## Create a list based in the passagers gender
survived_list = [] ## List to keep the survival info 
ages_list = []  ## List to keep the age info
class_list = []  ## List to keep teh class info


next(info)
for line in info:
    field = line.split(',')
    gender_list.append(field[5])
    survived_list.append(field[1])
    if (field[6] == ''):
        ages_list.append(0)
    else:
        ages_list.append(float(field[6]))    
    class_list.append(field[2])

    
info.close()

male_qty = generic_counter(gender_list,'male')  ## calculate qty man
woman_qty = generic_counter(gender_list,'female') ## calculate qty woman
survived = generic_counter(survived_list,'1')  ## calculate qty survived
young_passangers = ages_counter(ages_list,0,30) ## calculate qty young people
mature_passangers = ages_counter(ages_list,31,50)  ## calculate qty mature people
old_passangers = ages_counter(ages_list,51,200)  ## calculate qty old people
classes_validation = classes_counter(class_list) ## Execute methode to get the qty of people by class


# First point
print("In the titanic were {} of woman and {} of mans".format(str(male_qty),str(woman_qty)))


# second point
print("In the titanic survived {} people".format(str(survived)))

# third point
print("The people pass away in the Titanic was categorized in: Young: {} , Mature: {}, Old: {}".format(str(young_passangers),str(mature_passangers),str(old_passangers)))

#Fourth point

for info in classes_validation:
    print ("The qty of people passed away is {}".format(str(info)))
