# Q: Given 3 sides, WAP to find whether a given triangle is right angled or not.

int_num = list(map(int,input().split()))
x,y,z = sorted(int_num)
if x**2+y**2==z**2:
    print('Yes')
else:
    print('No')