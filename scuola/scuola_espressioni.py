
from sympy import symbols, simplify
import math

# Define the arithmetic expression
expression = "2 + 5 * 2 ** 2 * (7 - 3)"

# Step 1: Evaluate inside the parentheses
step1_result = eval(expression[expression.find('(')+1:expression.find(')')])
print(f"Step 1: Evaluate inside parentheses: {step1_result}")

# Step 2: Substitute the result back into the expression
expression = expression.replace(f"({step1_result})", str(step1_result))
print(f"Step 2: Substitute back into the expression: {expression}")

# Step 3: Evaluate exponentiation
while '**' in expression:
    exp_start = expression.find('**')
    exp_end = exp_start + 2
    left = expression.rfind(' ', 0, exp_start - 1) + 1 if exp_start > 0 else 0
    right = expression.find(' ', exp_end) if exp_end < len(expression) else len(expression)
    base, exponent = expression[left:exp_start], expression[exp_end:right]
    exponentiation_result = eval(base) ** eval(exponent)
    expression = expression[:left] + str(exponentiation_result) + expression[right:]
    print(f"Step 3: Evaluate exponentiation: {expression}")

# Step 4: Evaluate multiplication and addition
result = eval(expression)
print(f"Step 4: Evaluate multiplication and addition: {result}")
