
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


void Combined_plot(){


  double mA = 300;
  double mH = mA-100;
  double tanB = 1;  

  TFile* f = new TFile("Limit_XS_eff.root");

  // Observed

  TCanvas* C = new TCanvas("C","C",600,600);
  C->SetLogz(true);
  C->SetRightMargin(0.17);

  TH2D* h = f->Get("h24_lt");
  
  double limit = (1/1000.0) * h->Interpolate(mA,mH);

 
  TFile* f2 = new TFile("type2.root");
  TH2D* h_ggA = f2->Get("xs_ggA");
  TH2D* h_AZH = f2->Get("br_AZH");
  TH2D* h_Hbb = f2->Get("br_Hbb");

  double xs_tot = h_ggA->Interpolate(mH,tanB)*h_AZH->Interpolate(mH,tanB)*h_Hbb->Interpolate(mH,tanB)*0.067;
  

  double mu = limit/xs_tot;
  std::cout << "limit in xs : " << limit << std::endl; 
  std::cout << "cross-section : " << xs_tot << std::endl; 
  std::cout << mu << std::endl;


}
