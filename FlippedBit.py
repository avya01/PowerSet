num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

def flipbit(num1, num2):
    counter = 0
    while(num1>0 or num2>0):
        if((num1&1) != (num2&1)):
            counter+=1
        num1>>=1
        num2>>=1

    return counter

print(flipbit(num1,num2))
