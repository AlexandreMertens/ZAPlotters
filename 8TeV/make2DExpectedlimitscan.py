###############
### imports ###
###############

import math
import os
import numpy
from ROOT import *
from array import array
#ROOT.gSystem.Load('CMS_label_C')
#ROOT.gSystem.Load("DrawCanvas_C")

#setTDRStyle()

###################
### Definitions ###
###################

numDirs=36
numFiles=36

lumi=19.7

massResol=0.15
bin_width = 1.5
step_fraction = 2.0/3.0

runblind = 0
signal1 = 1


#DataCards_path = "/home/fynu/amertens/storage/THDM/DataCards/Combined/"

if runblind == 0 and signal1 == 1:
  DataCards_path = "/nfs/user/acaudron/unblindedDatacards2HDM/Combined/"
elif runblind == 0 and signal1 == 0:
  DataCards_path = "/nfs/user/acaudron/unblindedDatacards2HDMyieldsSignal/Combined/"
elif runblind == 1 and signal1 == 1:
  DataCards_path = "/nfs/user/acaudron/datacards2HDM/Combined/"
elif runblind == 1 and signal1 == 0:
  DataCards_path = "/nfs/user/acaudron/datacards2HDMyieldsSignal/Combined/"

run_combine = 0
plot_ratio = 1
plot_obs = 1
plot_c1 = 0 # limit Delphes Only
plot_c12 = 0 # limit hybrid
plot_c13 = 0 #limit CMSSW Only
plot_c14 = 0 #limit hybrid lower triangle
plot_c2 = 0 # Limit On Nev when sig=1 on mu when sigYields
plot_c3 = 0 # Limit On Nev when sig=1 on mu when sigYields
plot_c4 = 1 # AccxEff
plot_c42 = 1 #AccxEff
plot_c5 = 0 # cmssw points
plot_c6 = 1 # signal strenght
plot_syst = 0  # syst Error
######################
### Plotting style ###
######################

xtitlesize=0.04 
ytitlesize=0.04 
ztitlesize=0.04 
 
xtitleoffset=1.1 
ytitleoffset=1.45 
ztitleoffset=1
 
rightmargin=0.1258389 
leftmargin=0.1191275
bottommargin=0.1206294

xmax=1200
ymax=1200


#####################
### CMSSW/Delphes ###
#####################

myTGraph_ratio = TGraph2D(10) 
myTGraph_ratio.SetName("Ratio CMSSW/Delphes") 
h_ratio = TH2D("h_ratio","#epsilon_{CMSSW} / #epsilon_{Delphes}",500,0,xmax,500,0,ymax) 
myTGraph_ratio.SetHistogram(h_ratio)

myTGraph_ratio.SetPoint(0,35,142,0.411)
myTGraph_ratio.SetPoint(1,10,200,0.838)
myTGraph_ratio.SetPoint(2,190,200,0.796)
myTGraph_ratio.SetPoint(3,30,329,0.826) 
myTGraph_ratio.SetPoint(4,70,329,0.897) 
myTGraph_ratio.SetPoint(5,70,575,0.955) 
myTGraph_ratio.SetPoint(6,70,875,0.907) 
myTGraph_ratio.SetPoint(7,142,329,0.925) 
#myTGraph_ratio.SetPoint(5,142,575,) 
myTGraph_ratio.SetPoint(8,142,875,0.927) 
myTGraph_ratio.SetPoint(9,378,575,0.891)
myTGraph_ratio.SetPoint(10,378,875,0.911) 
myTGraph_ratio.SetPoint(11,575,875,0.890) 
myTGraph_ratio.SetPoint(12,761,875,0.849)  
myTGraph_ratio.SetPoint(13,50,1200,0.92)
myTGraph_ratio.SetPoint(14,1200,1200,0.85)


myTGraph_errratio = TGraph2D(10)
myTGraph_errratio.SetName("Ratio CMSSW/Delphes")
h_errratio = TH2D("errh_ratio","err Ratio",500,0,xmax,500,0,ymax)
myTGraph_errratio.SetHistogram(h_errratio)

myTGraph_errratio.SetPoint(0,35,142,0.52)
myTGraph_errratio.SetPoint(1,50,200,0.046)
myTGraph_errratio.SetPoint(2,200,200,0.033)
myTGraph_errratio.SetPoint(3,30,329,0.101)
myTGraph_errratio.SetPoint(4,70,329,0.020)
myTGraph_errratio.SetPoint(5,70,575,0.019)
myTGraph_errratio.SetPoint(6,70,875,0.039)
myTGraph_errratio.SetPoint(7,142,329,0.018)
#myTGraph_errratio.SetPoint(8,142,575,0.025) 
myTGraph_errratio.SetPoint(9,142,875,0.016)
myTGraph_errratio.SetPoint(10,378,575,0.016)
myTGraph_errratio.SetPoint(11,378,875,0.015)
myTGraph_errratio.SetPoint(12,575,875,0.016)
myTGraph_errratio.SetPoint(13,761,875,0.021)
myTGraph_errratio.SetPoint(14,50,1200,0.10)
myTGraph_errratio.SetPoint(8,1200,1200,0.10)


myTGraph_CMSSWEff = TGraph2D(10)
myTGraph_CMSSWEff.SetName("Efficiency CMSSW Only")
h_effcmssw = TH2D("eff_cmssw","Efficiency x Acceptance (CMSSW only)",500,0,xmax,500,0,ymax)
myTGraph_CMSSWEff.SetHistogram(h_effcmssw)

myTGraph_CMSSWEff.SetPoint(0,35,142,0.00013)
myTGraph_CMSSWEff.SetPoint(1,50,200,0.015)
myTGraph_CMSSWEff.SetPoint(2,90,200,0.029)
myTGraph_CMSSWEff.SetPoint(3,30,329,0.0031)
myTGraph_CMSSWEff.SetPoint(4,70,329,0.076)
myTGraph_CMSSWEff.SetPoint(5,70,575,0.085)
myTGraph_CMSSWEff.SetPoint(6,70,875,0.020)
myTGraph_CMSSWEff.SetPoint(7,142,329,0.095)
#myTGraph_CMSSWEff.SetPoint(8,142,575,0.056)
myTGraph_CMSSWEff.SetPoint(9,142,875,0.116)
myTGraph_CMSSWEff.SetPoint(10,378,575,0.122)
myTGraph_CMSSWEff.SetPoint(11,378,875,0.13)
myTGraph_CMSSWEff.SetPoint(12,575,875,0.117)
myTGraph_CMSSWEff.SetPoint(8,761,875,0.067)

if plot_ratio: 
   
  C_ratio=TCanvas("C_ratio","C_ratio",1000,900) 
  ROOT.gStyle.SetPalette(1) 
  ROOT.gStyle.SetOptStat(0) 
   
  gPad.SetRightMargin(rightmargin) 
  gPad.SetLeftMargin(leftmargin) 
  gPad.SetBottomMargin(bottommargin) 
  myTGraph_ratio.GetHistogram().Draw("colz") 

  myTGraph_ratio.GetHistogram().GetXaxis().SetTitle("M_{A} (GeV)") 
  myTGraph_ratio.GetHistogram().GetXaxis().SetTitleSize(xtitlesize) 
  myTGraph_ratio.GetHistogram().GetXaxis().SetTitleOffset(xtitleoffset) 
  myTGraph_ratio.GetHistogram().GetYaxis().SetTitle("M_{H} (GeV)") 
  myTGraph_ratio.GetHistogram().GetYaxis().SetTitleSize(ytitlesize) 
  myTGraph_ratio.GetHistogram().GetYaxis().SetTitleOffset(ytitleoffset) 
 
  gPad.Modified() 
  gPad.Update() 

  C_ratioErr=TCanvas("C_ratioErr","C_ratioErr",1000,900)
  ROOT.gStyle.SetPalette(1)
  ROOT.gStyle.SetOptStat(0)

  gPad.SetRightMargin(rightmargin)
  gPad.SetLeftMargin(leftmargin)
  gPad.SetBottomMargin(bottommargin)
  myTGraph_errratio.GetHistogram().Draw("colz")

  myTGraph_errratio.GetHistogram().GetXaxis().SetTitle("M_{A} (GeV)")
  myTGraph_errratio.GetHistogram().GetXaxis().SetTitleSize(xtitlesize)
  myTGraph_errratio.GetHistogram().GetXaxis().SetTitleOffset(xtitleoffset)
  myTGraph_errratio.GetHistogram().GetYaxis().SetTitle("M_{H} (GeV)")
  myTGraph_errratio.GetHistogram().GetYaxis().SetTitleSize(ytitlesize)
  myTGraph_errratio.GetHistogram().GetYaxis().SetTitleOffset(ytitleoffset)

  #CMS_lumi(C_ratioErr, 2, 0 );

  gPad.Modified()
  gPad.Update()


  C_CMSSWEff=TCanvas("C_CMSSWEff","C_CMSSWEff",1000,900)
  ROOT.gStyle.SetPalette(1)
  ROOT.gStyle.SetOptStat(0)
  gPad.SetLogz()
  gPad.SetRightMargin(rightmargin)
  gPad.SetLeftMargin(leftmargin)
  gPad.SetBottomMargin(bottommargin)
  myTGraph_CMSSWEff.GetHistogram().Draw("colz")

  myTGraph_CMSSWEff.GetHistogram().GetXaxis().SetTitle("M_{A} (GeV)")
  myTGraph_CMSSWEff.GetHistogram().GetXaxis().SetTitleSize(xtitlesize)
  myTGraph_CMSSWEff.GetHistogram().GetXaxis().SetTitleOffset(xtitleoffset)
  myTGraph_CMSSWEff.GetHistogram().GetYaxis().SetTitle("M_{H} (GeV)")
  myTGraph_CMSSWEff.GetHistogram().GetYaxis().SetTitleSize(ytitlesize)
  myTGraph_CMSSWEff.GetHistogram().GetYaxis().SetTitleOffset(ytitleoffset)

  gPad.Modified()
  gPad.Update()

  myTGraph_CMSSWEff.GetHistogram().SetMinimum(0.0001)
  myTGraph_CMSSWEff.GetHistogram().SetMaximum(0.3)

  #myTGraph_sigma.SetMarkerStyle(20)

  #C2.Modified()
  gPad.Modified()
  gPad.Update()
  C_CMSSWEff.Print("plots_v1/EffxAcc_CMSSWOnly.pdf","pdf")



