# Q.1 Write a Python program which accepts the user's first and last name and prints them in reverse order with a space between them.

# firstName = input("enter your first name : ");
# lastName = input("enter your last name : ");
# print(lastName + " " + firstName);







# Q.2 Write a Python program which accepts a sequence of comma-separated numbers from the user and generates a list and a tuple with those numbers.

# values = input("enter comma seprates numbers : ")
# list = values.split(" , ");
# tuple = tuple(list);
# print('list : ',list);
# print('tuple : ',tuple)







# Q.3 Write a Python program to display the first and last colours from the following list. 
# color_list = ["Red","Green","White" ,"Black"]

# color_list = ["red","green","white","black"];
# print("First color of the list : "+color_list[0]+ "\nLast color of the list : "+color_list[3])







# Q 4 Write a Python program to print the calendar of a given month and year.

# import calendar

# y = int(input("enter the year : "))
# m = int(input("enter the month : "))
# print(calendar.month(y,m))







# Q 5 Write a Python program to calculate number of days between two dates

# from datetime import date

# f_date = date(2014, 7, 2)
# l_date = date(2014, 7, 11)

# delta = l_date - f_date 
# print(delta.days)








# Q 6 Write a Python program to check whether a specified value is contained in a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

# def list(list_data,n):
#     for value in list_data:
#         if n==value:
#          return True
#     return False
# print(list([1,5,8,3],3))
# print(list([1,5,8,3],-1))








# Q 7 Write a Python program to print out a set containing all the colors from color_list_1 which are
# not present in color_list_2.
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])

# color_list_1 = set(["white","black","red"])
# color_list_2 = set(["red","green"])
# print("different color in color_list_1 to color_list_2")
# print(color_list_1.difference(color_list_2))
# print("different color in color_list_2 to color_list_1")
# print(color_list_2.difference(color_list_1))








# Q 8 Write a Python program to get the current username

# import os
# user = os.getlogin()
# print(user)








# Q 9 Write a python program to access environment variables.

# import os
# print(os.environ)







# Q 10 Write a program to get execution time for a Python method.

# import time

# start = time.time()

# a=0
# for i in range(1000):
#     a += (i**100)

# end = time.time()

# print("time take to execute program : ",end-start)









# Q 11 Write a Python program to get file creation and modification date/times.

# import os.path, time
# file = "./assingment.py"

# mod = os.path.getmtime(file)
# cre = os.path.getctime(file)
# print("modified time : ",time.ctime(mod))
# print("created time : ",time.ctime(cre))









# Q 12 Write a Python program to sort three integers without using conditional statements and
# loops


# x = int(input("enter first number : "))
# y = int(input("enter second number : "))
# z = int(input("enter third number : "))

# a1 = min(x,y,z)
# a3 = max(x,y,z)
# a2 = (x+y+z)-a1-a3

# print("after sorting : ",a1,a2,a3)









# Q 13 Write a Python program to get the system time.

# from datetime import datetime
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# print("current time : ",current_time)









# Q 14 Write a Python program to clear the screen or terminal.

# import os
# import time
# os.system("ls")
# time.sleep(2)
# os.system('clear')







# Data Structure



# Q 1. Write a Python program to create an array of 5 integers and display the array items.
# Access individual element through indexes.

# from array import *
# a = array('i',[2,3,4,5])
# for i in a:
#     print(i)
# print("access all numbers in array..")
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])







# Q 2 Write a Python program to reverse the order of the items in the array.

# from array import *
# my_array = array('i',[5,3,6,7,8])
# print("original array : "+str(my_array))

# my_array.reverse()
# print("after reversing array : ")
# print(str(my_array))








# Q 3. Write a Python program to get the number of occurrences of a specified element in an
# array

# from array import *
# my_array = array('i',[5,4,3,6,7,3,8,3])
# print("original array : "+str(my_array))

# print("ocurrance of 3 is array : "+str(my_array.count(3)))








# Q 4 Write a Python program to remove the first occurrence of a specified element from an
# array. 

# from array import *
# my_array = array('i',[4,3,5,3,7,3,8])
# print("original array : "+str(my_array))

# my_array.remove(3)
# print("after removing first occurance of 3 from array : "+str(my_array))
