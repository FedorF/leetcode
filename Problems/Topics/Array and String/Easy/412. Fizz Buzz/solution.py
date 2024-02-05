from typing import List


def run_fizz_buzz(n: int) -> List[str]:
    """


    Time complexity: O(n)
    Space complexity: O(1)

    """
    res = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            res.append("FizzBuzz")

        elif i % 3 == 0:
            res.append("Fizz")

        elif i % 5 == 0:
            res.append("Buzz")

        else:
            res.append(str(i))

    return res


if __name__ == '__main__':
    actual, expected = run_fizz_buzz(n=3), ["1", "2", "Fizz"]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = run_fizz_buzz(n=5), ["1", "2", "Fizz", "4", "Buzz"]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual = run_fizz_buzz(n=15)
    expected = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
