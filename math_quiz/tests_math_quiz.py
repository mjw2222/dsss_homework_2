import unittest
from math_quiz import gen_random_int, gen_random_math_operator, computation


class TestMathGame(unittest.TestCase):

    def test_gen_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = gen_random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_gen_random_math_operator(self):
        # Test if random operator is within specified values [+,-,*]
        for _ in range(1000):  # Test a large number of random values
            rand_operator = gen_random_math_operator()
            self.assertTrue(rand_operator in ['+', '-', '*'])

    def test_computation(self):
            # Test if computation computes correctly
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (2, -2, '-', '2 - -2', 4),
                (3, 0, '*', '3 * 0', 0),
                (9, -7, '*', '9 * -7', -63),
                (0, -7, '+', '0 + -7', -7),
                (0, -7, '-', '0 - -7', 7),
                (45, 2, '*', '45 * 2', 90),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = computation(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
