import matplotlib as mpl
import matplotlib.pyplot as plt
import math


def picture3():
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
        x1[i] = ((float(sesc[4])) ** 2 + (float(sesc[5])) ** 2) ** 0.5
        y1[i] = ((float(sesc[6])) ** 2 + (float(sesc[7])) ** 2) ** 0.5

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

    plt.title('Зависимость модуля скорости от расстояния до звезды')
    plt.xlabel('r')
    plt.ylabel('V(r)')

    plt.plot(x, y, color='blue', linestyle='solid')
    # plt.plot(xs, cos_vals, color = 'red', linestyle = 'dashed',
    # label = 'cos(x)')

    plt.legend(loc='upper right')
    fig.savefig('task3.png')

