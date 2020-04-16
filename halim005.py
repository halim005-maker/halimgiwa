# program to display the fibonacci sequence up to n-th term
# fibonacci series will start at 0 and travel upto below number
number = int(input("nplease enter the range number: "))
#initializing first and second values of the series
i = 0
first_value = 0
second_value = 1
# find & displaying fibonacci series
while(i ˂ number) :
    if(i ˂= 1) :
        next = i
    else:
        next = first_value + second_value
        first_value = second_value
        print(next)
        i = i + 1
