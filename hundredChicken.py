#!/usr/bin/python
#Filename:hundredChicken
#����5��Ǯһֻ��ĸ��3��Ǯһֻ��С��3ֻһ��Ǯ����100��Ǯ��һ��ֻ�������й�����
#ĸ����С��������Ҫ�У��󹫼���ĸ����С������
for a in range(1,100):
    for b in range(1,100):
        for c in range(3,100,3):
            if (5*a + 3*b + c/3 == 100) and (a + b + c == 100):
                print '������%dֻ��ĸ����%dֻ��С����%dֻ'%(a,b,c)
                break
            else:
                continue
