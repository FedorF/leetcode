def decode(s: str) -> str:
    """
    Apply stack approach.


    Time complexity: O(N)
    Space complexity: O(N)

    """
    stack = []
    i = 0
    while i < len(s):  # run through all elements
        if s[i] == "]":  # starting popping elements from stack and merging into one "message"
            message = ""
            while True:
                el = stack.pop()
                if el == "[":  # merge elements until open bracket is met
                    break
                message = el + message

            repeat = int(stack.pop())  # get number of repeating message
            stack.append(repeat * message)  # add resulting message to the stack

        elif s[i].isdigit() and (len(stack) > 0) and stack[-1].isdigit():  # merge consecutive numbers to one number
            stack[-1] += s[i]

        elif s[i].isalpha() and (len(stack) > 0) and stack[-1].isalpha():  # merge consecutive letters to one message
            stack[-1] += s[i]

        else:
            stack.append(s[i])

        i += 1

    return "".join(stack)


if __name__ == '__main__':
    actual, expected = decode("a"), "a"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = decode("10[a]"), "aaaaaaaaaa"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = decode("3[a2[c]]"), "accaccacc"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = decode("3[a]2[bc]"), "aaabcbc"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = decode("2[abc]3[cd]ef"), "abcabccdcdcdef"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual = decode("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")
    expected = "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
    assert actual == expected, f"expected: {expected}, actual: {actual}"
