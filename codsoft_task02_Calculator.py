def calc():
    print("===This is a simple calculator===")
    
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    
    print("\nChoose an operation:")
    print("1.Addition (+)")
    print("2.Subtraction (-)")
    print("3.Multiplication (*)")
    print("4.Division (/)")
    
    choice=input("\nEnter your choice (1/2/3/4): ")
    
    if (choice=="1"):
         sum=num1+num2
         print(f"\nResult: {num1} + {num2} = {sum}")
         
    elif (choice=="2"):
        sub=num1-num2
        print(f"\nResult: {num1} - {num2} = {sub}")
        
    elif (choice=="3"):
        mult=num1*num2
        print(f"\nResult: {num1} * {num2} = {mult}")
        
    elif (choice=="4"):
        if num2==0:
            print("\nDivision by zero is undefined.")
        else:
            div=num1/num2
            print(f"\nResult: {num1} / {num2} = {div}")
    
    else:
        print("!!Invalid choice!!\nPlease enter a valid input.")
        
calc()