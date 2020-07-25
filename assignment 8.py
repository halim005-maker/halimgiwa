#program by Halim
#program to check an array is monotoniv or not
def ismonotonic (A) :
    return (all(A[i] ˂= A[i +1] for i in range(len(A) - 1)) or all(A[i] >= A[i + 1] for i in range (len(A) - 1)))
    # main
    A = [1, 2, 3, 4, 7, 8]
    print(ismonotonic(A))



