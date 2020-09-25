A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sumLeft = 0
for row in range(len(A)):
    for column in range(len(A[row])):
        if row == column:
            sumLeft += A[row][column]
print(sumLeft)