#include <string>
#include <vector>

#include "TROOT.h"
#include "TFile.h"
#include "TDirectory.h"
#include "TChain.h"
#include "TObject.h"
#include "TCanvas.h"
#include "TMath.h"
#include "TLegend.h"
#include "TGraph.h"
#include "TGraph2D.h"
#include "TH1.h"
#include "TH2.h"
#include "TH3.h"
#include "TTree.h"
#include "TF1.h"
#include "TCutG.h"
#include "TGraphErrors.h"
#include "TGraphAsymmErrors.h"
#include "TMultiGraph.h"
#include "TPaveText.h"
#include "TLatex.h"
#include "TStyle.h"
#include "TMarker.h"
#include "finalPlots.C"

TGraph* getContourFilledX(TH2D* inputHisto, TCanvas* goodCanvas, int Width, int Style, int FillStyle, double X){
       TCanvas* c1 = new TCanvas("temp", "temp",600,600);

       TH2D* histo = (TH2D*)inputHisto->Clone("temp");

       double levels[] = {X};
       histo->SetContour(1, levels);
       histo->Draw("CONT LIST");
       c1->Update();
       TObjArray* contours = (TObjArray*)gROOT->GetListOfSpecials()->FindObject("contours");
       Int_t ncontours     = contours->GetSize();
       TList *list         = (TList*)contours->At(0);
       delete c1;

       goodCanvas->cd();
       printf("list size = %i\n", (int)list->GetSize());
       if(list->GetSize()<=0)return new TGraph(0);

       for(unsigned int i=0;i<list->GetSize();i++){
       TGraph* EXCLUSION   = (TGraph*)(list->At(i)->Clone("copy"));
       EXCLUSION->SetLineColor(1);
       EXCLUSION->SetLineWidth(Width);
       EXCLUSION->SetLineStyle(Style);
       EXCLUSION->SetFillColor(kBlack);
       EXCLUSION->SetFillStyle(FillStyle);
       //EXCLUSION->Draw("CL F same");
       }

       return EXCLUSION;
}


void DrawMasses(TString m1, TString m2){
  //text
  TPaveText *pave0 = new TPaveText(0.7,0.7,0.93,0.93,"brNDC");
  pave0->SetBorderSize(0);
  pave0->SetFillStyle(0);
  pave0->SetTextAlign(12);
  pave0->SetTextFont(62);
  pave0->SetTextSize(0.04);
  pave0->AddText("#splitline{2HDM type-II}{#splitline{"+m1+"}{"+m2+"}}" );
  pave0->Draw("same");

  }

void DrawThis(){

  //text
  TPaveText *pave1 = new TPaveText(0.1375839,0.9545455,0.4412752,0.9842657,"brNDC");
  pave1->SetBorderSize(0);
  pave1->SetFillStyle(0);
  pave1->SetTextAlign(12);
  pave1->SetTextFont(62);
  pave1->SetTextSize(0.06);
  pave1->AddText("CMS");

  TPaveText *pave2 = new TPaveText(0.2701342,0.9458042,0.5738255,0.9755245,"brNDC");;
  pave2->SetBorderSize(0);
  pave2->SetFillStyle(0);
  pave2->SetTextAlign(12);
  pave2->SetTextFont(52);
  pave2->SetTextSize(0.04);
  pave2->AddText("Preliminary");

  TPaveText *pave3 = new TPaveText(0.5604027,0.951049,0.864094,0.9807692,"brNDC");;
  pave3->SetBorderSize(0);
  pave3->SetFillStyle(0);
  pave3->SetTextAlign(12);
  pave3->SetTextFont(42);
  pave3->SetTextSize(0.04);
  pave3->AddText("19.8 fb^{-1} (8 TeV)");

  framework2d = new TH2F("Graph","Graph",1,-1,1,1,0.1,10);
  framework2d->SetStats(false);
  framework2d->SetTitle("");
  framework2d->GetXaxis()->SetTitle("cos(#beta-#alpha)");
  framework2d->GetYaxis()->SetTitle("tan #beta");
  framework2d->GetYaxis()->SetTitleOffset(1.42);
  //framework2d->GetZaxis()->SetTitle("Observed Limit");
  framework2d->Draw("");
  
  pave1->Draw("same");
  pave2->Draw("same");
  pave3->Draw("same");

  }

