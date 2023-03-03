"""
二进制数转字符串。给定一个介于0和1之间的实数（如0.72），类型为double，打印它的二进制表达式。
如果该数字无法精确地用32位以内的二进制表示，则打印“ERROR”。
输入：0.625
输出："0.101"
"""

import math
class Solution:
    def printBin(self, num: float) -> str:
        count=0
        lst = []
        while(num!=1 or count<=32):
            (xs,zs) = math.modf(num*2)
            zs = int(zs)
            lst.append(zs)
            num = xs
            count += 1
            if (zs==1 and xs==0) or count>32:
                break
        if count > 32:
            print("ERROR")
        else:
            mystr = '0.'
            for i in lst:
                mystr = mystr + str(i)
            print(mystr)

