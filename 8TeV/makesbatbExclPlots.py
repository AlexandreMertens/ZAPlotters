from ROOT import *
import array
import os


#mllbb=500 575 761 662 286 216 248

#mllbbs = [142, 163, 188, 216, 248, 286, 329, 378, 435, 500, 575, 662, 761, 875, 1006]
mllbbs = [662]
numDirs=36

massResol=0.15
bin_width = 1.5
step_fraction = 2.0/3.0


myTGraph_ratio = TGraph2D(10)
myTGraph_ratio.SetName("Ratio CMSSW/Delphes")
myTGraph_ratio.SetPoint(0,35,142,0.411)
myTGraph_ratio.SetPoint(1,10,200,0.838)
myTGraph_ratio.SetPoint(2,110,200,0.796)
myTGraph_ratio.SetPoint(3,30,329,0.826)
myTGraph_ratio.SetPoint(4,70,329,0.897)
myTGraph_ratio.SetPoint(5,70,575,0.955)
myTGraph_ratio.SetPoint(6,70,875,0.907)
myTGraph_ratio.SetPoint(7,142,329,0.925)
myTGraph_ratio.SetPoint(8,142,875,0.927)
myTGraph_ratio.SetPoint(9,378,575,0.891)
myTGraph_ratio.SetPoint(10,378,875,0.911)
myTGraph_ratio.SetPoint(11,575,875,0.890)
myTGraph_ratio.SetPoint(12,761,875,0.849)
myTGraph_ratio.SetPoint(13,50,1200,0.9)
myTGraph_ratio.SetPoint(14,1200,1200,0.85)


XSFile_path = "/home/fynu/amertens/Delphes_Analysis/2hdm/generation/sushi/SusHi-1.4.1/xsec_v2.root"
XSFile = TFile(str(XSFile_path))
ggH_G2D = XSFile.Get("nnloXsec")
HZA_G2D = XSFile.Get("ZA_BR")
Abb_G2D = XSFile.Get("bb_BR")



pathDelphesEff = "/home/fynu/amertens/storage/THDM/eff_v1/"
fileList = os.listdir(pathDelphesEff)
myTGraph_eff = TGraph2D(len(fileList))

OutputFile = "BBPs.root"
f = TFile(str(OutputFile),"RECREATE")


i = 0
for feff in fileList:
  DelphesFile = TFile(pathDelphesEff+feff)
  myG2D = DelphesFile.Get("Graph2D")
  mbb_eff = feff.split("_")[1].split(".")[0]
  mllbb_eff = feff.split("_")[0]
  #print "eff : ", myG2D.Interpolate(int(mbb),int(mllbb))
  myTGraph_eff.SetPoint(i,int(mbb_eff),int(mllbb_eff),myG2D.Interpolate(int(mbb_eff),int(mllbb_eff)))
  i += 1


myTGraph_eff.SetPoint(i,662,580,myG2D.Interpolate(int(662),int(560)))
print "eff added : " , myG2D.Interpolate(int(662),int(560))

#myTGraph_eff.Draw("colz")

myTGraph_eff.SetDirectory(0)

ggH_G2D.SetDirectory(0)
HZA_G2D.SetDirectory(0)
Abb_G2D.SetDirectory(0)


