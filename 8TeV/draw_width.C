void draw_width(){


   TCanvas *c1 = new TCanvas("c1","Heaviest H width, M_{A} = 15 GeV",200,10,700,500);
   c1->SetLogy();
   c1->SetFillColor(0);
   c1->SetGrid();

   const Int_t n = 8;
   Double_t M[n]= {126, 200, 350, 500, 600, 700, 800, 900};
   Double_t W_15[n]= {8.12477269e-02, 1.36517184e+00, 1.19121726e+01, 4.40044052e+01, 7.74130955e+01, 1.22668305e+02, 1.81925299e+02, 2.57306382e+02};

   const Int_t n2 = 6;
   Double_t M2[n2] = {350, 500, 600, 700, 800, 900};
   Double_t W_200[n2] = {2.16288379e+00, 2.69462533e+01, 5.58588957e+01, 9.67469376e+01, 1.51721744e+02, 2.22878605e+02};

   const Int_t n3 = 4;
   Double_t M3[n3] = {600, 700, 800, 900};
   Double_t W_500[n3] = {9.10391108e+00, 2.11743549e+01, 4.72556689e+01, 8.96368631e+01};

   const Int_t n4 = 2;
   Double_t M4[n4] = {800, 900};
   Double_t W_700[n4] = { 1.47759627e+01, 2.74841698e+01};


   const Int_t nA = 14;
   Double_t M_A[nA]= {10, 11, 15, 23, 53, 142, 248, 329, 378, 435, 500, 662, 875, 1006 };
   Double_t W_A[nA]= { 3.59374088e-04, 5.89460809e-04, 1.07254526e-03, 1.68222604e-03, 3.39350655e-03, 7.98661276e-03, 1.50107862e-02, 4.75666163e-02, 5.56925012e+00, 8.12049501e+00, 1.02416303e+01, 1.44832862e+01, 1.92577931e+01, 2.19907445e+01};


   TCanvas *c1 = new TCanvas("c1","c1",1000,900);

   gPad->SetLogy();
   gPad->SetGridx();
   gPad->SetGridy();
   gStyle->SetOptTitle(0);

   gPad->SetBottomMargin(0.15);
   gPad->SetLeftMargin(0.15);

   TGraph *gr = new TGraph(n,M,W_15);
   gr->SetLineColor(kRed-8);
   gr->SetLineWidth(4);
   gr->SetMarkerColor(kRed-8);
   gr->SetMarkerStyle(21);
   gr->SetTitle("Heaviest H width, M_{A} = 15 GeV");
   gr->GetXaxis()->SetTitle("M_{H}");
   gr->GetYaxis()->SetTitle("#Gamma_{Tot}^{H}");
   gr->GetXaxis()->SetTitleSize(0.05);
   gr->GetYaxis()->SetTitleSize(0.05);
   gr->GetXaxis()->SetLabelSize(0.05);
   gr->GetYaxis()->SetLabelSize(0.05);
   gr->GetXaxis()->SetTitleOffset(1.2);
   gr->GetYaxis()->SetTitleOffset(1.2);
   gr->GetXaxis()->SetNdivisions(5);


   gr->Draw("ACP");


   TGraph *gr2 = new TGraph(n2,M2,W_200);
   gr2->SetLineColor(kRed-6);
   gr2->SetLineWidth(4);
   gr2->SetMarkerColor(kRed-6);
   gr2->SetMarkerStyle(21);
   //gr->SetTitle("Heaviest H width, M_{A} = 15 GeV");
   //gr->GetXaxis()->SetTitle("M_{H}");
   //gr->GetYaxis()->SetTitle("#Gamma_{Tot}");
   gr2->Draw("CP");


   TGraph *gr3 = new TGraph(n3,M3,W_500);
   gr3->SetLineColor(kRed-3);
   gr3->SetLineWidth(4);
   gr3->SetMarkerColor(kRed-3);
   gr3->SetMarkerStyle(21);
   gr3->Draw("CP");


   TGraph *gr4 = new TGraph(n4,M4,W_700);
   gr4->SetLineColor(kRed+2);
   gr4->SetLineWidth(4);
   gr4->SetMarkerColor(kRed+2);
   gr4->SetMarkerStyle(21);
   gr4->Draw("CP");

  TPaveText *pave1 = new TPaveText(0.2,0.7,0.4,0.9,"brNDC");
  pave1->SetBorderSize(0);
  pave1->SetFillStyle(0);
  pave1->SetTextAlign(12);
  pave1->SetTextFont(62);
  pave1->SetTextSize(0.04);
  pave1->AddText("#splitline{cos(#beta-#alpha) = 0.01}{tan #beta = 1.5}");
  pave1->Draw("same");

   TLegend *leg = new TLegend(0.6,0.2,0.89,0.4);
   leg->SetLineColor(0);
   leg->SetFillStyle(0);   
   leg->AddEntry(gr,"M_{A} = 15 GeV","l");
   leg->AddEntry(gr2,"M_{A} = 200 GeV","l");
   leg->AddEntry(gr3,"M_{A} = 500 GeV","l");
   leg->AddEntry(gr4,"M_{A} = 700 GeV","l");
   leg->Draw();


   TCanvas *c2 = new TCanvas("c2","c2",1000,900);
   gPad->SetLogy();
   gPad->SetGridx();
   gPad->SetGridy();
   gStyle->SetOptTitle(0);

   gPad->SetBottomMargin(0.15);
   gPad->SetLeftMargin(0.15);

   TGraph *grA = new TGraph(nA,M_A,W_A);
   grA->SetLineColor(kRed-8);
   grA->SetLineWidth(4);
   grA->SetMarkerColor(kRed-8);
   grA->SetMarkerStyle(21);
   grA->SetTitle("A width (GeV)");
   grA->GetXaxis()->SetTitle("M_{A}");
   grA->GetYaxis()->SetTitle("#Gamma_{Tot}");
   grA->Draw("ACP");
   grA->GetXaxis()->SetTitleSize(0.05);
   grA->GetYaxis()->SetTitleSize(0.05);
   grA->GetXaxis()->SetLabelSize(0.05);
   grA->GetYaxis()->SetLabelSize(0.05);
   grA->GetXaxis()->SetTitleOffset(1.2);
   grA->GetYaxis()->SetTitleOffset(1.2);
   grA->GetXaxis()->SetNdivisions(10);

}
