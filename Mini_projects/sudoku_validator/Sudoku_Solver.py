# Rows correct, columns incorrect
# fertig = [
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
# ]

# correctly filled out Sudoku
fertig = [
    [7, 2, 1, 4, 3, 9, 6, 8, 5],
    [6, 3, 8, 5, 2, 7, 4, 1, 3],
    [5, 4, 3, 6, 1, 8, 7, 9, 2],
    [4, 1, 5, 7, 9, 6, 2, 3, 8],
    [3, 7, 6, 8, 5, 2, 1, 4, 9],
    [2, 8, 9, 3, 4, 1, 5, 7, 6],
    [9, 5, 2, 1, 7, 3, 8, 6, 4],
    [8, 3, 7, 2, 6, 4, 9, 5, 1],
    [1, 6, 4, 9, 8, 5, 3, 2, 7]
]

# fucntion to check individual lines


def checker(lines):
    answer = ""
    Summe = sum(lines)
    if Summe != 45:
        answer = "false"
    else:
        answer = "true"
    return answer


# looping to get all 1sts, 2nds,...
for i in range(9):
    rows = [row[i] for row in fertig]
    if checker(rows) == "true":
        print(checker(rows))
    else:
        print("false")
        quit()

# for k in range(9):
#     cols = [colr[k] for colr in rows]
#     if checker(cols) == "true":
#         print(checker(cols))
#     else:
#         print("false")
#         quit()

# print(checker(fertig))
