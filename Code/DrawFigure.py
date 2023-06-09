import matplotlib.pyplot as plt
import os
import numpy as np


def GetData(cnt_list_path, number_path):
    with open(cnt_list_path, 'r') as f:
        cnt_list = [int(line.strip()) for line in f]
    with open(number_path, 'r') as f:
        number = [int(line.strip()) for line in f]
    return cnt_list, number


P_name = ['192', '224', '256', '384', '521', '1279', '2203']

P_value = ['P_192 = 2 ** 192 - 2 ** 64 - 1',
           'P_224 = 2 ** 224 - 2 ** 96 + 1',
           'P_256 = 2 ** 256 - 2 ** 224 - 2 ** 96 + 2 ** 64 - 1',
           'P_384 = 2 ** 384 - 2 ** 128 - 2 ** 96 + 2 ** 32 - 1',
           'P_521 = 2 ** 521 - 1',
           'P_1279 = 2 ** 1279 - 1',
           'P_2203 = 2 ** 2203 - 1']

color_list = ['purple', 'green', '#FF69B4', '#B8860B', '#A0522D', '#1E90FF', '#FF6347']

symbol = ['s', '^', 'v', 'p', 'x', 'o', '<']

boundary = []
bias = 10

line_list = []

if __name__ == "__main__":
    cwd = os.getcwd()
    copy_output_path = os.path.join(cwd, '..', 'Copy_Output')

    f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True, facecolor='w')
    plt.subplots_adjust(wspace=0.05)

    for idx in range(len(P_name)):
        cnt_list_path = os.path.join(copy_output_path, 'P_' + P_name[idx] + '_cnt_list.txt')
        number_path = os.path.join(copy_output_path, 'P_' + P_name[idx] + '_number.txt')
        cnt_list, number = GetData(cnt_list_path, number_path)

        sort_idx = np.argsort(cnt_list)
        cnt_list = np.array(cnt_list)[sort_idx]
        number = np.array(number)[sort_idx]

        for i in range(len(number)):
            if number[i] > 10:
                number[i] = number[i] * 10

        if idx <= 4:
            line, = ax1.plot(cnt_list, number, symbol[idx] + '-', color=color_list[idx], markersize=6)
            if idx == 0:
                boundary.append(min(cnt_list))
            if idx == 4:
                boundary.append(max(cnt_list))
        elif idx == 5:
            line, = ax2.plot(cnt_list, number, symbol[idx] + '-', color=color_list[idx])
            boundary.append(min(cnt_list))
            boundary.append(max(cnt_list))
        else:
            line, = ax3.plot(cnt_list, number, symbol[idx] + '-', color=color_list[idx])
            boundary.append(min(cnt_list))
            boundary.append(max(cnt_list))
        line_list.append(line)

    ax1.set_xlim(boundary[0] - bias, boundary[1] + bias)
    ax2.set_xlim(boundary[2] - bias, boundary[3] + bias)
    ax3.set_xlim(boundary[4] - bias, boundary[5] + bias)

    ax1.spines['right'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax3.spines['left'].set_visible(False)
    ax1.yaxis.tick_left()
    ax2.yaxis.set_visible(False)
    ax3.yaxis.set_visible(False)

    d = .015
    kwargs = dict(transform=ax1.transAxes, color='k', clip_on=False)
    ax1.plot((1 - d, 1 + d), (-d, +d), **kwargs)
    ax1.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)

    kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
    ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)
    ax2.plot((-d, +d), (-d, +d), **kwargs)
    ax2.plot((1 - d, 1 + d), (-d, +d), **kwargs)
    ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)

    kwargs.update(transform=ax3.transAxes)  # switch to the bottom axes
    ax3.plot((-d, +d), (1 - d, 1 + d), **kwargs)
    ax3.plot((-d, +d), (-d, +d), **kwargs)

    line_label = []
    for idx, each_name in enumerate(P_name):
        line_label.append(P_value[idx])

    plt.legend(bbox_to_anchor=(1, 0.99), handles=line_list, labels=line_label, fontsize=20)

    # ax2.set_title("The Distribution of Iteration Rounds with Different Primes", fontsize=30, y=1.02)
    ax2.set_xlabel("Iteration Rounds", fontsize=30)
    ax1.set_ylabel("Sample Numbers", fontsize=30)

    ax1.grid(axis='x', alpha=0.4)
    ax2.grid(axis='x', alpha=0.4)
    ax3.grid(axis='x', alpha=0.4)

    ax1.set_yticks(range(0, 610000, 50000))

    plt.show()
