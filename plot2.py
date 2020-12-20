import matplotlib as mpl
import matplotlib.pyplot as plt
import math


def picture2():
    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    mpl.rcParams.update({'font.size': 10})

    text_f = open('stats.txt', 'r')

    s = 0

    for line in text_f:
        s += 1

    text_f = open('stats.txt', 'r')
    x1 = [0] * s
    y1 = [0] * s
    x = [0] * int(s / 2)
    y = [0] * int(s / 2)
    for i in range(s):
        sesc = text_f.readline().split()
        x1[i] = float(sesc[0])

        y1[i] = ((float(sesc[4])) ** 2 + (float(sesc[5])) ** 2) ** 0.5

    for i in range(s):
        if i < (s * 0.5):
            x[i] = x1[2 * i + 1]
            y[i] = y1[2 * i + 1]
    x = sorted(x)
    y = sorted(y)
    y.reverse()

    x_min = min(x)
    x_max = max(x)
    y_min = min(y)
    y_max = max(y)

    plt.axis([0.9 * x_min, 1.1 * x_max, 0.9 * y_min, 1.1 * y_max])
    # plt.axis([0, 10, 0, 20])

    plt.title('Зависимость расстояния спутника звезды до звезды от времени')
    plt.xlabel('t')
    plt.ylabel('r(t)')

    plt.plot(x, y, color='blue', linestyle='solid')
    # plt.plot(xs, cos_vals, color = 'red', linestyle = 'dashed',
    # label = 'cos(x)')

    plt.legend(loc='upper right')
    fig.savefig('task2.png')

