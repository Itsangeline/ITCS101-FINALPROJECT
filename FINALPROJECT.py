#act2
num1 = eval(input("Enter a number"))
num2 = eval(input("Enter another number"))
answer = num1 + num2
print(num1, "plus" ,num2, "=" ,answer,)

#act3
fullname = input("Enter your fullname")
age = input("Enter your age")
status = input("Enter your status")
birthmonth = input("Enter your birthmonth")
birthday = input("Enter your birthday")
birthyear = input("Enter your birthyear")
birthplace = input("Enter your birthplace")
address = input("Enter your address")
citizenship = input("Enter your citizenship")
print("Hi, I'm" ,fullname, "and I'm" ,age, "years old.",status, "and I was born on" ,birthmonth, birthyear, "on" ,birthplace, "I'm from" ,address,"and I'm a",citizenship,)

#act4
num1 = eval(input("Enter a number--->"))
num2 = eval(input("Enter another number--->"))
answer = num1 + num2
print("The sum of" ,num1, "and" ,num2, "is" ,answer)
diff = num1 - num2
print("The difference of" ,num1, "and" ,num2, "is" ,diff)
product = num1 * num2
print("The product of" ,num1, "and" ,num2, "is" ,product)
quotient = num1 // num2
print("The quotient of" ,num1, "and" ,num2, "is" ,quotient)
exponent = num1 ** num2
print("The exponent of" ,num1, "and" ,num2, "is" ,exponent)
remainder = num1 % num2
print("The remainder of" ,num1, "and" ,num2, "is" ,remainder)
fd = num1 / num2
print("The floordivision of" ,num1, "and" ,num2, "is" ,fd)

#act5
print("FAHRENHEIT TO CELSIUS CONVERTER")

temp = eval(input("Enter temperature in fahrenheit : "))
celsius = (temp - 32) * 5 / 9
print("The convertion of ",temp, "degrees Fahrenheit is" ,celsius, "degrees celsius")

#act6
x = 5
print(x)

#act7
gold = 0
miner = input("Hi, please enter your name--->")
hasmine = input("Did you mine something today? (yes/no)")

if hasmine == "yes":
    gold += 1
    print(f"Hi {miner}, today you have a total of {gold} gold")

#act9
age = eval(input("Enter your age--->"))
if age >=1 and age<=7:
    print("toddler")
elif age >=8 and age <=13:
    print("pre-teen")
elif age >=14 and age <=16:
    print("teen")
elif age >=17 and age <=25:
    print("teenager")
elif age >=25 and age <=50:
    print("adult")
elif age >=60 and age <=100:
    print("senior")

#act10
isDLL = input("Are you a current student of dll? (yes/no)")
if isDLL.lower == "yes":
    print("WELCOME TO THE DLL BSIT SCHOLARSHIP FORM")
isgg = input("Are you from Gulang-Gulang? (yes/no)")
if isgg.lower() == "yes":
    print("Please fillup the second form")
    islevel = input("What is your current level right now in DLL\nF-Freshmen\nS-Sophomore\nJ-Junior\nS2-Senior. Please input yor answer")

    if islevel.lower() == 'f':
        print("Hi Freshmen")
    elif islevel.lower() == 's':
        print("Hi Sophomore")
    elif islevel.lower() == 'j':
        print("Hi Junior")
    elif islevel.lower() == 'S2':
        print("Hi Senior")
    else:
        print("invalid")

    isneeded = input("Do you need this scholarship? (yes/no)")
    if isneeded.lower() == "yes":
        print("Scholarship Granted")
    else:
        print("Thank u for stopping by")

#act20
go = True

while go == True:
    name = input("Please enter a name--->")

    if name.lower() == "stop":
        print("loop stopped")
        break
        go = false

    else:
        print("program would continue")
        continue

#act21
count = 0
while go == True:
    name = input("Please enter a name---->")

    if name.lower == "stop":
        print("Loop has stopped")
        print(f"You have entered {count} number of names")
        break
    else:
        count += 1
        continue

#codechallenge1
print("\t\t*\n\t*\t*\t*\n*\t*\t*\t*\t*\n\t*\t*\t*\n\t\t*")

#codechallenge2
name = input("Pleasse enter your name: ")
print("\t\t*\n\t*\t*\t*\n*\t* hi, {name} \t*\t*\n\t*\t*\t*\n\t\t*")

#codechallenge4
num1 = eval(input("Enter a number--->"))
num2 = eval(input("Enter another number--->"))
answer = num1 + num2
print("The sum of" ,num1, "and" ,num2, "is" ,answer)
diff = num1 - num2
print("The difference of" ,num1, "and" ,num2, "is" ,diff)
product = num1 * num2
print("The product of" ,num1, "and" ,num2, "is" ,product)
quotient = num1 // num2
print("The quotient of" ,num1, "and" ,num2, "is" ,quotient)
exponent = num1 ** num2
print("The exponent of" ,num1, "and" ,num2, "is" ,exponent)
remainder = num1 % num2
print("The remainder of" ,num1, "and" ,num2, "is" ,remainder)
fd = num1 / num2
print("The floordivision of" ,num1, "and" ,num2, "is" ,fd)

