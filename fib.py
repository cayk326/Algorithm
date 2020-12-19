import time

def fib_recursion(n):
    '''
    --------------------
    Recursion method
    If you just coded using recursion, elapsed time will be huge.
    Because this method calculate same value over and over again.
    --------------------
    '''

    if n == 0:
        print('Please input value bigger than 0')
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib_recursion(n - 2) + fib_recursion(n - 1)

def fib_memo(n):
    '''
    Memo with dictionary method
    '''
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n -2) + fib_memo(n - 1)
    return memo[n]


def fib_gen(n):
    '''
    General method
    '''
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i - 2] + fib[i -1])
    return fib[n - 1]





def main():
    n = 5
    global memo
    memo = {1: 1, 2: 1}
    '''
    --------------------
    Recursion method
    --------------------    
    '''
    start = time.time()
    res = [fib_recursion(i) for i in range(1, n)]
    end = time.time()
    print('Elapsed time of recursion method is %.5f:' + str(end - start))
    '''
    --------------------
    '''


    '''
    --------------------
    Memo with dictionary method
    --------------------    
    '''
    start2 = time.time()
    res2 = [fib_memo(i) for i in range(1, n)]
    end2 = time.time()
    print('Elapsed time of memo method is %.5f:' + str(end2 - start2))


    '''
    --------------------
     General method
    --------------------    
    '''
    start3 = time.time()
    res3 = [fib_memo(i) for i in range(1, n)]
    end3 = time.time()
    print('Elapsed time of general method is %.5f:' + str(end3 - start3))










if __name__ == '__main__':
    main()