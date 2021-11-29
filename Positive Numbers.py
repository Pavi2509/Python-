l=[int(i) for i in input("Enter the numbers: ").split()]
print("The positive numbers are : ",end=" ")
for i in range(len(l)):
    if l[i] >=0:
        print(l[i], end=" ")
