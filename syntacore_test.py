import numpy as np
from syntacore import weight_spec
from collections import Counter

def test_for_fun(k, N):
    A = np.random.randint(0, 2, (k, N))
    with open('test.txt', 'w') as f:
        for i in ["".join(item) for item in A.astype(str)]:
            f.write(i + '\n')

    max_num = sum([2**i for i in range(k)])
    beta = np.zeros(k, dtype=int)
    for i in range(1, max_num + 1):
        symb = bin(i)[2:]
        el = [0 for _ in range(k - len(symb))]
        for s in symb:
            el.append(int(s))
        beta = np.vstack((beta, el))
    res = beta.dot(A)
    res = res % 2
    r = dict(Counter(res.sum(axis=1)))

    tres = weight_spec('test.txt')
    for k in r.keys():
        if tres[k] != r[k]:
            print('not ok')
            break
    for k in set(tres.keys()).difference(set(r.keys())):
        if tres[k] != 0:
            print('not ok')
            break
    return r

for i in range(3):
    N = np.random.randint(5, 10)
    k = np.random.randint(1, 9)

print('Done')
