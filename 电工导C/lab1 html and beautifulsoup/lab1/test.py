import numpy as np
import itertools

arr=[0]+[1 ,-3, 4, -2, -1, 6]
pre=[0]+list(itertools.accumulate(arr))
def findmax(l,r):
    if l>=r:return arr[l]
    mid=(l+r)//2
    x=0
    midMax=0
    for i in range(l,mid+1):
        x=max(x,pre[mid]-pre[i-1])
    midMax=x
    x=0
    for i in range(mid,r):
        x=max(x,pre[i]-pre[mid-1])
    midMax+=x
    return max(findmax(l,mid),findmax(max(mid+1,r),midMax))

findmax(1,len(arr)+1)
