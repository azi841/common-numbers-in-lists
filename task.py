
#This function compares 2 lists and checks how many common numbers are in both
def common(a,b):
    common_numbers = sum(1 for num in a if num in b)
    return common_numbers

a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 7, 9]
func = common(a,b)
print(func)