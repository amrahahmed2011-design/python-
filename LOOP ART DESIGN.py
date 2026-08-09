# Loop Art Designer
 
# Hashtags pyramid pattern
print("===== HASHTAGS PYRAMID PATTERN =====")
 
rows = int(input("Enter number of rows for hashtags pattern: "))
 
for i in range(rows):
    for j in range(i + 1):
        print("# ", end="")
    print()
 
 
# Floyd's Triangle pattern
print("===== FLOYD'S TRIANGLE =====")
 
rows = int(input("Enter number of rows for Floyd's Triangle: "))
number = 1
 
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(number, end=" ")
        number += 1
    print()
 
 
# Diamond number pattern
print("===== DIAMOND NUMBER PATTERN =====")

 
rowsize = int(input("Enter number of rows for diamond pattern: "))
 
if rowsize % 2 == 0:
    halfrows = rowsize // 2
else:
    halfrows = rowsize // 2 + 1
 
space = halfrows - 1
 

for i in range(1, halfrows + 1):
    for j in range(1, space + 1):
        print(" ", end="")
 
    space -= 1
    number = 1
 
    for j in range(2 * i - 1):
        print(number, end="")
        number += 1
 
    print()
 
space = 1
 
for i in range(1, halfrows):
    for j in range(1, space + 1):
        print(" ", end="")
 
    space += 1
    number = 1
 
    for j in range(2 * (halfrows - i) - 1):
        print(number, end="")
        number += 1
#FINAL MESSAGE
print("===== LOOP ART DESIGN COMPLETE =====")
print("You created hashtags, Floyd's triangle, and diamond patterns using nested loops!")