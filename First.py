if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort(reverse = True)
    a = arr[0]
    for i in range(0,n):
        if arr[i]!=a:
            print arr[i]
            break

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    list = []
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                if i+j+k!=n:
                    list.append([i,j,k])
    print(list)
from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(1,n+1):
        print(i,end = '')

def is_leap(year):
    leap = False
    if year%100 == 0:
        if year%400 ==0:
            leap = True
        else:
            leap = False
    else:
        if year%4 ==0:
            leap = True
    # Write your logic here
    
    return leap
if __name__ == '__main__':
    n = int(raw_input())
    for i in range(0,n):
        print i*i