void get_limits(Int_t i, TGraph2D* gr_obs, TGraph2D* gr_m2,TGraph2D* gr_m1,TGraph2D* gr_exp,TGraph2D* gr_p1,TGraph2D* gr_p2, TString strmH, Double_t mH, TString strmA, Double_t mA){

  TString file_path_sig1 = "/home/fynu/amertens/storage/CMSSW/CMSSW_6_1_1/src/HiggsAnalysis/CombinedLimit/python/v1_MH_"+strmH+"_Asymptotic_Unblind_Combined_/higgsCombineTest.Asymptotic.mA"+strmA+".root";

  Double_t limit;

  TGraph2D* myTGraph_ratio = new TGraph2D(10);
  myTGraph_ratio->SetName("Ratio CMSSW/Delphes");
  myTGraph_ratio->SetTitle("Ratio CMSSW/Delphes");
  myTGraph_ratio->SetPoint(0,35,142,0.411);
  myTGraph_ratio->SetPoint(1,10,200,0.838);
  myTGraph_ratio->SetPoint(2,110,200,0.796);
  myTGraph_ratio->SetPoint(3,30,329,0.826);
  myTGraph_ratio->SetPoint(4,70,329,0.897);
  myTGraph_ratio->SetPoint(5,70,575,0.955);
  myTGraph_ratio->SetPoint(6,70,875,0.907);
  myTGraph_ratio->SetPoint(7,142,329,0.925);
  myTGraph_ratio->SetPoint(8,142,875,0.927);
  myTGraph_ratio->SetPoint(9,378,575,0.891);
  myTGraph_ratio->SetPoint(10,378,875,0.911);
  myTGraph_ratio->SetPoint(11,575,875,0.890);
  myTGraph_ratio->SetPoint(12,761,875,0.849);
  myTGraph_ratio->SetPoint(13,50,1200,0.9);
  myTGraph_ratio->SetPoint(14,1200,1200,0.85);

  Double_t ratio = myTGraph_ratio->Interpolate(mA,mH);


  pathDelphesEff = "/home/fynu/amertens/storage/THDM/eff_v1/"+strmH+"_"+strmA+".root";
  DelphesFile = TFile(pathDelphesEff);
  TGraph2D* myG2D = DelphesFile.Get("Graph2D");
  Double_t eff = myG2D->Interpolate(int(mA),int(mH));

  Double_t lumi = 19.7;
  cout << "efficiency : " << eff << " ratio : " << ratio << endl;
  Double_t LumiEff = eff*ratio*lumi;

  TFile* f_Sig1 = new TFile(file_path_sig1);
  TTree* tree_Sig1 = (TTree*) f_Sig1->Get("limit");

  TBranch *branch  = tree_Sig1->GetBranch("limit");
  branch->SetAddress(&limit);

  branch->GetEntry(5);
  Double_t limit_obs = limit /(0.067*LumiEff);
  branch->GetEntry(0);
  Double_t limit_m2 = limit /(0.067*LumiEff);
  branch->GetEntry(1);
  Double_t limit_m1 = limit /(0.067*LumiEff);
  branch->GetEntry(2);
  Double_t limit_exp = limit /(0.067*LumiEff);
  branch->GetEntry(3);
  Double_t limit_p1 = limit /(0.067*LumiEff);
  branch->GetEntry(4);
  Double_t limit_p2 = limit /(0.067*LumiEff);

  gr_obs->SetPoint(i,mA,mH,limit_obs);
  gr_m2->SetPoint(i,mA,mH,limit_m2);
  gr_m1->SetPoint(i,mA,mH,limit_m1);
  gr_exp->SetPoint(i,mA,mH,limit_exp);
  gr_p1->SetPoint(i,mA,mH,limit_p1);
  gr_p2->SetPoint(i,mA,mH,limit_p2);

}


