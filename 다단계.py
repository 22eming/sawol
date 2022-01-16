def solution(enroll, referral, seller, amount): # 구성원 부모 판매자 개수
    member = dict()
    member["-"] = ["_", 0]
    for i in range(len(enroll)):
        member[enroll[i]] = [referral[i], 0]

    for i in range(len(seller)):
        sell = amount[i] * 100
        selle = seller[i]
        while sell != 0 and selle != "-":
            change = sell // 10
            member[selle][1] += sell - change
            sell = change
            selle = member[selle][0]
    return [ member[i][1] for i in enroll]

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],	["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]	,["young", "john", "tod", "emily", "mary"],	[12, 4, 2, 5, 10]))