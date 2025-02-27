# Smart Arithmetic Calculator

while True:
    print("\nChoose an operation :")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    user_choice = input("\nEnter Choice 1 - 5: ")

    if user_choice == "5":
        print("Goodbye! Have a good day!")
        break

    if user_choice not in ("1", "2", "3", "4"):
        print("Invalid choice! Try again.")
        continue

    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))

    if user_choice == "1":
        total = num1 + num2
        
    elif user_choice == "2":
        total = num1 - num2
       
    elif user_choice == "3":
        total = num1 * num2
  
    else:
        if num2 == 0:
            print("Can't divide by zero!")
            continue
        total = num1 / num2

    # Check if total is an integer
    formatted_total = int(total) if total.is_integer() else round(total, 2)

    print(f"\nResult = {formatted_total}\n")