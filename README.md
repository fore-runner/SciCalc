

# Scientific Calculator (SciCalc)

A command-line scientific calculator implemented in Python using a tokenizer and recursive descent parser. The calculator evaluates mathematical expressions while respecting operator precedence, associativity, functions, constants, and error handling.

## Features

- Basic arithmetic operations: `+`, `-`, `*`, `/`, `%`
- Exponentiation using `^`
- Support for parentheses and nested expressions
- Unary positive and negative operators
- Scientific notation
- Mathematical constants
- Scientific and mathematical functions
- Expression parsing without using `eval()`
- Helpful error messages for invalid expressions
- Interactive command-line interface

## Architecture

The calculator is divided into multiple components that work together to evaluate mathematical expressions.

### 1. Tokenizer

The tokenizer converts the input expression into a sequence of tokens.

For example:

```text
Input: 2 + 3 * (4 ^ 2)

Tokens: ['2', '+', '3', '*', '(', '4', '^', '2', ')']
```

It identifies numbers, operators, parentheses, function names, constants, and other supported symbols.

### 2. Recursive Descent Parser

The parser evaluates the tokenized expression using recursive descent parsing.

Different parsing functions handle different levels of operator precedence.

| Function | Responsibility |
|---|---|
| `parse_expression()` | Addition and subtraction |
| `parse_term()` | Multiplication, division, and modulo |
| `parse_factor()` | Unary positive and negative operators |
| `parse_power()` | Exponentiation |
| `parse_primary()` | Numbers, parentheses, constants, and functions |

This structure ensures that mathematical expressions are evaluated according to the correct precedence rules.

### 3. Calculator

The calculator coordinates the tokenization and parsing process.

It:
1. Tokenizes the input expression.
2. Initializes the parser position.
3. Starts parsing the expression.
4. Checks for unexpected remaining tokens.
5. Returns the calculated result.

### 4. Interactive CLI

The command-line interface accepts expressions from the user, displays their results, and continues running until the user exits.

---

## Approach

### Expression Tokenization

The input expression is converted into tokens before evaluation.

The tokenizer scans the expression character by character and identifies:

- Numeric values
- Operators
- Parentheses
- Function names
- Constants
- Commas

Whitespace is ignored during tokenization.

### Recursive Descent Parsing

The calculator uses recursive descent parsing to evaluate expressions.

Each parsing function is responsible for a specific level of precedence. Functions call lower-precedence parsing functions when necessary.

The parser follows the mathematical operator precedence rules:

1. Parentheses and functions
2. Exponentiation
3. Unary operators
4. Multiplication, division, and modulo
5. Addition and subtraction

Exponentiation is handled as a right-associative operator.

For example:

```text
2 ^ 3 ^ 2
```

is evaluated as:

```text
2 ^ (3 ^ 2)
```

which produces:

```text
512
```

### Expression Evaluation

After tokenization, the parser processes the tokens and evaluates the expression while maintaining the current token position.

The parser uses recursive function calls to handle nested expressions and parentheses.

For example:

```text
2 * (3 + 4)
```

The expression inside the parentheses is evaluated first, followed by the multiplication.

---

## Supported Operations

### Arithmetic Operators

| Operator | Description | Example |
|---|---|---|
| `+` | Addition | `5 + 3` |
| `-` | Subtraction | `5 - 3` |
| `*` | Multiplication | `5 * 3` |
| `/` | Division | `5 / 3` |
| `%` | Modulo | `5 % 3` |
| `^` | Exponentiation | `2 ^ 3` |

### Mathematical Constants

The calculator supports mathematical and scientific constants such as:

| Constant | Description |
|---|---|
| `PI` | Pi |
| `E` | Euler's number |
| `h` | Planck's constant |
| `G` | Gravitational constant |
| `Na` | Avogadro constant |
| `c` | Speed of light |
| `e` | Elementary charge |
| `kB` | Boltzmann constant |
| `epsilon0` | Vacuum permittivity |
| `mu0` | Vacuum permeability |

### Mathematical Functions

The calculator supports mathematical functions including:

- Trigonometric functions
- Inverse trigonometric functions
- Hyperbolic functions
- Logarithmic functions
- Exponential functions
- Factorial
- Combinations and permutations
- Roots
- Floor and ceiling
- Signum and Heaviside functions
- Sigmoid
- GCD and LCM
- Euler's totient function
- Fusc function

Functions are evaluated using Python's standard library where applicable.

---

## Design Decisions

### 1. Recursive Descent Parser

A recursive descent parser was chosen because it provides a straightforward way to implement mathematical operator precedence and associativity.

Instead of relying on Python's built-in expression evaluator, the calculator explicitly parses and evaluates expressions.

### 2. No Use of `eval()`

The calculator does not use `eval()`, `exec()`, or similar methods to evaluate user input.

Expressions are tokenized and parsed manually, providing greater control over supported syntax and error handling.

### 3. Separate Parsing Functions

Each parsing function handles a specific precedence level.

This separation makes the implementation easier to understand, maintain, debug, and extend.

### 4. Dictionary-Based Constants and Functions

Constants and mathematical functions are stored using dictionaries.

This allows names to be mapped to their corresponding values or implementations efficiently.

### 5. Standard Library Only

The calculator uses Python's standard library, including the `math` module, without requiring external dependencies.

This keeps the project lightweight and easy to run.

---

## Setup

### Requirements

- Python 3.x
- No external packages required

### Clone the Repository

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd <repository-directory>
```

### Run the Calculator

```bash
python scicalc.py
```

---

## Usage

Start the calculator:

```text
SciCalc>
```

Enter a mathematical expression:

```text
SciCalc> 2 + 3 * 4
14.0
```

More examples:

```text
SciCalc> 2 ^ 3 ^ 2
512.0

SciCalc> (2 + 3) * 4
20.0

SciCalc> 2 ^ -1
0.5

SciCalc> PI
3.141592653589793
```

To exit the calculator:

```text
exit
```

---

## Error Handling

The calculator handles invalid expressions and mathematical errors by displaying helpful error messages instead of terminating unexpectedly.

Examples of errors include:

- Invalid characters
- Invalid mathematical expressions
- Missing closing parentheses
- Unexpected tokens
- Division by zero
- Invalid function arguments
- Mathematical domain errors

The calculator continues accepting expressions after an error.

---

## Testing

The calculator can be tested using different categories of expressions.

### Basic Arithmetic

```text
2 + 3
10 - 4
5 * 6
10 / 2
10 % 3
```

### Operator Precedence

```text
2 + 3 * 4
(2 + 3) * 4
```

### Exponentiation

```text
2 ^ 3
2 ^ 3 ^ 2
2 ^ -1
```

### Parentheses

```text
(2 + 3)
2 * (3 + 4)
((2 + 3) * 4)
```

### Invalid Expressions

```text
2 +
2 *
(2 + 3
```

---

## Limitations

- The calculator operates through a command-line interface.
- Implicit multiplication is not supported.
- Mathematical expressions must follow the supported syntax.
- Function arguments must be provided according to the function's requirements.

---

## Future Improvements

- Add a graphical user interface.
- Add expression history.
- Add improved formatting for large and small numbers.
- Add more mathematical functions.
- Expand automated test coverage.

---

## Tech Used

- Python
- Python Standard Library
- `math` module
- Recursive Descent Parsing
- Tokenization

