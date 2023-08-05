import random

def generate_question():
    """
    Function to generate a random math question for middle school students.
    Returns the question as a string and the correct answer as an integer.
    """
    operations = ["addition", "subtraction", "multiplication", "division"]
    operation = random.choice(operations)
    
    if operation == "addition":
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        answer = num1 + num2
        return f"What is {num1} + {num2}? ", answer

    elif operation == "subtraction":
        num1 = random.randint(1, 50)
        num2 = random.randint(1, num1)
        answer = num1 - num2
        return f"What is {num1} - {num2}? ", answer

    elif operation == "multiplication":
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        answer = num1 * num2
        return f"What is {num1} * {num2}? ", answer

    elif operation == "division":
        divisor = random.randint(2, 12)
        num2 = random.randint(1, 12)
        num1 = divisor * num2
        answer = num1 // divisor
        return f"What is {num1} / {divisor}? (Enter the quotient only) ", answer

def main():
    print("Welcome to the Math Tutor for Middle School Students!")
    print("Type 'exit' to quit the program.\n")
    
    while True:
        question, correct_answer = generate_question()
        user_input = input(question)

        if user_input.lower() == "exit":
            print("Thank you for using the Math Tutor. Goodbye!")
            break

        try:
            user_answer = int(user_input)
            if user_answer == correct_answer:
                print("Correct! Great job!")
            else:
                print(f"Sorry, the correct answer is {correct_answer}. Keep trying!")
        except ValueError:
            print("Invalid input. Please enter a valid integer or type 'exit' to quit.")

if __name__ == "__main__":
    main()
