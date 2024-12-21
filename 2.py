def abc(number):
    if number <= 0:
        return False
    return(number&(number-1))==0
n = int(input("enter a number"))
if abc(n):
    print("the number is a power of two")
else:
    print("the number is not a power of two")