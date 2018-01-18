'''
# Functions by default in Python

name = "Owen Likes So much EAT"
print(name.lower()) # Function for lower letters
print (name.upper()) # Function for capital letters

numbers = []

for i in range(20):
    numbers.append(i)


numbers.remove(2)

for i in numbers:
    print(i)
    '''

# Customized methodes
'''
number1 = input('type first number')
number2 = input('type second number')

#sum = int(number1) + int(number2)

def metd_sum (n1,n2):
    sum = int(n1) + int(n2)
    return sum

result = metd_sum(number1,number2)

print("your sum is {}".format(result))
'''

l1 = [1,2,3,4,5,6]
l2 = [7,8,9,4,10,2,5,6]


def avg_list(numbers):
    count_sum = 0
    for i in numbers:
        count_sum += i

    return count_sum / len(numbers)

print(avg_list(l1))
print(avg_list(l2))



