class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        s = ''.join(x.lower() for x in s if x.isalnum())
        return s == s[::-1]

obj = Solution()
s = input()
print(obj.isPalindrome(s))
