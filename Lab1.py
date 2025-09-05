# Program Name: Lab1.py
# Course: IT3883/Section W02
# Student Name: Adam Hutcheson
# Assignment Number: Lab 1
# Due Date: 09/05/ 20XX
# Purpose: Create a menu to append, clear, and display user input

# list to append user data
user_list = []

# while loop to use menu
while True:
    print("\n1. Append data to input "
          "\n2. Clear input buffer"
          "\n3. Display input buffer"
          "\n4. Leave program")

    # saving user choice
    user_choice = input("Please select an option: ")

    # Append data (1)
    if user_choice == "1":
        user_input = input("Please type your input: ")
        user_list.append(user_input)

    # Clear input buffer (2)
    elif user_choice == "2":
        user_list.clear()

    # Display input buffer
    elif user_choice == "3":
        print(user_list)

    # Leave program
    elif user_choice == "4":
        print("Goodbye!")
        break
