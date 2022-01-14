# Q4 answer template

def solution(k, a, b):
    for i in range(k):
        if a[a.index(min(a))]<b[b.index(max(b))]:
            a[a.index(min(a))],b[b.index(max(b))]=b[b.index(max(b))],a[a.index(min(a))]
    answer=sum(a)
    return answer

k = 3
a = [1,2,5,4,3]
b = [5,5,6,6,5]
answer = solution(k, a, b)
print(answer)
