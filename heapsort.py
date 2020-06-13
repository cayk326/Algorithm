def heapify(data, i):
    left = 2 * i + 1# 左のノード
    right = 2 * i + 2# 右のノード
    size = len(data) - 1
    min = i#(i + 1) // 2... すなわち親ノード

    if(left <= size and data[min] > data[left]):# 親ノードよりも左下子ノードのほうが小さい時
        min = left# 左下子ノードのインデックスを親ノードインデックスとして記憶
    if(right <= size and data[min] > data[right]):# 親ノードよりも右下子ノードのほうが小さい時
        min = right# 右下子ノードのインデックスを親ノードインデックスとして記憶
    if min != i:# 交換が必要な場合
        data[i], data[min] = data[min], data[i]
        heapify(data, min)# 交換したらもう一度ヒープ構造をチェックする

def heapsort(data):
    for i in reversed(range(len(data) // 2)):# 根ノードのみを処理する。また、最下層から処理。
        heapify(data, i)# まず初めにヒープを構成する
    sorteddata = []
    for _ in range(len(data)):
        data[0], data[-1] = data[-1], data[0]#最後のノードと先頭のノードを入れ替える
        sorteddata.append(data.pop())#最小ノードを取り出してソート済みの配列に追加する
        heapify(data, 0)# ヒープを再構成
    print(sorteddata)

if __name__ == '__main__':
    data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
    print(heapsort(data))