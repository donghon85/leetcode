class Solution:
    def isValidSudoku(self, b: List[List[str]]) -> bool:

        rows = []
        n = len(b)
        for i in range(n):
            temp = []
            for j in range(n):
                if b[i][j] != '.':
                    temp.append(b[i][j])
            rows.append(temp)

        cols = []
        for i in range(n):
            temp = []
            for j in range(n):
                if b[j][i] != '.':
                    temp.append(b[j][i])
            cols.append(temp)

        sub1 = []
        for i in range(3):
            for j in range(3):
                if b[i][j] != '.':
                    sub1.append(b[i][j])

        sub2 = []
        for i in range(3):
            for j in range(3, 6):
                if b[i][j] != '.':
                    sub2.append(b[i][j])

        sub3 = []
        for i in range(3):
            for j in range(6, 9):
                if b[i][j] != '.':
                    sub3.append(b[i][j])

        sub4 = []
        for i in range(3, 6):
            for j in range(3):
                if b[i][j] != '.':
                    sub4.append(b[i][j])

        sub5 = []
        for i in range(3, 6):
            for j in range(3, 6):
                if b[i][j] != '.':
                    sub5.append(b[i][j])

        sub6 = []
        for i in range(3, 6):
            for j in range(6, 9):
                if b[i][j] != '.':
                    sub6.append(b[i][j])

        sub7 = []
        for i in range(6, 9):
            for j in range(3):
                if b[i][j] != '.':
                    sub7.append(b[i][j])

        sub8 = []
        for i in range(6, 9):
            for j in range(3, 6):
                if b[i][j] != '.':
                    sub8.append(b[i][j])

        sub9 = []
        for i in range(6, 9):
            for j in range(6, 9):
                if b[i][j] != '.':
                    sub9.append(b[i][j])

        for row in rows:
            if len(row) != len(set(row)):
                return False
        for col in cols:
            if len(col) != len(set(col)):
                return False

        if len(sub1) != len(set(sub1)) or len(sub2) != len(set(sub2)) or len(sub3) != len(set(sub3)) or len(
                sub4) != len(set(sub4)) or len(sub5) != len(set(sub5)) or len(sub6) != len(set(sub6)) or len(
                sub7) != len(set(sub7)) or len(sub8) != len(set(sub8)) or len(sub9) != len(set(sub9)):
            return False

        return True
