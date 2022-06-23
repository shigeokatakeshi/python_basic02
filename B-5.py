# スペース区切りで入力された整数群において、以下の4つの統計量を計算アプリを実装してください
# 合計値
# 最大値
# 最小値
# 平均値
# ただし、計算用の組み込み関数やライブラリは使わないこと(sum()やnp.mean()などはNG print()はOK)
# 1つの統計量につき、それ専用の関数を実装すること
# 実行例
# データを入力してください(スペース区切り) > 1 1 2 3 5 8 13 21
# 合計値: 54
# 最大値: 21
# 最小値: 1
# 平均値: 6

number = input("スペース区切り(一つ)で整数を入力してください: ")
number_non_space = number.split(" ")
element_number = len(number_non_space)

# 合計値


def total_number():
    total_value = 0

    for a in range(0, element_number):
        total_value = total_value + int(number_non_space[a])
    print(total_value)


# 最大値
def greatest_number():
    greatest_value = number_non_space[0]

    for b in range(1, element_number):
        if int(greatest_value) < int(number_non_space[b]):

            greatest_value = number_non_space[b]
    print(greatest_value)


# 最小値
def mini_number():
    mini_value = number_non_space[0]

    for c in range(1, element_number):
        if int(mini_value) >= int(number_non_space[c]):
            mini_value = number_non_space[c]

    print(mini_value)


# 平均値
def average_number():
    total_value = 0

    for a in range(0, element_number):
        total_value = total_value + int(number_non_space[a])
    print(total_value / element_number)



if __name__ == "__main__":
    total_number()
    greatest_number()
    mini_number()
    average_number()
