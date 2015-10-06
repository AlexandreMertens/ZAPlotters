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
  pave0->AddText("#splitline{"+m1+"}{"+m2+"}" );
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

void Plotter_sbatb_tautau(){

  
  Int_t mA=150;
  TString strmA = "150";
  Int_t mH=350;
  TString strmH = "350";

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

  TString file_path_sig1 = "/home/fynu/lperrini/scratch/Analysis_i2HDM_HZAtautau_2015/CMSSW_5_3_15/src/UserCode/llvv_fwk/test/zhtautau/computeLimits/NewFC_AllFixed_Log_5_ttZ/cards_H350toZA_SB_Asvfit_shapes/LimitTree.root";

  Double_t limit, mh;
  Float_t quantileExpected;

  LumiEff=1.0;

  TFile* f_Sig1 = new TFile(file_path_sig1);
  TTree* tree_Sig1 = (TTree*) f_Sig1->Get("limit");

  TBranch *branch  = tree_Sig1->GetBranch("limit");
  TBranch *massA = tree_Sig1->GetBranch("mh");
  TBranch *quantileExp = tree_Sig1->GetBranch("quantileExpected");
  branch->SetAddress(&limit);
  massA->SetAddress(&mh);
  quantileExp->SetAddress(&quantileExpected);
/*
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

 
  Double_t limit_obs, limit_m2, limit_m1, limit_exp, limit_p1, limit_p2;

  cout << "Entries : " << tree_Sig1->GetEntries() << endl;

  for (Int_t i = 0; i < tree_Sig1->GetEntries(); i++){

    tree_Sig1->GetEntry(i);
    cout << " mA " << mh << " quantileExp " << quantileExpected  << endl;
    if (abs(mh - mA) < 1) {
      if (fabs(quantileExpected + 1.0) < 0.01) {limit_obs = limit /(0.067*LumiEff);}
      else if (fabs(quantileExpected-0.025) < 0.01) {limit_m2 = limit /(0.067*LumiEff);}
      else if (fabs(quantileExpected-0.16) < 0.01) {limit_m1 = limit /(0.067*LumiEff);cout << " m1" << endl;}
      else if (fabs(quantileExpected-0.5) < 0.01) {limit_exp = limit /(0.067*LumiEff);}
      else if (fabs(quantileExpected-0.84) < 0.01) {limit_p1 = limit /(0.067*LumiEff);}
      else if (fabs(quantileExpected-0.975) < 0.01) {limit_p2 = limit /(0.067*LumiEff);cout << " p2" << endl;}
      }
    } 


  // Limit vs TanBeta cosba
  TString Xsec_path = "/home/fynu/amertens/Delphes/delphes/condor/xsec_H_ZA_ll_bb_tautau_tanb_cosba_"+strmH+"_"+strmA+".root";
  TFile *f4 = new TFile(Xsec_path);
  TCanvas* C_tbcba = new TCanvas("C_tbcba","C_tbcba",600,600);

  gPad->SetGrid();

  C_tbcba->SetLogy(true);
  //C_tbcba->SetRightMargin(0.17);

  TH2D* h_tbcba = f4->Get("h_HZttXsec");

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
