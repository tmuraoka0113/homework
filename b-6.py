import random


def main():
    # N面サイコロをM回振ったときの結果を表示する
    # N, M は正の整数とする
    n = int(input("N面サイコロの面数を入力してください: "))
    m = int(input("サイコロを振る回数を入力してください: "))

    results = []
    for _ in range(m):
        results.append(random.randint(1, n))

    print(results)


if __name__ == "__main__":
    main()