void Plotter_sbatb(){

  
  Int_t mA=163;
  TString strmA = "163";
  Int_t mH=329;
  TString strmH = "329";

  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(0);

  gStyle->SetPadLeftMargin(0.1191275);
  gStyle->SetPadRightMargin(0.05944056);
  gStyle->SetPadTopMargin(0.05944056);
  gStyle->SetPadBottomMargin(0.1206294);

  gStyle->SetTitleSize(0.04, "XYZ");
  gStyle->SetTitleXOffset(1.1);
  gStyle->SetTitleYOffset(1.45);
  gStyle->SetPalette(1);
  gStyle->SetNdivisions(505);
  gStyle->SetLabelSize(0.04,"XYZ");



  // Getting the limits from combine root files 

  TString file_path_sig1 = "/home/fynu/amertens/storage/CMSSW/CMSSW_6_1_1/src/HiggsAnalysis/CombinedLimit/python/v1_MH_"+strmH+"_Asymptotic_Unblind_Combined_/higgsCombineTest.Asymptotic.mA"+strmA+".root";

  Double_t limit;

/*
  TGraph2D* myTGraph_ratio = new TGraph2D(10);
  myTGraph_ratio->SetName("Ratio CMSSW/Delphes");
  myTGraph_ratio->SetTitle("Ratio CMSSW/Delphes");
  myTGraph_ratio->SetPoint(0,35,142,0.411);
  myTGraph_ratio->SetPoint(1,10,200,0.838);
  myTGraph_ratio->SetPoint(2,110,200,0.796);
  myTGraph_ratio->SetPoint(3,30,329,0.826);
  myTGraph_ratio->SetPoint(4,70,329,0.897);
  myTGraph_ratio->SetPoint(5,70,575,0.955);
  myTGraph_ratio->SetPoint(6,70,875,0.907);
  myTGraph_ratio->SetPoint(7,142,329,0.925);
  myTGraph_ratio->SetPoint(8,142,875,0.927);
  myTGraph_ratio->SetPoint(9,378,575,0.891);
  myTGraph_ratio->SetPoint(10,378,875,0.911);
  myTGraph_ratio->SetPoint(11,575,875,0.890);
  myTGraph_ratio->SetPoint(12,761,875,0.849);
  myTGraph_ratio->SetPoint(13,50,1200,0.9);
  myTGraph_ratio->SetPoint(14,1200,1200,0.85);

  Double_t ratio = myTGraph_ratio->Interpolate(mA,mH);
  
  pathDelphesEff = "/home/fynu/amertens/storage/THDM/eff_v1/"+strmH+"_"+strmA+".root";
  DelphesFile = TFile(pathDelphesEff);
  TGraph2D* myG2D = DelphesFile.Get("Graph2D");
  Double_t eff = myG2D->Interpolate(int(mA),int(mH));

  Double_t lumi = 19.7;
  cout << "efficiency : " << eff << " ratio : " << ratio << endl;
  Double_t LumiEff = eff*ratio*lumi;

  TFile* f_Sig1 = new TFile(file_path_sig1);
  TTree* tree_Sig1 = (TTree*) f_Sig1->Get("limit");

  TBranch *branch  = tree_Sig1->GetBranch("limit");
  branch->SetAddress(&limit);

  branch->GetEntry(5);
  Double_t limit_obs = limit /(0.067*LumiEff);
  branch->GetEntry(0);
  Double_t limit_m2 = limit /(0.067*LumiEff);
  branch->GetEntry(1);
  Double_t limit_m1 = limit /(0.067*LumiEff);
  branch->GetEntry(2);
  Double_t limit_exp = limit /(0.067*LumiEff);
  branch->GetEntry(3);
  Double_t limit_p1 = limit /(0.067*LumiEff);
  branch->GetEntry(4);
  Double_t limit_p2 = limit /(0.067*LumiEff);
*/
  TGraph2D* gr_m2=new TGraph2D(4);
  TGraph2D* gr_m1=new TGraph2D(4);
  TGraph2D* gr_exp=new TGraph2D(4);
  TGraph2D* gr_p1=new TGraph2D(4);
  TGraph2D* gr_p2=new TGraph2D(4);
  TGraph2D* gr_obs=new TGraph2D(4);

  get_limits(0, gr_obs, gr_m2, gr_m1, gr_exp, gr_p1, gr_p2, "329", 329, "142", 142);
  get_limits(1, gr_obs, gr_m2, gr_m1, gr_exp, gr_p1, gr_p2, "329", 329, "163", 163);
  get_limits(2, gr_obs, gr_m2, gr_m1, gr_exp, gr_p1, gr_p2, "378", 378, "123", 123);
  get_limits(3, gr_obs, gr_m2, gr_m1, gr_exp, gr_p1, gr_p2, "378", 378, "163", 163);



  Double_t limit_obs = gr_obs->Interpolate(150,350);
  Double_t limit_exp = gr_exp->Interpolate(150,350);
  Double_t limit_m2 = gr_m2->Interpolate(150,350);
  Double_t limit_m1 = gr_m1->Interpolate(150,350);
  Double_t limit_p1 = gr_p1->Interpolate(150,350);
  Double_t limit_p2 = gr_p2->Interpolate(150,350);




  // Limit vs TanBeta cosba
  //TString Xsec_path = "/home/fynu/amertens/Delphes/delphes/condor/xsec_H_ZA_ll_bb_tautau_tanb_cosba_"+strmH+"_"+strmA+".root";
  TString Xsec_path = "/home/fynu/amertens/Delphes/delphes/condor/xsec_H_ZA_ll_bb_tautau_tanb_cosba_350_150.root";
  TFile *f4 = new TFile(Xsec_path);
  TCanvas* C_tbcba = new TCanvas("C_tbcba","C_tbcba",600,600);

  gPad->SetGrid();

  C_tbcba->SetLogy(true);
  //C_tbcba->SetRightMargin(0.17);

  TH2D* h_tbcba = f4->Get("h_HZbbXsec");

  TGraph* g_obs = getContourFilledX(h_tbcba, C_tbcba, 3, 1,3645, limit_obs);
  TGraph* g_exp = getContourFilledX(h_tbcba, C_tbcba, 3, 7,0, limit_exp);


  Double_t contours[6];
  contours[0] = limit_m2;
  contours[1] = limit_m1;
  contours[2] = limit_exp;
  contours[3] = limit_p1;
  contours[4] = limit_p2;
  h_tbcba->SetContour(5, contours);

  TH2D* finalPlot_tbcba = h_tbcba;

  Int_t colors[] = {kYellow, kGreen, kGreen, kYellow, kWhite}; // #colors >= #levels - 1
  gStyle->SetPalette((sizeof(colors)/sizeof(Int_t)), colors);

  DrawThis();

  finalPlot_tbcba->Draw("cont list same");

  cout << "limits : " << limit_m2 << endl;
  cout << "limits : " << limit_m1 << endl;
  cout << "limits : " << limit_exp << endl;
  cout << "limits : " << limit_p1 << endl;
  cout << "limits : " << limit_p2 << endl;

  cout << "limits obs : " << limit_obs << endl;

   

//  TGraph* g_obs = getContourFilledX(finalPlot_tbcba, C_tbcba, 3, 1,3004, limit_obs);
//  TGraph* g_exp = getContourFilledX(finalPlot_tbcba, C_tbcba, 3, 7,4000, limit_exp);

  g_obs->Draw("CL F same");
  g_exp->Draw("CL F same");

  DrawMasses("M_{H} = 350 GeV", "M_{A} = 150 GeV");

  TGraph* g_yellow = new TGraph();
  g_yellow->SetFillColor(kYellow);
  TGraph* g_green = new TGraph();
  g_green->SetFillColor(kGreen);



  TLegend* leg = new TLegend(0.7,0.5,0.9,0.7);
  //leg->SetHeader("#splitline{THDM type II}{#splitline{M_{H} = 378}{M_{A} = 216}}");
  leg->SetLineColor(0);
  leg->SetFillColor(0);
  leg->AddEntry(g_obs,"Obs. Excl.","F");
  leg->AddEntry(g_exp,"Exp. Excl.","l");  
  leg->AddEntry(g_green,"1-sigma","F");
  leg->AddEntry(g_yellow,"2-sigma","F");
  leg->Draw();

  gPad->RedrawAxis("g"); // for "grid lines"

}
