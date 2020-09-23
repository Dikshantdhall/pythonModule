# 1

a,b,c = 1, 2.01, "string"

#2
a = 1 + 2j
b = 10
a, b = b, a 

# 3

# //// with result name 
firstNum = 10 
secNum = 30.0
resName = firstNum 
firstNum = secNum
secNum = resName

# /////without result name 
firstNum = 40.0 
secNum = 50
firstNum, secNum = secNum, firstNum


# 4 
# using python2 
userValue = raw_input("enter the value")
print(userValue)
# using Python3 
userValue = input("Enter the value")
print(userValue)


#5
firstNum = int(input("Enter the first Number"))
secNum = int(input("Enter the second Number"))
z = firstNum + secNum
result = z + 30
print(result)

# 6
value = eval(input("enter the value"))
print("The input value data type is : " + str(type(value)))

# 7
# using camelCase
firstNum = 10 
# using ladderCase
first_num =10
# using upperCase
FIRSTNUM = 10 

# 8
yes the value will be changed. Variables are essentially like an empty box, that can contain something like a string, number, or other value. When you assign it a value, the box will contain that value, and when you reassign it, it will empty out the old value, and the new value will be placed inside of it.

