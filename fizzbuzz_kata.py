# FizzBuzz kata
# https://codingdojo.org/kata/FizzBuzz/

def fizzbuzz_kata_tests():
    # Tests for fizz, buzz, fizzbuzz tests
    assert(fizzbuzz_kata_run("3") == "fizz"), "String 3 did not return fizz"
    assert(fizzbuzz_kata_run("5") == "buzz"), "String 5 did not return buzz"
    assert(fizzbuzz_kata_run("15") == "fizzbuzz"), "String 5 did not return fizzbuzz"
    assert(fizzbuzz_kata_run("90") == "fizzbuzz"), "String 5 did not return fizzbuzz"

    # Non divisible by 3 or 5
    assert(fizzbuzz_kata_run("1") == "1"), "String 1 did not return 1"
    assert(fizzbuzz_kata_run("98") == "98"), "String 5 did not return 98"

    # Empty, non-numerical, None
    assert(fizzbuzz_kata_run("") == "Empty, non-numerical"), "Empty string did not return Empty or non-numerical"
    assert(fizzbuzz_kata_run("letters") == "Empty, non-numerical"), "Letters did not return Empty or non-numerical"
    assert(fizzbuzz_kata_run(None) == "Empty, non-numerical"), "Letters did not return Empty or non-numerical"
    
    print("TESTS SUCCESSFUL")

def fizzbuzz_kata_run(number):
    def is_divisible_by_three_or_has_three(number):
        return int(number) % 3 == 0 or "3" in number

    def is_divisible_by_five_or_has_five(number):
        return int(number) % 5 == 0 or "5" in number

    # Validate input
    if number is None or not number.isnumeric():
        return "Empty, non-numerical"

    # Make calculations
    if is_divisible_by_three_or_has_three(number) and is_divisible_by_five_or_has_five(number):
        return "fizzbuzz"
    elif is_divisible_by_three_or_has_three(number):
        return "fizz"
    elif is_divisible_by_five_or_has_five(number):
        return "buzz"
    else:
        return number

fizzbuzz_kata_tests()