# Plot Heaviside Step Function

import matplotlib.pyplot as plt

# Heasiside Step Function
def heaviside(x):
    """Heaviside Step Function"""

    theta = None
    if x < 0:
        theta = 0.
    elif x == 0:
        theta = 0.5
    else:
        theta = 1.

    return theta

def interval_list(start, stop, step):
    """Create list of values from start to stop in increments defined by step"""

    interval = []
    value = start

    interval.append(value)

    done = False
    while not done:
        value += step
        interval.append(value)

        if(value == stop):
            done = True

    return interval

x = interval_list(-4.0, 4.0, 0.5)
y = []

for i in range(len(x)):
    y.append(heaviside(x[i]))

print("x\t Theta(x)")
print("-------------")

for i in range(len(x)):
    print(x[i], "\t", y[i])

plt.plot(x, y, '-o', color = "red", linewidth = 2)
plt.show()
