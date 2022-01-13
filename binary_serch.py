def binary_serch(a,key):
    start=0
    end=len(a)-1
    
    while start<=end:
        mid=(start+end)//2
        if a[mid]==key:
            return mid
        elif a[mid]<key:
            start=mid+1
        else:
            end=mid-1
    return -1
        
            
def solution(store, customer):
    answer = []
    for i in range(len(customer)):
        if binary_serch(store,customer[i])!=-1:
            answer.append('Yes')
        else:
            answer.append('No')
    return answer

store = [1,2,3,7,8]
customer = [1,5,8,4,6]
answer = solution(store, customer)
print(answer)
