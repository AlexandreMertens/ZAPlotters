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
//#include "tdrstyle.C"

TGraph* getExcludedArea(TH2D* limitHisto, double factor, int Triangle=0);
TGraph2D* getSignalStrength(TH2D* limitHisto, bool test=false);
TGraph2D* getTHxsec();
TH2D* getTHxsecHisto(TH2D* limitHisto);
TH2D* getHistoFromGraph(TGraph2D* graph, TH2D* grid, int Triangle=0);
TH2D* hideForbiddenRegion(TH2D* histo, bool pow10=false);
TGraph* getContour(TH2D* inputHisto, TCanvas* goodCanvas,  int Width=2, int Style=1);

TH2D* hideForbiddenRegion(TH2D* histo, bool pow10) {
        TH2D* toReturn = histo;//(TH2D*)histo->Clone("");
        for(int x=0;x<=histo->GetNbinsX();x++){
                for(int y=0;y<=histo->GetNbinsY()+1;y++){
                        double ma = histo->GetXaxis()->GetBinCenter(x);
                        double mh = histo->GetYaxis()->GetBinCenter(y);
                        if(fabs(mh-ma)<90){toReturn->SetBinContent(x,y, 0);
                        }else if(pow10 && toReturn->GetBinContent(x,y)!=0){
                           toReturn->SetBinContent(x,y, pow(10, toReturn->GetBinContent(x,y)) );
                        }
                }
        }
        return toReturn;
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

TGraph* get2SigmaContour(TH2D* inputHisto, TCanvas* goodCanvas, int Width, int Style){
       TCanvas* c1 = new TCanvas("temp", "temp",600,600); 

        TH2D* histo = (TH2D*)inputHisto->Clone("temp");
        for(int x=0;x<=histo->GetNbinsX();x++){
                for(int y=0;y<=histo->GetNbinsY()+1;y++){
                   if(histo->GetBinContent(x,y)<=0 || histo->GetBinContent(x,y)>=1E10)histo->SetBinContent(x,y, 1E9);
                }
        }

       double levels[] = {0.021, 0.022, 0.023};
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

       return NULL;
}

TGraph* getContourX(TH2D* inputHisto, TCanvas* goodCanvas, int Width, int Style, double X){
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
       EXCLUSION->Draw("CL same");
       }

       return NULL;
}

void DrawParam(){
  //text
  TPaveText *pave0 = new TPaveText(0.35,0.85,0.5,0.90,"brNDC");
  pave0->SetBorderSize(0);
  pave0->SetFillStyle(0);
  pave0->SetTextAlign(12);
  pave0->SetTextFont(62);
  pave0->SetTextSize(0.04);
  pave0->AddText("2HDM type-II");
  pave0->Draw("same");

  TPaveText *pave1 = new TPaveText(0.35,0.80,0.5,0.85,"brNDC");
  pave1->SetBorderSize(0);
  pave1->SetFillStyle(0);
  pave1->SetTextAlign(12);
  pave1->SetTextFont(62);
  pave1->SetTextSize(0.04);
  pave1->AddText("cos(#beta-#alpha) = 0.01");
  pave1->Draw("same");

  TPaveText *pave2 = new TPaveText(0.35,0.75,0.5,0.80,"brNDC");
  pave2->SetBorderSize(0);
  pave2->SetFillStyle(0);
  pave2->SetTextAlign(12);
  pave2->SetTextFont(62);
  pave2->SetTextSize(0.04);
  pave2->AddText("tan #beta = 1.5 ");
  pave2->Draw("same");

  }


