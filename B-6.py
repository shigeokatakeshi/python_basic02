# N面サイコロをM回振ったときの結果を表示してください
# N, M は正の整数とします
# N, M はユーザーからの入力を利用すること
# 実行例
# サイコロの面の数は?: 8
# 何回振りますか?: 20
# [6, 6, 8, 5, 1, 6, 4, 4, 3, 4, 7, 5, 7, 1, 4, 2, 5, 7, 1, 7]
import random


number_dice_face = input("サイコロの面の数は？: ")
number_shakes = input("何回振りますか？: ")


def dice_n():
    dice_count = []

    for a in range(1, int(number_dice_face) + 1):
        dice_count.append(a)

    return random.choices(dice_count, k=int(number_shakes))


print(dice_n())