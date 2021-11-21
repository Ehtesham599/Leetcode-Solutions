# Runtime: 48 ms
# Memory: 14.4 MB
class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        if num <= 3999 and num>= 1:
            symbol = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]   
            value =  [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
            i = 0
            while num > 0 :
                while num >= value[i]:
                    num -= value[i]
                    res += symbol[i]
                i += 1
        return res