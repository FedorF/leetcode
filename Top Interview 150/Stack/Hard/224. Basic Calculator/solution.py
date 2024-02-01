def calc(s: str) -> int:
    """
    Stack approach.
    Transform input string into separate terms (see Readme.md).


    Time complexity: O(len(s))
    Space complexity: O(len(s))

    """
    stack = []
    i = 0
    while i < len(s):
        if s[i] == " ":
            i += 1
            continue

        if s[i] == ")":  # starting popping elements from stack in order to sum elements inside brackets
            total = 0
            val = stack.pop()
            while val != "(":
                total += int(val)
                val = stack.pop()

            if stack and stack[-1] in ("-", "+"):  # consider sign before bracket
                if stack.pop() == "-":
                    total *= -1

            stack.append(total)  # add the resulting element to stack

        elif s[i].isdigit():
            # we should check stack[-1][-1], because, e.g. last number in stack could be -100, so check the last digit
            if stack and stack[-1][-1].isdigit():
                stack[-1] += s[i]  # add current digit to number in stack

            elif stack and stack[-1] in ("-", "+"):  # consider sign before current number (add sign before number)
                stack.append(stack.pop() + s[i])

            else:
                stack.append(s[i])
        else:  # add "(", "-", and "+" as-is
            stack.append(s[i])
        i += 1

    total = 0
    while stack:  # calculate sum of resulting stack
        total += int(stack.pop())

    return total


if __name__ == '__main__':
    actual, expected = calc(s="-1"), -1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc(s="1"), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc(s="-10 + 1"), -9
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc(s="10 + 1"), 11
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc(s="1 + 1"), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc(s=" 2-1 + 2 "), 3
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc(s="(1+(4+5+2)-3)+(6+8)"), 23
    assert actual == expected, f"expected: {expected}, actual: {actual}"
