# 3都府県のいくつかの駅名とある日の最高気温のデータを辞書として持っています
# このデータを使って3つの問を満たす実装をしてください
def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {"prefecture": "東京都", "station": "渋谷", "temperature": 6.5},
        {"prefecture": "東京都", "station": "池袋", "temperature": 7.0},
        {"prefecture": "東京都", "station": "新橋", "temperature": 7.5},
        {"prefecture": "大阪府", "station": "梅田", "temperature": 8.2},
        {"prefecture": "大阪府", "station": "大阪", "temperature": 9.3},
        {"prefecture": "大阪府", "station": "堺", "temperature": 9.5},
        {"prefecture": "福岡県", "station": "博多", "temperature": 13.0},
        {"prefecture": "福岡県", "station": "太宰府", "temperature": 15.0},
    ]
    # Q1. 全国の平均気温を計算してください(9.5となればOK)
    sum = 0
    for average in range(0, 8):
        average = weather_information[average]["temperature"]
        sum = sum + float(average)
    print(sum / 8)

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
    oosaka_count = 0
    oosaka_count2 = 1
    for a in range(0, 8):
        if weather_information[a]["prefecture"] == "大阪府":
            oosaka_count = oosaka_count + 1
    for a in range(0, 8):
        if oosaka_count == oosaka_count2:
            print(weather_information[a]["station"])
            break
        if weather_information[a]["prefecture"] == "大阪府":
            print(weather_information[a]["station"], end=",")
            oosaka_count2 = oosaka_count2 + 1

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)
    sum = 0
    fukuoka_count = 0
    for a in range(0, 8):
        if weather_information[a]["prefecture"] == "福岡県":
            average = a
            average = weather_information[average]["temperature"]
            sum = sum + float(average)
            fukuoka_count = fukuoka_count + 1
    print(sum / fukuoka_count)


if __name__ == "__main__":
    main()
