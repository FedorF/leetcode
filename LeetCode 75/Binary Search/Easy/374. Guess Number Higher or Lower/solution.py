def guess(num: int) -> int:
    pass


class Solution:
    @staticmethod
    def guess_number(n: int) -> int:
        l, r = 1, n
        while l < r:
            mid = (r + l) // 2
            response = guess(mid)

            if response == 0:
                return mid

            elif response == 1:
                l = mid + 1

            else:
                r = mid

        return l
