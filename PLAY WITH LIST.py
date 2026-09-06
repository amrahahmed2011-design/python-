l = [1,6, 3, 4, 5,0, 2,56,73,98,10, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print("ORIGINAL LIST: ", l)
#VARIABLE TO STORE THE SUM OF THE LIST
sum = 0
#FINDING THE SUM OF THE LIST
for i in l:
    sum += i #SUM = SUM +i
#DIVIDE THE TOTAL SUM BY THE LENGTH OF THE LIST
average = sum / len(l)
print("sum of the list: ", sum)
print("average of the list: ", average)
#SORTING THE ELEMENTS OF THE LIST
l.sort()
print("SORTED LIST: ", l)
#PRINTING THE FIRST ELEMENT OF THE LIST
print("FIRST ELEMENT OF THE LIST: ", l[0])

#PRINTING THE LAST ELEMENT OF THE LIST
print("LAST ELEMENT OF THE LIST: ", l[-1])
#SLICING THE LIST TO GET THE FIRST 5 ELEMENTS
print("FIRST 5 ELEMENTS OF THE LIST: ", l[0:5])