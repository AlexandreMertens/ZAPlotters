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



void finalPlots(){

}

