class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        apps = [0] * 26

        for i in range(len(s)):
            apps[ord(s[i]) - ord('a')] += 1
            apps[ord(t[i]) - ord('a')] -= 1
        
        for app in apps:
            if app != 0:
                return False
        return True