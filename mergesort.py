def mergesort(data):
    '''
    最初にリストを分割をしていく
    :param data:
    :return:
    '''
    print('Execute merge sort')
    if len(data) <= 1: # dataの長さが1以下の場合はこれ以上分割できない
        return data

    mid = len(data) // 2 #リストの半分の位置を計算する。このとき、切り捨て除算を使用
    left = mergesort(data[:mid])#左から中央までのデータを再帰的に分割
    right = mergesort(data[mid:])#中央から右端までのデータを再帰的に分割

    return merge(left, right)#結合


def merge(left, right):
    result=[]
    i, j = 0, 0
    while(i < len(left)) and (j < len(right)): #左の位置 < 左側データの個数 and 右の位置 < 右側データの個数
        if left[i] <= right[j]:# 左 <= 右のとき =をつけることで安定性を保つ
            result.append(left[i])# 左側から一つ取り出して追加
            i += 1
        else:
            result.append(right[j])# 右側から一つ取り出して追加
            j += 1

    # 余ったデータを追加する
    if i < len(left):
        result.extend(left[i:])# 左側の残りを追加
    if j < len(right):
        result.extend(right[j:])# 右側の残りを追加
    return result




if __name__ == '__main__':
    data = [6,15,4,2,8,5,11,9,7,13]
    print(mergesort(data))