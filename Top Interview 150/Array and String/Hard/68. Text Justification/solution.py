from typing import List


def make_wide_space(width: int) -> str:
    space = ""
    for i in range(width):
        space += " "
    return space


def calc_letters(text: List[str]) -> int:
    num_letters = 0
    for x in text:
        num_letters += len(x)
    return num_letters


def calc_spaces(text: List[str]) -> int:
    return len(text) - 1


def justify_line(text: List[str], width: int) -> str:
    if len(text) == 1:
        return text[0]

    num_letters = calc_letters(text)
    num_spaces = calc_spaces(text)
    output = ""
    base_width = (width - num_letters) // num_spaces
    remainder = (width - num_letters) % num_spaces
    for i in range(len(text)):
        output += text[i]
        if i < len(text) - 1:  # add space after words except last one
            if remainder > 0:  # increase space width if we have extra space
                output += make_wide_space(base_width + 1)
                remainder -= 1
            else:
                output += make_wide_space(base_width)

    return output


def justify_last_line(text: List[str], width: int) -> str:
    output = ""
    for i in range(len(text)):
        output += text[i]
        if i == len(text) - 1:
            output += make_wide_space(width - calc_letters(text) - calc_spaces(text))
        else:
            output += " "
    return output


def justify_full(text: List[str], width: int) -> List[str]:
    """
    Brute algorithm

    Time complexity: O(N^2)
    Space complexity: O(N)
    """
    line_width = 0
    lines = []
    current_line = []
    for i in range(len(text)):
        word = text[i]
        current_line.append(word)
        line_width += len(word)
        if i == len(text) - 1:  # it's the last word, so exit the cycle
            lines.append(current_line)
            continue
        if line_width + 1 + len(text[i + 1]) > width:  # finish current line
            lines.append(current_line)
            current_line = []
            line_width = 0
        else:  # take space width into account
            line_width += 1

    for i in range(len(lines)):
        if (i == len(lines) - 1) or (len(lines[i]) == 1):  # apply special function if it's the last line or if there is
            lines[i] = justify_last_line(lines[i], width)  # only one word in line
        else:
            lines[i] = justify_line(lines[i], width)
    return lines


if __name__ == '__main__':
    assert justify_line(["This", "is", "an"], 16) == "This    is    an"
    assert justify_line(["understand", "well"], 20) == "understand      well"
    assert justify_line(["a", "computer.", "Art", "is"], 20) == "a  computer.  Art is"

    assert justify_last_line(["shall", "be"], 16) == "shall be        "
    assert justify_last_line(["do"], 20) == "do                  "

    text = ["This", "is", "an", "example", "of", "text", "justification."]
    width = 16
    expected = [
        "This    is    an",
        "example  of text",
        "justification.  "
    ]
    assert justify_full(text, width) == expected

    text = ["What", "must", "be", "acknowledgment", "shall", "be"]
    width = 16
    expected = [
        "What   must   be",
        "acknowledgment  ",
        "shall be        "
    ]
    assert justify_full(text, width) == expected

    text = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
            "Art", "is", "everything", "else", "we", "do"]
    width = 20
    expected = [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  "
    ]
    assert justify_full(text, width) == expected

