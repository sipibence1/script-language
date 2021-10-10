def is_numeric(text):
    return text.isnumeric()

def is_supported_operator(text):
    return text in ['+','-','*','/']

def calculate(operand1, operator, operand2):
    rv = 0
    if operator == '+':
        rv = operand1 + operand2
    elif operator == '-':
        rv = operand1 - operand2
    elif operator == '*':
        rv = operand1 * operand2
    elif operator == '/':
        rv = operand1 / operand2
    return rv