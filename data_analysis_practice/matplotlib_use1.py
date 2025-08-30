import math
import matplotlib.pyplot as plt
import numpy as np

# 1 第一个绘图程序
def test1():
    x = np.arange(0, math.pi*2, 0.05)
    # print(x)
    y = np.sin(x)
    plt.plot(x, y)
    plt.xlabel("angle")
    plt.ylabel("sine")
    plt.title('sine wave')
    plt.show()

# 2 Matplotlib figure图形对象
def test2():
    x = np.arange(0, math.pi*2, 0.05)
    y = np.sin(x)
    fig = plt.figure()
    #add_axes() 的参数值是一个序列，序列中的 4 个数字分别对应图形的左侧y轴，底部x轴，宽度，和高度，且每个数字必须介于 0 到 1 之间。
    ax = fig.add_axes([0.15,0.1,0.8,0.8])
    ax.plot(x,y)
    ax.set_title("sine wave")
    ax.set_xlabel('angle')
    ax.set_ylabel('sine')

    y1 = np.cos(x)
    fig1 = plt.figure()
    ax1 = fig1.add_axes([0.2,0.1,0.5,0.8])
    ax1.plot(x,y1)
    ax1.set_title("cosine wave")
    ax1.set_xlabel('angle')
    ax1.set_ylabel('cosine')
    plt.show()

# 3 axes类使用详解
def test3():
    """
    Matplotlib 定义了一个 axes 类（轴域类），该类的对象被称为 axes 对象（即轴域对象），
    它指定了一个有数值范围限制的绘图区域。在一个给定的画布（figure）中可以包含多个 axes 对象，
    但是同一个 axes 对象只能在一个画布中使用。
    """
    y = [1, 4, 9, 16, 25, 36, 49, 64]
    x1 = [1, 16, 30, 42, 55, 68, 77, 88]
    x2 = [1, 6, 12, 18, 28, 40, 52, 65]
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    # 使用简写的形式color/标记符/线型
    # 1 axes.plot()：将一个数组的值与另一个数组的值绘制成线或标记，plot()方法具有可选格式的字符串参数
    # 用来指定线型、标记颜色、样式以及大小
    l1 = ax.plot(x1, y, 'ys-')
    l2 = ax.plot(x2, y, 'go--')
    # 2 legend():绘制图例。labels用来指定标签的名称；loc指定图例位置的参数
    ax.legend(labels=('tv', 'Smartphone'), loc='lower right')  # legend placed at lower right
    ax.set_title("Advertisement effect on sales")
    ax.set_xlabel('medium')
    ax.set_ylabel('sales')
    plt.show()

# 4 subplot()
def test4():
    # # 隐式映射：当只传入一个列表时，matplotlib自动将这个列表当作y值，x轴使用默认的[0,1,2,...,len(y)-1]
    # # 现在创建一个子图，它表示一个有2行1列的网格的顶部图。
    # # 因为这个子图将与第一个重叠，所以之前创建的图将被删除
    # plt.subplot(1, 1, 1)
    # plt.plot([0, 1, 2])
    # plt.xlabel("x")
    # plt.ylabel("y")
    # plt.title('y=x')
    # # 创建带有黄色背景的第二个子图
    # plt.subplot(221, facecolor='y')
    # plt.plot([2, 1, 0])
    # plt.xlabel("x")
    # plt.ylabel("y")
    # plt.title('y=-x+2')
    #
    # plt.show()

    # fig = plt.figure()
    # ax1 = fig.add_subplot(111)
    # ax1.plot([1, 2, 3])
    # ax2 = fig.add_subplot(221, facecolor='y')
    # ax2.plot([1, 2, 3])
    # fig.show()

    fig, axs = plt.subplots(2, 2)  # 返回 2x2 的子图数组
    axs[0, 0].plot([1, 2, 3])
    axs[0, 0].set_title("Top Left")
    axs[1, 1].plot([3, 2, 1])
    axs[1, 1].set_title("Bottom Right")
    plt.tight_layout()
    plt.show()

# 5 设置网格格式
def test5():
    # fig画布；axes子图区域
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    x = np.arange(1, 11)
    axes[0].plot(x, x ** 3, 'g', lw=2)
    # 开启网格
    axes[0].grid(True)
    axes[0].set_title('default grid')
    axes[1].plot(x, np.exp(x), 'r')
    # 设置网格的颜色，线型，线宽
    axes[1].grid(color='b', ls='-.', lw=0.25)
    axes[1].set_title('custom grid')
    axes[2].plot(x, x)
    axes[2].set_title('no grid')
    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    test5()