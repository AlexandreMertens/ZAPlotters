
#!/usr/bin/env python
import numpy as np
import pylab as pl
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import collections  as mc

txt_size = 20
mh=125


xl=np.arange(90+mh,1100,1)
xu=np.arange(0,1100,1)
yl=xl-90
yu=np.maximum(xu+90,125)
yb=np.maximum(10*xu,125)

fig, ax = plt.subplots()
fig.set_figheight(8)
fig.set_figwidth(8)


plt.xticks([0, 125, 1100],['','125',''], fontsize=txt_size)
plt.yticks([0, 125, 1100],['','125',''], fontsize=txt_size)
plt.xlabel('m$_A$ [GeV/$c^2$]', fontsize=txt_size)
plt.ylabel('m$_H$ [GeV/$c^2$]', fontsize=txt_size)
plt.xlim([0,1100])
plt.ylim([0,1100])

# Filling

ax.fill_between(xl,mh,yl, facecolor='coral')
ax.fill_between(xu,yu,1100, facecolor='coral')
lb, = pl.plot(xu,yb,color='black')
lb.set_dashes([2,4])

# mass points

mA=[50 ,100,50 ,100,50 ,100,200,50 ,100,200,300,400,50 ,50 ,100,200 ,400 ,700,50 ,200,500]
mH=[200,200,250,250,300,300,300,500,500,500,500,500,650,800,800,800,800,800,1000,1000,1000]

plt.plot(mA,mH,color='black', marker='o', linestyle = 'None')

# Text

ax.text(150,900, '$H$'+r'$\rightarrow$'+'$ZA$',size=txt_size, ha = 'left')
ax.text(900,250, '$A$'+r'$\rightarrow$'+'$ZH$',size=txt_size, ha = 'right')
ax.text(1100,1120, r'cos($\beta$-$\alpha$) $\approx$ 0, tan$\beta$ $\approx$ 1', size=txt_size, ha = 'right')

plt.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.15)

plt.savefig("signal_masses.png")
