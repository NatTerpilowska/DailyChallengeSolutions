min_value = int(input("Enter the lowest number: "))
max_value = int(input("Enter the highest number: "))

print("\nEven numbers from %d to %d are: " % (min_value, max_value))
for i in range(min_value, max_value+1):
    if(i%2==0):
        print(i, end=" ")