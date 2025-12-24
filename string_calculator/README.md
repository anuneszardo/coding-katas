# String Calculator Kata

## Problem

Implement a simple string-based calculator that takes a string of numbers and operators, and evaluates it incrementally using Test-Driven Development (TDD). Focus on adding one feature at a time and refactoring as you go.

---

## Requirements

Implement the following behavior incrementally:

1. **Basic Numbers**
   - If the input is an empty string, return `0`.
   - A single number returns its integer value.

2. **Addition**
   - Two numbers separated by `+` return their sum.

3. **Subtraction**
   - Handle `-` for subtraction.

4. **Whitespace**
   - Ignore whitespace around numbers or operators.

5. **(Optional) Extended Behavior**
   - Extend to support other operators (like `*`, `/`) or parentheses once core requirements are complete.

---

## Approach

- Follow **TDD**  — write a failing test first, then implement just enough code to pass it.
- Progress in **small, incremental steps**, only moving to the next requirement after the current one passes.
- Keep logic clear and expressive; favor readability over clever tricks.

---

## Testing Strategy

Include tests for:

- Empty and minimal input
- Single number and simple expression
- Multiple operators
- Whitespace handling
- Edge cases such as leading/trailing spaces

Example test cases:

| Input | Expected Output |
|-------|-----------------|
| `""` | `0` |
| `"1"` | `1` |
| `"1+2"` | `3` |
| `"4-2"` | `2` |
| `" 1 + 2 "` | `3` |

---

## Possible Improvements

- Add support for operator precedence
- Support parentheses
- Extend to floating point numbers
- Add detailed error reporting for invalid input

---

## Notes

The primary goal is to **practice incremental development and clean design** using TDD, not to build a full expression parser. Start simple, refactor often, and only add behavior one step at a time.
