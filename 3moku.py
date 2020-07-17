import random
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


def play(player1, player2):
    if check(player2):#ゲーム終了
        print([bin(player1),bin(player2)])
    board = player1 | player2
    if board == 0b111111111:#マスがすべて埋まったとき
        print([bin(player1),bin(player2)])
        return

    #ゲーム続行可能な時
    w = [i for i in range(9) if board & (1 << i) == 0]#左方向にビットシフト。 1 << iなら1を左い方向にiだけシフトする。置ける場所を探す
    r = random.choice(w)#wの中からラン団に選択
    play(player2, player1 | (1 << r))


if __name__ == '__main__':
    play(0,0)