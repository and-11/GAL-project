import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
theta_distibution = np.linspace(0, 2 * np.pi, 100)

def ellipse_y(x_val): 
    #ecuatia elipsei: x^2/a^2 + y^2/b^2 - 1 = 0
    val = 1 - (x_val**2) / a**2
    if val < 0:
        return None
    return b * np.sqrt(val)


raza_cerc = 1 #raza cerc
a = 1  #raza mare elipsa
b = 0.5  #raza mica elipsa
h = 1 #inaltime

#Cercul                            
x_cerc = raza_cerc * np.cos(theta_distibution)
y_cerc = raza_cerc * np.sin(theta_distibution)
z_cerc = np.zeros_like(theta_distibution)
ax.plot(x_cerc, y_cerc, z_cerc) #plot
ax.text(0, 0, 0, 'O', color='black', fontsize=10)

#Elipsa
x_elipsa = a * np.cos(theta_distibution)
y_elipsa = b * np.sin(theta_distibution)
z_elipsa = np.zeros_like(theta_distibution)
ax.plot(x_elipsa, y_elipsa, z_elipsa) #plot

beta = np.random.uniform(0, 2 * np.pi) #alegem doua puncte la intamplare pe cerc
alpha = 2*np.pi / 3

eh_lines = []
op_line = [None]
oq_line = [None]
dh_line = [None]

def update(frame):
    gamma = frame
    Px, Py = raza_cerc * np.cos(beta + gamma), raza_cerc * np.sin(beta+gamma)
    Qx, Qy = raza_cerc * np.cos(beta + alpha + gamma), raza_cerc * np.sin(beta + alpha + gamma)

    #perpendicularele din P si din Q
    Py_int = ellipse_y(Px)
    Py_proj = Py_int if Py >= 0 else -Py_int
    Qy_int = ellipse_y(Qx)
    Qy_proj = Qy_int if Qy >= 0 else -Qy_int

    Dx, Dy = Px, Py_proj
    Ex, Ey = Qx, Qy_proj

    #perpendiculara din D pe plan cu inaltimea h
    Hx, Hy, Hz = Dx, Dy, h

    line, = ax.plot([Ex, Hx], [Ey, Hy], [0, Hz], color='green', alpha=0.7)

    if op_line[0] is not None:
        op_line[0].remove()
    op_line[0], = ax.plot([0, Px], [0, Py], [0, 0], color='purple')

    if oq_line[0] is not None:
        oq_line[0].remove()
    oq_line[0], = ax.plot([0, Qx], [0, Qy], [0, 0], color='purple')

    if dh_line[0] is not None:
        dh_line[0].remove()
    dh_line[0], = ax.plot([Dx, Dx], [Dy, Dy], [0, Hz], color='purple')

    eh_lines.append(line)
    return [eh_lines, op_line[0], oq_line[0], dh_line[0]]

frames = np.linspace(0, 2 * np.pi, 120)
frames = np.concatenate([frames, frames]) 
ani = FuncAnimation(fig, update, frames=frames, interval=50)

ax.set_zlim(0, 1) 
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Generarea unui hiperboloid cu o panza')

#plt.show() #show on plot
ani.save("animation.gif", writer='pillow', fps=20) #save as gif
