def main():
    n1=int(input("enter 1 number "))
    n2=int(input("enter 2 number "))
    opr =(input("choose opretion +, -, *, / "))
    if opr=="+" :
        print(add(n1,n2))
    elif opr=="-" :
            print(sub(n1,n2))
    elif opr=="*" :
            print(mult(n1,n2))
    elif opr=="/" :
            print(f"{div(n1,n2):.2f}")
    else:
        print("wrong selection")





def add(x,y):
    return x+y


def sub(x,y):
    return x-y

def mult(x,y):
    return x*y

def div(x,y):
    return x/y


main()
