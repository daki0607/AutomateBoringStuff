def print_list(theList):
    for i in range(len(theList)):
        if i == len(theList) - 1:
            print(f"and {theList[i]}")
        else:
            print(f"{theList[i]}, ", end="")


L1 = ["apple", "banana", "orange", "raspberry", "grapefruit"]
L2 = [2, 3, 4, 10]
L3 = [5, "house", "fruit", -1]

print_list(L1)
print_list(L2)
print_list(L3)
