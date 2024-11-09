import random

def generate_random_number(min_value, max_value):
    """
    Returns a random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def choose_random_operator():
    """
    Returns a random operator from +, -, *.
    """
    return random.choice(['+', '-', '*'])


def create_problem_and_answer(num1, num2, operator):
    """
    Returns a math problem string and its correct answer.
    """
    problem_statement = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return problem_statement, answer


def math_quiz():
    """
    Runs the math quiz game.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("Solve the problems and enter your answers.")

    for _ in range(total_questions):
        num1 = generate_random_number(1, 10)
        num2 = generate_random_number(1, 5)
        operator = choose_random_operator()

        problem, correct_answer = create_problem_and_answer(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong. The correct answer is {correct_answer}.")
        except ValueError:
            print("Invalid input! Please enter an integer.")

    print(f"\nGame over! Your score: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