##############################
### Empty "observed" limit ###
##############################
if plot_obs:
 
  xP, yPmax, yPmin = array( 'd' ), array( 'd' ), array( 'd' )
  n=10
  for i in range(0,n):
     xP.append((1+i)*(87.5)-90)
     yPmax.append(875)
     yPmin.append((1+i)*(87.5))

  grshade = TGraph("Observed Exclusion (Events/GeV^{2})")
  for i in range(0,n):
    grshade.SetPoint(i,xP[i],yPmax[i])
    grshade.SetPoint(n+i,xP[n-i-1],yPmin[n-i-1])

  grshade2 = TGraph("Observed Exclusion on #sigma (fb)")
  for i in range(0,n):
    grshade2.SetPoint(i,xP[i],yPmax[i])
    grshade2.SetPoint(n+i,xP[n-i-1],yPmin[n-i-1])



  C0 = TCanvas("C0","C0",1000,900)
  gPad.SetLogz()
  gPad.SetRightMargin(rightmargin)
  gPad.SetLeftMargin(leftmargin)
  gPad.SetBottomMargin(bottommargin)
  grshade.SetFillStyle(3013)
  grshade.SetFillColor(16)
  grshade.Draw('Af')
  gPad.Update()
  #grshade.GetHistogram().SetTitle("Observed Exclusion (Events)")
  grshade.GetHistogram().GetXaxis().SetTitle("M_{bb} (GeV)")
  grshade.GetHistogram().GetXaxis().SetTitleSize(xtitlesize)
  grshade.GetHistogram().GetXaxis().SetTitleOffset(xtitleoffset)
  grshade.GetHistogram().GetXaxis().SetRangeUser(0,900)
  grshade.GetHistogram().GetYaxis().SetTitle("M_{Zbb} (GeV)")
  grshade.GetHistogram().GetYaxis().SetTitleSize(ytitlesize)
  grshade.GetHistogram().GetYaxis().SetTitleOffset(ytitleoffset)
  grshade.GetHistogram().GetYaxis().SetRangeUser(0,900)
  gPad.Update()

  C02 = TCanvas("C02","C02",1000,900)
  gPad.SetRightMargin(rightmargin)
  gPad.SetLeftMargin(leftmargin)
  gPad.SetBottomMargin(bottommargin)

  grshade2.SetFillStyle(3013)
  grshade2.SetFillColor(16)
  grshade2.Draw('Af')
  gPad.Update()
  #grshade.GetHistogram().SetTitle("Observed Exclusion (Events)")
  grshade2.GetHistogram().GetXaxis().SetTitle("M_{A} (GeV)")
  grshade2.GetHistogram().GetXaxis().SetTitleSize(xtitlesize)
  grshade2.GetHistogram().GetXaxis().SetTitleOffset(xtitleoffset)
  grshade2.GetHistogram().GetXaxis().SetRangeUser(0,900)
  grshade2.GetHistogram().GetYaxis().SetTitle("M_{H} (GeV)")
  grshade2.GetHistogram().GetYaxis().SetTitleSize(ytitlesize)
  grshade2.GetHistogram().GetYaxis().SetTitleOffset(ytitleoffset)
  grshade2.GetHistogram().GetYaxis().SetRangeUser(0,900)
  gPad.Update()


####################################
### TGraph2D and TH2 definitions ###
####################################

myTGraph = TGraph2D(100)
myTGraph.SetName("Limit")
h0 = TH2D("h0","Observed Exclusion (#mu)",2000,0,xmax,2000,0,ymax)
myTGraph.SetHistogram(h0)

myTGraph_sigma = TGraph2D(100)
myTGraph_sigma.SetName("Efficiency + Acceptance")
h1 = TH2D("h1","Efficiency x Acceptance (Delphes Only)",500,0,xmax,500,0,ymax)
myTGraph_sigma.SetHistogram(h1)

myTGraph_sigma_corrected = TGraph2D(100)
myTGraph_sigma_corrected.SetName("EfficiencyXAcceptanceCorrected")
h12 = TH2D("h12","Efficiency x Acceptance (hybrid)",500,0,xmax,500,0,ymax)
myTGraph_sigma_corrected.SetHistogram(h12)

myTGraph_limit = TGraph2D(100)
myTGraph_limit.SetName("limit_on_sigma")
h2 = TH2D("h2","Expected Exclusion on #sigma (fb) (FastSim)",500,0,xmax,500,0,ymax)
myTGraph_limit.SetHistogram(h2)

myTGraph_limit_corrected = TGraph2D(100)
myTGraph_limit_corrected.SetName("limit_on_sigma_corrected")
h22 = TH2D("h22","Expected Exclusion on #sigma (fb) (hybrid)",500,0,xmax,500,0,ymax)
myTGraph_limit_corrected.SetHistogram(h22)

myTGraph_limit_corrected_lt = TGraph2D(10)
myTGraph_limit_corrected_lt.SetName("limit_on_sigma_corrected_lt")
h22_lt = TH2D("h22_lt","Expected Exclusion on #sigma (fb) (hybrid)",500,0,xmax,500,0,ymax)
myTGraph_limit_corrected_lt.SetHistogram(h22_lt)


myTGraph_limit_CMSSWOnly = TGraph2D(100)
myTGraph_limit_CMSSWOnly.SetName("limit_on_sigma_CMSSWOnly")
h23 = TH2D("h23","Expected Exclusion on #sigma (fb) (CMSSW Only)",500,0,xmax,500,0,ymax)
myTGraph_limit_CMSSWOnly.SetHistogram(h23)

myTGraph_Obs_limit = TGraph2D(100)
myTGraph_Obs_limit.SetName("Observed_limit_on_sigma_corrected")
h24 = TH2D("h24","Observed Exclusion on #sigma (fb) (hybrid)",500,0,xmax,500,0,ymax)
myTGraph_Obs_limit.SetHistogram(h24)

myTGraph_Obs_limit_lt = TGraph2D(10)
myTGraph_Obs_limit_lt.SetName("Observed_limit_on_sigma_corrected_lt")
h24_lt = TH2D("h24_lt","Observed Exclusion on #sigma (fb) (hybrid)",500,0,xmax,500,0,ymax)
myTGraph_Obs_limit_lt.SetHistogram(h24_lt)

myTGraph2 = TGraph2D(100)
myTGraph2.SetName("Expected Exclusion (#mu)")
h3 = TH2D("h3","Expected Exclusion (Events)",500,0,xmax,500,0,ymax)
myTGraph2.SetHistogram(h3)

myTGraph_Excl = TGraph2D(50)
myTGraph_Excl.SetName("Expected Exclusion")
h_Excl = TH2D("h_Excl","Expected Exclusion on #mu",500,0,xmax,500,0,ymax)
myTGraph_Excl.SetHistogram(h_Excl)


myTGraph_ExclObs = TGraph2D(50)
myTGraph_ExclObs.SetName("Observed Exclusion")
h_ExclObs = TH2D("h_ExclObs","Observed Exclusion on #mu",500,0,xmax,500,0,ymax)
myTGraph_ExclObs.SetHistogram(h_ExclObs)

myTGraph_Syst = TGraph2D(100)
myTGraph_Syst.SetName("Syst Ratio")
h_Syst = TH2D("h_Excl","Systematics on ratio",500,0,xmax,500,0,ymax)
myTGraph_Syst.SetHistogram(h_Syst)


#XSFile_path = "/home/fynu/amertens/Delphes_Analysis/2hdm/xs.root"
XSFile_path = "/home/fynu/amertens/Delphes_Analysis/2hdm/generation/sushi/SusHi-1.4.1/xsec_v2.root"
XSFile = TFile(str(XSFile_path))
xsG2D = XSFile.Get("nnloXsec")
ZABRG2D = XSFile.Get("ZA_BR")
bbBRG2D = XSFile.Get("bb_BR")

xsG2D.SetDirectory(0)
ZABRG2D.SetDirectory(0)
bbBRG2D.SetDirectory(0)


XSFile_path_lt = "/home/fynu/amertens/Delphes_Analysis/2hdm/generation/sushi/SusHi-1.4.1/xsec_A_ZH_ll_bb_tautau.root"
XSFile_lt = TFile(str(XSFile_path_lt))
xsG2D_lt = XSFile_lt.Get("nnloXsec")
ZABRG2D_lt = XSFile_lt.Get("ZH_BR")
bbBRG2D_lt = XSFile_lt.Get("bb_BR")

