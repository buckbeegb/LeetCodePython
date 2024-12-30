class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        longest = len(s)
        found_palindrome = False
        while not(found_palindrome):
            for i in range(len(s) - longest+1):
                substring = s[i:i+longest]
                print(substring)
                for j in range(len(substring)//2):
                    print(j, substring[j], substring[-1-j])
                    if substring[j] != substring[-1-j]:
                        found_palindrome = False
                        break
                    else:
                        found_palindrome = True
                if found_palindrome:
                    return substring
            if not(found_palindrome):
                longest -= 1
                if longest == 1:
                    return s[0]
        return ""

input1 = "babad"
input2 = "cbbd"
input3 = "a"
print(Solution().longestPalindrome(input1))
print(Solution().longestPalindrome(input2))
print(Solution().longestPalindrome(input3))

