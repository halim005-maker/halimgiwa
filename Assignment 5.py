#Programmer_Halim

#Program to find the second largest number in a given series
number1 = int(input('Enter first number : \t'))
number2 = int(input("Enter second number : \t"))
number3 = int(input("Enter third number : \t"))
print ("number1, number2, number3")
numbers = (6,4,5)

print(f"Number: (numbers)")

first = -1
second = -1

for number in numbers:
    if number > first:
        second = first
        first = number

    
print(f"First: (first)")
print(f"Second: (second)")