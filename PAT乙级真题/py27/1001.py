#coding:utf-8
"""
	Author: gitzzg
	Date: 2017-2-10

	��Ŀ����
	��������[-2��31�η�, 2��31�η�]�ڵ�3������A��B��C�����ж�A+B�Ƿ����C��

	��������:
	�����1�и���������T(<=10)���ǲ��������ĸ�����������T�����������ÿ��ռһ�У�˳�����A��B��C���������Կո�ָ���


	�������:
	��ÿ�������������һ���������Case #X: true�����A+B>C�����������Case #X: false��������X�ǲ��������ı�ţ���1��ʼ����

	��������:
	4

	1 2 3

	2 3 4

	2147483647 0 2147483646

	0 -2147483648 -2147483647

	�������:
	Case #1: false

	Case #2: true

	Case #3: true

	Case #4: false
"""
T = int(raw_input())
numlist = []
for i in range(T):
    numin = map(int, raw_input().split())
    numlist.append(numin)
for i in range(T):
    print 'Case #%d:' % (i+1), str(numlist[i][0]+numlist[i][1]>numlist[i][2]).lower()