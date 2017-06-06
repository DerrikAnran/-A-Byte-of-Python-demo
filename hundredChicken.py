#!/usr/bin/python
#Filename:hundredChicken
#公鸡5文钱一只，母鸡3文钱一只，小鸡3只一文钱，用100文钱买一百只鸡，其中公鸡、
#母鸡、小鸡都必须要有，求公鸡、母鸡、小鸡数量
for a in range(1,100):
    for b in range(1,100):
        for c in range(3,100,3):
            if (5*a + 3*b + c/3 == 100) and (a + b + c == 100):
                print '公鸡有%d只，母鸡有%d只，小鸡有%d只'%(a,b,c)
                break
            else:
                continue
