import numpy as np
from copy import copy


def solution(key, lock):
    key_map = np.array(key)
    l_k = len(key)-1
    lock_map = np.pad(lock, ((l_k, l_k), (l_k, l_k)),
                      constant_values=1)
    for _ in range(4):
        for y in range(len(lock_map)-l_k):
            for x in range(len(lock_map)-l_k):
                tmp = copy(lock_map)
                tmp[y:y+l_k+1, x:x+l_k+1] += key_map
                combi = tmp[l_k:l_k+len(lock), l_k:l_k+len(lock)]
                if np.all(combi == 1):
                    return True
        key_map = np.rot90(key_map)
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
      [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
