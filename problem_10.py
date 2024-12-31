class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        matching_criteria = []
        for i in range(len(p)):
            if p[i] == "*":
                matching_criteria[-1] +=  "*"
            else:
                matching_criteria.append(p[i])
        for i in reversed(range(len(matching_criteria))):
            if i > 0 and matching_criteria[i-1] == matching_criteria[i] and "*" in matching_criteria[i]:
                matching_criteria.pop(i)
        s_counter = 0
        match_counter = 0
        while s_counter < len(s) and match_counter < len(matching_criteria):
            if "*" in matching_criteria[match_counter]:
                for i in range(len(s[s_counter:])):
                    if s[s_counter] == matching_criteria[match_counter][0] or matching_criteria[match_counter][0] == ".":
                        if match_counter < len(matching_criteria) - 1:
                            j = match_counter + 1
                            new_criterion = ""
                            while j < len(matching_criteria):
                                new_criterion += matching_criteria[j]
                                j += 1
                            print(new_criterion)
                            if Solution().isMatch(s[s_counter:], new_criterion):
                                return True
                        s_counter += 1
                    else:
                        break
                match_counter += 1
            else:
                if matching_criteria[match_counter] != "." and s[s_counter] != matching_criteria[match_counter]:
                    return False
                match_counter+= 1
                s_counter += 1
        while match_counter < len(matching_criteria):
            if "*" not in matching_criteria[match_counter]:
                return False
            match_counter += 1
        return (s_counter == len(s))

input1 = "aa"
input1a = "a"
input2 = "aa"
input2a = "a*"
input3 = "ab"
input3a = ".*"
input4 = "aab"
input4a = "c*a*b"
input5 = "mississippi"
input5a = "mis*is*p*."
input6 = "aaa"
input6a = "a*a"
input7 = "bbbba"
input7a = ".*a*a"
input8 = "aaaaaaaaaaaaaaaaaaa"
input8a = "a*a*a*a*a*a*a*a*a*b"
print(Solution().isMatch(input1, input1a))
print(Solution().isMatch(input2, input2a))
print(Solution().isMatch(input3, input3a))
print(Solution().isMatch(input4, input4a))
print(Solution().isMatch(input5, input5a))
print(Solution().isMatch(input6, input6a))
print(Solution().isMatch(input7, input7a))
print(Solution().isMatch(input8, input8a))

