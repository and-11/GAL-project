import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
theta_distibution = np.linspace(0, 2 * np.pi, 100)

#Cercul
raza_cerc = 1                               
x_cerc = raza_cerc * np.cos(theta_distibution)
y_cerc = raza_cerc * np.sin(theta_distibution)
z_cerc = np.zeros_like(theta_distibution)

#Elipsa
a = raza_cerc  #raza mare
b = 0.5  #raza mica

x_elipsa = a * np.cos(theta_distibution)
y_elipsa = b * np.sin(theta_distibution)
z_elipsa = np.zeros_like(theta_distibution)

#P si Q fixate pe cerc
alpha = np.pi / 1.5
beta = np.random.uniform(0, 2 * np.pi) #alegem doua puncte la intamplare pe cerc

Px, Py = raza_cerc * np.cos(beta), raza_cerc * np.sin(beta)
Qx, Qy = raza_cerc * np.cos(beta + alpha), raza_cerc * np.sin(beta + alpha)

#perpendicularele din P si din Q
def ellipse_y(x_val):
    val = 1 - (x_val**2) / a**2
    if val < 0:
        return None
    return b * np.sqrt(val)

Py_int = ellipse_y(Px)
Py_proj = Py_int if Py >= 0 else -Py_int

Qy_int = ellipse_y(Qx)
Qy_proj = Qy_int if Qy >= 0 else -Qy_int


#plotting
#plot cerc
ax.plot(x_cerc, y_cerc, z_cerc)
ax.text(0, 0, 0, 'O', color='black', fontsize=10)

#plot elipsa
ax.plot(x_elipsa, y_elipsa, z_elipsa)

#plot P si Q
ax.scatter(Px, Py, 0, color='red')
ax.scatter(Qx, Qy, 0, color='red')
ax.text(Px, Py, 0, 'P', color='red', fontsize=10)
ax.text(Qx, Qy, 0, 'Q', color='red', fontsize=10)

#razele din P si Q
ax.plot([0, Px], [0, Py], [0, 0], color='purple')
ax.plot([0, Qx], [0, Qy], [0, 0], color='purple')

#perpendicularele din P si Q pe elipsa
ax.plot([Px, Px], [Py, Py_proj], [0, 0], 'g--')
ax.plot([Qx, Qx], [Qy, Qy_proj], [0, 0], 'g--')
ax.text(Px, Py_proj, 0, 'D', color='green', fontsize=10)
ax.text(Qx, Qy_proj, 0, 'E', color='green', fontsize=10)


ax.set_zlim(0, 1) 
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Figure')
ax.legend()
plt.show()
