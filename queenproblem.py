def check(x, col):
    for i, row in enumerate(reversed(col)):
        if(x + i + 1 == row or x -i - 1 == row):
            return False
    return True

def search(col):
    # 全ての駒が配置できたら出力する
    if col.__len__() == N:
        print(col)
        return

    for i in range(N):
        if i not in col:#iがcolの中に無い、すなわちiが駒を置ける場所として認識されていないとき
            if check(i, col): #現在の位置とcolをcheck関数に投げる。斜めに駒が無いかをチェック
                print('駒を配置できる')
                col.append(i)# col(駒配置済み列が保存されたリスト)に追加
                search(col)# 再帰的に探索
                col.pop()


if __name__ == '__main__':

    N = 8
    search([])