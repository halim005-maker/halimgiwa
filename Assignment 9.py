#program by Halim
#program to swap first and last element of the list
def swapmiddle(List):
    size = len(List)
    # swap operation
    temp = List[0]
    List[0] = List[size - 1]
    List[size -1] = temp
    return List
# Driver code
List = ['1', '4', '7',]
print(swapmiddle(List))