#codechallenge5
name = input("Enter your name here--->")
deposit = eval(input("Please amount to deposit: "))
ans1= deposit // 1000
n1 = deposit % 1000
ans2 = n1 // 500
n2 = n1 % 500
ans3 = n2 // 200
n3 = n2 % 200
ans4 = n3 // 100
n4 = n3 % 100
ans5 = n4 // 50 
n5 = n4 % 50
ans6 = n5 // 20
n6= n5 % 20
ans7 = n6 // 10 
n7 = n6 % 10
ans8 = n7 // 5
n8 = n7 % 5
ans9 = n8 // 1
n9 = n8 // 1

print("Hello" ,name, "the breakdown of your deosit is:")
print(ans1, "- 1000")
print(ans2, "- 500")
print(ans3, "- 200")
print(ans4, "- 100")
print(ans5, "- 50")
print(ans6, "- 20")
print(ans7, "- 10")
print(ans8, "- 5")
print(ans9, "- 1")

#codechallenge6
prelim = eval(input("Enter your grade in prelim: "))
midterm = eval(input("Enter your grade in midterm: "))
finals= eval(input("Enter your grade in finals: "))
quizzes = eval(input("Enter your grade in quizzes: "))
projects = eval(input("Enter your grade in projects: "))

fg = (prelim * .15) + (midterm * .15) + (finals * .15) + (quizzes * .20) + (projects * .20)

if fg <= 100:
    print("Congrtulations you passed!")
elif fg:
    print ("invalid")
elif fg >= 75:
    print("Sorry you failed")

#codechallenge7
name = input("Please enter the costumer's name: ")
age = input("Age of the costumer?: ")
order = input("How many and waht did the costumer buy?: ")
price = eval(input("Enter the items price here: "))
total = eval(input("Enter the total prize of the item: "))

if age >= 60:
    discount_p = price * 0.25
else:
    print("not qualified for the discount")
if age <= 18: 
    discount_p = price * 0.25
else:
    print("not qualified for the discount")

tax = 0.5

if age >= 60 and age <= 18:
    print("discount_p :" ,discount_p)
    print("Hi",name,"your total is",total - discount_p,"with tax",tax,"\nThank you for buying!")
else:
    print("Hi",name,"your total is",total,"with" ,tax, "tax. \nThank you for buying!")

#codechallenge9
for x in range(11, 0, -1):
    for y in range(x, 0, -1):
        print("*", end="")
    print()

#codechallenge10
for x in range (1, 6):
    for y in range(6, x, -1):
        print(" ", end= " ")
    for a in range(1, x, 1):
        print("*", end= " ")
    for z in range(1, x, 1):
        print("*", end= " ")
    print()

for x in range (1, 6):
    for y in range(1, x, +1):
        print(" ", end= " ")
    for a in range(6, x, -1):
        print("*", end= " ")
    for z in range(6, x, -1):
        print("*", end= " ")
    print()

#codechallenge11
for x in range (1, 6):
    for y in range(6, x, -1):
        print(" ", end= " ")
    for a in range(4, x, 1):
        print("*", end= " ")
    for z in range(3, x, 1):
        print("*", end= " ")
    print()

for x in range (1, 6):
    for y in range(1, x, +1):
        print(" ", end= " ")
    for a in range(4, x, -1):
        print("*", end= " ")
    for z in range(3, x, -1):
        print("*", end= " ")
    print()

#codechallenge12
for x in range (1, 6):
    for y in range(6, x, -1):
        print(" ", end= " ")
    for a in range(1, x, 1):
        print("*", end= " ")
    for z in range(1, x, 1):
        print("*", end= " ")
    print()

for x in range (0, 6):
    for y in range(0, 4):
        print(" ", end= " ")
    for a in range(0, 2):
        print("*", end= " ")
    print()

#codechallenge14
go = True
num = count = 0
while go == "True":
    num = input("Please enter a number--->")

    if num.lower() == "stop":
        print("The loop has stopped")
        print(f"The sum of all number given is {count}")
        break
        go = False
    else:
        count += 1
        continue

#codechallenge15
import os

go = True
nt = 0
while go == "True":
    ask = input("Do you want to continue creating triangle? (yes/no)")
    if ask.lower() == "no":
        os.system("cls")
        print("program stopped")
        break
        go = False

    elif ask.lower() == "yes":
        os.system("cls")
        nt += 1

    for x in range (1, 7):
        for r in range(1, nt +1):
            for y in range(1, x, +1):
                print("%", end= " ")
    for z in range(6, x, -1):
        print(" ", end= " ")
        print(end= "")
    print()
    continue
else:
    os.system("cls")
    print("input note valid")
    
#codechallenge16
balance = 0
amount = 0

go = True

while go == "True":
    print("Welcome to my bank simulation prgram!")
    print("Select operation")
    print("1 - Create Account")
    print("2 - Deposit")
    print("3 - Check Balance")
    print("4 - Withdraw")
    print("5 - Exit")

    choice = input("Please enter your choice here: ")
    if choice == "1":
        print("Please provide th following information")
        fullname = ("Please enter your fullname here: ")
        print("account created")
    
    elif choice == "2":
        print("You must provide the initial deposit amount")
        amount = eval(input("Enter the amount fot the initial deposit"))
        print("Your current balance is: ")
        balance += amount;
        print(balance)
        continue
    elif choice == "3":
        print("Your balance is: ")
        print(balance)
    elif choice == "4":
        print("Please the amount to wthdraw: ")
        balance -= amount
        print("Your current balance is: ")
        print(balance)
    elif choice == "5":
        print("Program exits")
        break
    else:
        print("invalid choice")