myTGraph_SignalYield = TGraph2D(100)
myTGraph_SignalYield.SetName("Signal Yield")
h_SignalYield = TH2D("h_SignalYield","Signal Yields",500,0,xmax,500,0,ymax)
myTGraph_SignalYield.SetHistogram(h_SignalYield)


myTGraph_125XCheck = TGraph(10)
myTGraph_125XCheck.SetName("AtoZh Cross-check")


mllbb=10
n=-1
m=-1
m1=-1
m2=-1
m_eff=-1
itAZh=-1
m_lp1=0
m_lp2=0
for i in range(1,numDirs):
  dmllbb=massResol*mllbb*bin_width
  step_mllbb = dmllbb*step_fraction

  print mllbb

  #MH_dir = "MH_"+str(int(mllbb))+"_Asymptotic_NOSYST_Blind_"
  if runblind == 1 and signal1 == 1:
    MH_dir = "v1_MH_"+str(int(mllbb))+"_Asymptotic_Blind_Combined_"
  elif runblind == 1 and signal1 == 0 :
    MH_dir = "v1_MH_"+str(int(mllbb))+"_Asymptotic_Blind_Combined_SigYields_"
  elif runblind == 0 and signal1 == 1 :
    MH_dir = "v1_MH_"+str(int(mllbb))+"_Asymptotic_Unblind_Combined_"
  elif runblind == 0 and signal1 == 0 :
    MH_dir = "v1_MH_"+str(int(mllbb))+"_Asymptotic_Unblind_Combined_SigYields_"

  if run_combine == 1:
    mkdir_cmd = "mkdir "+MH_dir
    print mkdir_cmd
    rmdir_cmd = "rm -rf "+MH_dir
    os.system(rmdir_cmd)
    os.system(str(mkdir_cmd))
  mbb=10.0
  for j in range(1,numFiles):
    print mbb
    dmbb=massResol*mbb*bin_width
    step_mbb = dmbb*step_fraction
    yield_path = DataCards_path+str(int(mbb))+"_"+str(int(mllbb))+".txt"
    if (mbb < mllbb) and (mllbb > 126.0): #and os.path.isfile(yield_path):
      #yield_path = "/home/fynu/amertens/scratch/CMSSW/CMSSW_6_1_1/src/2HDM/mH"+str(int(mllbb-dmllbb))+"to"+str(int(mllbb+dmllbb))+"/Combined/testmA"+str(int(mbb-dmbb))+"to"+str(int(mbb+dmbb))+".txt"
      #yield_path = DataCards_path+str(int(mbb))+"_"+str(int(mllbb))+".txt"
      #combine_cmd = "combine -M Asymptotic -m "+str(int(mbb))+" -S 0 "+yield_path
      if runblind == 0 :
        combine_cmd = "combine -M Asymptotic -m "+str(int(mbb))+" "+yield_path
      elif runblind == 1 : 
	combine_cmd = "combine -M Asymptotic -m "+str(int(mbb))+" --run=blind "+yield_path
      #combine_cmd = "combine -M ProfileLikelihood --significance --pvalue -m "+str(int(mbb))+" "+yield_path+" -t -1 --expectSignal=1"

      print combine_cmd
      try:
        file_path = MH_dir+"/higgsCombineTest.Asymptotic.mA"+str(int(mbb))+".root"
        if run_combine == 1:
          os.system(str(combine_cmd))
          cp_cmd = "cp higgsCombineTest.Asymptotic.mH"+str(int(mbb))+".root "+file_path
          os.system(str(cp_cmd))

        fList = TFile(str(file_path)) 
        mytree  = fList.Get("limit")
        #for entry in mytree:
        mytree.GetEntry(2)
	limit=mytree.limit
	
	
	mytree.GetEntry(5)
	limit_obs=mytree.limit


	if limit > 0:

  	  print "Expected Limit(",(i-1)*numDirs+(j-1) , ", " , int(mbb) , ", " , int(mllbb),") = ", limit
	  print "Observed Limit(",(i-1)*numDirs+(j-1) , ", " , int(mbb) , ", " , int(mllbb),") = ", limit_obs
          limitGev2=limit/(2*dmbb*2*dmllbb)
	  n+=1
          myTGraph.SetPoint(n, mbb, mllbb, limit_obs)
	  myTGraph2.SetPoint(n, mbb, mllbb, limit)
	  try :
            DelphesFile_path = "/home/fynu/amertens/storage/THDM/eff_v1/"+str(int(mllbb))+"_"+str(int(mbb))+".root"
	    if os.path.isfile(DelphesFile_path) :
	      DelphesFile = TFile(DelphesFile_path)
              myG2D = DelphesFile.Get("Graph2D")
	      eff = myG2D.Interpolate(int(mbb),int(mllbb))

	      print "efficiency(",int(mbb), ", ", int(mllbb), ") =", eff,

	      if eff == 0:
		eff = myG2D.Interpolate(int(mbb),int(mllbb)-10)
		print "efficiency(",int(mbb), ", ", int(mllbb)-0.1, ") =", eff,
	      if eff == 0:
                eff = myG2D.Interpolate(int(mbb),int(mllbb)+10)
                print "efficiency(",int(mbb), ", ", int(mllbb)+0.1, ") =", eff,
	      if eff == 0:
                eff = myG2D.Interpolate(int(mbb-10),int(mllbb))
                print "efficiency(",int(mbb)-0.1, ", ", int(mllbb), ") =", eff,
	      if eff == 0:
                eff = myG2D.Interpolate(int(mbb+10),int(mllbb))
                print "efficiency(",int(mbb)+0.1, ", ", int(mllbb), ") =", eff,

	      print "cmssw efficiency :"

	                     
              CMSSWeff = myTGraph_CMSSWEff.Interpolate(int(mbb),int(mllbb))
	      print "efficiency_CMSSW(",int(mbb), ", ", int(mllbb), ") =", CMSSWeff
	      
              if CMSSWeff == 0:
                CMSSWeff = myTGraph_CMSSWEff.Interpolate(int(mbb),int(mllbb)-0.1)
              if CMSSWeff == 0:
                CMSSWeff = myTGraph_CMSSWEff.Interpolate(int(mbb),int(mllbb)+0.1)
              if CMSSWeff == 0:
                CMSSWeff = myTGraph_CMSSWEff.Interpolate(int(mbb-0.1),int(mllbb))
              if CMSSWeff == 0:
                CMSSWeff = myTGraph_CMSSWEff.Interpolate(int(mbb+0.1),int(mllbb))
              
	      
	      ratio = myTGraph_ratio.Interpolate(int(mbb),int(mllbb))

	      errratio = myTGraph_errratio.Interpolate(int(mbb),int(mllbb))
              if errratio == 0:
                errratio = myG2D_errratio.Interpolate(int(mbb),int(mllbb)-0.1)
              if errratio == 0:
                errratio = myG2D_errratio.Interpolate(int(mbb),int(mllbb)+0.1)
              if errratio == 0:
                errratio = myG2D_errratio.Interpolate(int(mbb-0.1),int(mllbb))
              if errratio == 0:
                errratio = myG2D_errratio.Interpolate(int(mbb+0.1),int(mllbb))



	      xs_ggH=xsG2D.Interpolate(int(mbb),int(mllbb))
	      za_BR = ZABRG2D.Interpolate(int(mbb),int(mllbb))
	      bb_BR = bbBRG2D.Interpolate(int(mbb),int(mllbb))

	      xspb = xs_ggH*za_BR*bb_BR*0.06729

	      if xspb == 0:
                xs_ggH = xsG2D.Interpolate(int(mbb),int(mllbb)-0.1)
                za_BR = ZABRG2D.Interpolate(int(mbb),int(mllbb)-0.1)
                bb_BR = bbBRG2D.Interpolate(int(mbb),int(mllbb)-0.1)
		xspb = xs_ggH*za_BR*bb_BR*0.06729
              if xspb == 0:
                xs_ggH = xsG2D.Interpolate(int(mbb),int(mllbb)+0.1)
                za_BR = ZABRG2D.Interpolate(int(mbb),int(mllbb)+0.1)
                bb_BR = bbBRG2D.Interpolate(int(mbb),int(mllbb)+0.1)
		xspb = xs_ggH*za_BR*bb_BR*0.06729
              if xspb == 0:
                xs_ggH = xsG2D.Interpolate(int(mbb)-1,int(mllbb)-1)
                za_BR = ZABRG2D.Interpolate(int(mbb)-1,int(mllbb)-1)
                bb_BR = bbBRG2D.Interpolate(int(mbb)-1,int(mllbb)-1)
		xspb = xs_ggH*za_BR*bb_BR*0.06729
              if xspb == 0:
                xs_ggH = xsG2D.Interpolate(int(mbb)+0.1,int(mllbb))
                za_BR = ZABRG2D.Interpolate(int(mbb)+0.1,int(mllbb))
                bb_BR = bbBRG2D.Interpolate(int(mbb)+0.1,int(mllbb))
		xspb = xs_ggH*za_BR*bb_BR*0.06729
	     
	      xs = 1000*xspb 

	      print "xs : ", xs

	      xs_lt = 0

	      if mbb > 125:

                xs_ggH_lt=xsG2D_lt.Interpolate(int(mllbb),int(mbb))
                za_BR_lt = ZABRG2D_lt.Interpolate(int(mllbb),int(mbb))
                bb_BR_lt = bbBRG2D_lt.Interpolate(int(mllbb),int(mbb))

                xspb_lt = xs_ggH_lt*za_BR_lt*bb_BR_lt*0.06729
                if xspb_lt == 0:
                  xs_ggH_lt = xsG2D_lt.Interpolate(int(mllbb),int(mbb)-0.1)
                  za_BR_lt = ZABRG2D_lt.Interpolate(int(mllbb),int(mbb)-0.1)
                  bb_BR_lt = bbBRG2D_lt.Interpolate(int(mllbb),int(mbb)-0.1)
                  xspb_lt = xs_ggH_lt*za_BR_lt*bb_BR_lt*0.06729
                if xspb_lt == 0:
                  xs_ggH_lt = xsG2D_lt.Interpolate(int(mllbb),int(mbb)+0.1)
                  za_BR_lt = ZABRG2D_lt.Interpolate(int(mllbb),int(mbb)+0.1)
                  bb_BR_lt = bbBRG2D_lt.Interpolate(int(mllbb),int(mbb)+0.1)
                  xspb_lt = xs_ggH_lt*za_BR_lt*bb_BR_lt*0.06729
                if xspb_lt == 0:
                  xs_ggH_lt = xsG2D_lt.Interpolate(int(mllbb)-1,int(mbb)-1)
                  za_BR_lt = ZABRG2D_lt.Interpolate(int(mllbb)-1,int(mbb)-1)
                  bb_BR_lt = bbBRG2D_lt.Interpolate(int(mllbb)-1,int(mbb)-1)
                  xspb_lt = xs_ggH_lt*za_BR_lt*bb_BR_lt*0.06729
                if xspb_lt == 0:
                  xs_ggH_lt = xsG2D_lt.Interpolate(int(mllbb)+0.1,int(mbb))
                  za_BR_lt = ZABRG2D_lt.Interpolate(int(mllbb)+0.1,int(mbb))
                  bb_BR_lt = bbBRG2D_lt.Interpolate(int(mllbb)+0.1,int(mbb))
                  xspb_lt = xs_ggH_lt*za_BR_lt*bb_BR_lt*0.06729

                xs_lt = 1000*xspb_lt


	      print "eff  : ", eff, " " 
	      print "xs   : ", xs, " " 
	      print "xs_lt: ", xs_lt, " "

              if eff > 0 : #and CMSSWeff > 0 :
		m+=1

		errDelphes = 1/sqrt(100000*eff)
		err_tot = sqrt(errratio*errratio+errDelphes*errDelphes)

		print "Errors"
		print "Err Delphes   :", errDelphes
		print "Err ratioDeco :", errratio
		print "Err Syst      :", err_tot
		

		print "filling Tgraphs.."
	        myTGraph_sigma.SetPoint(m, mbb, mllbb, eff)
	        #myTGraph_limit.SetPoint(m, mbb, mllbb, log10(limit/(20*eff)))
	        myTGraph_limit.SetPoint(m, mbb, mllbb, limit/(lumi*eff))
		#myTGraph_Excl.SetPoint(m,mbb,mllbb,limit/(lumi*eff*ratio*xs))
		print "signal strenght: ", limit/(lumi*eff*ratio*xs)
		print "Factor : ", lumi*eff*ratio*xs
		if ratio > 0:
		  m1+=1
		  #myTGraph_Excl.SetPoint(m1,mbb,mllbb,limit/(lumi*eff*ratio*xs))
		  myTGraph_limit_corrected.SetPoint(m1, mbb, mllbb, limit/(lumi*eff*ratio))
		  if plot_obs:
		    myTGraph_Obs_limit.SetPoint(m1, mbb, mllbb, limit_obs/(lumi*eff*ratio))
		    #myTGraph_ExclObs.SetPoint(m1, mbb, mllbb, limit_obs/(lumi*eff*ratio*xs))
		  m_eff+=1
		  myTGraph_sigma_corrected.SetPoint(m_eff, mbb, mllbb, eff*ratio)
		  m_eff+=1
                  myTGraph_sigma_corrected.SetPoint(m_eff, mllbb, mbb, eff*ratio)


		  limit_exp_xs = limit/(lumi*eff*ratio)
		  limit_exp_mu = limit/(lumi*eff*ratio*xs)
		  if xs_lt > 0 :
		    limit_exp_mu_lt = limit/(lumi*eff*ratio*xs_lt)

		  limit_obs_xs = limit_obs/(lumi*eff*ratio)
                  limit_obs_mu = limit_obs/(lumi*eff*ratio*xs)
		  if xs_lt > 0 :
		    limit_obs_mu_lt = limit_obs/(lumi*eff*ratio*xs_lt)

		  print "mbb : ", int(mbb), " "
                  print "m_lp1 : ", m_lp1

                  #### Lower Triangle ####
                  
		  myTGraph_limit_corrected_lt.SetPoint(m_lp1, mllbb, mbb, limit_exp_xs)
		  myTGraph_Obs_limit_lt.SetPoint(m_lp1, mllbb, mbb, limit_obs_xs)

		  if xs_lt > 0 :
		    myTGraph_Excl.SetPoint(m_lp2,mllbb,mbb,limit_exp_mu_lt)
		    myTGraph_ExclObs.SetPoint(m_lp2, mllbb, mbb, limit_obs_mu_lt)
		    m_lp2+=1
                  m_lp1+=1

                  #### Upper Triangle ####
		    
		  myTGraph_Excl.SetPoint(m_lp2,mbb,mllbb,limit_exp_mu)
		  myTGraph_limit_corrected_lt.SetPoint(m_lp1, mbb, mllbb, limit_exp_xs)	    
		  myTGraph_ExclObs.SetPoint(m_lp2, mbb, mllbb, limit_obs_mu)
                  myTGraph_Obs_limit_lt.SetPoint(m_lp1, mbb, mllbb, limit_obs_xs)
		  m_lp1+=1
		  m_lp2+=1


		
		  myTGraph_SignalYield.SetPoint(m1,mbb,mllbb,lumi*eff*ratio*xs)
		  if CMSSWeff > 0:
		    m2+=1
		    myTGraph_limit_CMSSWOnly.SetPoint(m2, mbb, mllbb, limit/(lumi*CMSSWeff))
		  myTGraph_Syst.SetPoint(m1, mbb, mllbb, err_tot)
