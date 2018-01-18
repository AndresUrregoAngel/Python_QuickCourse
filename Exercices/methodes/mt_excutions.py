
def numb_sum(n1,n2):
    sum = int(n1) + int(n2)
    return sum

def pair_numbers(numbers):
    counter_pair = 0
    for i in numbers:
        if(i % 2 == 0):  #mod
            print('this number is pair {}'.format(i))
            counter_pair += 1

    return print('in your list were {} of pairs'.format(int(counter_pair)))