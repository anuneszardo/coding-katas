import unittest

from fizzbuzz.translator import translate


class TestTranslator(unittest.TestCase):
    def test_translator_returns_same_value(self):
        self.assertTrue(translate(1),1)

    def test_translator_returns_fizz(self):
        self.assertTrue(translate(3),"Fizz")

    def test_translator_returns_buzz(self):
        self.assertTrue(translate(5),"Buzz")

    def test_translator_returns_fizzbuzz(self):
        self.assertTrue(translate(15),"FizzBuzz")

    def test_translator_does_not_ignore_case(self):
        self.assertNotEqual(translate(3),"FIZZ")
        self.assertNotEqual(translate(5),"buzz")
        self.assertNotEqual(translate(15),"FIZZbuzz")

    def test_translator_1_to_100(self):
        digit_count = 0
        fizzbuzzwhizzbang_count = 0
        fizzbuzz_count = 0
        fizz_count = 0
        buzz_count = 0
        for i in range(1,1156):
            value = translate(i)
            if value.isnumeric():
                digit_count += 1
            else:
                if value =='Fizz':
                    fizz_count += 1
                if value =='Buzz':
                    buzz_count += 1
                if value =='FizzBuzz':
                    fizzbuzz_count += 1
                if value =='FizzBuzzWhizzBang':
                    fizzbuzzwhizzbang_count += 1

        self.assertEqual(480,digit_count)
        self.assertEqual(264,fizz_count)
        self.assertEqual(140,buzz_count)
        self.assertEqual(76,fizzbuzz_count)
        self.assertEqual(1,fizzbuzzwhizzbang_count)