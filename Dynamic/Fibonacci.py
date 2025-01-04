
memo = [None] * 100

def fib(n):

    if memo[n] is not None:
        return memo[n]

    if n== 0 or n == 1 :
        return n


    memo[n] = fib(n - 1) + fib(n-2)

    return memo[n]

def fib_2(n):

    f_l = [0 , 1]
    for index in range(2 , n+1):
        n_f = f_l[index -1] + f_l[index - 2]
        f_l.append(n_f)

    return f_l[n]


