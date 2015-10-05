###############
### imports ###
###############

import math
import os
from ROOT import *
from ROOT import TMath as tmath

#ROOT.gSystem.Load('CMS_label_C')
#ROOT.gSystem.Load("DrawCanvas_C")


###################
### Definitions ###
###################
'''
mAHypoList = [30,50,70,90,110,130,150]
mHHypoList = [325,375,425,475]

mHBin = {325:1,
         375:2,
         425:3,
         475:4}

mABin = {  30:1,
           50:2,
           70:3,
           90:4,
          110:5,
          130:6,
          150:7 }
'''

numDirs=36
numFiles=36
massResol=0.15
bin_width = 1.5
step_fraction = 2.0/3.0

run_combine = 1

xmax = 1200
ymax = 1200

myTGraph = TGraph2D(100)
#myTGraph.SetNpx(100)
#myTGraph.SetNpy(100)
myTGraph.SetName("p-value")
h = TH2D("h","p-value",500,0,xmax,500,0,ymax)
myTGraph.SetHistogram(h)

myTGraph_sigma = TGraph2D(100)
#myTGraph.SetNpx(100)
#myTGraph.SetNpy(100)
myTGraph_sigma.SetName("# sigma")
h_sig = TH2D("h_sig","# sigma",500,0,xmax,500,0,ymax)
myTGraph_sigma.SetHistogram(h_sig)

DataCards_path = "/nfs/user/acaudron/unblindedDatacards2HDMMCstatV2/Combined/"

mllbb=10
n=-1
for i in range(1,numDirs):
  dmllbb=massResol*mllbb*bin_width
  step_mllbb = dmllbb*step_fraction

  MH_dir = "Obs_pvalue_MH_"+str(int(mllbb))
  if run_combine == 1:
    mkdir_cmd = "mkdir "+MH_dir
    print mkdir_cmd
    rmdir_cmd = "rm -rf "+MH_dir
    os.system(rmdir_cmd)
    os.system(str(mkdir_cmd))
  mbb=10.0
  for j in range(1,numFiles):
    dmbb=massResol*mbb*bin_width
    step_mbb = dmbb*step_fraction
    print step_mbb
    yield_path = DataCards_path+str(int(mbb))+"_"+str(int(mllbb))+".txt"
    
    if (mbb < mllbb) and (mllbb > 126.0): 
      combine_cmd = "combine -M ProfileLikelihood --signif -m "+str(int(mbb))+" "+yield_path+" --toysFreq"
      #combine_cmd = "combine -M ProfileLikelihood --significance --pvalue -m "+str(int(mbb))+" "+yield_path
      try:
        file_path = MH_dir+"/higgsCombineTest.ProfileLikelihood.mA"+str(int(mbb))+".root"
        if run_combine == 1:
          os.system(str(combine_cmd))
          cp_cmd = "cp higgsCombineTest.ProfileLikelihood.mH"+str(int(mbb))+".root "+file_path
          os.system(str(cp_cmd))
        fList = TFile(str(file_path)) 
        mytree  = fList.Get("limit")
        for entry in mytree:
          print "p-value(",(i-1)*numDirs+(j-1) , ", " , int(mbb) , ", " , int(mllbb),") = ", mytree.limit
          n+=1
          myTGraph.SetPoint(n, mbb, mllbb, mytree.limit)
	  nSigma = tmath.sqrt(2)*tmath.ErfInverse(1-2*mytree.limit)
	  print mbb, mllbb, mytree.limit, nSigma
	  myTGraph_sigma.SetPoint(n, mbb, mllbb, nSigma)
      except:
        print 'no background events'


    mbb+=step_mbb

    print '##############################################'
    print 'mbb:', mbb, 'myTGraph size', myTGraph.GetN()
    print '##############################################'

  mllbb+=step_mllbb

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
'''
C=TCanvas("C","C",2000,1000)
C.Divide(2)
C.cd(1)
myTGraph.Draw("CONT")
C.cd(2)
myTGraph.Draw("surf1")
C.Print("Limits_data.png","png")
C.Print("Limits_data.C","cxx")
'''

'''
C=TCanvas("C","C",1000,1000)
ROOT.gStyle.SetPalette(52)
C.SetRightMargin(0.2)
C.SetLogz()
myTGraph.Draw("colz")
myTGraph.GetXaxis().SetTitle("m_{bb}")
myTGraph.GetYaxis().SetTitle("m_{llbb}")
#myTGraph.GetZaxis().SetTitle("Expected Exclusion (Events / GeV^{2})")
#myTGraph.GetZaxis().SetLimits(0.0001,10.0)
C.Update();
C.Modified();
C.Print("Exp_Lim_BW_allBkg_colz.png","png")
'''

gStyle.SetOptStat(0)



