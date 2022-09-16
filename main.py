def haffman_algorithm(x):
    m = [[x.count(i), i] for i in sorted(set(x), key=lambda i: x.count(i))]
    while len(m) > 2:
        m.sort()
        al_new = [[m[0][0] + m[1][0], [m[0], m[1]]]] + m[2:]
        m = al_new
    return m


def code_tab(a, c, d):
    if isinstance(a[0][1], str):
        d[a[0][1]] = c + '0'
    else:
        d = code_tab(a[0][1], c + '0', d)
    if isinstance(a[1][1], str):
        d[a[1][1]] = c + '1'
    else:
        d = code_tab(a[1][1], c + '1', d)
    return d

def encode(mes, d):
    return ' '.join(d[x] for x in mes)

mes = input()
m = haffman_algorithm(list(mes))
d = code_tab(m, '', {})
print(encode(mes, d))
