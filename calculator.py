def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    if b==0:
        print("Zero division error")
    else:
        print(a/b)
    
print("Welcome To Calculator CLI App")
while True:
    x=int(input("Enter first number: "))
    y=int(input("Enter second number: "))
    print("What you want to do +,-,/,*")
    char=input("Enter your choice: ")
    if (char=='+'):
        print(add(x,y))
    elif char=='-':
        print(sub(x,y))
    elif char =='*':
        print(multi(x,y))
    else:
        div(x,y)
        
    choice= input("Do You want to continue yes/no: ")
    if choice.lower()=='no':
        break