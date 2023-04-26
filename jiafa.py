# -*- coding: utf-8 -*-
'''
实现相加函数:
计算范围为-99到99的整数和浮点数
方法需要传递两个参数a和b。
如果参数超出范围，打印提示语，返回提示信息
·传入在范围内的参数，方法返回a与b相加的结果
'''
resust=""
def jiafa(a,b):

    if (a>-99 and a <99) and (b>-99 and b <99):
        if (isinstance(a,int)==True or isinstance(a,float)==True) and (isinstance(b,int)==True or isinstance(b,float)==True) :
            result = a + b
            print(f"my result is {result}")
        else:
            result="请输入整数和浮点数"
            print(f"2 result  is {result}")
    else:

        result ="请输入-99到99的整数和浮点数"
        print(f"3 result is {result}")


    return  result
if __name__=='__main__':
    #a,b的初始值
    a=34
    b=3.1415
    test=jiafa(a,b)

