import re
import math

constants = {
    "PI": math.pi,
    "E": math.e,
    "h": 6.62607015e-34,
    "G": 6.67430e-11,
    "Na": 6.02214076e23,
    "c": 299792458,
    "e": 1.602176634e-19,
    "kB": 1.380649e-23,
    "epsilon0": 8.8541878188e-12,
    "mu0": 1.25663706127e-6
}

def signum(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def heaviside(x):
    return 0 if x < 0 else 1


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def antilog(x):
    return 10 ** x


def totient(n):
    if n < 1:
        raise ValueError("totient requires a positive integer")

    count = 0

    for k in range(1, n + 1):
        if math.gcd(k, n) == 1:
            count += 1

    return count


def fusc(n):
    if n < 0:
        raise ValueError("fusc requires a non-negative integer")

    if n == 0:
        return 0

    if n == 1:
        return 1

    if n % 2 == 0:
        return fusc(n // 2)

    return fusc(n // 2) + fusc(n // 2 + 1)


def root(x, n):
    if n == 0:
        raise ValueError("Root degree cannot be zero")

    if x < 0:
        if n % 2 == 0:
            raise ValueError("Even root of a negative number")

        return -((-x) ** (1 / n))

    return x ** (1 / n)

functions = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,

    "sinh": math.sinh,
    "cosh": math.cosh,
    "tanh": math.tanh,

    "log": math.log,
    "log10": math.log10,
    "antilog": antilog,
    "exp": math.exp,

    "fact": math.factorial,
    "nCr": math.comb,
    "nPr": math.perm,
    "root": root,

    "floor": math.floor,
    "ceil": math.ceil,
    "signum": signum,
    "heaviside": heaviside,
    "sigmoid": sigmoid,

    "gcd": math.gcd,
    "lcm": math.lcm,
    "totient": totient,
    "fusc": fusc
}

def tokenize(expression):
    tokens = []
    i = 0

    while i < len(expression):
        char = expression[i]

        if char.isspace():
            i += 1

        elif char.isdigit() or char == ".":
            match = re.match(r"\d*\.?\d+(?:[eE][+-]?\d+)?", expression[i:])

            if not match:
                raise ValueError("Invalid number")

            number = match.group()
            tokens.append(number)
            i += len(number)

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

    token = tokens[position]

    if token == "(":
        position += 1
        result = parse_expression()

        if position >= len(tokens) or tokens[position] != ")":
            raise ValueError("Missing closing bracket")

        position += 1
        return result

    else:
        position += 1

        if token in functions:

            if position >= len(tokens) or tokens[position] != "(":
                raise ValueError("Expected '(' after function")

            position += 1

            argument1 = parse_expression()

            if token in ["nCr", "nPr", "root", "gcd", "lcm"]:

                if position >= len(tokens) or tokens[position] != ",":
                    raise ValueError("Expected comma")

                position += 1
                argument2 = parse_expression()

                if position >= len(tokens) or tokens[position] != ")":
                    raise ValueError("Missing closing bracket")

                position += 1

                if token in ["nCr", "nPr", "gcd", "lcm"]:
                    if not float(argument1).is_integer() or not float(argument2).is_integer():
                        raise ValueError("Arguments must be integers")

                    return functions[token](int(argument1), int(argument2))

                if token == "root":
                    if not float(argument2).is_integer():
                        raise ValueError("Root degree must be an integer")

                return functions[token](argument1, argument2)

            else:

                if position >= len(tokens) or tokens[position] != ")":
                    raise ValueError("Missing closing bracket")

                position += 1

                if token in ["fact", "totient", "fusc"]:
                    if not float(argument1).is_integer():
                        raise ValueError("Argument must be an integer")

                    return functions[token](int(argument1))

                return functions[token](argument1)

        if token in constants:
            return constants[token]

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