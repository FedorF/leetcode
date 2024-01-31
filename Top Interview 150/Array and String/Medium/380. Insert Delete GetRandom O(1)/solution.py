import random


class RandomizedSet:
    """
    Store elements in list, and their indexes in hashmap.


    Time complexity: O(1)
    Space complexity: O(N)

    """

    def __init__(self):
        self.db = []
        self.inset = {}

    def insert(self, val: int) -> bool:
        """
        Add values to database and save its index in db.

        Time complexity: O(1)

        """
        if val in self.inset:
            return False

        self.db.append(val)
        self.inset[val] = len(self.db) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Remove value from hashmap and insert last element in db into index of element we should remove. Update this
        elements index in hashmap.
        Pop last element in db.

        (see illustration in Readme.md)


        Time complexity: O(1)

        """
        if val in self.inset:
            ind = self.inset.pop(val)
            if ind == len(self.db) - 1:
                self.db.pop()
                return True

            self.db[ind] = self.db[-1]
            self.inset[self.db[-1]] = ind
            self.db.pop()
            return True

        return False

    def getRandom(self) -> int:
        """
        Time complexity: O(1)

        """
        if len(self.inset) == 0:
            return

        ind = random.randint(0, len(self.db) - 1)
        return self.db[ind]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
