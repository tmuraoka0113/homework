# 合計値
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# 最大値
def calculate_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


# 最小値
def calculate_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


# 平均値
def calculate_mean(numbers):
    total = calculate_sum(numbers)
    mean = total // len(numbers)  # 小数点を省くために整数除算を使用
    return mean


data = input("データを入力してください(スペース区切り) > ")

numbers = list(map(int, data.split()))

print(f"合計値: {calculate_sum(numbers)}")
print(f"最大値: {calculate_max(numbers)}")
print(f"最小値: {calculate_min(numbers)}")
print(f"平均値: {calculate_mean(numbers)}")
