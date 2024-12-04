rows = int(input("行数を入力してください: "))
cols = int(input("列数を入力してください: "))

# 行列の生成
matrix = [[(i+1)*(j+1) for j in range(cols)] for i in range(rows)]

# 行列の表示
for row in matrix:
    print(' '.join(map(str, row)))
