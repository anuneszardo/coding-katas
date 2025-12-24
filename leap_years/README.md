# Leap Years Kata

## Problem
Implement a function that determines whether a given year is a leap year.

A leap year:
- Is divisible by 4
- Is **not** divisible by 100, unless it is also divisible by 400

## Approach
- Start with the simplest valid cases
- Incrementally add rules following TDD
- Keep the logic explicit and readable

## Testing Strategy
- Non-leap years
- Typical leap years (divisible by 4)
- Century years (divisible by 100)
- Special case years (divisible by 400)
- Invalid or missing input

## Possible Improvements
- Support batch processing of years
- Add input validation with custom error types
- Extend to calendar-related utilities
