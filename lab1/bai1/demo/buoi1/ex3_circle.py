import numpy as np
print("Circle Basic")
r = float(input("Moi ban nhap ban kinh r: "))
cv = np.pi * 2 * r
dt = np.pi * r **2
print("Chu vi hinh tron la: %f" % cv)
print("Dien tich hinh tron la: %f" % dt)