from collections import defaultdict
import sys
sys.setrecursionlimit(100001)

def mk_trie(trie, words):
    for word in words:
        cur = trie
        for w in word:
            if w in cur:
                cur = cur[w]
                cur['!'].append(len(word))
            else:
                cur[w] = {}
                cur = cur[w]
                cur['!'] = [len(word)]
    return trie

def search_trie(word, trie, lenth):
    count = 0
    if word[0] == '?':
        return trie['!'].count(lenth)
    elif word[0] in trie:
        count += search_trie(word[1:], trie[word[0]], lenth)
    return count

def solution(words, queries):
    answer = []
    rev_w, len_w = [], defaultdict(int)
    for w in words:
        rev_w.append(w[::-1])
        len_w[len(w)] += 1

    trie = mk_trie({}, words)
    rev_trie = mk_trie({}, rev_w)

    for q in queries:
        if q[0] == '?':
            if q[-1] == '?':
                answer.append(len_w[len(q)])
            else:
                answer.append(search_trie(q[::-1], rev_trie, len(q)))
        else:
            answer.append(search_trie(q, trie, len(q)))

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],	["fro??", "????o", "fr???", "fro???", "pro?", "?????"]))

# 검색 키워드는 와일드카드 문자인 '?'가 하나 이상 포함돼 있으며, '?'는 각 검색 키워드의 접두사 아니면 접미사 중 하나로만 주어집니다.