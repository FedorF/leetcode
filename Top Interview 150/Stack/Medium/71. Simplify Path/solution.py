def simplify_path(path: str) -> str:
    """
    Define stack.
    Split path by slash. Then iterate through elements and if element is equal to "..", delete last element from stack.
    Otherwise, add element to stack. At the end, join stack element with single slash

    Time complexity: O(n)
    Space complexity: O(n)
    """
    result = []
    for x in path.split("/"):
        if (len(x) > 0) and (x != "."):
            if x == "..":
                if len(result) > 0:
                    result.pop()
            else:
                result.append(x)
    return "/" + "/".join(result)


if __name__ == '__main__':
    assert simplify_path("/home/") == "/home"
    assert simplify_path("/../") == "/"
    assert simplify_path("/home//foo/") == "/home/foo"
    assert simplify_path("/home/user/./Downloads/../Pictures/././") == "/home/user/Pictures"
    assert simplify_path("/a/../../b/../c//.//") == "/c"
