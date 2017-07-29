import numpy
import pylab
from matplotlib.colors import LinearSegmentedColormap
from mpl_toolkits.mplot3d import Axes3D


#X, Y = numpy.meshgrid([1, 2, 3], [4, 5, 6, 7])

def makeData():
    #Строим сетку в интервале от -10 до 10 с шагом 0.1 по обоим координатам
    x = numpy.arange(-10, 10, 0.1)
    y = numpy.arange(-10, 10, 0.1)

    #Создаем двумерную матрицу-сетку
    xgrid, ygrid = numpy.meshgrid(x, y)

    #В узлах рассчитываем значение функции
    zgrid = numpy.sin(xgrid) * numpy.sin(ygrid) / (xgrid * ygrid)

    return xgrid, ygrid, zgrid


x, y, z = makeData()

fig = pylab.figure()
axes = Axes3D(fig)

axes.plot_surface(x, y, z, rstride = 3, cstride = 3, cmap = LinearSegmentedColormap.from_list
                                                            ("red_blue", ['b', 'w', 'r',], 256))
axes.plot_surface(x, y, z, rstride = 4, cstride = 5, cmap = pylab.cm.jet)

pylab.show()