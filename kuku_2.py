# 下記のような出力が得られる kuku_2.py を実装してください
# 任意の行数および任意の列数での掛け算の結果が得られます
# 出力例1
# $ python kuku_2.py
# 行数を入力してください: 4
# 列数を入力してください: 6
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24

last_number = int(input("行数を入力してください: "))
number_of_doubles = int(input("列数を入力してください: "))


for number1 in range(1, last_number + 1):
    for number2 in range(1, number_of_doubles + 1):
        print(number1 * number2, end=" ")
    print("")
