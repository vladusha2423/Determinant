def minor(a, im, jm):
    n = len(a)
    if n > 1:
        b = []
        for i in range(n):
            if not i == im:
                b.append([])
            for j in range(n):
                if not (i == im or j == jm):
                    b[len(b)-1].append(a[i][j])
        return b
    return a


def amount_determinant(a):
    amount = 0
    for j in range(len(a)):
        b = minor(a, 0, j)
        if len(b) > 1:
            amount += ((-1) ** j) * a[0][j] * amount_determinant(b)
        else:
            amount += ((-1) ** j) * a[0][j] * b[0][0]
    return amount
