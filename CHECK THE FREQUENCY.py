test_dict = {'a': 7, 'b': 7, 'c': 2, 'd': 1,"e": 7, 'f': 4, 'g': 6, 'h': 7, 'i': 9, 'j': 7}
#PRINTING THE ORIGIONAL DICTIONARY
print("The original dictionary is : " + str(test_dict))

#INITILIZE VALUE
K = 7
#USING LOOPS
#SELECTIVE KEY VALUES IN DICTIONARY
res = 0
for key in test_dict:
    if test_dict[key] == K:
        res += 1
#PRINTING RESULT
print("The frequency of K is : " + str(res))