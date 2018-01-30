# Temperature Conversion

temp_Fahrenheit = [60.1, 78.3, 98.8, 97.1, 101.3, 110.0]
temp_Kelvin = []

for theta in temp_Fahrenheit:
    T = (theta - 32) * (5/9) + 273.15
    temp_Kelvin.append(T)

# Show T in F and K side by side
for i in range(len(temp_Fahrenheit)):
    if(i == 0):
        print("Temp(F)  Temp(K)")
        print("----------------")

    print(temp_Fahrenheit[i], "\t", \
          "%.2f" % temp_Kelvin[i])
