import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
T = np.arange(0.0, 1.0, 0.0001)
t = np.append(-T,T)
t.sort()
p = 2
delta_f = 0.01
S = (1 - T**p)**(1/p)
s = np.copy(S)
S.sort()
s = np.append(S,s)
print(s)
l_1, = plt.plot(t, s, lw=2, color='red')
l_2, = plt.plot(t, -s, lw=2, color='red')

plt.axis([-1, 1, -1, 1])

axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)

sfreq = Slider(axfreq, 'Freq', 0.1, 4, valinit=p, valstep=delta_f)



def update(val):
    p_ch = sfreq.val
    X = (1 - T**p_ch)**(1/p_ch)
    x = np.copy(X)
    X.sort()
    x = np.append(X,x)
    print(x)
    l_1.set_ydata(x)
    l_2.set_ydata(-x)
    fig.canvas.draw_idle()
sfreq.on_changed(update)


resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    sfreq.reset()
button.on_clicked(reset)

rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)


def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw_idle()
radio.on_clicked(colorfunc)

plt.show()