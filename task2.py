# ////////1
if num % 3 == 0 and num %5 == 0:
    print("Consultadd Python Training")
elif num % 3 == 0:
    print("Consultadd")
elif num % 5 == 0:
    print("c")

# /////////2
optionList = int(input("enter the option from the list"))
firstNum = int(input("enter the first number"))
secNum = int(input("enter the second number"))

if optionList == 1:
    addNum = firstNum + secNum
    print("Addition of two numbers is " + str(addNum))
elif optionList == 2:
    if firstNum > secNum:
        subNum = firstNum - secNum
        print("Subtracttion of two numbers is " + str(subNum))
    else:
        print("Negative")
elif optionList == 3:
    divNum = firstNum/ secNum
    print("The division of two numbers is " + str(divNum))
elif optionList == 4:
    mulNum = firstNum * secNum
    print("The multiplication of numbers is " + str(mulNum))
elif optionList == 5:
    avgNum = (firstNum + secNum)/2
    print("The average is "+ str(avgNum))

# ////////3
a = 10 
b = 20 
c = 30 
avg = (a + b+ c) /3
print("avg =", avg)
if avg > a and avg > b and avg > c:
    print("avg is higher than a,b,c")
else:
    if avg > a and avg > b:
        print("avg is higher than a, b, c")
    else:
        if  avg > a and avg > c:
            print("avg is higher than a, c")
        else:
            if avg > b and avg > c:
                print("avg is higher than b,c ")
            else:
                if avg > a:
                    print("avg is just higher than a")
                else:
                    if avg > b:
                        print("avg is just higher than b")
                    elif avg > c:
                        print("avg is just higher than c")


# ////////4
while True:
    num = int(input("Enter the number"))
    if num < 0:
        break
    elif num > 0 :
        print("Good Going")
        continue

# ////////5 
for num in range(2000, 3200 + 1):
    if num % 7 == 0 and num % 5 != 0:
        print(num)

# /////////6 
# part1 
"int" object is not iterable
# part2
0,1,2

# part3
0,1,2,3,4

# ////////7
for i in range(0,7):
    if i == 3 or i == 6:
        continue
    else:
        print(i)

# ////////8
char1 = input("Enter the string")
countLetter = 0
for i in char1:
    if ord(i) >= 97 and ord(i) <= 122:
        countLetter = countLetter + 1
countDigits = len(char1) - countLetter
print("Letter " + str(countLetter))
print("Digits " + str(countDigits))

#////// 9
# part 1
suppose number is 10 
num = 10 
while True:
    guessNumber = input("Guess the lucky Number")
    if int(guessNumber) == num:
        break

# part2

num = 10 
while True:
    guessNumber = input("Guess the lucky Number")
    if int(guessNumber) == num:
        break
    else:
        ans= input("Want to continue guessing yes or no?")
        if ans == "no":
            break
        elif ans == "yes":
            continue

# /////// 10 
counter = 1
num = 10 
while counter <= 5:
    guesNum = input("guess the number")
    if int(guesNum) == num:
        print("Good Guess")
    else:
        print("Try Again")
    counter = counter + 1
print("Game Over")

# /////// 11

counter = 1
num = 20
flag = True 
while counter <= 5:
    guesNum = input("guess the number")
    if int(guesNum) == num:
        print("Good Guess")
        flag = False
        break
    counter = counter + 1
if flag == True:
    print("sorry but that was not very successful")





















