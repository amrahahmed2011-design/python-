rowsize = int(input("Enter the number of rows for the diamond pattern: "))
if rowsize % 2 == 0:
    halfdiamondrows = int(rowsize / 2)
else:
    halfdiamondrows = int((rowsize + 1) / 2)
space = halfdiamondrows - 1
#OUTER LOOP TO HANDLE NUMBER OF ROWS
for i in range(1, halfdiamondrows + 1):
    #INNER LOOP TO HANDLE NUMBER OF SPACES
    for j in range(1, space + 1):
        print(end=" ")
    space = space - 1
    num = 1
    #INNER LOOP TO HANDLE NUMBER OF STARS
    for j in range( (2 * i-1)):
        print(end=" " + str(num))
        num = num + 1
    print()
space = 1
for i in range(1, halfdiamondrows):
    #INNER LOOP TO HANDLE NUMBER OF SPACES
    for j in range(1, space + 1):
        print(end=" ")
    space = space + 1
    num = 1
    #INNER LOOP TO HANDLE NUMBER OF STARS
    for j in range( 1 , (2 * halfdiamondrows - i)):
        print(end= " " + str(num))
        num = num + 1
    print()

