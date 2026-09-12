#CREATE A TUPLE WITH DIFFERNT DATA TYPES
tuplex = ("Hello", 42, 3.14, True)
print(tuplex)
#CREATE A TUPLE
tuple2 = (1, 2, 3, 4, 5)
print(tuple2)
#TUPLES ARE IMMUTABLE
#USING MERGE OPERATOR
tuplex = tuplex + (8,)
print(tuplex)
#COUNT THE NUMBER OF OCCURANCES OF AN ELEMENT IN A TUPLE
tuple3 = (1, 2, 3, 4, 5, 1, 2, 1)
print(tuple3.count(1))
#CREATE A TUPLE
tuple4 = (1,2,3,4,5,6,7,8,9,10)
#SLICING A TUPLE
_slice = tuple4[4:9]
print(_slice)
# IF THE START INDEX IS NOT SPECIFIED, IT WILL START FROM THE BEGINNING OF THE TUPLE
_slice = tuple4[:2]
print(_slice)