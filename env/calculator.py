import secret_logic

def ask():
    print("calculator application, please give me the ")

    print("1. operand")
    text = input()
    while not secret_logic.is_numeric(text):
        print("bad input, again")
        text = input()
    operand1 = int(text)

    print("operator (+ | - | * | /)")
    text = input()
    while not secret_logic.is_supported_operator(text):
        print("bad input, again")
        text = input()
    operator = text

    print("2. operand")
    text = input()
    while not secret_logic.is_numeric(text):
        print("bad input, again")
        text = input()
    operand2 = int(text)

    return operand1, operator, operand2

op1, oper, op2 = ask()
