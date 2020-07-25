#program by Halim
# python program to replace comma with dot in a given string
def replace(str):
    maketrans = str.maketrans
    final = str.translate(maketrans(', .', '., '))
    return final

#driving code
string = "14,191,444.1"
print(replace(string))