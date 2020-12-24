class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numbers = dict([("I",1), ("V", 5 ), ('X', 10), ("L", 50), ("C", 100) ,("D", 500), ("M", 1000)])
        running_total = 0
        for index in range(len(s)-1):
            if (roman_numbers[s[index]] < roman_numbers[s[index+1]]):
                running_total -= roman_numbers[s[index]]
            else:
                running_total += roman_numbers[s[index]]
        running_total += roman_numbers[s[len(s) - 1]]

        return(running_total)
