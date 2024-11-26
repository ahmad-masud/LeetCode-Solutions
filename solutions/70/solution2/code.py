class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def backtrack(steps: int) -> int:
            if steps == n:
                return 1
            elif steps > n:
                return 0
            elif steps in memo:
                return memo[steps]

            memo[steps] = backtrack(steps + 1) + backtrack(steps + 2)
            
            return memo[steps]

        return backtrack(0)