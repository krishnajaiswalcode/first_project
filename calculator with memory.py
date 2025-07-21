Memory = "history_of_Calculator.txt"
import os

def show_history():
    if not os.path.exists(Memory):
        print("No history found !")
        return
    with open(Memory, "r") as file:
        lines = file.readlines()
        if not lines:
            print("No history found !")
        else:
            for line in reversed(lines):
                print(line.strip())

def clear_history():
    with open(Memory, "w"):
        pass
    print("History cleared.")

def save_to_history(equation,result):
    with open(Memory, "a") as file:
        file.write(f"{equation} = {result}\n")

def calculate(user_input):
    parts = user_input.strip().split()
    if len(parts) != 3:
        print("Invalid input. Use format: [e.g. 8 + 8]")
        return
    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid numbers. Please enter valid numeric values.")
        return

    result = None
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Use only + - * /")
        return
    # Show integer if result is whole number
    if isinstance(result, float) and result.is_integer():
        result = int(result)
    print(f"Result: {result}")
    save_to_history(user_input, result)

def main():
    print("--- SIMPLE CALCULATOR (type history, clear or exit) ---")
    while True:
        user_input = input("Enter calculation (+ - * /) or command (history, clear, exit): ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        elif user_input.lower() == "history":
            show_history()
        elif user_input.lower() == "clear":
            clear_history()
        elif user_input:
            calculate(user_input)

if __name__ == "__main__":
    main()
