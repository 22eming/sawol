def mk_trie(trie, words):
    for word in words:
        cur = trie
        for w in word:
            if w in cur:
                cur = cur[w]
                cur['!'] += 1
            else:
                cur[w] = {}
                cur = cur[w]
                cur['!'] = 1
    return trie

def sear_word(trie, word, answer):
    if word == '':
        return answer
    elif '!' in trie and trie['!'] == 1:
        return answer
    else:
        return sear_word(trie[word[0]], word[1:], answer+1)

def solution(words):
    answer = 0
    trie = mk_trie({}, words)
    for word in words:
        answer += sear_word(trie, word, 0)

    return answer

print(solution(["word","war","warrior","world"]))