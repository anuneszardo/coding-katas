
def translate(number: int) -> str:
    DIVISOR_TEXT = {
        3: "Fizz",
        5: "Buzz",
        7: "Whizz",
        11: "Bang",
    }
    result = "".join(text for divisor, text in DIVISOR_TEXT.items() if number % divisor == 0)
    return result or str(number)

if __name__ == '__main__':
    for number in range(1, 1156):
        print(translate(number))