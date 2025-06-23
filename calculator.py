print("Welcome To Calculator CLI App")
while True:
    x=int(input("Enter first number: "))
    y=int(input("Enter second number: "))
    print("What you want to do +,-,/,*")
    char=input("Enter your choice: ")
    if (char=='+'):
        print(x+y)
    elif char=='-':
        print(x-y)
    elif char =='*':
        print(x*y)
    else:
        if y==0:
            print("Zero division error")
        else:
            print(x/y)
    choice= input("Do You want to continue yes/no: ")
    if choice=='no':
        break