C2=TCanvas("C2","C2",600,600)
ROOT.gStyle.SetPalette(52)
#ROOT.setTDRStyle()
C2.SetTopMargin(0.05)
C2.SetRightMargin(0.2)
C2.SetLeftMargin(0.2)
#C2.SetBottomMargin(0.2)
C2.SetLogz()
myTGraph.GetHistogram().Draw("colz")
#myTGraph.SetTitle("p-value")
#myTGraph.GetXaxis().SetRangeUser(0,1200)
#myTGraph.GetYaxis().SetRangeUser(0,1200)
myTGraph.GetHistogram().GetXaxis().SetTitle("M_{bb} (GeV)")
'''
myTGraph.GetHistogram().GetXaxis().SetTitleSize(0.07)
myTGraph.GetHistogram().GetXaxis().SetTitleOffset(0.6)
'''
myTGraph.GetHistogram().GetYaxis().SetTitle("M_{Zbb} (GeV)")
'''
myTGraph.GetHistogram().GetYaxis().SetTitleSize(0.07)
myTGraph.GetHistogram().GetYaxis().SetTitleOffset(0.8)
'''
myTGraph.GetHistogram().GetZaxis().SetTitle("p-value")


f = TFile("Limit_pvalue.root","recreate")
myTGraph.GetHistogram().Write()
f.Close()


'''
myTGraph.GetHistogram().GetZaxis().SetTitleSize(0.07)
myTGraph.GetHistogram().GetZaxis().SetTitleOffset(0.6)
#myTGraph.GetZaxis().SetLimits(0.0001,10.0)
myTGraph.SetMarkerStyle(20); 
#myTGraph.GetZaxis().SetRangeUser(0.00000000001,0.5)
'''

'''
box1 = TBox(446,513,704,811)
box1.SetLineWidth(2)
box1.SetLineColor(kBlack)
box1.SetFillStyle(0)
#box1.SetFillColor(0)
box1.Draw()

box2 = TBox(72,222,114,350)
box2.SetLineWidth(2)
box2.SetLineColor(kBlack)
box2.SetFillStyle(0)
#box1.SetFillColor(0)
box2.Draw()
'''

#CMS_lumi(C2, 2, 0 )

gPad.Modified()
gPad.Update()


#C2.Print("plots_v1/pvalue_BW.pdf","pdf")
#C2.Print("plots_v1/pvalue_BW.C","cxx")

'''

C3=TCanvas("C3","C3",1200,1000)
#ROOT.gStyle.SetPalette(1)
C3.SetRightMargin(0.2)
C3.SetLeftMargin(0.2)
myTGraph_sigma.GetHistogram().Draw("colz")
myTGraph_sigma.SetTitle("# of #sigma")
#myTGraph.GetXaxis().SetRangeUser(0,1200)
#myTGraph.GetYaxis().SetRangeUser(0,1200)
myTGraph_sigma.GetHistogram().GetXaxis().SetTitle("M_{bb} (GeV)")
myTGraph_sigma.GetHistogram().GetXaxis().SetTitleSize(0.07)
myTGraph_sigma.GetHistogram().GetXaxis().SetTitleOffset(0.6)
myTGraph_sigma.GetHistogram().GetYaxis().SetTitle("M_{Zbb} (GeV)")
myTGraph_sigma.GetHistogram().GetYaxis().SetTitleSize(0.07)
myTGraph_sigma.GetHistogram().GetYaxis().SetTitleOffset(0.8)
myTGraph_sigma.GetHistogram().GetZaxis().SetTitle("p-value")
myTGraph_sigma.GetHistogram().GetZaxis().SetTitleSize(0.07)
myTGraph_sigma.GetHistogram().GetZaxis().SetTitleOffset(0.6)
#myTGraph.GetZaxis().SetLimits(0.0001,10.0)
#myTGraph.GetZaxis().SetRangeUser(0.00000000001,0.5)

C3.Print("plots_v1/NSigma.pdf","pdf")
C3.Print("plots_v1/NSigma.C","cxx")



signif99_263 = myTGraph_sigma.Interpolate(99,263)
signif104_270 = myTGraph_sigma.Interpolate(104,270)

print signif99_263, signif104_270

'''
'''
fList={}
treeList={}

binx=0
biny=0

###########
### Run ###
###########

for MH in mHHypoList:

    print "======= MH=", MH
    MHmin = str(MH-25)
    MHmax = str(MH+25)

    for MA in mAHypoList:

        print "MA=", MA
        filename = "MH_"+MHmin+"-"+MHmax+"/Mu/higgsCombineTest.ProfileLikelihood.mH"+str(MA)+".root"
        print "filename = ", filename

        fList[MH] = TFile(filename)
        mytree  = fList[MH].Get("limit")

        for entry in mytree:
            
            print "p-value = ", entry.limit
            myTH2D.SetBinContent(mABin[MA], #[tree.mh],
                                 mHBin[MH],
                                 entry.limit
                                 )

####################
### Colored plot ###
####################

C=TCanvas("C","C",1000,500)
C.Divide(2)
C.cd(1)
myTH2D.Draw("colz")
C.cd(2).SetLogz()
myTH2D.Draw("colz")
C.Draw()

################
### B&W plot ###
################

C2=TCanvas("C2","C2",1000,500)
C2.Divide(2)
ROOT.gStyle.SetPalette(52)
C2.cd(1)
myTH2D.Draw("colz")
C2.cd(2).SetLogz()
myTH2D.Draw("colz")
'''
print "==> Now you have your 2D p-value scans of MH vs MA :-)"

###########
### FIN ###
###########
