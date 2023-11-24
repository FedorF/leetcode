from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Let's define hashmap with sorted word as key, and all anagrams as values. Then traverse through list, sort word and
    check if it's in hashmap.

    Time complexity: O(n*m*log(m)) ~ O(n), due to m <= 100 << n < 10e4 (where m is word's length)
    Space complexity: O(n)
    """
    seen = {}
    for s in strs:
        s_sorted = ''.join(sorted(s))
        if s_sorted in seen:
            seen[s_sorted].append(s)
        else:
            seen[s_sorted] = [s]
    return list(seen.values())


if __name__ == '__main__':
    input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    assert group_anagrams(input) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
