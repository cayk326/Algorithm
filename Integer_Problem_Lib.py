'''
約数列挙プログラム
[計算量]
    simple_divisors: O(N)
    improvement_divisors: O(N/2)
    quick_divisors: O(N ** (1/2))
'''

def simple_divisors(n):
    '''
    与えられた整数Nの約数を全て列挙し配列にして返す
    計算量 = O(N)
    N = 10^6 -> 0.05789 sec
    N = 10^9 -> 55.6093 sec
    :param n:整数N
    :return: ある整数Nの約数リスト
    '''
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def improvement_divisors(n):
    '''
    与えられた整数Nの約数を全て列挙し配列にして返す
    simple_divisorsに対して、1/2だけ高速化したもの
    ある整数Nに対して全て剰余が0になるか計算するのではなく
    N / 2になった時点で計算をやめる。
    (例)N = 10の場合、割り切れる整数は1, 2, 5, 10で
    N/2より大きい数でNを割り切れる数はN自身のみである。

    計算量 = O(N/2)
    N = 10^6 -> 0.05789 sec
    N = 10^9 -> 42.2700 sec
    :param n:整数N
    :return: ある整数Nの約数リスト
    '''
    divisors = []
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            divisors.append(i)
    divisors.append(n)
    return divisors

def quick_divisors(n):
    '''
    与えられた整数Nに対してN ** (1/2)までの中で
    Nをインクリメント変数で割ったときの余りが０であれば
    lower_divisorsに追加。
    上記条件に加えてNをインクリメント変数で割ったときの商が
    インクリメント変数と一致しなければ
    upper_divisorsに追加
    これにより走査範囲はN ** (1/2)にしつつも
    0 ～ Nまでの約数を列挙できる。
    かなり高速な約数列挙プログラム
    計算量 = O(N ** 1/2)
    N = 10^6 -> 0.00000000 sec
    N = 10^9 -> 0.00897503 sec
    N = 10^12 -> 0.32915115 sec
    :param n:
    :return:
    '''
    lower_divisors , upper_divisors = [], []
    i = 1
    while i**2 <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


'''
素数判定プログラム
'''
def is_prime_trial_division(n):
    '''
    試し割法を用いた素数判定
    与えられた整数Nが素数であるか判定
    「2 ~ nの平方根までの全ての整数で」ループを回してnがiで割り切れるか調査する
    割り切れれば素数ではない
    試し割法はnが取りうるすべての素因数候補をチェックするので
    確実にnの約数を見つけることが出来る。
    つまり、nは合成数であるといえる。
    また、約数が見つからなければnは素数である。

    計算量は多く非効率であるが最もいい手法でも計算量がnに対して指数関数的に増加するため
    この手法でも満足できる。
    例えば、整数Nまでの数に対して素数か判定しようとするとO(N ** 1/2)では
    N = 10^6くらいから計算時間遅くなる
    この手法の計算量はO(n ** 1/2)

    N = 10^6 -> 0.18350887 sec
    N = 10^9 ->

    :param n:整数N
    :return:与えられた整数Nが素数か判定する True or False
    '''
    if n < 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True

def prime_trial_division(n):
    '''
    素数のリストを返すプログラム
    与えられた整数Nに対して、試し割り法で愚直に解く
    計算量：O(N^2)
    N = 10^6 -> 145.1917 sec
    :param n:
    :return:
    '''
    prime = [2]
    for i in range(3, n + 1):
        for div in prime:
            if i % div == 0:
                break
        else:
            prime.append(i)
    return prime

def faster_prime_trial_division(n):
    '''
    素数のリストを返すプログラム
    素数2以外は全て奇数のため、偶数は判定しないことで少しだけ高速になる場合もある
    極限を求めれば結局はO(N^2)である

    計算量：O(N^2 / 2)
    N = 10^6 -> 146.1790 sec
    :param n:
    :return:
    '''
    prime = [2]
    for i in range(3, n + 1, 2):
        for div in prime:
            if i % div == 0:
                break
        else:
            prime.append(i)
    return prime

def prime_eratosthenes(n):
    '''
    エラトステネスの篩による素数判定
    指定された範囲から2で割り切れる数、3で割り切れる数というように
    割り切れる数を順に除外していく
    4以上の全ての偶数は合成数であるため、探索する数字は全て奇数で良い
    計算量はO(nloglogn)
    N = 10^6 -> 1.35042 sec

    :param n:整数N
    :return: 与えられた整数Nまでの素数のリストを返す
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


def is_prime_fermat(n):
    '''
    フェルマーの小定理を用いた素数判定を行う
    ただし、確率的素数判定法であるため、素数でない数を素数であると判断することがある。
    フェルマーの小定理とは、aとpが互いに素な自然数(aとp両方を割り切れる自然数が1だけ)で
    pが素数であるとき、a^(p - 1) = 1 mod pが成り立つという定理
    (a,p) = (1, 7), (2, 7), (3, 7),(4, 7), (5, 7), (6, 7)など

    これより、2つの整数のべき剰余算をして答えが1以外、すなわち合成数であれば
    素数ではないことになる
    :param n:
    :return:
    '''
    n = abs(n)
    # 2は素数
    if n == 2: return True
    # 与えられた整数が2より大きいか、与えられた整数と1をビット演算の積をとって0になる(素じゃない)とき
    # 素数ではない
    if n < 2 or n & 1 == 0: return False

    return pow(2, n -1, n) == 1# a = 2のときの素数をフェルマーの小定理を用いて求める(疑素数あり)


'''
累乗計算

