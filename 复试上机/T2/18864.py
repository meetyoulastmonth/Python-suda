#先把全部因子分解，然后判断质数
# def func_prime(n:int) ->int:
#     '''
#     一个数可以分解为多个质数乘积的结果
#     ex: 18 = 2*3*3
#     :param n:
#     :return: 所分解成质因子的个数
#     '''
#     if n<2:
#         return 0
#     if n<3:
#         return 1
#     if n==4:
#         return 2
#     if n==5:
#         return 1
#     if n==18:
#         return 3
#     count = 0
#     ok= True
#     for j in range(2, n):
#         if n % j == 0:
#             ok = False
#             break
#     if ok:
#         count += 1
#     yinzi = []
#     i = 2
#     while i*i<=n:
#         if n%i==0:
#             yinzi.append(i)
#             if i*i!=n:
#                 yinzi.append(n//i)
#         i+=1
#     for i in range(len(yinzi)):
#         count+=func_prime(yinzi[i])
#
#     return count

def func_prime1(n:int) ->int:
    '''
    一个数可以分解为多个质数的乘积
    ex: 18 = 2*3*3  return:3
    :param n:
    :return: 质因子的个数
    '''
    ans = []
    old = n
    while n>1 and not isPrime(n):
        for i in range(2,n):
            if n%i == 0:
                ans.append(i)
                n = n//i
                break
    if n!=old:
        ans.append(n)
    print(ans)
    return len(ans)

def isPrime(n:int) ->bool:
    for i in range(2,n):
        if n%i==0:
            return False
    return True
if __name__ == '__main__':
    print(func_prime1(27))
    print(func_prime1(25))
    pass
