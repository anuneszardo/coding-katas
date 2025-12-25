

def string_calculator(string_number: str) -> int:
    tokens = tokenize(string_number)
    stack = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == '*':
            left = stack.pop()
            right = tokens[i + 1]
            stack.append(left * right)
            i += 2
        else:
            stack.append(token)
            i += 1
    return sum(stack)


def tokenize(expression: str):
    tokens = []
    current_number = ""
    is_minus = False

    for char in expression:
        if char.isdigit():
            current_number += char
            if is_minus:
                tokens.append(int('-' + current_number))
                is_minus = False
                current_number = ""
                continue
        else:
            if current_number:
                tokens.append(int(current_number))
                current_number = ""

            if char in "-*":
                if char == '-':
                    is_minus = True
                    continue
                tokens.append(char)

    if current_number:
        tokens.append(int(current_number))

    return tokens