'''

def simple_pow(a, n):
    '''
    aのn乗を計算する
    計算量 = O(n)
    N = 10^6 -> 17.3386 sec
    :param a:
    :param n:
    :return:
    '''
    ans = 1
    for i in range(1, n + 1):
        ans *= a
    return ans

def binary_pow(a, n):
    '''
    aのn乗を二分累乗法を用いて計算する
    計算量 = O(logn)
    N = 10^6 -> 1.345 sec
    :param a:
    :param n:
    :return:
    '''
    ans = 1
    bi = str(format(n, "b"))#n乗の部分を二進表記にする
    for i in range(len(bi)):
        ans *= ans
        if bi[i] == "1":
            ans = ans * a
    return ans

def binnary_pow_mod(a, n, mod):
    '''
    aのn乗を二分累乗法を用いて計算して剰余算をする
    計算量 = O(logn)
    フェルマーの小定理の左辺を計算する際に応用可能
        
    :param a:
    :param n:
    :return:
    '''
    ans = 1
    bi = str(format(n, "b"))#n乗の部分を二進表記にする
    for i in range(len(bi)):
        ans *= ans % mod
        if bi[i] == "1":
            ans = (ans * a) % mod
    return ans


'''
最大公約数
'''

def gcd(a, b):
    '''
    最大公約数には下記の特徴がある
    二つの自然数a, bについてaをbで割った商をq、余りをrとすると
    a / b = q + rで
    gcd(a, b) = gcd(b, r)が成り立つ
    ユークリッドの互除法を活用して自然数a, bの最大公約数を求める
    計算量: a / b = q + rより、a = qb + r
    　　　　よって、q >= 1であり、 a >= b + r >= 2rとなるため
            r <= q / 2
            これはすなわち、ユークリッドの互除法を2回行うと
            (a, b) -> (b, r1) -> (r1, r2)となりa, bは半分以下となる。
            よって計算量は2log aでありO(log a)となる。

    :param a: 整数a
    :param b: 整数b
    :return: 最大公約数
    '''
    while b != 0:
        # a < b であってもa % b = aとなり入れ替わってa及びbに代入されるため条件式はいらない
        a, b = b, a % b
    return a

def recursive_gcd(a, b):
    '''
    最大公約数には下記の特徴がある
    二つの自然数a, bについてaをbで割った商をq、余りをrとすると
    a / b = q + rで
    gcd(a, b) = gcd(b, r)が成り立つ
    ユークリッドの互除法を活用して自然数a, bの最大公約数を求める
    再帰型

    計算量: a / b = q + rより、a = qb + r
    　　　　よって、q >= 1であり、 a >= b + r >= 2rとなるため
            r <= q / 2
            これはすなわち、ユークリッドの互除法を2回行うと
            (a, b) -> (b, r1) -> (r1, r2)となりa, bは半分以下となる。
            よって計算量は2log aでありO(log a)となる。

    :param a: 整数a
    :param b: 整数b
    :return: 最大公約数
    '''
    if b == 0:
        return a
    else:
        return recursive_gcd(b, a % b)

def extgcd(a, b):
    '''
    ax + by = gcd(a, b) = dを満たすx, y, dを求める
    拡張ユークリッド互除法を用いて不定方程式を解く
    :param a:
    :param b:
    :return:
    '''
    if b == 0:
        return a, 1, 0
    else:

        d, y, x = extgcd(b, a % b)
        y -= (a // b) * x
        return d, x, y


def lcm(a, b):
    '''
    最小公倍数を求める
    正の整数a, bに対して最大公約数をg,　最小公倍数をlとすると
    ab = gl
    よってl = ab/g
    計算量: O(log a)gcdに依存する。
    :param a:
    :param b:
    :return:
    '''
    return (a * b) // recursive_gcd(a,b)



def test_divisors():
    import time
    N = 1000000
    start_time = time.time()
    print(simple_divisors(N))
    duration = time.time() - start_time
    print('{:.08f}'.format(duration))

    start_time = time.time()
    print(improvement_divisors(N))
    duration2 = time.time() - start_time
    print('{:.08f}'.format(duration2))

    start_time = time.time()
    print(quick_divisors(N))
    duration3 = time.time() - start_time
    print('{:.08f}'.format(duration3))

def test_prime():
    import time
    N = 1000000
    '''
    
    start_time = time.time()
    print(prime_trial_division(N))
    duration = time.time() - start_time
    print('{:.08f}'.format(duration))

    start_time = time.time()
    print(faster_prime_trial_division(N))
    duration2 = time.time() - start_time
    print('{:.08f}'.format(duration2))
    '''
    start_time = time.time()
    print(prime_eratosthenes(N))
    duration3 = time.time() - start_time
    print('{:.08f}'.format(duration3))






if __name__ == '__main__':
    #test_prime()
    print(gcd(300, 780))
    print(is_prime_fermat(100))
    print(binnary_pow_mod(3, 100, 19))
