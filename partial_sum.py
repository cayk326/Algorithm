'''
<部分和問題>
  {a0, a1,,, aN-1}の集合において、考えられる部分和のパターン2^N通りを調べれば解ける
  これらの部分集合は0以上2^N未満の整数値に対応付けることが出来る。
'''


'''
<Bit brute-force>
  計算量：2^N通りの状態についてi=0->N-1まで調べるためO(N2^N)となる
  
'''
def bit_brute_force(N, W, A):
    exist = False
    for bit in range(1 << N):
        total = 0
        for i in range(N):
            if bit & (1 << i):
                total += A[i]
        if total == W:
            exist = True
    if exist == True:
        print("Yes")
    else:
        print("No")



if __name__ == '__main__':
    '''
    ex)
    N W
    a0 a1 a2 ... aN-1
    '''
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    bit_brute_force(N, W, A)

