rows = int(input("Enter the number of rows: "))
number = 1
print("Floyd's Triangle:")
#OUTER LOOP TO HANDLE NUMBER OF ROWS
for i in range(1, rows + 1):
#INNER LOOP TO HANDLE NUMBER OF COLUMNS
    for j in range(1, i + 1):
        print(number, end="  ")
#DISPLAYING NUMBERS IN FLOYD'S TRIANGLE
        number = number + 1
    print()