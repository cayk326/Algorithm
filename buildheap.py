def min_heapify(data, index):
    '''
    あるノードとその配下のノードがヒープ条件を満たすようにする
    つまり、最小ヒープを構成する
    各ノードについてmin_heapifyを繰り返し適用することでヒープを構築する。
    min_heapはbuild_heapから呼び出す

    ■ヒープ条件
    　子ノードは親ノードより常に大きいか等しいもしくは小さいか等しい
    　つまり親ノードとその子ノードに着目した時、親ノードが最小もしくは最大の数になる

    <プロセス>
    1. あるノードiに着目する
    2. あるノードiとその子ノード(左：2*i, 右：2*i+1)はヒープ条件を満たさないが
    　　子ノード(左：)とその配下のノードがヒープ条件を満たすとき
    　　あるノードとその子ノードがヒープ条件を満たすようにノードの交換をする
    :param data:
    :param index:
    :return:
    '''
    left = 2 * index + 1# 左の子ノードのインデックス
    right = 2 * index + 2# 右の子ノードのインデックス
    length = len(data) - 1
    minimum = index# 最小ノードのインデックス

    #左子ノードに対して最小ノードminimumが大きい時は最小ノードminimumをleftにする
    if left <= length and data[minimum] > data[left]:
        minimum = left
    #右子ノードに対して最小ノードminimumが大きい時は最小ノードminimumをrightにする
    if right <= length and data[minimum] > data[right]:
        minimum = right
    # 最小ノードのインデックスとインデックスが一致しないとき、ヒープ条件を満たさないのでノードを交換する
    # このIf文の前の二つのIf文が実行されている場合、最小ノードと仮定していたMinimumは最小では無かったことになるので
    # このif文が実行される
    if minimum != index:
        data[index], data[minimum] = data[minimum], data[index]# 最小ノードを親へ持ってくる
        min_heapify(data, minimum)

def min_build_heap(data):
    # 走査するのはdataの長さ // 2から0までで良い。この範囲でしか子ノードを持たない。
    for i in reversed(range(len(data) // 2)):
        min_heapify(data, i)

def min_heap_push(heap, val):
    heap.append(val)# 値を追加する
    min_build_heap(heap)# ヒープを再構築する

def min_heap_pop(heap):
    '''
    最小値を取り出す。その後、二番目に小さい値を根ノードとして
    再度ヒープを構築する
    :param heap:
    :return:
    '''
    new = heap.pop()# ポップした後の根ノード
    if heap:
        result = heap[0]# heap_popはheapの先頭を返す
        heap[0] = new# 先頭を変える
        min_build_heap(heap)# 再構成する
        return result
    return new



def max_heapify(data, index):
    '''
    あるノードとその配下のノードがヒープ条件を満たすようにする
    つまり、最小ヒープを構成する
    各ノードについてmax_heapifyを繰り返し適用することでヒープを構築する。
    max_heapifyはbuild_heapから呼び出す

    ■ヒープ条件
    　子ノードは親ノードより常に大きいか等しいもしくは小さいか等しい
    　つまり親ノードとその子ノードに着目した時、親ノードが最小もしくは最大の数になる

    <プロセス>
    1. あるノードiに着目する
    2. あるノードiとその子ノード(左：2*i, 右：2*i+1)はヒープ条件を満たさないが
    　　子ノード(左：)とその配下のノードがヒープ条件を満たすとき
    　　あるノードとその子ノードがヒープ条件を満たすようにノードの交換をする
    :param data:
    :param index:
    :return:
    '''
    left = 2 * index + 1# 左の子ノードのインデックス
    right = 2 * index + 2# 右の子ノードのインデックス
    length = len(data) - 1
    maximum = index# 最大ノードのインデックス

    #左子ノードに対して最大ノードmaximumが大きい時は最大ノードmaximumをleftにする
    if left <= length and data[maximum] < data[left]:
        maximum = left
    #右子ノードに対して最大ノードmaximumが大きい時は最大ノードmaximumをrightにする
    if right <= length and data[maximum] < data[right]:
        maximum = right
    # 最大ノードのインデックスとインデックスが一致しないとき、ヒープ条件を満たさないのでノードを交換する
    # このIf文の前の二つのIf文が実行されている場合、最大ノードと仮定していたmaximumは最大では無かったことになるので
    # このif文が実行される
    if maximum != index:
        data[index], data[maximum] = data[maximum], data[index]# 最大ノードを親へ持ってくる
        max_heapify(data, maximum)


def max_build_heap(data):
    for i in reversed(range(len(data) // 2)):
        max_heapify(data, i)


def max_heap_push(heap, val):
    heap.append(val)# 値を追加する
    max_build_heap(data)# ヒープを再構築する

def max_heap_pop(heap):
    '''
    最大値を取り出す。その後、二番目に大きい値を根ノードとして
    再度ヒープを構築する
    :param heap:
    :return:
    '''
    new = heap.pop()
    if heap:
        result = heap[0]
        heap[0] = new
        max_build_heap(heap)
        return result
    return new





if __name__ == '__main__':
    data = [1, 3, 5, 7, 9, 8, 16, 14, 10, 2]
    min_build_heap(data)
    print()
    min_heap_push(data, 0)
    min_heap_pop(data)
    print()
    max_build_heap(data)
    max_heap_push(data, 100)
    max_heap_pop(data)
    print()