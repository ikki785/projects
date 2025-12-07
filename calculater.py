import math
while True:
    print("""enter your opption""")
    print("(1)add")
    print("(2)sub")
    print("(3)multi")
    print("(4)div")
    print("(5)square")
    print("(6)square root")
    op = input("")
    if op == "1" :
        while True :
            a = int(input("enter a number :"))
            b = int(input("enter a number :"))
            try :
                c = a +b
                print(c)
                break
            except ValueError:
                print("pls try again:(")
    elif op == "2" :
        while True :
            a = int(input("enter a number :"))
            b = int(input("enter a number :"))
            try :
                c = a - b
                print(c)
                break
            except ValueError:
                print("pls try again:(")
    elif op == "3" :
        while True :
            a = int(input("enter a number :"))
            b = int(input("enter a number :"))
            try :
                c = a * b
                print(c)
                break
            except ValueError:
                print("pls try again:(")
    elif op == "4" :
        while True :
            a = int(input("enter a number :"))
            b = int(input("enter a number :"))
            if a or b == 0:
                print("you can't enter 0 as input")
            else:
                try :
                    c = a / b
                    print(c)
                    break
                except ValueError:
                    print("pls try again:(")
    elif op == "5" :
        while True :
            a = int(input("enter a number :"))
            try :
                c = a * a
                print(c)
                break
            except ValueError:
                print("pls try again:(")
    elif op == '6':
        while True :
            a = int(input("enter a number :"))
            try :
                c = math.sqar(a)
                print(c)
                break
            except ValueError:
                print("pls try again:(")
    else :
        print("pls enter 1 or 2 or 3 or 4 or 5")
    print("do you want to continue [y/n]")
    p = input()
    if p == "n" or p == "N" or p == "no":
        print("thanks :)")
        break
