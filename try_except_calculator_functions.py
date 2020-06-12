#!/usr/bin/env python3

#Simple calculator program that uses try/except blocks to handle valueError and divide by 0 exceptions

def display_menu():

    print("Welcome to Lina's Calculator")
    print()
    print("Calculator Operation Options: ")
    print("Add - add two numbers")
    print("Subtract - subtract two numbers")
    print("Divide - divide two numbers")
    print("Multiply - multiply two numbers")
    print("Exit - Exit the program")
    print()

def get_input():
    while True: #make sure the user enters an integer
        try:
            num1 = int(input("Please enter an integer: "))
            return num1 
        except ValueError:
            print("Invalid integer. Please try again.")
            continue


def add(num1, num2):
    sum = num1 + num2
    print ("The sum of your numbers is: " + str(sum))

def subtract(num1, num2):
    diff = num1 - num2
    print ("The difference of your numbers is: " + str(diff))

def multiply(num1, num2):
    product = num1 * num2
    print ("The product of your numbers is: " + str(product))

def divide(num1, num2):
    try:
        divisor = num1 / num2
        print ("The division of your numbers is: " + str(divisor))
    except ArithmeticError as e:
        print("Error. You can't divide by zero!")
    except ZeroDivisionError:
        print("Awesome!")       


def main():
    display_menu()
    while True:
        option = input("Please select the operation you wish to perform: ")
        num1 = get_input()  # what ever was returned from the function get_input()
        num2 = get_input()
        if option == "add":
            add(num1, num2)
        elif option == "subtract":
            subtract(num1, num2)
        elif option == "divide":
            divide(num1, num2)
        elif option == "multiply":
            multiply(num1, num2)
        elif option == "exit":
            break
        else:
            print("Error.Not a valid option. Please try again.\n")
    print()
    print("Thank you for using Lina's Calculator")

if __name__ == "__main__":
    main()
            
        
       
