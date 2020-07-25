#program by Halim
#program to count the number of vowel in a given string using a set.
def vowel_count(str):
    #initializing count variable to 0
    count = 0
    vowel = set("aeiou")
    for alphabet in str:
        if alphabet in vowel:
            count = count + 1
print("No. of vowels :", count)
# driver code
str = "meninblack"
# function call
vowel_count(str)

