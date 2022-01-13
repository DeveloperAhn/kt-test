def solution(lottos, win_nums):
    answer = []
    rank=[6,6,5,4,3,2,1]
    lotto_max=0
    lotto_min=0
    for i in lottos:
        if i in win_nums:
            lotto_min+=1
        elif i==0:
            lotto_max+=1
        
    answer.append(rank[lotto_max+lotto_min])        
    answer.append(rank[lotto_min])
    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
answer = solution(lottos, win_nums)
print(answer)
