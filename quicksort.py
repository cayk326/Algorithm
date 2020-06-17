def quicksort(data):
    print('Execute quick sort')
    if len(data) <= 1:
        return data

    pivot = data[0] #pivotをデータの先頭にする
    left, right, same = [], [], 0 # 初期化

    for i in data:
        if i < pivot:#iがpivotより小さい時、左側に追加
            left.append(i)
        elif i > pivot:#iがpivotより大きい時、右側に追加
            right.append(i)
        else:#pivotとおなじ数をカウント
            same += 1
    left = quicksort(left)
    right = quicksort(right)

    return left + [pivot] * same + right




if __name__ == '__main__':
    data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
    print(quicksort(data))