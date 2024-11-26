class Solution:
    def climbStairs(self, n: int) -> int:
        def backtrack(steps: int) -> int:
            if steps == n:
                return 1
            elif steps > n:
                return 0

            return backtrack(steps + 1) + backtrack(steps + 2)

        return backtrack(0)