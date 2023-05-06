print('hello world')

# Binary Search

def binary_search(list, item):

    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None    

my_list = [1, 3, 6, 15, 29, 50]

print(binary_search(my_list, 3))
print(binary_search(my_list, 29))
print(binary_search(my_list, 50))


# okay, i am back. Need to make sure and code for 1 hour a day

# Alex just got a new hula hoop, he loves it but feels discouraged because his little brother is better than him

# Write a program where Alex can input (n) how many times the hoop goes round and it will return him an encouraging message :)

#     If Alex gets 10 or more hoops, return the string "Great, now move on to tricks".
#     If he doesn't get 10 hoops, return the string "Keep at it until you get it".

def hoopCounts(n):
    if n >= 10:
        print('Great work')
    else:
        print('Nope fucko, keep trying.')
        