row1= int(input("enter number of rows:"))
col1= int(input("enter number of columns:"))
matrix1=[]
print(f"Enter each row with {col1} space seperated number: ")

for i in range(row1):
    row_m1= list(map(int,input().split()))
    matrix1.append(row_m1)

row2= int(input("enter number of rows:"))
col2= int(input("enter number of columns:"))
matrix2 = []
print(f"Enter each row with {col2} space seperated number: ")

for i in range(row2):
    row_m2 = list(map(int, input().split()))
    matrix2.append(row_m2)

result=[[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix2[0]))]
for i in range(len(matrix1[0])):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j]+=matrix1[i][k]*matrix2[k][j]

print(result)

