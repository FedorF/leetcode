def is_happy(number: int) -> bool:
    """
    Let's say we start with a one-digit number to check if it's a happy number, for example : 4
        4^2= 16
        16->37
        37->58
        ..............
        83->73
        73->58 (loop)
    The reason this sort of loop exists because with a one-digit number we can have square sum as 81,
    which is a 2-digit number. With a 2-digit number (like 99), we can have square sum as a 3-digit number
    (81+81 = 162), but with a 3-digit number (no matter how large, even 999-> 243),
    we cannot have a square sum as a 4-digit number.

    So starting with a one-digit number, we are limited to at max 3-digit sum squares.
    And since the number of numbers that can be represented as a sum of squares and are <1000 are limited,
    the hashset won't be infinitely wrong.
    Similar approach works for bigger numbers involving 5,6,7 .... digits.

    Complexity: O(1)
    """
    seen = set()
    squared_sum_of_digits = number
    while True:
        squared_sum_of_digits = sum(int(x) ** 2 for x in str(squared_sum_of_digits))
        if squared_sum_of_digits == 1:
            return True

        if squared_sum_of_digits in seen:
            return False
        seen.add(squared_sum_of_digits)


if __name__ == '__main__':
    assert is_happy(19) is True
    assert is_happy(2) is False
    assert is_happy(99499492904) is False
    assert is_happy(99499492953405054904) is False
