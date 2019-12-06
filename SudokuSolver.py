sudoku1 = [
    [4, 0, 9, 0, 0, 8, 0, 3, 0],
    [7, 5, 0, 0, 3, 2, 0, 1, 8],
    [0, 0, 0, 5, 0, 0, 2, 0, 6],
    [8, 0, 0, 0, 0, 3, 9, 0, 0],
    [0, 3, 0, 0, 4, 0, 0, 7, 5],
    [0, 0, 1, 2, 0, 7, 0, 0, 0],
    [0, 0, 8, 4, 0, 0, 0, 0, 9],
    [0, 1, 0, 0, 0, 9, 0, 4, 0],
    [2, 0, 0, 7, 1, 0, 8, 5, 0]
]

sudoku2 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 8]
]

def Display(s):
    countX = 0
    countY = 0
    for i in range(len(s)):
        if countY == 0 or countY == 3 or countY == 6:
                print('+' + '-' * 7 + '+' + '-' * 7 + '+' + '-' * 7 + '+')
        for j in range(len(s[1])):
            if countX == 0 or countX == 3 or countX == 6:
                print('|', end=' ')
            if s[i][j] == 0:
                print(' ', end=' ')
            else:
                print(s[i][j], end=' ')
            if countX == 8:
                print('|', end='')
                
            countX += 1
        countX = 0
        countY += 1

        print('')
    print('+' + '-' * 7 + '+' + '-' * 7 + '+' + '-' * 7 + '+')

    print('')

def SolveSudoku(newSudoku):
    for i in range(len(sudoku1)):
        for j in range(len(sudoku1[1])):
            if newSudoku[i][j] == 0:
                for num in range(1, len(newSudoku) + 1):
                    if CheckInBox(i, j, num, newSudoku) and CheckInX(i, j, num, newSudoku) and CheckInY(i, j, num, newSudoku):
                        newSudoku[i][j] = num
                        if SolveSudoku(newSudoku):
                            flag = True
                            for a in range(len(sudoku1)):
                                for b in range(len(sudoku1[1])):
                                    if newSudoku[a][b] == 0:
                                        flag = False
                            if flag:
                                Display(newSudoku)
                                exit()

                            newSudoku[i][j] = 0

                return True

def CheckInBox(a, b, num, s):
    horizontal = (b // 3) * 3
    vertical = (a // 3) * 3
    flag = False
    for i in range(vertical , vertical + 3):
        for j in range(horizontal, horizontal + 3):
            if num == s[i][j]:
                flag = True

    return not(flag)

def CheckInX(a, b, num, s):
    flag = False
    for i in range(0, len(s[1])):
        if num == s[a][i]:
            flag = True
    return not(flag)
    
def CheckInY(a, b, num, s):
    flag = False
    for i in range(0, len(s[1])):
        if num == s[i][b]:
            flag = True
    return not(flag)

if __name__ == "__main__":
    print("Select a sudoku to be solved.\n1.) This sudoku can be solved (Medium).")
    Display(sudoku1)
    print("2.) This sudoku cannot be solved.")
    Display(sudoku2)
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        val = SolveSudoku(sudoku1)
    elif choice == 2:
        val = SolveSudoku(sudoku2)

    if val:
        print("Sudoku can't be solved!")