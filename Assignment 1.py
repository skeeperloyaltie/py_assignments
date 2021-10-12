# Assignment 1
# Part one
def greatestOfFour(w, x, y, z):
	# define variable lenghts
    if x > y and z > w and x > w:
        return x
    elif y > z and y > w:
		# return y 
        return y
    elif z > w:
		# return Z
        return z
    else:
        return w


# Read input
# accept user input. 
print("Enter four numbers to check the greatest: ")
w = input("Enter 1st Number: ")
x = input("Enter 2nd Number: ")
y = input("Enter 3rd Number: ")
z = input("Enter 4th Number: ")

# call function
print("Greatest of them all: ")
print(greatestOfFour(int(w), int(x), int(y), int(z)))


# Part two
# define function
def reverse(sentence):
	# split sentence first
    sp = sentence.split()
    li = sp[:: -1]
    fd = " ".join(li)
    return fd

# Read user input
print("Enter sentence: ")

sentence = str(input("Enter Sentence: "))
# call function.
print(reverse(sentence))


# Part Three
# define function
def oddNumbers(n1, n2):
    if n1 % 2 == 1:
        return list(range(n1, n2 + 1, 2))
    else:
        return list(range(n1 + 1, n2 + 1, 2))

# read user input
n1 = int(input("Enter n1 number: "))
n2 = int(input("Enter n2 number: "))
# call function
print(oddNumbers(n1, n2))


# Part four
# define function 
def calculateTotalSalary(month_sal, no_of_years):
    if no_of_years > 5:
        increment = month_sal * 105 / 100
        return increment
    else:
        return month_sal

# read user input
month_sal = int(input("Enter Monthly salary: "))
no_of_years = int(input("Enter Number of years: "))
# call function
print(calculateTotalSalary(month_sal, no_of_years))


# Part five
# define function
def listMax(numList):
    max_num = numList[0]
    for num in numList:
        if num > max_num:
            max_num = num
    return max_num
# read user input
num_list = [65, 78, 98, 55, 13]
# call function
print(f"Max number: {listMax(num_list)}")

# Part six
# define function
def profit_or_loss(cost_price, selling_price):
    if cost_price > selling_price:
        loss = cost_price - selling_price
        print("Loss:")
        return loss
    else:
        profit = selling_price - cost_price
        print("Profit:")
        return profit
# define user input and read it
costPrice = float(input("Enter the cost price: "))
sellingPrice = float(input("Enter the selling price: "))
# call function
print(profit_or_loss(costPrice, sellingPrice))


# Part seven
# define function.
def printEvenIndexChar(str):
    modified_string = str[::2]
    return modified_string
# call user input.
str = input("Enter a string: ")
# use function.
print(f"Modified string: {printEvenIndexChar(str)}")


# Part eight
# define function
def rental_car_cost(rate_per_day, no_of_days):
    rental_cost = rate_per_day * no_of_days
    if no_of_days >= 7:
        rental_cost -= 50
    elif no_of_days >= 3:
        rental_cost -= 20

    return rental_cost
# call user input
ratePerDay = int(input("Enter the rate per day: "))
noOfDays = int(input("Enter the number of days: "))
# call funtion 
print(f"Cost: {rental_car_cost(ratePerDay, noOfDays)}")


# Part nine
# define function 
def average(list):
    average = sum(list) / len(list)
    return average
# call user input and call function.
print(f"Average: {average([3, 6, 10, 8, 6])}")


# Part ten
# define function.
def square_of_numbers():
    square_list = []
    for i in range(1, 31):
        square_list.append(i * i)
    return square_list
# call function
print(square_of_numbers())


# Home Work
# part one
def degreeToFahrenheit(degree_celcius):
    fahrenheit = (degree_celcius * 5 / 9) + 32
    return fahrenheit
# Call function
degree = float(input("Enter temperature (degree celcius): "))
print(f"temp in fahrenheit: {degreeToFahrenheit(degree)}")


# part two
# define function
def countVowels(sentence):
    num_vowels = 0
    for char in sentence:
        if char in "aeiouAEIOU":
            num_vowels = num_vowels + 1
    return num_vowels
# define function
sentence = input("Enter a sentence: ")
print(f"number of vowels: {countVowels(sentence)}")

# part three
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
# call function
number = int(input("Enter a number: "))
print(f"Factorial: {factorial(number)}")


# part four
def commonData(list1, list2):
    for element in list1:
        if element in list2:
            return True
    return False
# call function
print(commonData(["name", "word", "sentence"], ["name", "letter", "vowels"]))
print(commonData(["name", "word", "sentence"], ["alphabet", "letter", "vowels"]))


# part five
# define function
def sortList(nList, order):
    if order == "a":
        nList.sort()
    elif order == "d":
        nList.sort(reverse=True)
    return nList
# list 
list = [4, 5, 2, 1, 6, 3]
# read user input
order = input("Enter the order: a(ascending) or d(descending): ")
print(sortList(list, order))
# define list two
list1 = ["nma", "akdjfk", "kdjfk"]
order = input("Enter the order: a(ascending) or d(descending): ")
print(sortList(list1, order))


# part six
# define function
def string_countupperlower(sentence):
    upper_case = 0
    lower_case = 0
    for letter in sentence:
        if letter.isupper():
            upper_case += 1
        elif letter.islower():
            lower_case += 1

    print(f"Lower case: {lower_case}\nUpper case: {upper_case}")
# call function
sentence = input("Enter the sentence: ")
string_countupperlower(sentence)


# part seven
# define function
def sortList(nList, order):
    if order == "a":
        nList.sort()
    elif order == "d":
        nList.sort(reverse=True)
    return nList
# List function, call function 
list = [4, 5, 2, 1, 6, 3]
order = input("Enter the order: a(ascending) or d(descending): ")
print(sortList(list, order))

