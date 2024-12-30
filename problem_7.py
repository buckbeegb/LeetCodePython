class Solution:
    def reverse(self, x: int) -> int:
        reversed = 0
        digits = []
        is_negative = False if x >= 0 else True
        if is_negative:
            x = x * -1
        while x != 0:
            digits.append(x % 10)
            x = x // 10
        for i in range(len(digits)):
            reversed += digits[len(digits)- 1 - i] * (10 ** i)
        reversed = reversed * -1 if is_negative else reversed
        if reversed > 2147483647 or reversed < -2147483648:
            return 0
        else:
            return reversed

input1 = 123
input2 = -123
input3 = 120
input4 = 1534236469
print(Solution().reverse(input1))
print(Solution().reverse(input2))
print(Solution().reverse(input3))
print(Solution().reverse(input4))