#		  myTGraph_limit_CMSSWOnly.SetPoint(m1, mbb, mllbb, limit/(lumi*CMSSWeff))      
	    #else :
	      #m+=1
	      #myTGraph_sigma.SetPoint(n, mbb, mllbb, 0)
	      #myTGraph_limit.SetPoint(m, mbb, mllbb, 0)

	  #else :
	    #m+=1
	    #myTGraph_sigma.SetPoint(n, mbb, mllbb, 0)
	    #myTGraph_limit.SetPoint(m, mbb, mllbb, 0)

	  except:
	    print DelphesFile_path, " not existing . "
	  #m+=1
	  #myTGraph_sigma.SetPoint(n, mbb, mllbb, 0)
	  #myTGraph_limit.SetPoint(m, mbb, mllbb, 0)

      #myTGraph.SetPoint(n, mbb, mllbb, mytree.limit)
      #else : 
	#myTGraph.SetPoint(n, mbb, mllbb, 0)
	#myTGraph2.SetPoint(n, mbb, mllbb, 0)
	#m+=1
	#myTGraph_sigma.SetPoint(n, mbb, mllbb, 0)
	#myTGraph_limit.SetPoint(m, mbb, mllbb, 0)
      except:
        print 'no background events'
      #myTGraph.SetPoint(n, mbb, mllbb, 0)
      #myTGraph2.SetPoint(n, mbb, mllbb, 0)
      #m+=1
      #myTGraph_sigma.SetPoint(n, mbb, mllbb, 0)
      #myTGraph_limit.SetPoint(m, mbb, mllbb, 0)


    mbb+=step_mbb

    #print '##############################################'
    #print 'mllbb', mllbb , 'mbb:', mbb, 'myTGraph size', myTGraph.GetN()
    #print '##############################################'

  mllbb+=step_mllbb


print "##################################################",
print "N = ", n


n+=1
myTGraph2.SetPoint(n,20,215,10)
it=-1
for mllbb in range (240,1100):
  it+=1
  limit126 = myTGraph_limit_corrected.GetHistogram().Interpolate(125,mllbb)
  myTGraph_125XCheck.SetPoint(it, mllbb, limit126)

Azh_limit = TGraph(6)
Azh_limit.SetPoint(0, 225, 20)
Azh_limit.SetPoint(1, 270, 17)
Azh_limit.SetPoint(2, 322, 10)
Azh_limit.SetPoint(3, 405, 5)
Azh_limit.SetPoint(4, 485, 3)
Azh_limit.SetPoint(5, 600, 2)

