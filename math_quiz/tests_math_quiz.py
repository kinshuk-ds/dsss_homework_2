import unittest
from math_quiz import generate_random_number, random_operator, create_problem_and_answer

class TestMathGame(unittest.TestCase):

    def test_generate_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        # Test if the operator generated is within the allowed operators
        allowed_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
            operator = random_operator()
            self.assertIn(operator, allowed_operators)

    def test_create_problem_and_answer(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 3, '-', '10 - 3', 7),
            (6, 2, '*', '6 * 2', 12),
            (7, 3, '-', '7 - 3', 4),
            (4, 5, '*', '4 * 5', 20)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = create_problem_and_answer(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