void DrawParamLucia(){
       TLatex *tt2c = new TLatex(350,950,"2HDM type-II");
       tt2c->SetTextAlign(22); tt2c->SetTextSize(0.03);
       tt2c->SetTextAngle( 0 );

       TLatex *tt2b = new TLatex(350,900,"tan(#beta) = 1.5 ; cos(#beta - #alpha) = 0.01");
       tt2b->SetTextAlign(22); tt2b->SetTextSize(0.03);
       tt2b->SetTextAngle( 0 );

       TLatex *tt2 = new TLatex(350,850,"H #rightarrow Z(ll)A(bb)");
       tt2->SetTextAlign(22); //tt2->SetTextSize(0.1);
       tt2->SetTextAngle( 0 );

       TLatex *tt3 = new TLatex(950,500,"A #rightarrow Z(ll)H(bb)");
       tt3->SetTextAlign(22); //tt3->SetTextSize(0.1);
       tt3->SetTextAngle(90);

       TLatex *tt3b = new TLatex(900,500,"tan(#beta) = 1.5 ; cos(#beta - #alpha) = 0.01");
       tt3b->SetTextAlign(22); tt3b->SetTextSize(0.03);
       tt3b->SetTextAngle(90);

       TLatex *tt3c = new TLatex(850,500,"2HDM type-II");
       tt3c->SetTextAlign(22); tt3c->SetTextSize(0.03);
       tt3c->SetTextAngle(90);

       tt2c->Draw("same");
       tt2b->Draw("same");
       tt2->Draw("same");
       tt3->Draw("same");
       tt3b->Draw("same");
       tt3c->Draw("same");
       
}


void DrawParamXsec(){

 
  TLatex *tt22 = new TLatex(350,950,"H #rightarrow Z(ll)A(bb)");
  tt22->SetTextAlign(22); //tt22->SetTextSize(0.1);
  tt22->SetTextAngle( 0 );
  TLatex *tt33 = new TLatex(950,500,"A #rightarrow Z(ll)H(bb)");
  tt33->SetTextAlign(22); //tt33->SetTextSize(0.1);
  tt33->SetTextAngle(90);

  tt22->Draw("same");
  tt33->Draw("same");

}

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
  //pave2->AddText("Preliminary");

  TPaveText *pave3 = new TPaveText(0.5604027,0.951049,0.864094,0.9807692,"brNDC");;
  pave3->SetBorderSize(0);
  pave3->SetFillStyle(0);
  pave3->SetTextAlign(12);
  pave3->SetTextFont(42);
  pave3->SetTextSize(0.04);
  pave3->AddText("19.8 fb^{-1} (8 TeV)");

  framework2d = new TH2F("Graph","Graph",1,0,1000,1,0,1000);
  framework2d->SetStats(false);
  framework2d->SetTitle("");
  framework2d->GetXaxis()->SetTitle("M_{A} (GeV)");
  framework2d->GetYaxis()->SetTitle("M_{H} (GeV)");
  framework2d->GetYaxis()->SetTitleOffset(1.42);
  //framework2d->GetZaxis()->SetTitle("Observed Limit");
  framework2d->Draw("");


  h2->Draw("colz same");

  pave1->Draw("same");
  pave2->Draw("same");
  pave3->Draw("same");

  }



void DrawThisTH2Pval(TH2* h2){

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

  framework2d = new TH2F("Graph","Graph",1,0,1000,1,0,1000);
  framework2d->SetStats(false);
  framework2d->SetTitle("");
  framework2d->GetXaxis()->SetTitle("M_{bb} (GeV)");
  framework2d->GetYaxis()->SetTitle("M_{Zbb} (GeV)");
  framework2d->GetYaxis()->SetTitleOffset(1.42);
  //framework2d->GetZaxis()->SetTitle("Observed Limit");
  framework2d->Draw("");
  

  h2->Draw("colz same");

  pave1->Draw("same");
  pave2->Draw("same");
  pave3->Draw("same");
  
  }




