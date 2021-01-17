import heapq
def heapsort(data):
    h = data.copy()
    heapq.heapify(h) # ヒープの構成
    return [heapq.heappop(h) for _ in range(len(data))]# dataの長さだけheappopを実行。これにより、小さい順に出力される

if __name__ == '__main__':

    data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
    print(heapsort(data))