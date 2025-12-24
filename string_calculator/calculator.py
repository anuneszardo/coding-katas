


def string_calculator(string_number: str) -> int:
    list_values = []
    previous_value=''
    for char in string_number:
        if char.isnumeric() or char == '*':
            list_values.append(int((previous_value + char).strip()))
        elif char == '-':
            previous_value = char
    return sum(list_values)