for j in range(len(mllbbs)):
  mllbb = mllbbs[j]
  mbb=10.0

  TGAS_1 = TGraphAsymmErrors(0)
  TGAS_2 = TGraphAsymmErrors(0)

  myTG_0 = TGraph(5)
  myTG_1 = TGraph(5)
  myTG_2 = TGraph(5)
  myTG_3 = TGraph(5)
  myTG_4 = TGraph(5)
  myTG_5 = TGraph(5)

  myTG_Y = TGraph(5)


  n=-1
  for i in range(1,numDirs):
    dmbb=massResol*mbb*bin_width
    step_mbb = dmbb*step_fraction
  
    MH_dir_SigY = "v1_MH_"+str(int(mllbb))+"_Asymptotic_Unblind_Combined_SigYields_"
    MH_dir_Sig1 = "v1_MH_"+str(int(mllbb))+"_Asymptotic_Unblind_Combined_"
    file_path_SigY = MH_dir_SigY+"/higgsCombineTest.Asymptotic.mA"+str(int(mbb))+".root"
    file_path_Sig1 = MH_dir_Sig1+"/higgsCombineTest.Asymptotic.mA"+str(int(mbb))+".root"

    exp_limit = 100


    if mbb < mllbb :
      try:

        mA = int(mbb)
        mH = int(mllbb)
        gROOT.cd()
        #eff = myTGraph_eff.Interpolate(mbb,mllbb)
        #print "eff", eff

        eff = myTGraph_eff.Interpolate(int(mA),int(mH))
        print "eff", eff
        if eff == 0 : eff = myTGraph_eff.Interpolate(int(mA),int(mH)-0.1)
        if eff == 0 : eff = myTGraph_eff.Interpolate(int(mA),int(mH)+0.1)
        if eff == 0 : eff = myTGraph_eff.Interpolate(int(mA-0.1),int(mH))
        if eff == 0 : eff = myTGraph_eff.Interpolate(int(mA+0.1),int(mH))
        if eff == 0 : eff = myTGraph_eff.Interpolate(int(mA-0.1),int(mH)-0.01)
        if eff==0 and int(mA)<int(mH)-90 and int(mH)/int(mA)<5: print "eff=0", mA, mH
        ratio = myTGraph_ratio.Interpolate(int(mA),int(mH))

        f_Sig1=TFile(file_path_Sig1)
        tree_Sig1 = f_Sig1.Get("limit")

        f_SigY=TFile(file_path_SigY)
        tree_SigY = f_SigY.Get("limit")

        gROOT.cd()

        print "mbb : ", mbb

        print eff, ratio

        ggH_=ggH_G2D.Interpolate(int(mA),int(mH))
        if ggH_ == 0 : ggH_ = ggH_G2D.Interpolate(int(mA),int(mH)-0.1)
        if ggH_ == 0 : ggH_ = ggH_G2D.Interpolate(int(mA),int(mH)+0.1)
        if ggH_ == 0 : ggH_ = ggH_G2D.Interpolate(int(mA-0.1),int(mH))
        if ggH_ == 0 : ggH_ = ggH_G2D.Interpolate(int(mA+0.1),int(mH))
        if ggH_ == 0 : ggH_ = ggH_G2D.Interpolate(int(mA-0.1),int(mH)-0.01)
        if ggH_ == 0 and int(mA)<int(mH)-90 and int(mH)/int(mA)<5: print "ggH_=0", mA, mH
        HZA_=HZA_G2D.Interpolate(int(mA),int(mH))
        if HZA_ == 0 : HZA_ = HZA_G2D.Interpolate(int(mA),int(mH)-0.1)
        if HZA_ == 0 : HZA_ = HZA_G2D.Interpolate(int(mA),int(mH)+0.1)
        if HZA_ == 0 : HZA_ = HZA_G2D.Interpolate(int(mA-0.1),int(mH))
        if HZA_ == 0 : HZA_ = HZA_G2D.Interpolate(int(mA+0.1),int(mH))
        if HZA_ == 0 : HZA_ = HZA_G2D.Interpolate(int(mA-0.1),int(mH)-0.01)
        if HZA_ == 0 and int(mA)<int(mH)-90 and int(mH)/int(mA)<5: print "HZA_=0", mA, mH
        Abb_=Abb_G2D.Interpolate(int(mA),int(mH))
        if Abb_ == 0 : Abb_ = Abb_G2D.Interpolate(int(mA),int(mH)-0.1)
        if Abb_ == 0 : Abb_ = Abb_G2D.Interpolate(int(mA),int(mH)+0.1)
        if Abb_ == 0 : Abb_ = Abb_G2D.Interpolate(int(mA-0.1),int(mH))
        if Abb_ == 0 : Abb_ = Abb_G2D.Interpolate(int(mA+0.1),int(mH))
        if Abb_ == 0 : Abb_ = Abb_G2D.Interpolate(int(mA-0.1),int(mH)-0.01)
        if Abb_ == 0 and int(mA)<int(mH)-90 and int(mH)/int(mA)<5: print "Abb_=0", mA, mH


        #SignalYields = 19.7*eff*ratio*ggH_*HZA_*Abb_*0.06729*1000
        SignalYields = 19.7*eff*ratio

        print "SignalYields : " , SignalYields

        tree_Sig1.GetEntry(2)
        if tree_Sig1.limit > 0  and SignalYields > 0:
	  n+=1
	  myTG_2.SetPoint(n,int(mbb),tree_Sig1.limit/SignalYields)
	  TGAS_1.SetPoint(n,tree_Sig1.mh,tree_Sig1.limit/SignalYields)
          TGAS_2.SetPoint(n,tree_Sig1.mh,tree_Sig1.limit/SignalYields)
	  exp_limit = tree_Sig1.limit/SignalYields
          tree_Sig1.GetEntry(0)
	  TGAS_2.SetPointEYlow(n,abs(tree_Sig1.limit/SignalYields-exp_limit))
          tree_Sig1.GetEntry(4)
          TGAS_2.SetPointEYhigh(n,abs(tree_Sig1.limit/SignalYields-exp_limit))
          tree_Sig1.GetEntry(1)
          TGAS_1.SetPointEYlow(n,abs(tree_Sig1.limit/SignalYields-exp_limit))
          tree_Sig1.GetEntry(3)
          TGAS_1.SetPointEYhigh(n,abs(tree_Sig1.limit/SignalYields-exp_limit))


          tree_Sig1.GetEntry(5)
          myTG_5.SetPoint(n,int(mbb),tree_Sig1.limit/SignalYields) 
        
          tree_SigY.GetEntry(5)	
          myTG_Y.SetPoint(n,int(mbb),tree_SigY.limit)
      except:
        print 'no background events'

    mbb+=step_mbb


  Cname = "C_"+str(mllbb)
  C = TCanvas(Cname,Cname,1200,500)
  C.SetLeftMargin(0.2)
  C.SetBottomMargin(0.2)
  C.SetTitle(" ")
  #C.SetLogy()

  #TH1_4=myTG_4.GetHistogram()
  #TH1_4.SetFillColor(kYellow)

  '''
  myTG_2.SetFillColor(kYellow)
  myTG_2.SetFillStyle(1001)
  myTG_2.Draw('A E3')
  myTG_1.SetFillColor(kGreen)
  myTG_1.SetFillStyle(1001)
  myTG_1.Draw('E3 SAME')
  myTG_2.Draw("C")
  myTG_5.Draw("C*")
  '''

  TGAS_2.SetFillColor(kYellow)
  TGAS_2.SetFillStyle(1001)
  TGAS_2.SetLineWidth(0)
  TGAS_1.SetFillColor(kGreen)
  TGAS_1.SetFillStyle(1001)
  TGAS_1.SetLineWidth(0)

  myTG_2.SetLineColor(kBlack)
  myTG_2.SetLineStyle(9)
  myTG_2.SetLineWidth(2)

  myTG_5.SetLineColor(kBlack)
  myTG_5.SetLineWidth(2)

  title = "M_{H} = "+str(int(mllbb))
  TGAS_2.SetTitle(title)
  TGAS_2.GetXaxis().SetTitle("M_{A}")
  TGAS_2.GetXaxis().SetTitleSize(0.045)
  TGAS_2.GetXaxis().SetTitleOffset(0.8)
  TGAS_2.Draw('A E3')
  TGAS_1.Draw('E3')
  myTG_2.Draw("L")
  myTG_5.Draw("L")

  leg = TLegend(0.59,0.68,0.89,0.88)
  leg.SetLineColor(0)
  leg.SetFillColor(0)
  leg.AddEntry(TGAS_1,"CL_{s} Expected #pm 1 #sigma","F")
  leg.AddEntry(TGAS_2,"CL_{s} Expected #pm 2 #sigma","F")
  leg.AddEntry(myTG_2,"CL_{s} Expected","L")
  leg.AddEntry(myTG_5,"CL_{s} Observed","L")
  leg.Draw()

  OutputFile = "BBPs.root"
  f = TFile(str(OutputFile), "UPDATE")
  #f.Open()
  C.Write()
  C.Print("plots_v1/BBP_"+str(mllbb)+".pdf","pdf")
  f.Close()

##################
### THE END :( ###
##################
 
