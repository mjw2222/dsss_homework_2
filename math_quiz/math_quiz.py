import random


def gen_random_int(min_value, max_value):
    """
    Generate a random integer.

    Parameters
    ----------
    min_value : int
        Minimum value for random integer generation.
    max_value : int
        Maximum value for random integer generation.

    Returns
    -------
    int
        the random integer generated from min and max.
    """

    # Check if input values have correct type and value
    try:
        value = random.randint(min_value, max_value)
    except ValueError:
        print("Value Error: Use integers as min and max values, min value !<= max value")
        return 0
    except TypeError:
        print("Type Error: Requested type for min and may values is integer")
        return 0

    return value



def gen_random_math_operator():
    """
    Choose a random math operator out of the following: +, -, *.

    Parameters
    ----------

    Returns
    -------
    string
        The random math operator.

    """
    return random.choice(['+', '-', '*'])


def computation(operand1, operand2, operator):
    """
    Compute the result depending on the input values operand1 and operand2 and the operator.

    Parameters
    ----------
    operand1 : int
        The first input integer.
    operand2 : int
        The second input integer.
    operator : str
        The math operator.

    Returns
    -------
    problem : string
        The problem statement to be computed.
    answer : int
        The result of the computation.
    """
    # Combining the input to state the problem
    problem = f"{operand1} {operator} {operand2}"
    # computations
    if operator == '-': answer = operand1 - operand2 # - operation
    elif operator == '+': answer = operand1 + operand2 # + operation
    else: answer = operand1 * operand2 # * operation
    return problem, answer

def math_quiz():
    score = 0 # Variable to keep score
    num_computation = 3 # Set number of computations

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    if type(num_computation) != int:
        raise ValueError("You must provide an integer for the number of computations")

    for _ in range(num_computation):
        # Generate random operands (int) and operator
        operand1 = gen_random_int(1, 10); operand2 = gen_random_int(1, 5); operator = gen_random_math_operator()

        # Generate and print problem statement and store result with computation()
        problem, answer = computation(operand1, operand2, operator)
        print(f"\nQuestion: {problem}")

        # Read user answer to printed problem statement
        user_answer = input("Your answer: ")
        user_answer = int(user_answer)

        # Compare user answer and actual answer
        if user_answer == answer: # Correct user answer: increment score
            print("Correct! You earned a point.")
            score += -(-1)
        else: # Incorrect user answer: print correct answer
            print(f"Wrong answer. The correct answer is {answer}.")

    # Print final score
    print(f"\nGame over! Your score is: {score}/{num_computation}")

if __name__ == "__main__":
    math_quiz()
