import matplotlib.pyplot as plt
from pandas import date_range, Series, DataFrame, read_csv, qcut
from pandas.tools import plotting
from numpy.random import rand, randn
from pylab import *
import brewer2mpl
from matplotlib import rcParams

#colorbrewer2 Dark2 qualitative color table
dark2_colors = brewer2mpl.get_map('Dark2', 'Qualitative', 7).mpl_colors

rcParams['figure.figsize'] = (10, 6)
rcParams['figure.dpi'] = 150
rcParams['axes.color_cycle'] = dark2_colors
rcParams['lines.linewidth'] = 2
rcParams['axes.facecolor'] = 'white'
rcParams['font.size'] = 14
rcParams['patch.edgecolor'] = 'white'
rcParams['patch.facecolor'] = dark2_colors[0]
rcParams['font.family'] = 'StixGeneral'

def remove_border(axes = None, top = False, right = False, left = True, bottom = True):

    ax = axes or plt.gca()
    ax.spines['top'].set_visible(top)
    ax.spines['right'].set_visible(right)
    ax.spines['left'].set_visible(left)
    ax.spines['bottom'].set_visible(bottom)

    #turn off all ticks
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticks_position('none')

    #now re-enable visibles
    if top:
        ax.xaxis.tick_top()

    if bottom:
        ax.xaxis.tick_bottom()

    if left:
        ax.yaxis.tick_left()

    if right:
        ax.yaxis.tick_right()

if __name__ == '__main__':

    x = linspace(0, 5, 10)
    y = x ** 2
    figure()
    plot(x, y, 'r')
    xlabel('x')
    ylabel('y')
    title('title')


    ##########################################################

    fig, ax = plt.subplots()

    ax.plot(x, x**2, label = r"$y = \alpha^2$")
    ax.plot(x, x**3, label = r"$y = \alpha^3$")
    ax.set_xlabel(r'$\alpha$', fontsize = 18)
    ax.set_ylabel(r'$y$', fontsize = 18)
    ax.set_title('title')
    ax.legend(loc = 2)  #upper left corner

    ##########################################################

    fig, axes = plt.subplots(nrows = 1, ncols = 2)

    for ax in axes:
        ax.plot(x, y, 'r')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('title')

    fig.tight_layout()
    show()
    ##########################################################
    #Метод .plot() Для Series и DataFrame обьектов , это всего лишь
    #обёртка для plt.plot:

    ts = Series(randn(1000), index = date_range('1/1/2000', periods = 1000))
    ts = ts.cumsum()
    ts.plot()

    df = DataFrame(randn(1000, 4), index = ts.index, columns = list('ABCD'))
    df = df.cumsum()

    plt.figure()
    df.plot()
    plt.legend(loc = 'best')

    show()

    ##########################################################
    #Для того, чтобы перейти на логарифмическую шкалу надо задать параметр Logy.
    #df.plot(logy = True)


    plt.figure()
    df.ix[5].plot(kind = 'bar')
    plt.axhline(0, color = 'k')
    show()

    ##########################################################
    #Gistogram
    plt.figure()
    df['A'].diff().hist()

    plt.figure()
    df['A'].diff().hist(bins = 50)

    plt.figure()
    df.diff().hist(color = 'k', alpha = 0.5, bins = 50)

    show()

    ##########################################################
    #Box-plot

    df = DataFrame(rand(10, 2), columns = ['Col1', 'Col2'])
    df['X'] = Series(['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'])
    plt.figure()
    bp = df.boxplot(by = 'X')
    show()

