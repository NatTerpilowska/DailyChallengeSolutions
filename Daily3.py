min = int(input("Enter the lowest number: "))
max = int(input("Enter the highest number: "))

print("Even numbers from %d to %d are: " % (min, max))
for i in range(min, max+1):
    if(i%2==0):
        print(i, end=" ")