#include "TH1.h"
#include "TAttLine"
#include "TLine"
void bin_width()
{


Double_t mHgen[3] = {378,575,1158};
//mHgen = {200,350};//,350,400,600,800};
Double_t mAgen[9] = {53,123,248,329,378,500,575,662,875};
//TCanvas *c1 = new TCanvas("c1","efficiencies",200,10,700,500);
//TCanvas *c2 = new TCanvas("c2","X-sections",200,10,700,500);
//TCanvas *c3 = new TCanvas("c3","c3",200,10,700,500);

//c1->Divide(1,4);
//c2->Divide(1,4);
//c3->Divide(1,4);

TGraph *gr_mAw[3];
TGraph *gr_eff[6];
TString files[10][10];
TGraph *gr_mHw[3];

//for (Int_t i = 2; i < 6; i++){

static const Int_t sizeH = 3;

for (Int_t i = 1; i < sizeH+1/*.size()*/; i++){

  static const int sizeA = 9;
  cout << "size A : " << sizeA << endl; 
  Double_t eff[sizeA];
  Double_t mA_d[sizeA];
  Double_t mH_d[sizeA];
  Double_t mA_w[sizeA];
  Double_t mH_w[sizeA];

  for (Int_t j = 0; j < sizeA/*.size()*/; j++){
    //xsec_t[j] = xsec[i-2][j];
    //files[i][j]="/home/fynu/amertens/scratch/Analysis/thdm/histos/H_sba_95_";
    files[i-1][j]="/home/fynu/amertens/storage/THDM/histos/v1_";
    files[i-1][j]+=mHgen[i-1];
    files[i-1][j]+="_";
    files[i-1][j]+=mAgen[j];
    files[i-1][j]+="_stage_3.root";
    cout <<  files[i-1][j] << endl;

    if (mHgen[i-1]>mAgen[j]+90){

      TFile f(files[i-1][j],"read");
      TH1D* bb_Mass = (TH1D*) f.Get("bb_Mass");
      TH1D* llbb_Mass = (TH1D*) f.Get("llbb_Mass");
      eff[j] = bb_Mass->GetEntries()/(Double_t) 100000;
      cout << bb_Mass->GetEntries() << endl;

      //(Double_t) mA_d[j]-20, (Double_t) mA_d[j]+20);
      if (eff[j] > 0.01){
        TF1 * f1 = new TF1("gauss", "[0] / sqrt(2.0 * TMath::Pi()) / [2] * exp(-(x-[1])*(x-[1])/2./[2]/[2])", 0.5*mAgen[j], 1.5*mAgen[j]);
        //f1->SetParNames("Constant","Mean","Sigma");
        f1->SetParameters(bb_Mass->GetEntries(),bb_Mass->GetMean(),bb_Mass->GetRMS());
        bb_Mass->Fit("gauss");
        mA_w[j] = 3.0 * f1->GetParameter(2); ///mAgen[j];
        delete f1;
        }
      else mA_w[j] = 100;

      if (eff[j] > 0.01){
        TF1 * f2 = new TF1("gauss2", "[0] / sqrt(2.0 * TMath::Pi()) / [2] * exp(-(x-[1])*(x-[1])/2./[2]/[2])", 0.5*mHgen[i-1], 1.5*mHgen[i-1]);
        //f1->SetParNames("Constant","Mean","Sigma");
        f2->SetParameters(llbb_Mass->GetEntries(),llbb_Mass->GetMean(),llbb_Mass->GetRMS());
        llbb_Mass->Fit("gauss2");
        mH_w[j] = 3.0 * f2->GetParameter(2); // /(Double_t) mHgen[i-1];
        delete f2;
       }
      else mH_w[j] = 100;

      cout <<"mA masses :" <<  mAgen[j] << endl;
      cout <<"mA eff :" << eff[j] << endl;
      cout <<"mA width :" << mA_w[j]  << endl;
      }
    else 
	{
	mA_w[j] = 10000;
	mH_w[j] = 10000;
	}
    }

  TString title = "mH = ";
  title += mHgen[i-1];
//  c1->cd(6-i);
//  gPad->SetLogy();
//  gr_eff[7-i] = new TGraph(10,mAgen,eff);
//  gr_eff[7-i]->SetTitle(title);
//  gr_eff[7-i]->GetXaxis()->SetLimits(0,1000);
//  gr_eff[5-i]->Draw("A*");

//  c2->cd(6-i);
//  gPad->SetLogy();
/*
  gr_xsec[9-i] = new TGraph(10,mA_d,xsec_t);
  gr_xsec[9-i]->SetTitle(title);
  gr_xsec[9-i]->GetXaxis()->SetLimits(0,1000);
//  gr_xsec[5-i]->Draw("A*");
*/
  //c3->cd(6-i);

  Int_t size = sizeof(mAgen)/sizeof(mAgen[0]);
  cout << size << sizeof(mA_w)/sizeof(mA_w[0]) << endl;

  gr_mAw[sizeH-i] = new TGraph((Int_t) sizeof(mAgen)/sizeof(mAgen[0]),mAgen,mA_w);
  //TGraph* gr = new TGraph(5,mAgen,mA_w);
  gr_mAw[sizeH-i]->SetTitle(title);
  gr_mAw[sizeH-i]->GetXaxis()->SetLimits(0,1500);
  gr_mAw[sizeH-i]->Draw("A*");

  gr_mHw[sizeH-i] = new TGraph((Int_t) sizeof(mAgen)/sizeof(mAgen[0]),mAgen,mH_w);
  gr_mHw[sizeH-i]->SetTitle(title);
  gr_mHw[sizeH-i]->GetXaxis()->SetLimits(0,1500);

  }

/*
TCanvas *c1 = new TCanvas("c1","c1",200,10,700,500);
c1->Divide(1,6);
for (Int_t i = 2; i < 8; i++){
        c1->cd(8-i);
	//gPad->SetLogy();
        gr_eff[7-i]->GetYaxis()->SetLabelSize(0.12);
        gr_eff[7-i]->GetXaxis()->SetLabelSize(0.12);
        gr_eff[7-i]->Draw("A*");
        }
*/
/*
TCanvas *c2 = new TCanvas("c2","c2",200,10,700,500);
c2->Divide(1,4);
for (Int_t i = 2; i < 6; i++){
        c2->cd(6-i);
	gPad->SetLogy();
	gr_xsec[5-i]->GetYaxis()->SetLabelSize(0.07);
        gr_xsec[5-i]->GetXaxis()->SetLabelSize(0.07);
	//gr_xsec[5-i]->SetTitleSize(0.2);
        gr_xsec[5-i]->Draw("A*");
        }
*/

cout << "Plotting ... " << gr_mAw << endl;

TCanvas *c3 = new TCanvas("c3","mA width",200,10,700,900);
c3->Divide(1,sizeH);
TLine* line1 = new TLine(0,0,1200,540);
line1->SetLineWidth(3);
line1->SetLineColor(kRed);
for (Int_t i = 1; i < sizeH+1; i++){
	c3->cd(sizeH+1-i);
	gPad->SetBottomMargin(0.3);
	gPad->SetLeftMargin(0.2);
	gr_mAw[sizeH-i]->GetYaxis()->SetRangeUser(0,1200);
        gr_mAw[sizeH-i]->GetYaxis()->SetLabelSize(0.08);
	gr_mAw[sizeH-i]->GetYaxis()->SetNdivisions(5);
        gr_mAw[sizeH-i]->GetXaxis()->SetLabelSize(0.08);
	//gr_xsec[5-i]->SetTitleSize(0.2);
        gStyle->SetTitleH(0.15);
        gStyle->SetTitleY(0.8);
        gStyle->SetTitleX(0.7);
	gr_mAw[sizeH-i]->Draw("A*");
        gr_mAw[sizeH-i]->GetYaxis()->SetTitle("3 #times RMS (M_{bb})");
        gr_mAw[sizeH-i]->GetYaxis()->SetTitleSize(0.08);
	gr_mAw[sizeH-i]->GetXaxis()->SetTitle("M_{bb}");
        gr_mAw[sizeH-i]->GetXaxis()->SetTitleSize(0.08);
        gr_mAw[sizeH-i]->GetXaxis()->SetNdivisions(5);
        gr_mAw[sizeH-i]->GetXaxis()->SetRangeUser(0,1200);

        line1->Draw();

        cout << "pad " << sizeH-i << " drawn"<<endl;
	}

TCanvas *c4 = new TCanvas("c4","mH width",200,10,700,900);
c4->Divide(1,sizeH);



for (Int_t i = 1; i < sizeH+1; i++){
        c4->cd(sizeH+1-i);
	gPad->SetBottomMargin(0.3);
        gPad->SetLeftMargin(0.2);
        gr_mHw[sizeH-i]->GetYaxis()->SetRangeUser(0,1200);
        gr_mHw[sizeH-i]->GetYaxis()->SetLabelSize(0.08);
	gr_mHw[sizeH-i]->GetYaxis()->SetNdivisions(5);
	gr_mHw[sizeH-i]->GetXaxis()->SetLabelSize(0.08);
	gStyle->SetTitleH(0.15);
	gStyle->SetTitleY(0.8);
	gStyle->SetTitleX(0.7);
        gr_mHw[sizeH-i]->GetYaxis()->SetTitle("3 #times RMS (M_{Zbb})");
        gr_mHw[sizeH-i]->GetYaxis()->SetTitleSize(0.08);
        gr_mHw[sizeH-i]->GetXaxis()->SetTitle("M_{bb}");
        gr_mHw[sizeH-i]->GetXaxis()->SetTitleSize(0.08);
        gr_mHw[sizeH-i]->GetXaxis()->SetNdivisions(5);
        gr_mHw[sizeH-i]->GetXaxis()->SetRangeUser(0,1200);
        gr_mHw[sizeH-i]->Draw("A*");
	TLine* line2 = new TLine(0,0.45*mHgen[i-1],1200,0.45*mHgen[i-1]);
	line2->SetLineWidth(3);
	line2->SetLineColor(kRed);
	line2->Draw();

        }
}
