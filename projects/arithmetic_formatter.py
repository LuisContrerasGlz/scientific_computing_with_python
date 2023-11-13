"""

Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side.

Rules
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

Situations that will return an error:

If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
    The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
    Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
    Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.

If the user supplied the correct format of problems, the conversion you return will follow these rules:
    There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
    Numbers should be right-aligned.
    There should be four spaces between each problem.
    There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. 

"""

def arithmetic_arranger(problems, show_solution=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    line_1 = ""
    line_2 = ""
    line_3 = ""
    line_4 = ""

    for problem in problems:

        first_operand, operator, second_operand = problem.split()

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        if not (first_operand.isdecimal() and second_operand.isdecimal()):
            return "Error: Numbers must only contain digits."
        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_operand_length = max(len(first_operand), len(second_operand))
        formatted_first_operand = first_operand.rjust(max_operand_length + 2)
        formatted_second_operand = operator + second_operand.rjust(
            max_operand_length + 1)

        result = str(eval(problem))
        formatted_result = result.rjust(max_operand_length + 2)

        max_length = max(len(formatted_first_operand),
                         len(formatted_second_operand), len(formatted_result))

        line_1 += formatted_first_operand + "    "
        line_2 += formatted_second_operand + "    "
        line_3 += "-" * max_length + "    "
        line_4 += formatted_result + "    " if show_solution else ""

    arranged_problems = line_1.rstrip() + "\n" + line_2.rstrip() + "\n" + line_3.rstrip()
    if show_solution:
        arranged_problems += "\n" + line_4.rstrip()

    return arranged_problems