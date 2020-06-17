def quicksort(data):
    print('Execute quick sort')
    if len(data) <= 1:
        return data

    pivot = data[0] #pivotをデータの先頭にする
    left, right = [], []# 初期化

    left = [i for i in data[1:] if i <= pivot]#iがpivot未満のとき(pivot含む)、左側に追加
    right = [i for i in data[1:] if i > pivot]#iがpivotより大きい時、右側に追加

    left = quicksort(left)
    right = quicksort(right)

    return left + [pivot] + right




if __name__ == '__main__':
    data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
    print(quicksort(data))