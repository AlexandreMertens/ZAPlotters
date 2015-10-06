#include "Fit/Fitter.h"


void ratioPlotsForCamille()
{

  // llbb_Mass_reco mfJetEta_450_600 mfJetEta_250_300 lljjMass_reco mjj_HighMass_reco drll_HighMass_reco

//   TString Variable = "bb_Mass_gen_cut";
//   TString Variable2 = "Zbb_Mass_reco";
   TString Variable = "bb_Mass_reco";
   TString x_title = "M_{bb}";
   Int_t N_Rebin = 6;

   Double_t yTopLimit = 3;

   TFile *f1 = TFile::Open("/home/fynu/amertens/storage/test/MG_PY6_/output/MG_PY6_/MG_PY6v9.root");
   TH1D *h1 = (TH1D*)f1->Get(Variable);
   h1->Sumw2();
//   h1->Add((TH1D*)f1->Get(Variable2));
   h1->SetDirectory(0);
   f1->Close();

   TFile *f2 = TFile::Open("/home/fynu/amertens/storage/test/aMCNLO_PY8_/output/aMCNLO_PY8_/aMCNLO_PY8v9.root");
   TH1D *h2 = (TH1D*)f2->Get(Variable);
   h2->Sumw2();
//   h2->Add((TH1D*)f2->Get(Variable2));
   h2->SetDirectory(0);
   f2->Close();

/*
   TFile *f3 = TFile::Open("/home/fynu/amertens/storage/test/MG_PY8_/output/MG_PY8_/MG_PY8.root");
   TH1D *h3 = (TH1D*)f3->Get(Variable);
   h3->SetDirectory(0);
   f3->Close();
*/
//   h1->Sumw2();
//   h2->Sumw2();
//   h3->Sumw2();

   cout << "MG_PY6      : " << h1->Integral() << endl;
   cout << "aMC@NLO_PY8 : " << h2->Integral() << endl;


   //h1->Scale(1.0/151456.0);
   //h2->Scale(1.0/1.45192e+09);
   //h2->Scale(1./12132.9);
   h1->Scale(1.0/h1->Integral());
   h2->Scale(1.0/h2->Integral());

   h1->Sumw2();
   h2->Sumw2();



//   h3->Scale(1.0/h3->Integral());

   h1->Rebin(N_Rebin);
   h2->Rebin(N_Rebin);
//   h3->Rebin(N_Rebin);

   TH1D *h1c = h1->Clone();
   h1c->Sumw2();
   TH1D *h2c = h2->Clone();
   h2c->Sumw2();

   TH1D *h1c2 = h1->Clone();
   h1c2->Sumw2();

   h2c->Add(h1c,-1);
   h2c->Divide(h1c);


   h1->SetTitle("");
   h2->SetTitle("");
//   h3->SetTitle("");


   h1->SetLineColor(kRed);
//   h3->SetLineColor(kGreen);

   TCanvas *c1 = new TCanvas("c1","example",600,700);
   TPad *pad1 = new TPad("pad1","pad1",0,0.5,1,1);
   pad1->SetBottomMargin(0);
   gStyle->SetOptStat(0);
   pad1->Draw();
   pad1->cd();
   h2->DrawCopy();
//   h3->DrawCopy("same");
   h1->GetYaxis()->SetLabelSize(0.1);
   h1->GetYaxis()->SetRangeUser(0, 0.2);// ,yTopLimit);
   h1->GetYaxis()->SetTitleSize(0.06);
   h1->GetYaxis()->SetTitleOffset(0.7);



   h1->Draw("same");

   TLegend *leg = new TLegend(0.6,0.7,0.89,0.89);
   leg->SetLineColor(0);
   leg->SetFillColor(0);
   //leg->AddEntry(h1,"t#bar{t} uncertainty","f");
   leg->AddEntry(h1,"MG5 + PY6","l");
   leg->AddEntry(h2,"aMC@NLO + PY8","l");
//   leg->AddEntry(h3,"MG5 + PY8","l");
   leg->Draw();

   
   c1->cd();

   TPad *pad2 = new TPad("pad2","pad2",0,0,1,0.5);
   pad2->SetTopMargin(0);
   pad2->SetBottomMargin(0.4);
   pad2->Draw();
   pad2->cd();
   pad2->SetGrid();
   h2->SetStats(0);
   h2->Divide(h1);
   //h2->SetMarkerStyle(21);
   h2->Draw("ep");
   h2->GetYaxis()->SetLabelSize(0.1);
   h2->GetYaxis()->SetRangeUser(-0.5, 2.5);// ,yTopLimit);
   h2->GetYaxis()->SetTitle("aMC@NLO+PY8 / MG5+PY6");
   h2->GetYaxis()->SetTitleSize(0.06);
   h2->GetYaxis()->SetTitleOffset(0.7);
   h2->GetXaxis()->SetLabelSize(0.1);
   h2->GetXaxis()->SetTitle(x_title);
   h2->GetXaxis()->SetTitleSize(0.16);
   h2->GetXaxis()->SetTitleOffset(0.9);
 //  Double_t matrix[4][4];
   h2->Fit("pol3","","",100.0,600.0);
   TF1 *ratio = h2->GetFunction("pol3");
   TVirtualFitter *fitter = TVirtualFitter::GetFitter();
   TMatrixD matrix(4,4,fitter->GetCovarianceMatrix());
   Double_t errorPar00 = fitter->GetCovarianceMatrixElement(0,0);
   Double_t errorPar11 = fitter->GetCovarianceMatrixElement(1,1);
   Double_t errorPar22 = fitter->GetCovarianceMatrixElement(2,2);
   Double_t errorPar33 = fitter->GetCovarianceMatrixElement(3,3);
//   c1->cd();

   matrix.Print();

   //const TMatrixDSym m = matrix;
   const TMatrixDEigen eigen(matrix);
   const TMatrixD eigenVal = eigen.GetEigenValues();
   const TMatrixD V = eigen.GetEigenVectors(); 

   cout << "V" << endl;

   V.Print();

   cout << "eigenVal" << endl;

   eigenVal.Print();



   cout << "Recomputed diag" << endl;

   //const TMatrixD Vt(TMatrixD::kTransposed,V);
   //const TMatrixD Vinv = V.Invert();
   const TMatrixD Vt(TMatrixD::kTransposed,V);
   //cout << "V-1" << endl;
   //Vinv.Print();
   cout << "Vt" << endl;
   Vt.Print();

   const TMatrixD VAVt = Vt*matrix*V;
   VAVt.Print();


   const TVectorD FittedParam(4);
   FittedParam(0) = fitter->GetParameter(0);
   FittedParam(1) = fitter->GetParameter(1);
   FittedParam(2) = fitter->GetParameter(2);
   FittedParam(3) = fitter->GetParameter(3);
   FittedParam.Print();


   //const TVectorD FittedParamNB(4);
   const TVectorD PNb = V*FittedParam;
   cout << "Pnb" << endl;
   PNb.Print();
  

   cout << " Generating other parameters values " << endl;

   cout <<" V " << V(0,0) << endl;

   TRandom3 r;
   const TVectorD NewP(4);

   TH1D *hist100 = new TH1D("h100","h100",200,-5,5);
   TH1D *hist200 = new TH1D("h200","h200",200,-5,5);
   TH1D *hist400 = new TH1D("h400","h400",200,-5,5);
   TH1D *hist600 = new TH1D("h600","h600",100,-5,5);
   TH1D *hist800 = new TH1D("h800","h800",100,-5,5);
   TH1D *hist1000 = new TH1D("h1000","h1000",100,-5,5);

   TH1D *histp0 = new TH1D("p0","p0",100,-0.2,0.3);
   TH1D *histp1 = new TH1D("p1","p1",100,0.0,0.01);
   TH1D *histp2 = new TH1D("p2","p2",100,-0.00001,0);
   TH1D *histp3 = new TH1D("p3","p3",100,0,0.000000002);



   for (Int_t i = 0; i< 500; i++){
     NewP(0) = r.Gaus(PNb(0),sqrt(eigenVal(0,0)));
     NewP(1) = r.Gaus(PNb(1),sqrt(eigenVal(1,1)));
     NewP(2) = r.Gaus(PNb(2),sqrt(eigenVal(2,2)));
     NewP(3) = r.Gaus(PNb(3),sqrt(eigenVal(3,3)));
     //NewP.Print();

     //FittedParam.Print();

     const TVectorD NewP2 = Vt*NewP;
     //NewP2.Print();

     histp0->Fill(NewP2(0));
     histp1->Fill(NewP2(1));
     histp2->Fill(NewP2(2));
     histp3->Fill(NewP2(3));



     TF1 *newFit=new TF1("test","[0]+x*[1]+[2]*pow(x,2)+[3]*pow(x,3)",0,1400);
     newFit->SetParameters(NewP2(0),NewP2(1),NewP2(2),NewP2(3));
     newFit->SetLineColor(kBlue);

     Double_t area=0;
     for(Int_t it=1; it < 16; it++){
       //cout << "bin : " << it << " " << h1c2->GetBinContent(it) << endl;
       area += h1c2->GetBinContent(it)*newFit->Eval(100*it+50);
       }
   
     //newFit->Draw("same");
     //cout <<"val: " << newFit->Eval(200) << endl;
     hist100->Fill(newFit->Eval(100)/area);
     hist200->Fill(newFit->Eval(200)/area);
     hist400->Fill(newFit->Eval(400)/area);
     hist600->Fill(newFit->Eval(600)/area);
     hist800->Fill(newFit->Eval(800)/area);
     hist1000->Fill(newFit->Eval(1000)/area);
     }

   c1->cd();
   TCanvas *c2 = new TCanvas("c2","c2",1000,1000);
   c2->cd();
   c2->Divide(3,2);
   c2->cd(1);
   hist100->Draw();
   c2->cd(2);
   hist200->Draw();
   c2->cd(3);
   hist400->Draw();
   c2->cd(4);
   hist600->Draw();
   c2->cd(5);
   hist800->Draw();
   c2->cd(6);
   hist1000->Draw();



Double_t m_100,m_200,m_400,m_600,m_800,m_1000;
Double_t s_100,s_200,s_400,s_600,s_800,s_1000;

hist100->Fit("gaus","","",0.3,0.5);
TVirtualFitter *fitter = TVirtualFitter::GetFitter();
m_100 = fitter->GetParameter(1);
s_100 = fitter->GetParameter(2);

hist200->Fit("gaus","","",0.5,0.7);
TVirtualFitter *fitter = TVirtualFitter::GetFitter();
m_200 = fitter->GetParameter(1);
s_200 = fitter->GetParameter(2);

hist400->Fit("gaus","","",0.9,1.1);
TVirtualFitter *fitter = TVirtualFitter::GetFitter();
m_400 = fitter->GetParameter(1);
s_400 = fitter->GetParameter(2);

hist600->Fit("gaus","","",1.1,1.3);
TVirtualFitter *fitter = TVirtualFitter::GetFitter();
m_600 = fitter->GetParameter(1);
s_600 = fitter->GetParameter(2);

hist800->Fit("gaus","","",0.5,2);
TVirtualFitter *fitter = TVirtualFitter::GetFitter();
m_800 = fitter->GetParameter(1);
s_800 = fitter->GetParameter(2);

hist1000->Fit("gaus","","",0.5,2.5);
TVirtualFitter *fitter = TVirtualFitter::GetFitter();
m_1000 = fitter->GetParameter(1);
s_1000 = fitter->GetParameter(2);


Double_t x[6],y[6],ym[6],yup[6],ydown[6];
x[0]=100; x[1]=200; x[2]=400;x[3]=600; x[4]=800; x[5]=1000;
yup[0]=ratio->Eval(100)+s_100;
yup[1]=ratio->Eval(200)+s_200;
yup[2]=ratio->Eval(400)+s_400;
yup[3]=ratio->Eval(600)+s_600;
yup[4]=ratio->Eval(800)+s_800;
yup[5]=ratio->Eval(1000)+s_1000;
ydown[0]=ratio->Eval(100)-s_100;
ydown[1]=ratio->Eval(200)-s_200;
ydown[2]=ratio->Eval(400)-s_400;
ydown[3]=ratio->Eval(600)-s_600;
ydown[4]=ratio->Eval(800)-s_800;
ydown[5]=ratio->Eval(1000)-s_1000;

y[0]=1+s_100/ratio->Eval(100);
y[1]=1+s_200/ratio->Eval(200);
y[2]=1+s_400/ratio->Eval(400);
y[3]=1+s_600/ratio->Eval(600);
y[4]=1+s_800/ratio->Eval(800);
y[5]=1+s_1000/ratio->Eval(1000);

ym[0]=-s_100/m_100;
ym[1]=-s_200/m_200;
ym[2]=-s_400/m_400;
ym[3]=-s_600/m_600;
ym[4]=-s_800/m_800;
ym[5]=-s_1000/m_1000;


TGraph* g = new TGraph(6,x,y);
TGraph* gm = new TGraph(6,x,ym);
TGraph* gup = new TGraph(6,x,yup);
TGraph* gdown = new TGraph(6,x,ydown);


TCanvas *c3 = new TCanvas("c3","c3",1000,1000);
c3->cd();

//gup->Draw("AC*");
//gdown->Draw("C*");
g->Draw("AC*");

gPad->SetBottomMargin(0.2);
gPad->SetLeftMargin(0.2);
gStyle->SetOptStat(0);

g->GetXaxis()->SetTitle("M_{Zbb}");
g->GetXaxis()->SetRangeUser(50,1100);
g->GetYaxis()->SetLabelSize(0.06);
g->GetYaxis()->SetTitle("Uncertainty");
g->GetYaxis()->SetTitleSize(0.06);
g->GetYaxis()->SetTitleOffset(1.4);
g->GetXaxis()->SetLabelSize(0.06);
g->GetXaxis()->SetTitleSize(0.06);
g->GetXaxis()->SetTitleOffset(1);
g->GetYaxis()->SetNdivisions(5);

TFile f("syst_zbx.root","recreate");
g->Write();
f.Close();


//gm->Draw("C*");
//g->SetMaximum(1);
//g->SetMinimum(-1);
//h2c->Draw("same");


TH1D *h22=h2->Clone();

TCanvas *c5 =  new TCanvas("c5","c5",1000,1000);

gPad->SetBottomMargin(0.2);
gPad->SetLeftMargin(0.2);
gStyle->SetOptStat(0);

h22->Draw();
h22->GetXaxis()->SetRangeUser(50,1100);
h22->GetYaxis()->SetLabelSize(0.06);
h22->GetYaxis()->SetTitleSize(0.06);
h22->GetYaxis()->SetTitleOffset(1.4);
h22->GetXaxis()->SetLabelSize(0.06);
h22->GetXaxis()->SetTitleSize(0.06);
h22->GetXaxis()->SetTitleOffset(1);

ratio->SetLineColor(kRed);
ratio->Draw("same");

gup->Draw("C");
gdown->Draw("C");


TLegend *leg = new TLegend(0.6,0.7,0.89,0.89);
leg->SetLineColor(0);
leg->SetFillColor(0);
leg->AddEntry(h22,"aMC@NLO / MG5","lep");
leg->AddEntry(ratio,"best fit","l");
leg->AddEntry(gup,"Syst Error (#pm 1 #sigma)","l");
leg->Draw();




TCanvas *c4 = new TCanvas("c4","c4",1000,1000);
c4->Divide(2,2);
c4->cd(1);
histp0->Draw();
c4->cd(2);
histp1->Draw();
c4->cd(3);
histp2->Draw();
c4->cd(4);
histp3->Draw();


}
