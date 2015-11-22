import math
from ROOT import *


C=TCanvas("C5","C5",1000,900)

C.Update()
C.Modified()
'''
gPad.SetRightMargin(0.2)
gPad.SetLeftMargin(0.2)
gPad.SetBottomMargin(0.2)
'''

MassPoints = TGraph(21)

MassPoints.SetPoint(0,50,200)
MassPoints.SetPoint(1,100,200)

MassPoints.SetPoint(2,50,250)
MassPoints.SetPoint(3,100,250)

MassPoints.SetPoint(4,50,300)
MassPoints.SetPoint(5,100,300)
MassPoints.SetPoint(6,200,300)

MassPoints.SetPoint(7,50,500)
MassPoints.SetPoint(8,100,500)
MassPoints.SetPoint(9,200,500)
MassPoints.SetPoint(10,300,500)
MassPoints.SetPoint(11,400,500)

MassPoints.SetPoint(12,50,650)

MassPoints.SetPoint(13,50,800)
MassPoints.SetPoint(14,100,800)
MassPoints.SetPoint(15,200,800)
MassPoints.SetPoint(16,400,800)
MassPoints.SetPoint(17,700,800)

MassPoints.SetPoint(18,50,1000)
MassPoints.SetPoint(19,200,1000)
MassPoints.SetPoint(20,500,1000)

MassPoints.SetMarkerStyle(21)
MassPoints.GetXaxis().SetLimits(0,1100)
MassPoints.SetMinimum(0)
MassPoints.SetMaximum(1100)

MassPoints.Draw("AP")

LineBoostedRegion = TLine(0,0,110,1100)
LineKin = TLine(0,90,1010,1100)
LineBoostedRegion.SetLineColor(kRed)
LineBoostedRegion.SetLineWidth(3)
LineBoostedRegion.SetLineStyle(2)
LineBoostedRegion.Draw()
LineKin.SetLineWidth(3)
LineKin.SetLineStyle(2)
LineKin.Draw("same")


gPad.Update()
gPad.Modified()


