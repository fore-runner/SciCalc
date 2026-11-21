import math

def tokenize(expression):
    tokens = []
    i = 0

    while i < len(expression):
        char = expression[i]

        if char.isspace():
            i += 1

        elif char.isdigit() or char == ".":
            number = ""

            while i < len(expression) and (expression[i].isdigit() or expression[i] == "."):
                number += expression[i]
                i += 1

            tokens.append(number)

        elif char.isalpha() or char == "_":
            name = ""

            while i < len(expression) and (expression[i].isalnum() or expression[i] == "_"):
                name += expression[i]
                i += 1

            tokens.append(name)

        elif char in "+-*/%^(),":
            tokens.append(char)
            i += 1

        else:
            raise ValueError(f"Invalid character: {char}")

    return tokens

tokens = []
position = 0


def parse_expression():
    global position

    result = parse_term()

    while position < len(tokens):
        operator = tokens[position]

        if operator == "+":
            position += 1
            result += parse_term()

        elif operator == "-":
            position += 1
            result -= parse_term()

        else:
            break

    return result


def parse_term():
    global position

    result = parse_factor()

    while position < len(tokens):
        operator = tokens[position]

        if operator == "*":
            position += 1
            result *= parse_factor()

        elif operator == "/":
            position += 1
            result /= parse_factor()

        elif operator == "%":
            position += 1
            result %= parse_factor()

        else:
            break

    return result


def parse_factor():
    global position

    if position >= len(tokens):
        raise ValueError("Unexpected end of expression")

    token = tokens[position]

    if token == "+":
        position += 1
        return parse_factor()

    elif token == "-":
        position += 1
        return -parse_factor()

    else:
        return parse_power()

def parse_power():
    global position

    base = parse_primary()

    if position < len(tokens) and tokens[position] == "^":
        position += 1
        exponent = parse_factor()
        return base ** exponent

    return base

def parse_primary():
    global position

    if position >= len(tokens):
        raise ValueError("Unexpected end of expression")
    
    token=tokens[position]

    if token == "(":
        position += 1
        result = parse_expression()
    
        if position >= len(tokens) or tokens[position] != ")":
            raise ValueError("Missing closing bracket")
    
        position += 1
        return result
    else:
        position+=1
        return float(token)


def calculate(expression):
    global tokens, position

    tokens = tokenize(expression)
    position = 0
    
    result = parse_expression()

    if position < len(tokens):
        raise ValueError("Unexpected token")
    
    return result


def main():
    while True:
        expression = input("SciCalc> ")

        if expression.lower() == "exit":
            break
        try:
            result = calculate(expression)
            print(result)
        except( ValueError, IndexError, ZeroDivisionError ) as error:
            print(f"[ERROR]{error}")

main()