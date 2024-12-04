def main():
    # ユーザーから行数と列数を入力として受け取る
    rows = int(input("行数を入力してください: "))
    cols = int(input("列数を入力してください: "))

    # 掛け算表を生成して表示
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            result = i * j
            print(f"{i} x {j} = {result:>2}", end=" | ")
        print()


if __name__ == "__main__":
    main()
