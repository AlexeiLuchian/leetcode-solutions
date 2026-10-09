class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True

        x_copy = x
        x_reversed = int(str(x)[::-1])

        if x_copy == x_reversed:
            return True
        return False
        