C_XC=TCanvas("C_XC","C_XC",1000,900)
ROOT.gStyle.SetPalette(1)
ROOT.gStyle.SetOptStat(0)
gPad.SetLogy()
myTGraph_125XCheck.SetLineColor(kRed)
myTGraph_125XCheck.SetLineWidth(3)
Azh_limit.SetLineWidth(3)
myTGraph_125XCheck.Draw("AC")
myTGraph_125XCheck.SetMinimum(1)
myTGraph_125XCheck.SetMaximum(200)
myTGraph_125XCheck.GetXaxis().SetTitle("M_{A} [GeV]")
myTGraph_125XCheck.GetYaxis().SetTitle("#sigma #times B (A #rightarrow Zh #rightarrow llbb) [fb] ")
gPad.SetRightMargin(rightmargin)
gPad.SetLeftMargin(leftmargin)
gPad.SetBottomMargin(bottommargin)
myTGraph_125XCheck.GetXaxis().SetTitleSize(xtitlesize)
myTGraph_125XCheck.GetXaxis().SetTitleOffset(xtitleoffset)
myTGraph_125XCheck.GetYaxis().SetTitleSize(ytitlesize)
myTGraph_125XCheck.GetYaxis().SetTitleOffset(ytitleoffset)

Azh_limit.Draw("C")

legend=TLegend(0.6,0.6,0.8,0.8)
legend.AddEntry(myTGraph_125XCheck, "H #rightarrow ZA", "l")
legend.AddEntry(Azh_limit, "A #rightarrow Zh", "l")
legend.SetLineColor(0)
legend.SetFillColor(0)
legend.Draw()

gPad.Modified()
gPad.Update()

'''
  hadd_cmd = "hadd "+MH_dir+"/higgsCombineTest.ProfileLikelihood.root "+MH_dir+"/higgsCombineTest.ProfileLikelihood.mA*.root"
  os.system(str(hadd_cmd))
  fList = TFile(MH_dir+"/higgsCombineTest.ProfileLikelihood.root")
  mytree  = fList.Get("limit")
  j=0
  for entry in mytree:
    print "p-value(",(i-1)*5+(j-1) , ", " , mbb , ", " , mllbb,") = ", entry.limit
    j+=1
    myTGraph.SetPoint((i-1)*5+(j-1), mbb, mllbb,entry.limit)
'''


print 'M value :', m, m1

if plot_c1:
  
  C=TCanvas("C","C",1000,900)
  ROOT.gStyle.SetPalette(1)
  ROOT.gStyle.SetOptStat(0)
  
  gPad.SetLogz()
  gPad.SetLogz()
  gPad.SetRightMargin(rightmargin)
  gPad.SetLeftMargin(leftmargin)
  gPad.SetBottomMargin(bottommargin)
  myTGraph_limit.GetHistogram().Draw("colz")
  #gPad.Update()
  
  #myTGraph_limit.GetHistogram().GetXaxis().SetLimits(0,1000)
  #myTGraph_limit.GetHistogram().GetYaxis().SetLimits(0,1000)
  
  #myTGraph_limit.GetHistogram().SetMargin(0.0)
  myTGraph_limit.GetHistogram().GetXaxis().SetTitle("M_{A} (GeV)")
  myTGraph_limit.GetHistogram().GetXaxis().SetTitleSize(xtitlesize)
  myTGraph_limit.GetHistogram().GetXaxis().SetTitleOffset(xtitleoffset)
  myTGraph_limit.GetHistogram().GetYaxis().SetTitle("M_{H} (GeV)")
  myTGraph_limit.GetHistogram().GetYaxis().SetTitleSize(ytitlesize)
  myTGraph_limit.GetHistogram().GetYaxis().SetTitleOffset(ytitleoffset)
  myTGraph_limit.GetHistogram().SetMinimum(1)
  myTGraph_limit.GetHistogram().SetMaximum(100)
  #myTGraph_limit.GetHistogram().GetXaxis().SetRangeUser(0,1000)
  #myTGraph_limit.GetHistogram().GetYaxis().SetRangeUser(0,1000)
  #myTGraph_limit.GetHistogram().SetTitle("Expected Exclusion on #sigma (fb)")
  
  gPad.Modified()
  gPad.Update()

  C.Print("plots_v1/ExpExcl_FastSim.pdf","pdf")

if plot_c12:

  C12=TCanvas("C12","C12",1000,900)
  ROOT.gStyle.SetPalette(1)
  ROOT.gStyle.SetOptStat(0)

  gPad.SetLogz()
  gPad.SetLogz()
  gPad.SetRightMargin(rightmargin)
  gPad.SetLeftMargin(leftmargin)
  gPad.SetBottomMargin(bottommargin)
  myTGraph_limit_corrected.GetHistogram().Draw("colz")
  #gPad.Update()

  #myTGraph_limit.GetHistogram().GetXaxis().SetLimits(0,1000)
  #myTGraph_limit.GetHistogram().GetYaxis().SetLimits(0,1000)

  #myTGraph_limit.GetHistogram().SetMargin(0.0)
  myTGraph_limit_corrected.GetHistogram().GetXaxis().SetTitle("M_{A} (GeV)")
  myTGraph_limit_corrected.GetHistogram().GetXaxis().SetTitleSize(xtitlesize)
  myTGraph_limit_corrected.GetHistogram().GetXaxis().SetTitleOffset(xtitleoffset)
  myTGraph_limit_corrected.GetHistogram().GetYaxis().SetTitle("M_{H} (GeV)")
  myTGraph_limit_corrected.GetHistogram().GetYaxis().SetTitleSize(ytitlesize)
  myTGraph_limit_corrected.GetHistogram().GetYaxis().SetTitleOffset(ytitleoffset)
  myTGraph_limit_corrected.GetHistogram().SetMinimum(1)
  myTGraph_limit_corrected.GetHistogram().SetMaximum(100)
  #myTGraph_limit.GetHistogram().GetXaxis().SetRangeUser(0,1000)
  #myTGraph_limit.GetHistogram().GetYaxis().SetRangeUser(0,1000)

  gPad.Modified()
  gPad.Update()
  C12.Print("plots_v1/ExpExcl_hybrid.pdf","pdf")


if plot_c13:

  C13=TCanvas("C13","C13",1000,900)
  ROOT.gStyle.SetPalette(1)
  ROOT.gStyle.SetOptStat(0)

  gPad.SetLogz()
  gPad.SetLogz()
  gPad.SetRightMargin(rightmargin)
  gPad.SetLeftMargin(leftmargin)
  gPad.SetBottomMargin(bottommargin)
  myTGraph_limit_CMSSWOnly.GetHistogram().Draw("colz")
  #gPad.Update()

  #myTGraph_limit.GetHistogram().GetXaxis().SetLimits(0,1000)
  #myTGraph_limit.GetHistogram().GetYaxis().SetLimits(0,1000)

  #myTGraph_limit.GetHistogram().SetMargin(0.0)
  myTGraph_limit_CMSSWOnly.GetHistogram().GetXaxis().SetTitle("M_{A} (GeV)")
  myTGraph_limit_CMSSWOnly.GetHistogram().GetXaxis().SetTitleSize(xtitlesize)
  myTGraph_limit_CMSSWOnly.GetHistogram().GetXaxis().SetTitleOffset(xtitleoffset)
  myTGraph_limit_CMSSWOnly.GetHistogram().GetYaxis().SetTitle("M_{H} (GeV)")
  myTGraph_limit_CMSSWOnly.GetHistogram().GetYaxis().SetTitleSize(ytitlesize)
  myTGraph_limit_CMSSWOnly.GetHistogram().GetYaxis().SetTitleOffset(ytitleoffset)
  myTGraph_limit_CMSSWOnly.GetHistogram().SetMinimum(1)
  myTGraph_limit_CMSSWOnly.GetHistogram().SetMaximum(100)
  #myTGraph_limit.GetHistogram().GetXaxis().SetRangeUser(0,1000)
  #myTGraph_limit.GetHistogram().GetYaxis().SetRangeUser(0,1000)

  gPad.Modified()
  gPad.Update()
  C13.Print("plots_v1/ExpExcl_CMSSWOnly.pdf","pdf")


if plot_c14:

  C14=TCanvas("C14","C14",1000,900)
  #ROOT.setTDRStyle()

  ROOT.gStyle.SetPalette(1)
  ROOT.gStyle.SetOptStat(0)

  gPad.SetLogz()
  gPad.SetLogz()
  gPad.SetRightMargin(rightmargin)
  gPad.SetLeftMargin(leftmargin)
  gPad.SetBottomMargin(bottommargin)
  
  #myTGraph_limit_corrected_lt.GetHistogram().Add(myTGraph_limit_corrected.GetHistogram())
  myTGraph_limit_corrected_lt.GetHistogram().Draw("colz")
  #gPad.Update()

  #myTGraph_limit.GetHistogram().GetXaxis().SetLimits(0,1000)
  #myTGraph_limit.GetHistogram().GetYaxis().SetLimits(0,1000)

  #myTGraph_limit.GetHistogram().SetMargin(0.0)
  myTGraph_limit_corrected_lt.GetHistogram().GetXaxis().SetTitle("M_{A} (GeV)")
  myTGraph_limit_corrected_lt.GetHistogram().GetXaxis().SetTitleSize(xtitlesize)
  myTGraph_limit_corrected_lt.GetHistogram().GetXaxis().SetTitleOffset(xtitleoffset)
  myTGraph_limit_corrected_lt.GetHistogram().GetYaxis().SetTitle("M_{H} (GeV)")
  myTGraph_limit_corrected_lt.GetHistogram().GetYaxis().SetTitleSize(ytitlesize)
  myTGraph_limit_corrected_lt.GetHistogram().GetYaxis().SetTitleOffset(ytitleoffset)
  myTGraph_limit_corrected_lt.GetHistogram().GetZaxis().SetTitle("Expected #sigma_{95%} (fb)")
  myTGraph_limit_corrected_lt.GetHistogram().GetZaxis().SetTitleSize(ztitlesize)
  myTGraph_limit_corrected_lt.GetHistogram().GetZaxis().SetTitleOffset(ztitleoffset)
  myTGraph_limit_corrected_lt.GetHistogram().SetMinimum(1)
  myTGraph_limit_corrected_lt.GetHistogram().SetMaximum(100)
  #myTGraph_limit.GetHistogram().GetXaxis().SetRangeUser(0,1000)
  #myTGraph_limit.GetHistogram().GetYaxis().SetRangeUser(0,1000)

  #CMS_lumi(C14, 2, 0 )

  gPad.Modified()
  gPad.Update()
  C14.Print("plots_v1/ExpExcl_hybrid_2sided.pdf","pdf")


