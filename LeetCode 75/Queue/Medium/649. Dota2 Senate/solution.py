from collections import deque


def predict_victory(senate: str) -> str:
    """
    Queue approach.
    Define two queues for both dire and radiant. Each senator represents by its rank in the input string.
    At each loop cycle we'll compare ranks of first senators in both queues.
    We'll add senator with less rank to the end of its queue for the next round. We'll increase his rank by number of
    senators in order to keep relative order.

    (See picture in the Readme.md)


    Time complexity: O(n)
    Space complexity: O(n)

    """
    dire_party, rad_party = deque(), deque()
    for i in range(len(senate)):  # initiate queues
        if senate[i] == "D":
            dire_party.append(i)
        else:
            rad_party.append(i)

    while dire_party and rad_party:  # start voting
        dire = dire_party.popleft()
        radiant = rad_party.popleft()

        if dire < radiant:  # compare senators' ranks
            dire_party.append(len(senate) + dire)  # add to the end
        else:
            rad_party.append(len(senate) + dire)  # add to the end

    if len(dire_party) == 0:
        return "Radiant"

    return "Dire"


if __name__ == '__main__':
    actual, expected = predict_victory("DRRDRDRDRDDRDRDR"), "Radiant"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = predict_victory("RRRDDDD"), "Radiant"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = predict_victory("RD"), "Radiant"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = predict_victory("RDD"), "Dire"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = predict_victory("R"), "Radiant"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = predict_victory("RRRRDDD"), "Radiant"
    assert actual == expected, f"expected: {expected}, actual: {actual}"
