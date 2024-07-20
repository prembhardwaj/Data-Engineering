     
def def_calculator(x,y,o):
    if o == "+":
        cal = x + y
    elif o == "-":
        cal = x - y
    elif o == "*":
        cal = x*y
    elif cal == "/":
        cal = x/y
    else:
        print( "Operator not recognized")

    return cal


try :
    x = int(input("Enter X: "))
    y = int(input("Enter Y: "))
    o = input("Enter operator: ")
    
except (TypeError, ValueError):
    print("check input values for X & Y should be integers")

else:
    result = def_calculator(x,y,o)
    print(result)