if plot_obs:
 
  C_Obs=TCanvas("C_Obs","C_Obs",1000,900)
  ROOT.gStyle.SetPalette(1)
  ROOT.gStyle.SetOptStat(0)

  gPad.SetLogz()
  gPad.SetLogz()
  gPad.SetRightMargin(rightmargin)
  gPad.SetLeftMargin(leftmargin)
  gPad.SetBottomMargin(bottommargin)
  myTGraph_Obs_limit.GetHistogram().Draw("colz")
  #gPad.Update()

  #myTGraph_limit.GetHistogram().GetXaxis().SetLimits(0,1000)
  #myTGraph_limit.GetHistogram().GetYaxis().SetLimits(0,1000)

  #myTGraph_limit.GetHistogram().SetMargin(0.0)
  myTGraph_Obs_limit.GetHistogram().GetXaxis().SetTitle("M_{A} (GeV)")
  myTGraph_Obs_limit.GetHistogram().GetXaxis().SetTitleSize(xtitlesize)
  myTGraph_Obs_limit.GetHistogram().GetXaxis().SetTitleOffset(xtitleoffset)
  myTGraph_Obs_limit.GetHistogram().GetYaxis().SetTitle("M_{H} (GeV)")
  myTGraph_Obs_limit.GetHistogram().GetYaxis().SetTitleSize(ytitlesize)
  myTGraph_Obs_limit.GetHistogram().GetYaxis().SetTitleOffset(ytitleoffset)
  myTGraph_Obs_limit.GetHistogram().SetMinimum(1)
  myTGraph_Obs_limit.GetHistogram().SetMaximum(100)
  #myTGraph_limit.GetHistogram().GetXaxis().SetRangeUser(0,1000)
  #myTGraph_limit.GetHistogram().GetYaxis().SetRangeUser(0,1000)

  gPad.Modified()
  gPad.Update()
  C_Obs.Print("plots_v1/ObsExcl_hybrid.pdf","pdf")

if plot_obs:

  C_Obs_lt=TCanvas("C_Obs_lt","C_Obs_lt",1000,900)
  #ROOT.setTDRStyle()

  ROOT.gStyle.SetPalette(1)
  ROOT.gStyle.SetOptStat(0)

  gPad.SetLogz()
  gPad.SetLogz()
  gPad.SetRightMargin(rightmargin)
  gPad.SetLeftMargin(leftmargin)
  gPad.SetBottomMargin(bottommargin)
  #myTGraph_Obs_limit_lt.GetHistogram().Add(myTGraph_Obs_limit.GetHistogram())
  myTGraph_Obs_limit_lt.GetHistogram().Draw("colz")
  #gPad.Update()

  #myTGraph_limit.GetHistogram().GetXaxis().SetLimits(0,1000)
  #myTGraph_limit.GetHistogram().GetYaxis().SetLimits(0,1000)

  #myTGraph_limit.GetHistogram().SetMargin(0.0)
  myTGraph_Obs_limit_lt.GetHistogram().GetXaxis().SetTitle("M_{A} (GeV)")
  myTGraph_Obs_limit_lt.GetHistogram().GetXaxis().SetTitleSize(xtitlesize)
  myTGraph_Obs_limit_lt.GetHistogram().GetXaxis().SetTitleOffset(xtitleoffset)
  myTGraph_Obs_limit_lt.GetHistogram().GetYaxis().SetTitle("M_{H} (GeV)")
  myTGraph_Obs_limit_lt.GetHistogram().GetYaxis().SetTitleSize(ytitlesize)
  myTGraph_Obs_limit_lt.GetHistogram().GetYaxis().SetTitleOffset(ytitleoffset)
  myTGraph_Obs_limit_lt.GetHistogram().GetZaxis().SetTitle("Observed #sigma_{95%} (fb)")
  myTGraph_Obs_limit_lt.GetHistogram().GetZaxis().SetTitleSize(ztitlesize)
  myTGraph_Obs_limit_lt.GetHistogram().GetZaxis().SetTitleOffset(ztitleoffset)
  myTGraph_Obs_limit_lt.GetHistogram().SetMinimum(1)
  myTGraph_Obs_limit_lt.GetHistogram().SetMaximum(100)
  #myTGraph_limit.GetHistogram().GetXaxis().SetRangeUser(0,1000)
  #myTGraph_limit.GetHistogram().GetYaxis().SetRangeUser(0,1000)

  #CMS_lumi(C_Obs_lt, 2, 0 )

  gPad.Modified()
  gPad.Update()

  C_Obs_lt.Print("plots_v1/ObsExcl_hybrid_2sided.pdf","pdf")

  f = TFile("Limit_Xs.root","recreate")
  myTGraph_sigma_corrected.GetHistogram().Write()
  myTGraph_Obs_limit_lt.GetHistogram().Write()
  myTGraph_limit_corrected_lt.GetHistogram().Write()
  f.Close()




'''
# code for PCOL Option
C.cd(2)
gPad.SetRightMargin(0.2)
gPad.SetLeftMargin(0.2)
gPad.SetBottomMargin(0.2)
myTGraph_limit.Draw("pcol")
myTGraph_limit.GetXaxis().SetTitle("M_{bb}")
myTGraph_limit.GetXaxis().SetTitleSize(0.07)
myTGraph_limit.GetXaxis().SetTitleOffset(1.1)
myTGraph_limit.GetYaxis().SetTitle("M_{Zbb}")
myTGraph_limit.GetYaxis().SetTitleSize(0.07)
myTGraph_limit.GetYaxis().SetTitleOffset(1.1)
myTGraph_limit.SetMarkerStyle(20)
myTGraph_limit.SetMarkerSize(1)
myTGraph_limit.SetTitle("Expected Exclusion on #sigma")
gPad.Modified()
gPad.Update()
gPad.GetView().TopView()
#myTGraph_limit.GetZaxis().SetRangeUser(1,10000.0)

C.Print("Exp_Lim_Xsec_colz.png","png")

C2=TCanvas("C2","C2",750,1000)
ROOT.gStyle.SetPalette(55)
'''


if plot_c2 : 
  C2=TCanvas("C2","C2",1000,900)
  gPad.SetLogz()
  gPad.SetRightMargin(rightmargin)
  gPad.SetLeftMargin(leftmargin)
  gPad.SetBottomMargin(bottommargin)
  myTGraph.GetHistogram().Draw("colz")
  gPad.Update()
  #myTGraph.SetTitle("Expected Exclusion (Events / GeV^{2})")
  myTGraph.GetHistogram().GetXaxis().SetTitle("M_{bb} (GeV)")
  myTGraph.GetHistogram().GetXaxis().SetTitleSize(xtitlesize)
  myTGraph.GetHistogram().GetXaxis().SetTitleOffset(xtitleoffset)
  myTGraph.GetHistogram().GetYaxis().SetTitle("M_{Zbb} (GeV)")
  myTGraph.GetHistogram().GetYaxis().SetTitleSize(ytitlesize)
  myTGraph.GetHistogram().GetYaxis().SetTitleOffset(ytitleoffset)
  myTGraph.GetHistogram().GetZaxis().SetTitle("Expected Exclusion (Events / GeV^{2})")
  myTGraph.GetHistogram().GetZaxis().SetTitleSize(ztitlesize)
  myTGraph.GetHistogram().GetZaxis().SetTitleOffset(ztitleoffset)
  myTGraph.GetHistogram().SetMinimum(1)
  myTGraph.GetHistogram().SetMaximum(1000)
  gPad.Update()
  C2.Print("plots_v1/ObsExcl_mu.pdf","pdf")
  

if plot_c3:  
  C3=TCanvas("C3","C3",1000,900)
  ROOT.gStyle.SetPalette(1)
  #set_palette("color", 999)
  ROOT.gStyle.SetOptStat(0)
  gPad.SetLogz()
  gPad.SetRightMargin(rightmargin)
  gPad.SetLeftMargin(leftmargin)
  gPad.SetBottomMargin(bottommargin)
  myTGraph2.GetHistogram().Draw("colz")
  gPad.Update()
  #myTGraph2.GetHistogram().SetTitle("Expected Exclusion (Events / GeV^{2})")
  myTGraph2.GetHistogram().GetXaxis().SetTitle("M_{bb} (GeV)")
  myTGraph2.GetHistogram().GetXaxis().SetTitleSize(xtitlesize)
  myTGraph2.GetHistogram().GetXaxis().SetTitleOffset(xtitleoffset)
  myTGraph2.GetHistogram().GetYaxis().SetTitle("M_{Zbb} (GeV)")
  myTGraph2.GetHistogram().GetYaxis().SetTitleSize(ytitlesize)
  myTGraph2.GetHistogram().GetYaxis().SetTitleOffset(ytitleoffset)
  #myTGraph2.GetHistogram().GetZaxis().SetTitle("Expected Exclusion (Events / GeV^{2})")
  myTGraph2.GetHistogram().GetZaxis().SetTitleSize(ztitlesize)
  myTGraph2.GetHistogram().GetZaxis().SetTitleOffset(ztitleoffset)
  myTGraph2.GetHistogram().SetMinimum(1)
  myTGraph2.GetHistogram().SetMaximum(1000)

  gPad.Modified()
  gPad.Update()
  
  f = TFile("Limit_NeV.root","recreate")
  myTGraph.GetHistogram().Write()
  myTGraph2.GetHistogram().Write()
  f.Close()