void finalPlots(){


       TCutG* cutg = new TCutG("mycut",7);
       cutg->SetPoint(0,0    ,0);
       cutg->SetPoint(1,0    ,90);
       cutg->SetPoint(2,910, 1000);
       cutg->SetPoint(3,1000, 1000);
       cutg->SetPoint(4,1000, 910);
       cutg->SetPoint(5,90    ,0);
       cutg->SetPoint(6,0    ,0);
       //cutg->SetFillStyle(1001);
       cutg->SetFillColor(18);
       cutg->SetLineStyle(0);
       cutg->SetLineColor(18);

       TText *tt1 = new TText(500,500,"Kinematically forbidden");
       tt1->SetTextAlign(22); //tt1->SetTextSize(0.1);
       tt1->SetTextAngle(46);


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


/*
  // Limit On Nev

  TFile* f = new TFile("Limit_NeV.root");

  // Observed

  TCanvas* C_ev_obs = new TCanvas("C_ev_obs","C_ev_obs",600,600);
  C_ev_obs->SetLogz(true);
  C_ev_obs->SetRightMargin(0.17);

  TH2D* h_ev = f->Get("h0");
  h_ev->SetLabelSize(0.04,"Z");

  TH2D* finalPlot_ev = hideForbiddenRegion(h_ev, false);
  //finalPlot->Draw("colz");
  DrawThisTH2Pval(finalPlot_ev);


  // Expected

  TCanvas* C_ev_exp = new TCanvas("C_ev_exp","C_ev_exp",600,600);

  C_ev_exp->SetLogz(true);
  C_ev_exp->SetRightMargin(0.17);

  TH2D* h2_ev = f->Get("h3");
  h2_ev->SetLabelSize(0.04,"Z");

  TH2D* finalPlot2_ev = hideForbiddenRegion(h2_ev, false);
  //finalPlot2->Draw("colz");
  DrawThisTH2Pval(finalPlot2_ev);

*/

  // Limit On X-sec

  TFile* f = new TFile("Limit_XS_eff.root");

  // Observed

  TCanvas* C = new TCanvas("C","C",600,600);
  C->SetLogz(true);
  C->SetRightMargin(0.17);

  TH2D* h = f->Get("h24_lt");
  h->SetLabelSize(0.04,"Z");
  h->GetZaxis()->SetRangeUser(0.1,100);
  h->GetZaxis()->SetTitleSize(0.04);
  h->GetZaxis()->SetTitleOffset(1.30);


  TH2D* finalPlot = hideForbiddenRegion(h, false);
  //finalPlot->Draw("colz");
  DrawThisTH2Limit(finalPlot);
  DrawParamXsec();

  cutg->Draw("same f");
  tt1->Draw("same");

  

  Double_t limit_obs =  finalPlot->Interpolate(200,400);

  // Expected

  TCanvas* C2 = new TCanvas("C2","C2",600,600);

  C2->SetLogz(true);
  C2->SetRightMargin(0.17);

  TH2D* h2 = f->Get("h22_lt");
  h2->SetLabelSize(0.04,"Z");

  TH2D* finalPlot2 = hideForbiddenRegion(h2, false);
  finalPlot2->GetZaxis()->SetRangeUser(0.1,100);
  finalPlot2->GetZaxis()->SetTitle("Expected #sigma_{95%} (fb)");
  finalPlot2->GetZaxis()->SetTitleSize(0.04);
  finalPlot2->GetZaxis()->SetTitleOffset(1.45);

  //finalPlot2->GetZaxis()->SetTitle("Expected);
  //finalPlot2->Draw("colz");
  DrawThisTH2Limit(finalPlot2);
  DrawParamXsec();

  cutg->Draw("same f");
  tt1->Draw("same");


  Double_t limit_exp =  finalPlot2->Interpolate(200,400);

  // Signal Strenght

  TFile* f2 = new TFile("Limit_Mu.root");

  // Expected

  TCanvas* C_Mu = new TCanvas("C_Mu","C_Mu",600,600);
  C_Mu->Update();

  C_Mu->SetLogz(true);
  C_Mu->SetRightMargin(0.17);

  TH2D* h_Mu = f2->Get("h_Excl");
  h_Mu->GetZaxis()->SetRangeUser(0.1,100000);
  h_Mu->GetZaxis()->SetTitleOffset(1.5);
  h_Mu->SetLabelSize(0.04,"Z");

  TH2D* finalPlot_Mu = hideForbiddenRegion(h_Mu, false);

  cout << "title :  " << finalPlot_Mu->GetZaxis()->GetTitle() << endl; 

  cout << finalPlot_Mu->GetZaxis()->GetTitle() << endl;
  
  DrawThisTH2Limit(finalPlot_Mu);
  DrawParamLucia();  

  cutg->Draw("same f");
  tt1->Draw("same");

  TGraph* g_exp = getContour(finalPlot_Mu, C_Mu, 3, 7);
  //g_exp->Draw("CL same");

  C_Mu->Modified();
  C_Mu->Update();  


  TLegend* leg = new TLegend(0.3,0.13,0.6,0.18);
  leg->SetLineStyle(0);
  leg->SetLineColor(0);
  leg->SetFillStyle(0);
  leg->AddEntry(g_exp,"Exp. Excl.","l");
  leg->Draw();

 
  
  // Observed

  TCanvas* C2_Mu = new TCanvas("C2_Mu","C2_Mu",600,600);

  C2_Mu->SetLogz(true);
  C2_Mu->SetRightMargin(0.17);

  TH2D* h2_Mu = f2->Get("h_ExclObs");
  h2_Mu->GetZaxis()->SetRangeUser(0.1,100000);
  h2_Mu->GetZaxis()->SetTitleOffset(1.5);

  TH2D* finalPlot2_Mu = hideForbiddenRegion(h2_Mu, false);
  //finalPlot_Mu->GetZaxis()->SetTitle("Observed #sigma_{95%} (fb)");
  //finalPlot2_Mu->Draw("colz");
  DrawThisTH2Limit(finalPlot2_Mu);

  DrawParamLucia();

  cutg->Draw("same f");
  tt1->Draw("same");

  TGraph* g_obs = getContour(finalPlot2_Mu, C2_Mu, 3, 1);
  TGraph* g_exp = getContour(finalPlot_Mu, C2_Mu, 3, 7);

  //g_exp->Draw("CL same");
  //g_obs->Draw("CL same");

  TLegend* leg = new TLegend(0.3,0.13,0.6,0.23);
  leg->SetLineStyle(0);
  leg->SetLineColor(0);
  leg->SetFillStyle(0);
  leg->AddEntry(g_exp,"Exp. Excl.","l");
  leg->AddEntry(g_obs,"Obs. Excl.","l");
  leg->Draw();
  

  // P-Value


  TFile* f3 = new TFile("Limit_pvalue.root");

  TCanvas* C_pval = new TCanvas("C_pval","C_pval",600,600);

  C_pval->SetLogz(true);
  C_pval->SetRightMargin(0.17);

  TH2D* h_pval = f3->Get("h");

  TH2D* finalPlot_pval = hideForbiddenRegion(h_pval, false);
  //finalPlot2_Mu->Draw("colz");
  DrawThisTH2Pval(finalPlot_pval);

  //get2SigmaContour(finalPlot_pval, C_pval, 3, 1);



  // Efficiency map

  TCanvas* C_eff = new TCanvas("C_eff","C_eff",600,600);

  C_eff->SetLogz(true);
  C_eff->SetRightMargin(0.17);

  TH2D* h_eff = f->Get("h12");

  TH2D* finalPlot_eff = hideForbiddenRegion(h_eff, false);
  //finalPlot2_Mu->Draw("colz");
  DrawThisTH2Limit(finalPlot_eff);

  finalPlot_eff->GetZaxis()->SetTitle("efficiency");
  finalPlot_eff->GetZaxis()->SetTitleOffset(1.5);
  finalPlot_eff->GetZaxis()->SetTitleSize(0.04);

  // Limit vs TanBeta cosba
  TFile *f4 = new TFile("/home/fynu/amertens/Delphes_Analysis/2hdm/generation/sushi/SusHi-1.4.1/xsec_H_ZA_ll_bb_tautau_tanb_cosba.root");
  TCanvas* C_tbcba = new TCanvas("C_tbcba","C_tbcba",600,600);

  C_tbcba->SetLogz(true);
  C_tbcba->SetRightMargin(0.17);

  TH2D* h_tbcba = f4->Get("h_HZbbXsec");

  TH2D* finalPlot_tbcba = h_tbcba;

  finalPlot_tbcba->Draw("colz");

  cout << "limits : " << limit_exp << " " << limit_obs << endl;
 
  limit_obs = limit_obs/(0.067);
  limit_exp = limit_exp/(0.067); 

  cout << "limits : " << limit_exp << " " << limit_obs << endl;


  getContourX(finalPlot_tbcba, C_tbcba, 3, 1, limit_obs);
  getContourX(finalPlot_tbcba, C_tbcba, 3, 7, limit_exp);



  


}
