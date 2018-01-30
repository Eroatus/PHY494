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

x1 = -3
x2 = 0
x3 = 3

theta1 = heaviside(x1)
theta2 = heaviside(x2)
theta3 = heaviside(x3)

print("Theta(" + str(x1) + ") = " + str(theta1))
print("Theta(" + str(x2) + ") = " + str(theta2))
print("Theta(" + str(x3) + ") = " + str(theta3))
