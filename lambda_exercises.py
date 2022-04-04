""" 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
"""

from http.client import PRECONDITION_REQUIRED
from itertools import count
import string


original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


filtered_list = list(filter(lambda num: num % 2 == 0, original_list))

print(filtered_list)

filtered_list = list(filter(lambda num: num % 2 != 0, original_list))

print(filtered_list)

"""
 2)
find which days of the week have exactly 6 characters.
"""

weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

filtered_list2 = list(filter(lambda n: len(n) == 6, weekdays))

print(filtered_list2)

""" 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

"""
Original_list = ["orange", "red", "green", "blue", "white", "black"]

Remove_words = ["orange", "black"]

filtered_list3 = list(filter(lambda x: x not in Remove_words, Original_list))

print(filtered_list3)


""" 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 """
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]
filtered_list4 = list(filter(lambda x: x not in list2, list1))

print(filtered_list4)


""" 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

"""
o1= ['red', 'black', 'white', 'green', 'orange']

substring1= "ack"

filtered_list5 = list(filter(lambda x: substring1 in x, o1))

print(filtered_list5)

substring2= "abc"

filtered_list6 = list(filter(lambda x: substring2 in x, o1))

print(filtered_list6)


""" 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
"""


str1 = input("Type a string")
check1 = lambda str1: any(x.isupper() for x in str1)
print(check1(str1))
check2 = lambda str1: any(x.islower() for x in str1)
print(check2(str1))
check3= lambda str1: any(x.isdigit() for x in str1)
print(check3(str1))
check4= lambda str1: len(str1) >= 8
print(check4(str1))




"""
 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

original_scores.sort(key = lambda x: x[1])

print(original_scores)