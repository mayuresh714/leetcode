
def mergeSortInPlace(arr,start = 0,end = 0):
    if end - start == 1:
        return 
    mid = (start+end)//2
    mergeSortInPlace(arr,start,mid)
    mergeSortInPlace(arr,mid,end )
    merge(arr,start,mid,end)

def merge(lis,start,mid,end):
    while mid < end:
        ind = mid
        while ind  and lis[ind- 1]>lis[ind]:
            lis[ind-1],lis[ind] = lis[ind],lis[ind-1]
            ind -= 1
        mid+=1


if __name__ == "__main__":
    lis = [ i for i in range(100,0,-1)]
    l = len(lis) 
    mergeSortInPlace(lis,0,l)
    print(lis)