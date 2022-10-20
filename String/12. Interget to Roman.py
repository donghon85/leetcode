class Solution:
    def intToRoman(self, num: int) -> str:
        a = ["", "M", "MM", "MMM"]

        b = ["", "C", "CC", "CCC", "CD",
             "D", "DC", "DCC", "DCCC", "CM"]

        c = ["", "X", "XX", "XXX", "XL",
             "L", "LX", "LXX", "LXXX", "XC"]

        d = ["", "I", "II", "III", "IV",
             "V", "VI", "VII", "VIII", "IX"]

        m, num = num // 1000, num % 1000
        m2, num = num // 100, num % 100
        m3, num = num // 10, num % 10

        return a[m] + b[m2] + c[m3] + d[num]