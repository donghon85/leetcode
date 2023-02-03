class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        ans = [[""] * n for _ in range(numRows)]
        row, col, idx = 0, 0, 0
        direction = "D"
        while idx < n:
            ans[row][col] = s[idx]
            if direction == "D":
                if row + 1 >= numRows:
                    direction = "U"
                    col + 1
                else:
                    row += 1

            if direction == "U":
                if row - 1 < 0:
                    direction = "D"
                    row += 1
                else:
                    row -= 1
                    col += 1
            idx += 1

        answer = ""
        for i in range(len(ans)):
            answer += ''.join(ans[i])
        return answer


