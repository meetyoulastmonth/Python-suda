def func_inv(L):
    '''
    一个至少包含三个元素的整形列表L，若i<j<k,L[i]>L[j]>L[k]是一组逆序对
    返回列表逆序对的个数
    :param L: [1,8,5,3,4,1]
    :return: 7
    '''
    n = len(L)
    count = 0
    for i in range(n-2):
        j = i+1
        while j<n-1:
            while j<n-1 and L[j]>=L[i]:
                j+=1
            if j>=n-1:
                continue
            k = j+1
            while k<n:
                while k<n and L[k]>=L[j]:
                    k+=1
                if k<n:
                    count+=1
                k+=1
            j+=1
    return count


if __name__ == '__main__':
    print(func_inv([1,8,5,3,4,1]))
    print(func_inv([1,2,3]))
    pass
