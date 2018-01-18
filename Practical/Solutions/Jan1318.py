input_f = open("E:\\Sources\\ssa-pop3-eng.csv", "r")
output_f = open("E:\\Sources\\output.txt", "w")
next(input_f)

for i in input_f:
    x = i.split(',')
    if (int(x[3])>1000):
        new_line = "{},{},{}".format(str(x[0]),str(x[1]),str(x[3]))
        output_f.write(new_line)










for element in input_f:
    print(element)

