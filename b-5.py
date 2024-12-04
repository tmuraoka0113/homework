def main():
    # データ入力を受け取る
    data = input("データを入力してください(スペース区切り) > ").split()

    # 入力データを整数リストに変換
    numbers = list(map(int, data))

    # 合計値
    total = 0
    for number in numbers:
        total += number

    # 最大値
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number

    # 最小値
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number

    # 平均値
    average = total // len(numbers)

    print(f"合計値: {total}")
    print(f"最大値: {maximum}")
    print(f"最小値: {minimum}")
    print(f"平均値: {average}")


if __name__ == "__main__":
    main()
