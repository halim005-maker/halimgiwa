#program by Halim
#program to sort the values of one list using the second list.
first_list = ["a", "b", "c", "d"]
second_list = ['4,' '6', '8', '10']
zipped_pairs = zip(first_list, second_list)
sorted_pairs = sorted(zipped_pairs)
result = [item[1] for item in sorted_pairs]
print(result)