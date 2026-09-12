#FUNCTION TO CHECK WHETHER THE GIVEN NUMBER IS A PLAINDROME OR NOT
def palindrome(r):
    e = len(r)-1
    s = 0
    while(s<e):
        if(r[s] != r[e]):
            return False
        s += 1
        e -= 1
    return True

r = (1,7,5,6,2,1)
if (palindrome(r)):
    print("The given number is a palindrome")
else:
    print("The given number is not a palindrome")