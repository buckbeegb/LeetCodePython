class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        i = 0
        stringRows = ["" for _ in range(numRows)]
        while i < len(s):
            for j in range(numRows + (numRows - 2)):
                print(i+j)
                if i+j < len(s):
                    if j > numRows - 1:
                        stringRows[numRows - (j - numRows) - 2] += s[i+j]
                    else:
                        stringRows[j] += s[i+j]
            i += numRows + (numRows - 2)
        newStr = ""
        print(stringRows)
        for row in stringRows:
            newStr += row
        return newStr

input1 = "PAYPALISHIRING"
input2 = "a"
numRows1 = 3
numRows2 = 4
numRows3 = 1
print(Solution().convert(input1, numRows1))
print(Solution().convert(input1, numRows2))
print(Solution().convert(input2, numRows3))

