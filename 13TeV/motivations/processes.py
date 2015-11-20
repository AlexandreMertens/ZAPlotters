
#!/usr/bin/env python
import numpy as np
import pylab as pl
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import collections  as mc

txt_size = 20
mh=125


xl=np.arange(90+mh,1000,1)
xu=np.arange(0,1000,1)
yl=xl-90
yu=np.maximum(xu+90,125)
yb=np.maximum(10*xu,125)

fig, ax = plt.subplots()
fig.set_figheight(8)
fig.set_figwidth(8)


plt.xticks([0, 125, 1000],['','125',''], fontsize=txt_size)
plt.yticks([0, 125, 1000],['','125',''], fontsize=txt_size)
plt.xlabel('m$_A$ [GeV/$c^2$]', fontsize=txt_size)
plt.ylabel('m$_H$ [GeV/$c^2$]', fontsize=txt_size)
plt.xlim([0,1000])
plt.ylim([0,1000])

# Filling

ax.fill_between(xl,mh,yl, facecolor='coral')
ax.fill_between(xu,yu,1000, facecolor='coral')
lb, = pl.plot(xu,yb,color='black')
lb.set_dashes([2,4])

# Text

ax.text(150,850, '$H$'+r'$\rightarrow$'+'$ZA$',size=txt_size, ha = 'left')
ax.text(850,250, '$A$'+r'$\rightarrow$'+'$ZH$',size=txt_size, ha = 'right')
ax.text(1000,1020, r'cos($\beta$-$\alpha$) $\approx$ 0, tan$\beta$ $\approx$ 1', size=txt_size, ha = 'right')

plt.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.15)

plt.savefig("processes.png")
