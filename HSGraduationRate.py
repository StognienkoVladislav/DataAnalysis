import matplotlib.pyplot as plt
from numpy.matlib import rand
from pandas import DataFrame, np

from ExploratoryAnalysis import remove_border, show

if __name__ == '__main__':

    change = [23.2, 22.7, 19.7, 13.9, 13.1, 12.8, 12.7,
              12.6, 12.0, 11.5, 10.8, 10.4, 10.4, 9.8, 9.2,
              9.2, 8.8, 7.7, 6.9, 6.9, 6.4, 5.6, 5.3, 5.3, 5.2, 4.9,
              4.8, 4.6, 3.6, 3.1, 0.7, -.3, -.7, -1.2, -1.5, -1.7,
              -1.7, -1.8, -2, -2.3, -2.4, -3.6, -3.7,
              -4.9, -6.5, -6.6, -11.6, -14.8, -17.6, -23.1]
    city = ['Philadelphia', 'Tucson', 'Kansas City, MO',
            'El Paso', 'Portland, Ore.', 'New York', 'Dallas',
            'Columbus', 'Mesa', 'Austin', 'Atlanta', 'Fort Worth',
            'Miami', 'Houston', 'Chicago', 'Oakland', 'Virginia Beach',
            'Baltimore', 'Denver', 'Detroit', 'San Antonio', 'Phoenix',
            'Oklahoma City', 'Indianapolis', 'Milwaukee', 'Sacramento',
            'Washington, D.C.', 'Colorado Springs', 'Honolulu', 'Nashville',
            'Jacksonville', 'Louisville', 'Seattle',
            'Memphis', 'Fresno', 'Boston', 'Mineappolis',
            'San Jose', 'Tulsa', 'Charlotte', 'San Diego', 'Los Angeles',
            'Long Beach', 'Cleveland', 'San Francisco', 'Albuquerque',
            'Arlington, TX', 'Omaha', 'Wichita', 'Las Vegas']

    grad = DataFrame({'change': change, 'city': city})

    plt.figure(figsize=(3, 8))

    change = grad.change[grad.change > 0]
    city = grad.city[grad.change > 0]
    pos = np.arange(len(change))

    plt.title('1995-2005 Change in HS graduation rate')
    plt.barh(pos, change)

    # add the numbers to the side of each bar
    for p, c, ch in zip(pos, city, change):
        plt.annotate(str(ch), xy=(ch + 1, p + .5), va='center')

    # cutomize ticks
    ticks = plt.yticks(pos + .5, city)
    xt = plt.xticks()[0]
    plt.xticks(xt, [' '] * len(xt))

    # minimize chartjunk
    remove_border(left=False, bottom=False)
    plt.grid(axis='x', color='white', linestyle='-')

    # set plot limits
    plt.ylim(pos.max(), pos.min() - 1)
    plt.xlim(0, 30)


    df2 = DataFrame(rand(10, 4), columns=['a', 'b', 'c', 'd'])
    df2.plot(kind = 'bar')

    df2.plot(kind = 'bar', stacked = True)      #Пропорциональное распределение значений

    df2.plot(kind = 'barh', stacked = True)     #Отображ горизонтально

    show()

