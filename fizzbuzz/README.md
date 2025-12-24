# FizzBuzz Kata

## Problem
Implement a function that returns a sequence of values from 1 to _n_ with the following rules:

- Numbers divisible by 3 are replaced with `"Fizz"`
- Numbers divisible by 5 are replaced with `"Buzz"`
- Numbers divisible by both 3 and 5 are replaced with `"FizzBuzz"`
- All other numbers are returned as their string representation

## Approach
- Start with the simplest case and incrementally add rules
- Favor readability over compact or clever implementations
- Avoid deeply nested conditionals by keeping the logic explicit

## Testing Strategy
- Base cases (single values, small ranges)
- Divisibility by 3
- Divisibility by 5
- Divisibility by both 3 and 5
- Edge cases such as zero or invalid input

## Possible Improvements
- Make the rules configurable (e.g. different divisors or labels)
- Support custom ranges
- Refactor to a rule-based or data-driven implementation
