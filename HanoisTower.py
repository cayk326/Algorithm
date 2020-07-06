def hanoi(n, src, dst, via):
    print('Execute hanois tower')
    if n > 1:
        print()
        hanoi(n - 1, src, via, dst)# srcのn -1 の台をviaに移動
        print(src + '->' + via)
        hanoi(n - 1, src, dst, via)# srcのn -1 の台をdstに移動

    else:
        print(src + '->' + dst)




if __name__ == '__main__':
    n = int(input())
    hanoi(n, 'a', 'b', 'c')