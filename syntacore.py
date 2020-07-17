def weight_spec(filename):
    with open(filename) as f:
        lines = f.read().split('\n')
        N = len(lines[0])
        k = len(lines)
#       Считываю матрицу в транспонированном виде
        A = [[int(line[i]) for line in lines] for i in range(N)]

    max_num = sum([2**i for i in range(k)])
    counter = {_: 0 for _ in range(N + 1)}
    for i in range(max_num + 1):
        Q = [sum([int(x) * el for x, el in zip(bin(i)[2:], line[(k - len(bin(i)[2:])):])]) % 2 for line in A]
        counter[sum(Q)] += 1

    with open('res.txt', 'w') as f:
        for i, j in counter.items():
            f.write(str(i) + '\t' + str(j) + '\n')
    return counter
