# print('hello world')

# # Binary Search

# def binary_search(list, item):

#     low = 0
#     high = len(list) - 1

#     while low <= high:
#         mid = (low + high)
#         guess = list[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None    

# my_list = [1, 3, 6, 15, 29, 50]

# print(binary_search(my_list, 3))
# print(binary_search(my_list, 29))
# print(binary_search(my_list, 50))


# # okay, i am back. Need to make sure and code for 1 hour a day

# # Alex just got a new hula hoop, he loves it but feels discouraged because his little brother is better than him

# # Write a program where Alex can input (n) how many times the hoop goes round and it will return him an encouraging message :)

# #     If Alex gets 10 or more hoops, return the string "Great, now move on to tricks".
# #     If he doesn't get 10 hoops, return the string "Keep at it until you get it".

# def hoopCounts(n):
#     if n >= 10:
#         print('Great work')
#     else:
#         print('Nope fucko, keep trying.')




# # Fix the function

# # I created this function to add five to any number that was passed in to it and return the new value. It doesn't throw any errors but it returns the wrong number.

# # Can you help me fix the function?

# def add_five(num):
#     total = num + 5
#     return total


# # Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
# # Examples

# # "This is an example!" ==> "sihT si na !elpmaxe"
# # "double  spaces"      ==> "elbuod  secaps"


# def reverse_words(text):
    
#     words = text.split(" ")
#     for i in range(len(words)):
#         words[i] = words[i][::-1]
#     return " ".join(words)
    


# # Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# # Examples:

# # solution('abc', 'bc') # returns true
# # solution('abc', 'd') # returns false

# def solution(string, ending):
#     return string.endswith(ending)
#     pass


# # Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

# def bool_to_word(boolean):
#     if boolean:
#         return 'Yes'
#     else:
#         return 'No'
    
# def bool_words(bool):
#     return 'Yes' if bool else 'No'



# # You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

# def get_middle(word):
#     # get the length of the word
#     length = len(word)
#     # check if word is even
#     if length % 2 == 0: 
#         # divide the word in 2 and return the middle two letters
#         return word[length // 2 - 1:length // 2 + 1]
#     else:
#         # if odd, return the middle letter
#         return word[length // 2]


# # Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

# # Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.


# def lovefunc( flower1, flower2 ):
#     if flower1 %2 == 0 and flower2 %2 != 0:
#         return True
#     elif flower1 %2 != 0 and flower2 %2 == 0:
#         return True
#     else: 
#         return False


# # 217. Contains Duplicate
# # Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """

#         # set can not contain multiple of same, check if length is same as nums
#         # return
#         nums_set = len(set(nums))
        
#         return nums_set != len(nums)

# class Solution(object):
#     def hasDupes(nums):
#         nums.sort()

#         for i in range(len(nums) - 1):
#             if nums[i] == nums[i + 1]:
#                 return True
#         return False
    


# class Solution(object):
#     def containsAnagram(s, t):
#         # check correct length
#         if len(s) != len(t):
#             return False
        
#         # convert lists for easier comparison
#         s_chars = list(s)
#         t_chars = list(t)

#         # sort low to high
#         s_chars.sort()
#         t_chars.sort()

#         # if correct, true
#         return s_chars == t_chars
    

#     print(containsAnagram('manage', 'manager'))
#     print(containsAnagram('rat', 'tar'))
#     print(containsAnagram('popular', 'movies'))
    

# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

# Write a function which takes a list of strings and returns each line prepended by the correct number.

# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

# def number(lines):
#     numbered_lines = []
#     for i, line in enumerate(lines):
#         numbered_lines.append(str(i + 1)+ ": " + line)
#     return numbered_lines
        
# def num(lines):
#     return(f"{i + 1}: {line}" for i, line in enumerate(lines))

# print(num(['a', 'b', 'c']))


