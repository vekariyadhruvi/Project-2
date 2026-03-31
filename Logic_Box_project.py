print("WELCOME to the PATTERN GENERATOR and NUMBER ANALYZER:)")

while True:
    print("\nSelect an option:")
    print("1. Pattern Generation")
    print("2. Number Analysis")
    print("3. Exit")

    choice=int(input("Enter your choice(1-3):"))
    

    if choice==1:
        n=int(input("Enter number of rows for the pattern:"))

        if n<=0:
            print("Number of rows must be positive.")
            break

        print("Pattern:")

        for i in range(1,n+1):
            print("*"*i)

    elif choice==2:
        start=int(input("\nEnter the start value of the range:"))
        end=int(input("Enter the end value of the range:"))

        if end<start:
            print("End must be greater than start.")
            continue

        sum=0
        for i in range(start, end+1):
            if i%2==0:
                print(f"Number {i} is Even")
            else:
                print(f"Number {i} is Odd")

            sum=sum+i
        print(f"Sum of all numbers from {start} to {end} is: {sum} \n")

    
    elif choice==3:
        print("Exiting the program, Goodbye!")
        break

    else:
        print("Invalid option chosen, Please choose again from 1, 2 or 3.")