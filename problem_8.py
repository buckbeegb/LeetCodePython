class Solution:
    def myAtoi(self, s: str) -> int:
        v = ""
        for i in range(len(s)):
            if s[i] != " ":
                v = s[i:]
                break
        multiplier = 1
        if len(v) < 1:
            return 0
        if v[0] == "-" or v[0] == "+" :
            multiplier = -1 if v[0] == "-" else 1
            v = v[1:]
        int_list = []
        for i in range(len(v)):
            val = ord(v[i]) - 48
            if val < 0 or val > 9:
                break
            else:
                int_list.append(val)
        output = 0
        for i in range(len(int_list)):
            output += int_list[len(int_list)-1-i] * (10 ** i)
        return max(min(output * multiplier, 2147483647), -2147483648)

input1 = "42"
input2 = "   -042"
input3 = "1337c0d3"
input4 = "0-1"
input5 = "words and 987"
input6 = ""
print(Solution().myAtoi(input1))
print(Solution().myAtoi(input2))
print(Solution().myAtoi(input3))
print(Solution().myAtoi(input4))
print(Solution().myAtoi(input5))
print(Solution().myAtoi(input6))

