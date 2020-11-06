def fibonacci_par(num):
    seq = [1, 2]
    par = []
    soma = ()

    par.clear()
    for i in range(num):
        seq.append(seq[len(seq) - 1] + seq[len(seq) - 2])
        if seq[i] % 2 == 0:
            par.append(seq[i])
            soma = sum(par)

    return soma


if __name__ == '__main__':
    print(fibo(4500))
