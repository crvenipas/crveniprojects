for i in reversed(range(1,100)):
    vj = 'Вжжжж'
    ps = 'Пшшшш'
    if i % 3 == 0 and i % 5 == 0:
        print(ps, vj, sep = '')
    elif i%3 == 0:
        print(vj)
    elif i%5 == 0:
        print(ps)
    else:
        print(i)

for j in reversed(range(1,100)):
    x = ''
    if j % 3 == 0:
        x += 'Вжжжж'
    if j % 5 == 0:
        x += 'Пшшшш'
    if j % 3 != 0 and j % 5 != 0:
        x += str(j)
    print(x)