#!/usr/bin/env python3
def solve(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1-num2
    if operator == "/":
        return num1/num2
    if operator == "*":
        return num1*num2

valid_operators = {"*", "/", "+", "-"}

def calc():
    numbers = []
    operator = ""
    while len(numbers) < 2:
        try:
            numbers.append(int(input("\nPlease enter a number\n")))
        except ValueError:
            print("thats not a number")

    while True:
        try:
            operator = input("\nPlease choose an operator: +, -, *, /\n")
            if operator not in valid_operators:
                raise ValueError()
            break
        except ValueError:
            print("Please choose a valid operator")
    print(f"\n{solve(numbers[0], numbers[1], operator)}")

calc()


