# /////// 1 To reverse string 
# def reverseString(str1):
#     str1 = str1[::-1]
#     return str1
# x = reverseString("1234abcd")
# print(x)

# /////// 2 

# def countLetters(str1):
#     upperCount = 0
#     lowerCount = 0
#     for i in str1:
#         if ord(i) >= 65 and ord(i) <= 90:
#             upperCount = upperCount + 1
#         elif ord(i) >= 97 and ord(i) <= 122:
#             lowerCount = lowerCount+1
#     print("Total Upper case characters:" +str(upperCount))
#     print("Total lower case characters:" +str(lowerCount))
# countLetters("consultADD")

# /////// 3
# def newList(l1):
#     l2 = l1.copy()
#     for i in range(len(l2)):
#         l2[i] = l2[i]  + 5
#     return l2
    
# x = newList([5,4,10,3])
# print(x)

# ////////4
# def sortWords(str1):
#     str1 = str1.split("-")
#     print(str1)
#     for i in range(len(str1)):
#         str1[i] = sorted(str1[i])
#         str1[i] = "".join(str1[i])
#     print("-".join(str1))
# sortWords("Welcome-to-coding")


# /////////5
# def capitalWords(str1):
#     str1 = str1.split()
#     print(str1)
#     for i in range(len(str1)):
#         str1[i] = str1[i].upper()
#     print(" ".join(str1))
# capitalWords("Hello world \n Practice makes perfect")


# ///////// 6
# def sumIntegral(num1, num2):
#     print(num1+num2)
# sumIntegral("30","40")

# ///////// 7
# def maxLength(str1, str2):
#     if len(str1) > len(str2):
#         print(str1)
#     elif len(str1) < len(str2):
#         print(str2)
#     else:
#         print(str1)
#         print(str2)
# maxLength("Happy", "world")

# /////////// 8
# def genTuple():
#     l1 = []
#     for i in range(1, 20):
#         if i * i < 20:
#             l1.append(i)
#     print(tuple(l1))
# genTuple()
            



# /////////// 9
# def showNumbers(limit):
#     for i in range(limit +1):
#         if i%2 ==0 :
#             print(i, "EVEN")
#         else:
#             print(i, "ODD")
# showNumbers(3)

# ////////10
# seq = [i for i in range(1,21)]
# filtered = filter(lambda x: x%2 ==0,seq )
# for i in filtered:
#     print(i)

# ////////11


# ////////// 12

# def divisionError(num1, num2):
#     try:
#         if num1/num2:
#             print("division is successful")
#     except ZeroDivisionError:
#         print("exception caught. Enter the numbers again")
# divisionError(5, 0)

# //////////13
import functools
l1 =[[1,2,3],[4,5], [6,7,8]]
# def flatten(l1):
#     for sub in l1:
#         for i in sub:
#             l2.append(i)
#     print(l2)
print(functools.reduce(lambda x: [ i for sub in l1 for i in sub], l1)

# //////////14
# 1 ans is  2

# 2  it will print f is not defined.












