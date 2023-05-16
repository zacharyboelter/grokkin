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




# Fix the function

# I created this function to add five to any number that was passed in to it and return the new value. It doesn't throw any errors but it returns the wrong number.

# Can you help me fix the function?

def add_five(num):
    total = num + 5
    return total


# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
# Examples

# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"


def reverse_words(text):
    
    words = text.split(" ")
    for i in range(len(words)):
        words[i] = words[i][::-1]
    return " ".join(words)
    


# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def solution(string, ending):
    return string.endswith(ending)
    pass


# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

def bool_to_word(boolean):
    if boolean:
        return 'Yes'
    else:
        return 'No'
    
def bool_words(bool):
    return 'Yes' if bool else 'No'



# You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

def get_middle(word):
    # get the length of the word
    length = len(word)
    # check if word is even
    if length % 2 == 0: 
        # divide the word in 2 and return the middle two letters
        return word[length // 2 - 1:length // 2 + 1]
    else:
        # if odd, return the middle letter
        return word[length // 2]



def lovefunc( flower1, flower2 ):
    if flower1 %2 == 0 and flower2 %2 != 0:
        return True
    elif flower1 %2 != 0 and flower2 %2 == 0:
        return True
    else: 
        return False