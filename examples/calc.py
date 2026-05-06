num1=int(input("Enter the Number1 : "))
num2=int(input("Enter the Number2 : "))
option=int(input("Select Option \n 1. For Addition Enter 1 \n 2. For Substraction Enter 2 \n 3. For Multiplication Enter 3 \n 4. For Division Enter 4 "))


def Add():
    Add=num1+num2
    print(Add)

def Sub():
    Sub=num1-num2
    print(Sub)

def Multi():
    Multi=num1*num2
    print(Multi)

def Div():
    Div=num1/num2
    print(Div)

def Calc(Opt):
    if Opt==1:
        Add()
    elif Opt==2:
        Sub()
    elif Opt==3:
        Multi()
    elif Opt==4:
        Div()
    else:
        print("Invalid Number please enter correct number")

Calc(option)                

