from collections import defaultdict


n, m ,k = map(int, input().split())

vote_dict = defaultdict(int)
rank_list = [2,3,1]
for rank in range(3):
    for i in list(map(int,input().split())):        # 투표
        vote_dict[i] += rank_list[rank]

max_val = max(vote_dict.values())
print(min([k for k,v in vote_dict.items() if max_val == v]))
