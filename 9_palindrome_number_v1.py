class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True

        x_copy = x
        x_reversed = x % 10
        x //=10
        
        while x:
            last_digit = x % 10
            x_reversed = x_reversed * 10 + last_digit
            x //= 10

        if x_reversed == x_copy:
            return True
        return False