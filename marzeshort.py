def marge_short(list):
    #short list ascending order+short list descending order
    if len(list)<=1:
        return list
    
    left,right=split(list)
    left=marge_short(left)
    right=marge_short(right)
    return merge(left,right)

def split(list):
    mid=len(list)//2
    left=list[:mid]
    right=list[mid:]
    return left,right
#short list ascending order+short list descending order
def merge(left,right):
    l1=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            l1.append(left[i])
            i+=1
        else:
            l1.append(right[j])
            j+=1
    while i<len(left):
       
        l1.append(left[i])
        i+=1
    while j<len(right):
        
        l1.append(right[j])
        j+=1
        
    return l1
alist=[54,26,93,17,77,31,44,55,20] #list
def verify_sorted(list):
    n=len(list)
    if n==0 or n==1:
        return True
    return list[0]<list[1] and verify_sorted(list[1:])

l=marge_short(alist)
print(l)
verify_sorted(l)