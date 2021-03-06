maze = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 9],
    [9, 0, 9, 0, 0, 0, 9, 9, 0, 9, 9, 9],
    [9, 0, 9, 9, 0, 9, 0, 0, 0, 9, 0, 9],
    [9, 0, 0, 0, 9, 0, 0, 9, 9, 0, 9, 9],
    [9, 9, 9, 0, 0, 9, 0, 9, 0, 0, 0, 9],
    [9, 0, 0, 0, 9, 0, 9, 0, 0, 9, 1, 9],
    [9, 0, 9, 0, 0, 0, 0, 9, 0, 0, 9, 9],
    [9, 0, 0, 9, 0, 9, 0, 0, 9, 0, 0, 9],
    [9, 0, 9, 0, 9, 0, 9, 0, 0, 9, 0, 9],
    [9, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
]
N = 12

pos = [[1,1,0]] # 初期位置　posには探索する位置が格納されている

while(len(pos)) > 0:
    x, y, depth = pos.pop()# リストから探索する位置を取得する

    #ゴールについたとき
    if maze[x][y] == 1:
        print(depth)
        break
    #ゴールについてない場合、現在の位置を探索済みとしてセットする
    maze[x][y] = 2

    #現在地からの上下左右方向に遷移できるポジションを全て探索して、posにセットする。最大で4つ
    if maze[x - 1][y] < 2:
        pos.append([x - 1, y, depth + 1])#移動回数を増やして現在位置の左側情報をリストに追加

    if maze[x + 1][y] < 2:
        pos.append([x + 1, y, depth + 1])#移動回数を増やして現在位置の右側情報をリストに追加

    if maze[x][y - 1] < 2:
        pos.append([x, y - 1, depth + 1])#移動回数を増やして現在位置の上側情報をリストに追加

    if maze[x][y + 1] < 2:
        pos.append([x, y + 1, depth + 1])  # 移動回数を増やして現在位置の下側情報をリストに追加

    print('-------------------------------',end='\n')
    print('Step No:' + str(depth),end='\n')
    for i in range(N):
        print(maze[i],end='\n')
    print('-------------------------------',end='\n')
