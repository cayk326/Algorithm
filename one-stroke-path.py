'''
与えられたグラフの中にパスがどれだけ存在するか計算する
パス→全ての頂点を一回ずつのみ通る経路
入力例
N M
a1 b1
a2 b2

aM bM

3 3
1 2
1 3
2 3
'''


def dfs(v, visited):
#頂点Vと訪問済みリストを受け取る
    if not False in visited:# 訪問済みリストにFalseが何もない場合→どこにも訪問していない場合
        return 1
    ans = 0
    #全ての頂点にdfsをそれぞれ適用したいのでfor文を使用する
    for i in range(N):
        # 対象の頂点におけるある隣接頂点iが存在しなければスキップ
        if not graph[v][i]:
            continue
        # 訪問済みリストの中にある、ある頂点についてTRUE→すでに訪問済みならスキップ
        if visited[i]:
            continue


        visited[i] = True#訪問済みにする
        ans += dfs(i, visited)# 更にdfsで深堀
        visited[i] = False#最後にFalseにする

    return ans



N, M = map(int, input().split())#頂点N、辺M
graph = [[0] * N for _ in range(N)]# 頂点の数だけ隣接行列を初期化

#頂点と辺の条件から隣接行列を構成
for _ in range(M):
    a, b = map(int, input().split())
    # インデックスを考慮して1を引く
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

visited = [False] * N # 訪問済みリスト
visited[0] = True# 最初の頂点を訪問済みにする
print(dfs(0, visited))


