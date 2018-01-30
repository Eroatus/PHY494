import myfuncs, matplotlib.pyplot
matplotlib.pyplot.plot([-4 + 0.5*i for i in range(17)], [myfuncs.heaviside(-4 + 0.5*i) for i in range(17)], '-o', color = "red", linewidth = 2)
matplotlib.pyplot.show()