#C2.SetLogz()


if plot_c4:
 
  C4=TCanvas("C4","C4",1000,900)
 
  C4.Update()
  C4.Modified()
  gPad.SetRightMargin(rightmargin)
  gPad.SetLeftMargin(leftmargin)
  gPad.SetBottomMargin(bottommargin)
  #gPad.SetTopMargin()
  gPad.SetLogz()
  myTGraph_sigma.GetHistogram().Draw("colz")
  myTGraph_sigma.GetHistogram().GetXaxis().SetTitle("M_{A} (GeV)")
  myTGraph_sigma.GetHistogram().GetXaxis().SetTitleSize(xtitlesize)
  myTGraph_sigma.GetHistogram().GetXaxis().SetTitleOffset(xtitleoffset)
  myTGraph_sigma.GetHistogram().GetYaxis().SetTitle("M_{H} (GeV)")
  myTGraph_sigma.GetHistogram().GetYaxis().SetTitleSize(ytitlesize)
  myTGraph_sigma.GetHistogram().GetYaxis().SetTitleOffset(ytitleoffset)
  myTGraph_sigma.GetHistogram().GetZaxis().SetTitle("#epsilon")
  myTGraph_sigma.GetHistogram().GetZaxis().SetTitleSize(ztitlesize)
  myTGraph_sigma.GetHistogram().GetZaxis().SetTitleOffset(ztitleoffset)
  myTGraph_sigma.GetHistogram().SetMinimum(0.0001)
  myTGraph_sigma.GetHistogram().SetMaximum(0.3)

  #myTGraph_sigma.SetMarkerStyle(20)
 
  #C2.Modified()
  gPad.Modified()
  gPad.Update()
  C4.Print("plots_v1/EffxAcc_FastSim.pdf","pdf")

if plot_c42:

  C42=TCanvas("C42","C42",1000,900)

  C42.Update()
  C42.Modified()
  gPad.SetRightMargin(rightmargin)
  gPad.SetLeftMargin(leftmargin)
  gPad.SetBottomMargin(bottommargin)
  #gPad.SetTopMargin()
  gPad.SetLogz()
  myTGraph_sigma_corrected.GetHistogram().Draw("colz")
  myTGraph_sigma_corrected.GetHistogram().GetXaxis().SetTitle("M_{A} (GeV)")
  myTGraph_sigma_corrected.GetHistogram().GetXaxis().SetTitleSize(xtitlesize)
  myTGraph_sigma_corrected.GetHistogram().GetXaxis().SetTitleOffset(xtitleoffset)
  myTGraph_sigma_corrected.GetHistogram().GetYaxis().SetTitle("M_{H} (GeV)")
  myTGraph_sigma_corrected.GetHistogram().GetYaxis().SetTitleSize(ytitlesize)
  myTGraph_sigma_corrected.GetHistogram().GetYaxis().SetTitleOffset(ytitleoffset)
  myTGraph_sigma_corrected.GetHistogram().GetZaxis().SetTitle("#epsilon")
  myTGraph_sigma_corrected.GetHistogram().GetZaxis().SetTitleSize(ztitlesize)
  myTGraph_sigma_corrected.GetHistogram().GetZaxis().SetTitleOffset(ztitleoffset)
  myTGraph_sigma_corrected.GetHistogram().SetMinimum(0.0001)
  myTGraph_sigma_corrected.GetHistogram().SetMaximum(0.3)


  gPad.Modified()
  gPad.Update()
  C42.Print("plots_v1/EffxAcc_hybrid.pdf","pdf")



if plot_c5:
  
  C5=TCanvas("C5","C5",1000,900)
  
  C5.Update()
  C5.Modified()
  gPad.SetRightMargin(rightmargin)
  gPad.SetLeftMargin(leftmargin)
  gPad.SetBottomMargin(bottommargin)
  #gPad.SetTopMargin()
  #gPad.SetLogz()
  CMSSWPoints = TGraph(12)
  CMSSWPoints.SetPoint(0,35,142)
  CMSSWPoints.SetPoint(1,30,329)
  #CMSSWPoints.SetPoint(2,142,575)
  CMSSWPoints.SetPoint(3,70,575)
  CMSSWPoints.SetPoint(4,378,875)
  CMSSWPoints.SetPoint(5,70,875)
  CMSSWPoints.SetPoint(6,142,329)
  CMSSWPoints.SetPoint(7,70,329)
  CMSSWPoints.SetPoint(8,378,575)
  CMSSWPoints.SetPoint(9,142,875)
  CMSSWPoints.SetPoint(10,575,875)
  CMSSWPoints.SetPoint(11,761,875)
  CMSSWPoints.SetPoint(12,50,200)
  CMSSWPoints.SetPoint(2,90,200)
  
  CMSSWPoints.SetMarkerStyle(21)
  CMSSWPoints.GetXaxis().SetLimits(0,1200)
  CMSSWPoints.SetMinimum(0)
  CMSSWPoints.SetMaximum(1200)
  '''
  CMSSWPoints.GetXaxis().SetTitle("M_{A}")
  CMSSWPoints.GetYaxis().SetTitle("M_{H}")
  #CMSSWPoints.GetXaxis().SetTitleOffSet(1.1)
  CMSSWPoints.GetYaxis().SetTitleOffset(1.5)
  CMSSWPoints.GetXaxis().SetTitleSize(0.06)
  CMSSWPoints.GetYaxis().SetTitleSize(0.06)
  CMSSWPoints.GetXaxis().SetLabelSize(0.05)
  CMSSWPoints.GetYaxis().SetLabelSize(0.05)
  CMSSWPoints.GetXaxis().SetNdivisions(5)
  CMSSWPoints.GetYaxis().SetNdivisions(5)
  '''
  myTGraph_ratio.GetHistogram().Draw("colz")
  CMSSWPoints.Draw("P")
  #LineBoostedRegion = TLine(0,0,120,1200)
  #LineKin = TLine(0,90,1110,1200)
  #LineOneOne = TLine(0,0,1000,1000)
  #LineBoostedRegion.SetLineColor(kRed)
  #LineBoostedRegion.SetLineWidth(3)
  #LineBoostedRegion.SetLineStyle(2)
  #LineBoostedRegion.Draw()
  #LineKin.SetLineWidth(3)
  #LineKin.Draw()
  #LineOneOne.SetLineWidth(3)
  #LineOneOne.Draw()
  #t1 = TPaveText(0.5,0.35,0.7,0.50,"brNDC")
  #t1.AddText("M_{A}+M_{Z}>M_{H}")
  #t1.SetFillColor(0)
  #t1.Draw("same")
  
  
  #myTGraph_sigma.GetHistogram().SetTitle("Acceptance + Selection Efficiency")
  
  myTGraph_ratio.GetHistogram().GetXaxis().SetTitle("M_{A} (GeV)")
  myTGraph_ratio.GetHistogram().GetXaxis().SetTitleSize(xtitlesize)
  myTGraph_ratio.GetHistogram().GetXaxis().SetTitleOffset(xtitleoffset)
  myTGraph_ratio.GetHistogram().GetYaxis().SetTitle("M_{H} (GeV)")
  myTGraph_ratio.GetHistogram().GetYaxis().SetTitleSize(ytitlesize)
  myTGraph_ratio.GetHistogram().GetYaxis().SetTitleOffset(ytitleoffset)
  #myTGraph_sigma.GetHistogram().GetZaxis().SetTitle("#epsilon #times Acc.")
  myTGraph_ratio.GetHistogram().GetZaxis().SetTitleSize(ztitlesize)
  myTGraph_ratio.GetHistogram().GetZaxis().SetTitleOffset(ztitleoffset)
  #myTGraph_sigma.SetMarkerStyle(20)
  
  #C2.Modified()
  gPad.Modified()
  gPad.Update()
  C5.Print("plots_v1/ratio_comparison_points.pdf","pdf")
 
