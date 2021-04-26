'''
https://atcoder.jp/contests/abc007/tasks/abc007_3
入力例
7 8
2 2
4 5
########
#......#
#.######
#..#...#
#..##..#
##.....#
########
答え= 11
'''
from collections import deque
import queue

def show_maze(R, C, maze, cnt, flag):
    print('------------------------------------')
    print('No' + str(cnt))
    if flag == True:
        print('◎このイタレーションでは最短経路の更新がありました')
    else:
        print('×このイタレーションでは最短経路の更新がありませんでした')
    for i in range(R):
        print(maze[i][:])
    print('------------------------------------')

def solve_bfs(R, C, start, goal, maze):
    '''
    与えられた迷路とスタート座標、ゴール座標から最短経路を求める
    キューを使用した幅優先探索を用いている。
    スタート地点から四つの方向(上下左右)に移動した際に通行可能な道('.')で迷路の外に飛び出さなければ
    スタート地点からの距離を計上する
    ゴールにたどり着いたときには自動的に最短経路が求まっている。
    :param R: 迷路の行数
    :param C: 迷路の列数
    :param start: スタート座標
    :param goal: ゴール座標
    :param maze: 迷路を表す二次元配列
    :return: 最短経路
    '''

    '''
    探索に入る前の準備工程
    '''
    visited = [[False] * C for _ in range(R)]# あるマスの訪問済みリストの作成と初期化
    visited[start[0]][start[1]] = True# 初期位置は訪問済みにする
    # dequeを使う場合
    to_visit_deque = deque([start])#訪問予定のマスの集合を表すリストをdequeを使って構成し、初期値としてスタート地点の座標を入れる
    maze[start[0]][start[1]] = 0# スタート地点を移動回数0として初期化する。

    skip_flag = False  # 処理がスキップされたかどうか
    cnt_invest = 0# 調査の回数を格納する



    # 訪問予定リストの中身が存在する間はキューからデキューし続けて、最短経路を探索する
    while len(to_visit_deque):
        curr_y, curr_x = to_visit_deque.popleft()# 訪問予定リストから座標をデキューして、現在のマスの座標としてセットする
        for dy, dx in DIRECTIONS:# 現在のマスから右左上下方向にそれぞれ移動。ループは四回回る
            cnt_invest += 1
            show_maze(R, C, maze, cnt_invest, skip_flag)
            skip_flag = False  # 処理がスキップされたかどうか

            # 移動した後のマス目の座標
            next_y = curr_y - dy
            next_x = curr_x - dx
            # 移動したあとのマスがx座標が0以上Rより小さく、y座標が0以上でCより小さい
            # さらに移動したあとのマスが"."であれば、訪問したことがあるか評価する
            if 0 <= next_y < R and 0 <= next_x < C and maze[next_y][next_x] == '.':
                # 移動した後のマスがすでに訪問済みだった場合は以降の処理をスキップ
                if visited[next_y][next_x] == True:
                    continue
                # 移動した後のマスが初訪問である場合、現在のマスまでの距離 + 1を代入する
                maze[next_y][next_x] = maze[curr_y][curr_x] + 1
                skip_flag = True
                # 移動した後のマスがゴールの座標と同じである場合、距離を返す
                if (next_y, next_x) == goal:
                    return maze[next_y][next_x]
                # まだゴールにたどり着いていなければ移動したマスを訪問済みにする
                # 更に移動した後のマスを訪問予定リストに追加
                else:
                    visited[next_y][next_x] = True
                    to_visit_deque.append((next_y, next_x))# 将来、移動した後のマスを起点に四方向の探索が行われる


def solve_dfs(R, C, start, goal, maze):
    visited = [[False] * C for _ in range(R)]# あるマスの訪問済みリストの作成と初期化
    visited[start[0]][start[1]] = True# 初期位置は訪問済みにする
    # dequeを使う場合
    to_visit_stack = [start]#訪問予定のマスの集合を表すリストをpopを使って構成し、初期値としてスタート地点の座標を入れる
    maze[start[0]][start[1]] = 0# スタート地点を移動回数0として初期化する。


    while to_visit_stack:
        curr_y, curr_x = to_visit_stack.pop()  # 訪問予定リストから座標をpopして、現在のマスの座標としてセットする

        for dy, dx in DIRECTIONS:  # 現在のマスから右左上下方向にそれぞれ移動。ループは四回回る
            # 移動した後のマス目の座標
            next_y = curr_y - dy
            next_x = curr_x - dx
            # 移動したあとのマスがx座標が0以上Rより小さく、y座標が0以上でCより小さい
            # さらに移動したあとのマスが"."であれば、訪問したことがあるか評価する
            if 0 <= next_y < R and 0 <= next_x < C and maze[next_y][next_x] != '#':
                # 移動した後のマスがすでに訪問済みだった場合は以降の処理をスキップ
                if visited[next_y][next_x] == True:
                    continue
                # 移動した後のマスが初訪問である場合、現在のマスまでの距離 + 1を代入する
                maze[next_y][next_x] = maze[curr_y][curr_x] + 1
                skip_flag = True
                # 移動した後のマスがゴールの座標と同じである場合、距離を返す
                if (next_y, next_x) == goal:
                    return maze[next_y][next_x]
                # まだゴールにたどり着いていなければ移動したマスを訪問済みにする
                # 更に移動した後のマスを訪問予定リストに追加
                else:
                    visited[next_y][next_x] = True
                    to_visit_stack.append((next_y, next_x))  # 将来、移動した後のマスを起点に四方向の探索が行われる


if __name__ == '__main__':

    #入力の受け取り
    Row, Column = map(int, input().split())#行数Row、列数Column
    sy, sx = map(lambda n: n - 1,map(int, input().split()))# スタート座標
    gy, gx = map(lambda n: n - 1,map(int, input().split()))# ゴール座標
    maze = [list(input()) for _ in range(Row)]# 迷路全体
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]# 4方向への進み方を格納したリスト
    #print(solve_bfs(Row, Column, (sy, sx), (gy, gx), maze))
    print(solve_dfs(Row, Column, (sy, sx), (gy, gx), maze))