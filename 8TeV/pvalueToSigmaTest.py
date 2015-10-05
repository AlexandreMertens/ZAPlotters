from ROOT import TMath as tmath
from ROOT import *


#pvalue=1-0.682689492137086

pvalue = 0.003

sigma = tmath.sqrt(2)*tmath.ErfInverse(1-2*pvalue)

print sigma