if plot_c6:
  C6=TCanvas("C6","C6",1000,900)

  C6.Update()
  C6.Modified()
  gPad.SetRightMargin(rightmargin)
  gPad.SetLeftMargin(leftmargin)
  gPad.SetBottomMargin(bottommargin)
  #gPad.SetTopMargin()
  gPad.SetLogz()
  #myTGraph_Excl.GetHistogram().SetContourLevel(0,0.5)
  #myTGraph_Excl.GetHistogram().SetContourLevel(1,1)
  #myTGraph_Excl.GetHistogram().SetContourLevel(2,1.5)
  myTGraph_Excl.GetHistogram().Draw("colz")
  
  myTGraph_Excl.GetHistogram().GetXaxis().SetTitle("M_{A} (GeV)")
  myTGraph_Excl.GetHistogram().GetXaxis().SetTitleSize(xtitlesize)
  myTGraph_Excl.GetHistogram().GetXaxis().SetTitleOffset(xtitleoffset)
  myTGraph_Excl.GetHistogram().GetYaxis().SetTitle("M_{H} (GeV)")
  myTGraph_Excl.GetHistogram().GetYaxis().SetTitleSize(ytitlesize)
  myTGraph_Excl.GetHistogram().GetYaxis().SetTitleOffset(ytitleoffset)
  myTGraph_Excl.GetHistogram().GetZaxis().SetTitle("Expected #mu = #sigma_{95%} / #sigma_{TH}")
  myTGraph_Excl.GetHistogram().GetZaxis().SetTitleSize(ztitlesize)
  myTGraph_Excl.GetHistogram().GetZaxis().SetTitleOffset(ztitleoffset)
  
  myTGraph_Excl.GetHistogram().SetMinimum(0.1)
  myTGraph_Excl.GetHistogram().SetMaximum(10)
  
  '''
  mycontoursarray=gROOT.GetListOfSpecials().FindObject("contours")
  print "mycontoursarray = ", mycontoursarray
  mytlist=mycontoursarray.At(0)
  print "mytlist = ", mytlist
  mytgraph=mytlist.First()

  #g1.SetMaximum(10.)
  #g1.SetMinimum(0.001)
  #g1.Draw("col2z")
  C6.cd(3)

  mytgraph.SetLineWidth(3)
  mytgraph.SetLineColor(kBlack)
  mytgraph.SetLineStyle(kDashed)
  mytgraph.Draw("LP")
  

  #myTGraph_sigma.SetMarkerStyle(20)

  C2.Modified()
  gPad.Modified()
  gPad.Update()

  '''
  #CMS_lumi(C6, 2, 0 )
  C6.Print("plots_v1/ExpLim_Signal_strenght_1.pdf","pdf")



  gStyle.SetOptTitle(0)


  C62=TCanvas("C62","C62",1000,900)

  C62.Update()
  C62.Modified()
  gPad.SetRightMargin(rightmargin)
  gPad.SetLeftMargin(leftmargin)
  gPad.SetBottomMargin(bottommargin)
  #gPad.SetTopMargin()

  gPad.SetLogz()
  #myTGraph_Excl.GetHistogram().SetContourLevel(0,0.5)
  #myTGraph_Excl.GetHistogram().SetContourLevel(1,1)
  #myTGraph_Excl.GetHistogram().SetContourLevel(2,1.5)
  myTGraph_ExclObs.GetHistogram().Draw("colz")
  
  myTGraph_ExclObs.GetHistogram().GetXaxis().SetTitle("M_{A} (GeV)")
  myTGraph_ExclObs.GetHistogram().GetXaxis().SetTitleSize(xtitlesize)
  myTGraph_ExclObs.GetHistogram().GetXaxis().SetTitleOffset(xtitleoffset)
  myTGraph_ExclObs.GetHistogram().GetYaxis().SetTitle("M_{H} (GeV)")
  myTGraph_ExclObs.GetHistogram().GetYaxis().SetTitleSize(ytitlesize)
  myTGraph_ExclObs.GetHistogram().GetYaxis().SetTitleOffset(ytitleoffset)
  myTGraph_ExclObs.GetHistogram().GetZaxis().SetTitle("Observed #mu = #sigma_{95%} / #sigma_{TH}")
  myTGraph_ExclObs.GetHistogram().GetZaxis().SetTitleSize(ztitlesize)
  myTGraph_ExclObs.GetHistogram().GetZaxis().SetTitleOffset(ztitleoffset)
  
  myTGraph_ExclObs.GetHistogram().SetMinimum(0.1)
  myTGraph_ExclObs.GetHistogram().SetMaximum(10)
  
  #myTGraph_sigma.SetMarkerStyle(20)

  #C2.Modified()
  gPad.Modified()
  gPad.Update()
  #CMS_lumi(C62, 2, 0 )
  C62.Print("plots_v1/ObsLim_Signal_strenght_1.pdf","pdf")

  

  f = TFile("Limit_Mu.root","recreate")
  myTGraph_Excl.GetHistogram().Write()
  myTGraph_ExclObs.GetHistogram().Write()
  f.Close()


if plot_syst:
  gStyle.SetOptTitle(0)
  C7=TCanvas("C7","C7",1000,900)

  C7.Update()
  C7.Modified()
  gPad.SetRightMargin(rightmargin)
  gPad.SetLeftMargin(leftmargin)
  gPad.SetBottomMargin(bottommargin)

  gPad.SetLogz()
  myTGraph_Excl.GetHistogram().Draw("colz")
  myTGraph_Excl.GetHistogram().SetMinimum(0.1)
  myTGraph_Excl.GetHistogram().SetMaximum(1000)
  gPad.Modified()
  gPad.Update()


  #CMS_lumi(C7, 2, 0 )

  ROOT.setTDRStyle()

  C7.Print("plots_v1/ExpLim_Signal_strenght_2.pdf","pdf")

  '''
  conts = gROOT.GetListOfSpecials().FindObject("contours")
  
  curv = conts[1]
  gc = curv.Clone()
  gc.Draw()
  '''
  


if plot_syst:
  gStyle.SetOptTitle(0)
  C_Syst=TCanvas("C_syst","C_syst",1000,900)

  C_Syst.Update()
  C_Syst.Modified()
  gPad.SetRightMargin(rightmargin)
  gPad.SetLeftMargin(leftmargin)
  gPad.SetBottomMargin(bottommargin)
  #gPad.SetTopMargin()
  gPad.SetLogz()
  #myTGraph_Excl.GetHistogram().SetContourLevel(0,0.5)
  #myTGraph_Excl.GetHistogram().SetContourLevel(1,1)
  #myTGraph_Excl.GetHistogram().SetContourLevel(2,1.5)
  myTGraph_Syst.GetHistogram().Draw("colz")
  myTGraph_Syst.GetHistogram().GetXaxis().SetTitle("M_{A} (GeV)")
  myTGraph_Syst.GetHistogram().GetXaxis().SetTitleSize(xtitlesize)
  myTGraph_Syst.GetHistogram().GetXaxis().SetTitleOffset(xtitleoffset)
  myTGraph_Syst.GetHistogram().GetYaxis().SetTitle("M_{H} (GeV)")
  myTGraph_Syst.GetHistogram().GetYaxis().SetTitleSize(ytitlesize)
  myTGraph_Syst.GetHistogram().GetYaxis().SetTitleOffset(ytitleoffset)
  myTGraph_Syst.GetHistogram().GetZaxis().SetTitle("expected exclusion on #mu")
  myTGraph_Syst.GetHistogram().GetZaxis().SetTitleSize(ztitlesize)
  myTGraph_Syst.GetHistogram().GetZaxis().SetTitleOffset(ztitleoffset)
  myTGraph_Syst.GetHistogram().SetMinimum(0.01)
  myTGraph_Syst.GetHistogram().SetMaximum(0.5)

  #myTGraph_sigma.SetMarkerStyle(20)


  CMSSWPoints = TGraph(12)
  CMSSWPoints.SetPoint(0,35,142)
  CMSSWPoints.SetPoint(1,30,329)
  #CMSSWPoints.SetPoint(2,142,575)
  CMSSWPoints.SetPoint(2,70,575)
  CMSSWPoints.SetPoint(3,378,875)
  CMSSWPoints.SetPoint(4,70,875)
  CMSSWPoints.SetPoint(5,142,329)
  CMSSWPoints.SetPoint(6,70,329)
  CMSSWPoints.SetPoint(7,378,575)
  CMSSWPoints.SetPoint(8,142,875)
  CMSSWPoints.SetPoint(9,575,875)
  CMSSWPoints.SetPoint(10,761,875)
  CMSSWPoints.SetPoint(11,50,200)
  CMSSWPoints.SetPoint(12,90,200)
  
  CMSSWPoints.SetMarkerStyle(21)
  CMSSWPoints.GetXaxis().SetLimits(0,1200)
  CMSSWPoints.SetMinimum(0)
  CMSSWPoints.SetMaximum(1200)

  CMSSWPoints.Draw("P")

  #C2.Modified()
  gPad.Modified()
  gPad.Update()
  C_Syst.Update();
  C_Syst.Print("plots_v1/SystErrorRatioWP.pdf","pdf")


  C_Syst.Update();
 

'''
f = TFile("limits.root","recreate")
myTGraph_SignalYield.Write()
myTGraph_Syst.Write()
f.Close()
'''


'''
C2=TCanvas("C2","C2",2000,1000)
C2.Divide(2)
ROOT.gStyle.SetPalette(52)
C2.cd(1)
myTGraph.GetXaxis().SetTitle("m_{bb}")
myTGraph.GetYaxis().SetTitle("m_{llbb}")
myTGraph.Draw("colz")
myTGraph.GetZaxis().SetRangeUser(0,10)
C2.cd(2).SetLogz()
myTGraph.Draw("colz")
C2.Print("Exp_Lim_BW_allBkg.png","png")
C2.Print("Exp_Lim_BW_allBkg.C","cxx")
'''


print "==> Now you have your plots of MH vs MA :-)"

###########
### FIN ###
###########
