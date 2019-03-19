def sum_array(array):

    '''Return sum of all items in array'''
    return sum(array)
    #if len(array) == 1:
        #return array[0]
    #else:
        #return array[0] + sum_array(array[1:])

#print(sum_array([1,3,5,7,9]))
#print(sum_array([]))




def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

#print(fibonacci(0))
#print(fibonacci(1))
#print(fibonacci(3))
#print(fibonacci(8))


def factorial(n):
    x = 1
    y = 2

    while y <= n:
        x = x * y
        y += 1
    return x

print(factorial(5))



def reverse(word):

    '''Return word in reverse'''
    word = "".join(reversed(word))
    return word
#print (reverse('2111'))
