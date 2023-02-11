class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = list(s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC"))
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, 
                "D": 500, "M": 1000}
        summe = 0
        for element in numbers:
            summe += dic[element]
        return summe 
