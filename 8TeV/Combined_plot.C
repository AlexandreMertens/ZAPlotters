
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
#include "TColor.h"

void DrawThisTH2Limit(TH2* h2){

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

  framework2d = new TH2F("Graph","Graph",1,145,600,1,0.5,10);
  framework2d->SetStats(false);
  framework2d->SetTitle("");
  framework2d->GetXaxis()->SetTitle("M_{H} (GeV)");
  framework2d->GetYaxis()->SetTitle("tan #beta");
  framework2d->GetYaxis()->SetTitleOffset(1.42);
  framework2d->GetZaxis()->SetTitle("#mu = #sigma_{excl} / #sigma_{TH}");
  framework2d->Draw("");


  h2->Draw("colz same");

  pave1->Draw("same");
  pave2->Draw("same");
  pave3->Draw("same");

  }


TGraph* getContour(TH2D* inputHisto, TCanvas* goodCanvas, int Width, int Style){
       TCanvas* c1 = new TCanvas("temp", "temp",600,600);

        TH2D* histo = (TH2D*)inputHisto->Clone("temp");
        for(int x=0;x<=histo->GetNbinsX();x++){
                for(int y=0;y<=histo->GetNbinsY()+1;y++){
                   if(histo->GetBinContent(x,y)<=0 || histo->GetBinContent(x,y)>=1E10)histo->SetBinContent(x,y, 1E9);
                }
        }

       double levels[] = {0.9, 1.0, 1.1};
       histo->SetContour(3, levels);
       histo->Draw("CONT LIST");
       c1->Update();
       TObjArray* contours = (TObjArray*)gROOT->GetListOfSpecials()->FindObject("contours");
       Int_t ncontours     = contours->GetSize();
       TList *list         = (TList*)contours->At(1);
       delete c1;

       goodCanvas->cd();
       printf("list size = %i\n", (int)list->GetSize());
       if(list->GetSize()<=0)return new TGraph(0);

       for(unsigned int i=0;i<list->GetSize();i++){
       TGraph* EXCLUSION   = (TGraph*)(list->At(i)->Clone("copy"));
       EXCLUSION->SetLineColor(1);
       EXCLUSION->SetLineWidth(Width);
       EXCLUSION->SetLineStyle(Style);
       EXCLUSION->Draw("CL same");
       }

       return EXCLUSION;
}

void set_plot_style()
{
    const Int_t NRGBs = 5;
    const Int_t NCont = 255;

    Double_t stops[NRGBs] = { 0.00, 0.34, 0.61, 0.84, 1.00 };
    Double_t red[NRGBs]   = { 0.00, 0.00, 0.87, 1.00, 0.51 };
    Double_t green[NRGBs] = { 0.00, 0.81, 1.00, 0.20, 0.00 };
    Double_t blue[NRGBs]  = { 0.51, 1.00, 0.12, 0.00, 0.00 };
    TColor::CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont);
    gStyle->SetNumberContours(NCont);
}

void Combined_plot(){

  // Style
  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(0);

  gStyle->SetPadLeftMargin(0.1191275);
  gStyle->SetPadRightMargin(0.1258389);
  gStyle->SetPadTopMargin(0.05944056);
  gStyle->SetPadBottomMargin(0.1206294);

  gStyle->SetTitleSize(0.04, "XYZ");
  gStyle->SetTitleXOffset(1.1);
  gStyle->SetTitleYOffset(1.45);
  gStyle->SetPalette(1);
  gStyle->SetNdivisions(505);
  gStyle->SetLabelSize(0.04,"XYZ");

  double tanB_step = 0.1;
  double mH_step = 5; 

  TFile* f = new TFile("Limit_XS_eff.root");

  TH2D* h_obs = f->Get("h24_lt");
  TH2D* h_exp = f->Get("h22_lt");

  TFile* f2 = new TFile("type1.root");
  TH2D* h_ggA = f2->Get("xs_ggA");
  TH2D* h_AZH = f2->Get("br_AZH");
  TH2D* h_Hbb = f2->Get("br_Hbb");

  int n=0;

  TGraph2D *g_exp = new TGraph2D(100);
  TGraph2D *g_obs = new TGraph2D(100);

  for (int mH = 145; mH <= 600; mH+=mH_step){
      for (double tanB = 0.5; tanB < 10; tanB+=tanB_step){  
          double mA = mH+100;
          double limit_obs = (1/1000.0) * h_obs->Interpolate(mA,mH);
          double limit_exp = (1/1000.0) * h_exp->Interpolate(mA,mH);
          double xs_tot = h_ggA->Interpolate(mH,tanB)*h_AZH->Interpolate(mH,tanB)*h_Hbb->Interpolate(mH,tanB)*0.067;
          double mu_obs = limit_obs/xs_tot;
          double mu_exp = limit_exp/xs_tot;
          g_exp->SetPoint(n,mH,tanB,mu_exp);
          g_obs->SetPoint(n,mH,tanB,mu_obs);
          n+=1;
      }
  }

  set_plot_style();
  TCanvas* C = new TCanvas("C","C",600,600);
  C->SetLogz(true);
  C->SetRightMargin(0.17);
  
  TH2D* mu_obs_histo = g_obs->GetHistogram();
  TH2D* mu_exp_histo = g_exp->GetHistogram();

  DrawThisTH2Limit(mu_obs_histo);
  mu_obs_histo->GetZaxis()->SetTitle("#mu = #sigma_{excl} / #sigma_{TH}");
  TGraph* g_exp_excl = getContour(mu_exp_histo, C, 3, 7);
  TGraph* g_obs_excl = getContour(mu_obs_histo, C, 3, 1);

  
  std::cout << "exp excl: " << g_exp_excl->GetN() << std::endl;

  std::cout << "obs excl: " << g_obs_excl->GetN() << std::endl;

  Double_t x_obs[20],y_obs[20];
  Double_t x_exp[20],y_exp[20];

  std::cout << "mH obs = ";
  for (int i=0; i < g_obs_excl->GetN(); i++){
    g_obs_excl->GetPoint(i,x_obs[i],y_obs[i]);
    std::cout << x_obs[i] << ", ";
  }
  std::cout << std::endl;

  std::cout << "tb obs = ";
  for (int i=0; i < g_obs_excl->GetN(); i++){
    g_obs_excl->GetPoint(i,x_obs[i],y_obs[i]);
    std::cout << y_obs[i] << ", ";
  }
  std::cout << std::endl;

  std::cout << "mH exp = ";
  for (int i=0; i < g_exp_excl->GetN(); i++){
    g_exp_excl->GetPoint(i,x_exp[i],y_exp[i]);
    std::cout << x_exp[i] << ", ";
  }
  std::cout << std::endl;

  std::cout << "tb exp = ";
  for (int i=0; i < g_exp_excl->GetN(); i++){
    g_exp_excl->GetPoint(i,x_exp[i],y_exp[i]);
    std::cout << y_exp[i] << ", ";
  }
  std::cout << std::endl;



  C->Modified();
  C->Update();

}
