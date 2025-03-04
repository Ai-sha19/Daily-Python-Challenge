while True:
    user_input = (input("Enter a number (or type 'exit' to quit): "))

    if user_input.lower() == 'exit':
        print("Goodbye! Have a good day!")
        break

    try:
        number = int(user_input)
        if number % 2 == 0:
            print(f"{number} is an even number")
        else:
            print(f"{number} is an odd number")

    except ValueError:
        print("Invalid input! Please enter a valid number.")         
    

