import heapq
from typing import List


class TrieNode:
    """
    Prefix tree node implementation with minheap storage of sub-nodes keys. So, children keys are kept
    in lexicographical order.
    
    """

    def __init__(self):
        self.is_end = False
        self.children_nodes = {}  # sub-nodes storage
        self.children = []  # sub-nodes keys storage

    def insert(self, word: str):
        """

        Time complexity: O(len(word))
        Space complexity: O(len(word) * log(len(self.children)))

        """
        node = self
        for c in word:
            if c not in node.children_nodes:
                node.children_nodes[c] = TrieNode()  # add node for current letter
                heapq.heappush(node.children, c)  # add current letter to heap
            node = node.children_nodes[c]
        node.is_end = True

    def find_similar(self, query: str, n: int) -> List[str]:
        """

        Time complexity: O(len(query))

        """
        node = self
        for c in query:  # find query prefix node
            if c not in node.children_nodes:
                return []
            node = node.children_nodes[c]

        def dfs(cur_node: TrieNode, suggestion: str):
            nonlocal res, n
            if n <= 0 or not cur_node:
                return

            if cur_node.is_end:  # found a word - ddd it to resulting list
                res.append(suggestion)
                n -= 1

            # drawn n letters from current node's children.
            # we should get lexicographical order, so use minheap
            for child in heapq.nsmallest(n, cur_node.children):
                # iterate through all sub-nodes of current child
                dfs(cur_node.children_nodes[child], suggestion + child)

            return

        res = []
        dfs(node, query)
        return res


class SuggestSystem:

    def __init__(self, n_suggest: int = 3):
        self.trie = TrieNode()
        self.n_suggest = n_suggest
        self.is_fitted = False

    def __repr__(self):
        return f"{str(self.__class__.__name__)}()"

    def fit(self, documents: List[str]):
        for doc in documents:
            self.trie.insert(doc)
        self.is_fitted = True

    def suggest(self, query: str) -> List[str]:
        if not self.is_fitted:
            raise Exception(f"{self} is not fitted. Run fit() first")

        res = self.trie.find_similar(query, self.n_suggest)
        return res


def get_suggestions(documents: List[str], query: str) -> List[List[str]]:
    suggest_system = SuggestSystem()
    suggest_system.fit(documents)
    res = []
    q = ""
    for i in range(len(query)):
        q += query[i]
        res.append(suggest_system.suggest(q))

    return res


if __name__ == '__main__':
    expected = [["mobile", "moneypot", "monitor"],
                ["mobile", "moneypot", "monitor"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"]]
    actual = get_suggestions(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse")
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    expected = [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]]
    actual = get_suggestions(["havana"], "havana")
    assert actual == expected, f"expected: {expected}, actual: {actual}"
