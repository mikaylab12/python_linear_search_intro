# Mikayla Beelders
# python searching algorithms task from handout

# linear search task

x =int(input("Please enter a number: "))
list_1 = [1, 68, 46, 3, 90, 24, 19, 5, 12, 9, 7, 21, 47, 23, 44, 15, 31, 12, 12, 78, 52, 84, 11, 15 ]
n = len(list_1)
def linear_search(list_1, x, n):
    for i in range(0, n):
        if (list_1[i] == x):
            return i
    return "Nope"

result = linear_search( list_1, x, n)
if result == "Nope":
    print("Nope")
else:
    print("Element found at index: ", result)