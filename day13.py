# #matrix
# #1.printing matrix reading input from user
# rows=int(input("enter no.of rows: "))
# cols=int(input("enter no.of cols: "))
# matrix=[]
# for i in range(rows):
#     row=list(map(int,input("enter elements in rows: ").split()))
#     matrix.append(row)
# print("matrix: ")
# for i in range(rows):
#     for j in range(cols):
#         print(matrix[i][j], end=" ")
#     print()
# print()
# #printing matrix rows to cols
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=' ')
    print()
print('\n')

#printing matrix cols to rows
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[j][i],end=' ')
    print()