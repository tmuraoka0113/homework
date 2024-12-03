def main():
    data = input("データを入力してください(スペース区切り) > ").split()

    numbers = list(map(int, data))

    total = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    average = total // len(numbers)

    print(f"合計値: {total}")
    print(f"最大値: {maximum}")
    print(f"最小値: {minimum}")
    print(f"平均値: {average}")


if __name__ == "__main__":
    main()
