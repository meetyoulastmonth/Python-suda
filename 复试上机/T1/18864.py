def func_str(s:str, k:int) -> int:
    '''
    给定字符串s，找到满足条件的子串，条件是：子串中包含且仅包含的k个不同字符
    返回子串列表，以长度升序，长度相同时以字典顺序
    ex: s='aadbac',k=2
    return: ['ac', 'ad', 'ba', 'db', 'aad']
    :param s: 给定字符串
    :param k: 子串中有且仅有的k个不同字符
    :return: 排序后的字串列表
    '''
    ans = []
    string = ''
    for i in range(len(s)):
        string = ''
        count = 0
        for j in range(i,len(s)):
            if s[j] not in string:
                count+=1
            string += s[j]
            if count==k:
                ans.append(string)
            elif count>k:
                break
    ans.sort(key=lambda x:(len(x),x))
    return ans


if __name__ == '__main__':
    print(func_str('aadbac',2))
    print(func_str('qqwe',4))
    print(func_str('abac',2))
    print(func_str('qwed',1))
    print(func_str('we',0))
    pass
