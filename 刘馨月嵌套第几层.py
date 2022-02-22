def level(mylist):
    #  递归函数的头部
    if  isinstance(mylist,list):  #判断mylist变量是否是一个列表
        max_level = 0
        for x in mylist:
            if isinstance(x,list):
                max_level += level(x)
    #求列表的每一个元素的嵌套层数的最大值
        return  max_level+1
    else:  #不是列表，递归结束条件
        return  0
                  
origin=eval(input())
print(level(origin))