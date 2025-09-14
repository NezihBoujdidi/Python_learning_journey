class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        for i in range(len(s)-1):
            if symbol_value[s[i]]<symbol_value[s[i+1]]:
                total -= symbol_value[s[i]]
            else:
                total += symbol_value[s[i]]
        total += symbol_value[s[-1]]
        return total
