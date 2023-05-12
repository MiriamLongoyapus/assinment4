#Write a function that takes an unknown number of arguments and returns their sum.
def my_fun(*args):
    return sum(args)
print(my_fun(50,60))


#Write a function that takes two arguments, the first being a string and the second being an 
# #unknown number of integers. The function should return a new string where the integers have been added to the original string.
def string(str,num):
    empty_string=""
    for n in range(0,num):
        empty_string +=str
        return empty_string
print(string("Miriam",2))

#Write a function that takes an unknown number of keyword arguments and returns a dictionary where
# the keys are the argument names and the values are the argument values.
def nums(**kwargs):
    return kwargs
print(nums(a=5))

#Write a function that takes a function and an unknown number of arguments, and returns the result 
#of calling the function with the arguments.

#Write a function that takes a list of integers and an unknown number of keyword arguments. The function 
#should return a new list where each integer in the original list has been multiplied by the value of the 
#corresponding keyword argument.

#Write a function that takes a list of integers and an unknown number of additional integers as arguments. The function
# should return the index of the first occurrence of the sum of the list and the additional integers
def list_integers(list, y):
    sum=(list) + sum(y)
    for i in y:
        if list == sum:
            return i
list=[10,34]
print(list_integers(list))

#Write a function that takes an unknown number of keyword arguments, each with a string value. The function should concatenate
# all the strings and return the resulting string.