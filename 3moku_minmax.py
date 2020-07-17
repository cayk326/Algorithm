goal = [
    0b111000000, 0b000111000, 0b000000111, 0b100100100,
    0b010010010, 0b001001001, 0b100010001, 0b001010100
]


#ゲームが終了したかどうかチェックする
#3目並べならば、ゲーム終了の状態は9通り
def check(player):
    for mask in goal:
        if player & mask == mask:
            return True
    return False

def minmax(player1, player2, turn):
    if check(player2):#ゲーム終了状態か
        if turn:#自分の番なら勝ち
            return 1
        else:#相手の番なら負け
            return -1
    board = player1 | player2#盤面をセットする
    if board == 0b111111111:#全て盤面が埋まっているか
        return 0

    w = [i for i in range(9) if board & (1 << i) == 0]#置ける場所を探す
    if turn:
        return min([minmax(player2,player1 |  (1 << i), not turn) for i in w])
    else:
        return max([minmax(player2,player1 |  (1 << i), not turn) for i in w])



def play(player1, player2, turn):
    if check(player2):#ゲーム終了
        print([bin(player1),bin(player2)])
    board = player1 | player2
    if board == 0b111111111:#マスがすべて埋まったとき
        print([bin(player1),bin(player2)])
        return

    #ゲーム続行可能な時
    w = [i for i in range(9) if board & (1 << i) == 0]#左方向にビットシフト。 1 << iなら1を左い方向にiだけシフトする。置ける場所を探す

    #mini-max method。評価値を調べる
    r = [minmax(player1,player2 | (1 << i), True) for i in w]

    #評価値が最も高いものを選択
    j = w[r.index(max(r))]

    play(player2, player1 | (1 << j), not turn)


if __name__ == '__main__':
    play(0,0, True)