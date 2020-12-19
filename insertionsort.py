def insertionsort(data):
    print('Execute insertion sort')
    for i in range(1, len(data)):
        temp = data[i] # 配列の左端のデータをソート済みとみなし、ソート開始位置の数をtempに記憶
        j = i - 1 # ソート済みの配列の右端のインデックスを抽出
        while(j >= 0 and data[j] > temp):
            '''
            このwhile文では
            1. インデックスIを境に左側がソート済み配列、右側がソート対象配列になる
            2. ソートが終わったとみなしている配列をインデックスJをデクリメントしつつ、インデックスiの値と比較
            3. もし2でdata[j] > data[i]を満たせば、場所を交換する。
            4. そのとき、data[j]を一つ後ろ、すなわちdata[j + 1]に移して、jをデクリメントしてから値をスワップする
            '''
            data[j + 1] = data[j] #要素を一つ後ろにずらす
            j -= 1
        data[j + 1] = temp
    return data

if __name__ == '__main__':
    data = [5,3,4,7,2,8,6,9]
    print(insertionsort(data))