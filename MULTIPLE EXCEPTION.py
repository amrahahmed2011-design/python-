try:
    num1,num2 = eval(input("ENTER TWO NUMBERS , SEPARATED BY COMMA : "))
    result = num1 / num2
    print("THE ANSWER IS :",result)

except ZeroDivisionError:
    print("DIVISION BY ZERO IS ERROR !")
except SyntaxError:
    print("COMMA IS MISSING ENTER TWO NUMBER SEPARATED BY COMMA LIKE THIS 1,2")
except:
    print("WRONG INPUT !")
else:
    print("NO EXCEPTIONS ")
finally:
    print("THIS WILL EXECUTE NO MATTER WHAT")
