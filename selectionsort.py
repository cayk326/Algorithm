def selectionsort(data):
    print('Execute selection sort')
    for i in range(len(data)):
        minIdx = i #最小値の位置をセットする
        for j in range(i+1,len(data)):# 比較対象のインデックスの隣から探索開始
            if data[minIdx] > data[j]:# 最小値と仮定している数字よりも小さい数を見つけた場合
                minIdx = j # 最小値のインデックスを更新
        data[i], data[minIdx] = data[minIdx], data[i] # 値を入れ変える


    return data


if __name__ == '__main__':
    data = [6,4,1,-1,-1,8,5,3,7]
    print(selectionsort(data))