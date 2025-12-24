
def translate(number: int) -> str:
    if number % 1155 == 0:
        return "FizzBuzzWhizzBang"
    if number % 15 == 0:
        return "FizzBuzz"
    if number % 21 == 0:
        return "FizzWhizz"
    if number % 55 == 0:
        return "BuzzBang"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    if number % 7 == 0:
        return "Whizz"
    if number % 11 == 0:
        return "Bang"
    return str(number)


if __name__ == '__main__':
    for number in range(1, 1156):
        print(translate(number))