class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        if num == 0:
            return ""
        if num // 1000 != 0:
            while num >= 1000:
                roman += "M"
                num = num - 1000
            return roman + Solution().intToRoman(num)
        elif num // 900 != 0:
            return "CM" + Solution().intToRoman(num - 900)
        elif num // 500 != 0:
            return "D" + Solution().intToRoman(num - 500)
        elif num // 400 != 0:
            return "CD" + Solution().intToRoman(num - 400)
        elif num // 100 != 0:
            while num >= 100:
                roman += "C"
                num = num - 100
            return roman + Solution().intToRoman(num)
        elif num // 90 != 0:
            return "XC" + Solution().intToRoman(num - 90)
        elif num // 50 != 0:
            return "L" + Solution().intToRoman(num-50)
        elif num // 40 != 0:
            return "XL" + Solution().intToRoman(num-40)
        elif num // 10 != 0:
            while num >= 10:
                roman += "X"
                num -= 10
            return roman + Solution().intToRoman(num)
        elif num == 9:
            return "IX"
        elif num >= 5:
            return "V" + Solution().intToRoman(num-5)
        elif num == 4:
            return "IV"
        else:
            while num > 0:
                roman += "I"
                num -= 1
            return roman
        


input1 = 3749
input2 = 58
input3 = 1994
input4 = 10
print(Solution().intToRoman(input1))
print(Solution().intToRoman(input2))
print(Solution().intToRoman(input3))
print(Solution().intToRoman(input4))
