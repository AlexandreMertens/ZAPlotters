#!/usr/bin/env python
import numpy as np
import pylab as pl
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import collections  as mc


# some values

mh = 125
m1 = 70
m2 = 200
m3 = 400
mhc = 410

col_h = 'black' 
col_A = 'red'
col_H = 'darkred'
col_Hc = 'coral'

txt_size = 20
txt_offset = 5

plt.figure()
#plt.plot(x,y)

lines_h = [[(0.2, mh), (0.8, mh)],[(1.2, mh), (1.8, mh)],[(2.2, mh), (2.8, mh)]]
lines_A = [[(0.2, m3), (0.8, m3)],[(1.2, m2), (1.8, m2)],[(2.2, m1), (2.8, m1)]]
lines_H = [[(0.2, m2), (0.8, m2)],[(1.2, m3), (1.8, m3)],[(2.2, m3), (2.8, m3)]]
lines_Hc= [[(0.2, mhc), (0.8, mhc)],[(1.2, mhc), (1.8, mhc)],[(2.2, mhc), (2.8, mhc)]]

cols_h = np.array([col_h,col_h,col_h])
cols_A = np.array([col_A,col_A,col_A])
cols_H = np.array([col_H,col_H,col_H])
cols_Hc = np.array([col_Hc,col_Hc,col_Hc])

lc_h = mc.LineCollection(lines_h, colors=cols_h, linewidths=2)
lc_A = mc.LineCollection(lines_A, colors=cols_A, linewidths=2)
lc_H = mc.LineCollection(lines_H, colors=cols_H, linewidths=2)
lc_Hc = mc.LineCollection(lines_Hc, colors=cols_Hc, linewidths=5)

fig, ax = pl.subplots()
fig.set_figheight(8)
fig.set_figwidth(8)

ax.add_collection(lc_h)
ax.add_collection(lc_A)
ax.add_collection(lc_H)
ax.add_collection(lc_Hc)

ax.text(0.5,mh+txt_offset, '$h$',size=txt_size, ha = 'center')
ax.text(1.5,mh+txt_offset, '$h$',size=txt_size, ha = 'center')
ax.text(2.5,mh+txt_offset, '$h$',size=txt_size, ha = 'center')

ax.text(0.5,mhc+txt_offset, '$A,H^\pm$',size=txt_size, ha = 'center')
ax.text(1.5,mhc+txt_offset, '$H,H^\pm$',size=txt_size, ha = 'center')
ax.text(2.5,mhc+txt_offset, '$H,H^\pm$',size=txt_size, ha = 'center')

ax.text(0.5,m2+txt_offset, '$H$',size=txt_size, ha = 'center')
ax.text(1.5,m2+txt_offset, '$A$',size=txt_size, ha = 'center')
ax.text(2.5,m1+txt_offset, '$A$',size=txt_size, ha = 'center')


#plt.xticks([0.5, 1.5, 2.5, 3], ['A'+r'$\rightarrow$'+'ZH', 'H'+r'$\rightarrow$'+'ZA', 'H'+r'$\rightarrow$'+'ZA', ''], fontsize=txt_size)
plt.xticks([0.5, 1.5, 2.5, 3], ['MSSM-like', 'im2HDM', 'im2HDM', ''], fontsize=txt_size)
plt.yticks([0,125,500], fontsize=txt_size)
plt.ylabel('m [GeV/$c^2$]', fontsize=txt_size)

#show()
plt.savefig("hierarchies.png")
