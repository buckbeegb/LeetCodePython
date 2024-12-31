class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        combinations = [""]
        letter_map = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        for i in range(len(digits)):
            new_combs = []
            for comb in combinations:
                for val in letter_map[digits[i]]:
                    new_combs.append(comb + val)
            combinations = new_combs
        return combinations if combinations[0] != "" else []


input1 = "23"
input2 = ""
input3 = "2"
print(Solution().letterCombinations(input1))
print(Solution().letterCombinations(input2))
print(Solution().letterCombinations(input3))
