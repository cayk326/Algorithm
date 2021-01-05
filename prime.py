def is_prime_trial_division(n):
    '''
    試し割法を用いた素数判定
    「2 ~ nの平方根までの全ての整数で」ループを回してnがiで割り切れるか調査する
    割り切れれば素数ではない
    試し割法はnが取りうるすべての素因数候補をチェックするので
    確実にnの約数を見つけることが出来る。
    つまり、nは合成数であるといえる。
    また、約数が見つからなければnは素数である。

    計算量は多く非効率であるが最もいい手法でも計算量がnに対して指数関数的に増加するため
    この手法でも満足できる。n = 10^5もしくは10^6くらいから計算時間遅くなる
    この手法の計算量はO(n ** 1/2)

    改善手法として、予め素数のリストを用意してその素数リストの奇数部だけを使って
    判定すると幾分か高速化できる
    素数リストはエラストテネスの篩を使うとよい
    でも、そんなことするなら最初からエラトステネスの篩を使ったほうが良い。。。
    :param n:
    :return:
    '''
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_prime_eratosthenes(n):
    '''
    エラトステネスの篩による素数判定
    指定された範囲から2で割り切れる数、3で割り切れる数というように
    割り切れる数を順に除外していく
    4以上の全ての偶数は合成数であるため、探索する数字は全て奇数で良い
    計算量はO(nloglogn)
    :param n:
    :return:
    '''
    if n <= 1:
        return []

    prime = [2]
    limit = int(n ** 0.5)
    # 奇数のリストを作成
    odd_list = [i + 1 for i in range(2, n, 2)]

    while limit > odd_list[0]:
        prime.append(odd_list[0])
        # 割り切れない数で構成されたリストをリスト内包表記で作成し、odd_listを更新する
        odd_list = [j for j in odd_list if j % odd_list[0] != 0]

    return prime + odd_list # リストを結合

if __name__ == '__main__':
    ans = is_prime_eratosthenes(10**5)
    print(ans)
    for i in range(200):
        if is_prime_trial_division(i):
            print(i, end=' ')


