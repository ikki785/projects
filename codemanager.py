import os
folder = "/Users/sumanboparai/Documents/program files"   
pr = os.listdir(folder)
while True:
    print("enter your option")
    print("(1)view your files ")
    print("(2)create new file")
    ops = input("")
    if ops == "1":
        print("enter your option")
        print("(1)add code")
        print("(2)deleat file")
        fileops = input("")
        if fileops == "1":
            for f in pr:
                print(f)
            print("\n")
            print("enter your file name")
            filename = input()
            
            if filename in pr:
                path1 = os.path.join(folder, filename) 
                
    
                with open(path1, 'r') as read_file:
                    print("\n--- File Content ---\n")
                    print(read_file.read())
                print("enter your code here")
                code1 = ""

                

                with open(path1, 'w') as new:
                    while True:
                        new_code = input()
                        if new_code == 'n':
                            break
                        if new_code == "":
                            break
                        code1 += '\n' + new_code

                    new.write(code1)
                
            else:
                print('this file does not exest enter again')
        
            break
        elif fileops == '2':
            while True:
                filename1 = input("enter your file name")
                full_path = os.path.abspath(filename1)
                if os.path.exists(full_path):
                    os.remove(full_path)
                    break
                else:
                    print("this file does not exist")
        else :
            print("this is not the option enter again")
            
    elif ops == '2':
        new_file = input('enter your file name')
       
        with open(new_file,'w') as f:
            f.write('')
            print("file created",new_file)
            print("enter your code here")
            while True:
                    new_code = input()
                    code = code + '\n' + new_code
                    if new_code == "":

                        path = os.path.join(pr, new_file)
                        with open(path,'w')as new:
                            new.write(code)
                        break
                
                
    else:
        print("this is not the option enter again")
