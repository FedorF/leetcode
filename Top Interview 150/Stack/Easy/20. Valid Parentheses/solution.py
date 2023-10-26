def is_valid(parentheses: str):
    """
    Let's keep track of already seen elements. On each step add element to history if it's an opening parentheses.
    and remove last added item if current element is closing one.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    closing = {']': '[', '}': '{', ')': '('}
    history = []
    for x in parentheses:
        if x in closing:
            if len(history) == 0:
                return False

            if closing[x] != history.pop():
                return False
        else:
            history.append(x)

    return len(history) == 0


if __name__ == '__main__':
    assert is_valid('(([]))') is True
    assert is_valid('()[]{}') is True
    assert is_valid(']') is False
    assert is_valid('][') is False
    assert is_valid('({)}') is False
