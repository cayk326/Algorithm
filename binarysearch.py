def binarysearch(data, target):
    print('Execute binary search')
    left = 0 #探索範囲の左端
    right = len(data) - 1#探索範囲の右端
    while(left <= right):
        mid = (left + right) // 2#探索範囲の中央値

        if data[mid] == target:#中央の値と探索値が一致した時
            return mid

        elif data[mid] <= target:
            left = mid + 1#中央の値よりも探索値が大きければ左端の値を中央より一つ先の場所にする
        else:
            right = mid - 1#中央の値よりも探索値が小さければ右端の値を中央より一つ前の場所にする
    return -1


if __name__ == '__main__':
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    print(binarysearch(data, 10))
