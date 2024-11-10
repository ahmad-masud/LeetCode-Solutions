class Solution:
    def reverseString(s: List[str]) -> None:
        def helper(l, r):
            if l >= r:
                return
            s[l], s[r] = s[r], s[l]
            helper(l + 1, r - 1)

        helper(0, len(s) - 1)