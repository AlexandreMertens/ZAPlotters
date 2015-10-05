



void drawLimitContour(){


  TFile* f = new TFile("Limit_mu.root","update");
  TH2D *h_exp = f->Get("h0");

  TString name = "Obs";

  TCanvas* c = new TCanvas("c","test",0,0,600,600);
  h_exp->Draw("colz");

  Double_t contours[1];
  contours[0] = 1.0;


  TCanvas* c1 = new TCanvas("c1","Contour List",0,0,600,600);
  c1->SetRightMargin(0.15);
  c1->SetTopMargin(0.15);
  c1->Divide(5);
  c1->cd(1);

  h_exp->SetContour(1,contours);
  h_exp->Draw("CONT Z LIST");

  c1->Update();  

  TObjArray *conts = (TObjArray*)gROOT->GetListOfSpecials()->FindObject("contours");
  TList* contLevel = NULL;
  TGraph* curv     = NULL;
  TGraph* gc       = NULL;
  
  if (conts == NULL){
      printf("*** No Contours Were Extracted!\n");
      TotalConts = 0;
      return;
   } else {
      TotalConts = conts->GetSize();
      cout << "conts size : " << TotalConts << endl;
   }

  contLevel = (TList*) conts->At(0);

  printf("Contour %d has %d Graphs\n", 0, contLevel->GetSize());

  c1->cd(2);
  curv = (TGraph*)contLevel->First();
  gc = (TGraph*)curv->Clone();
  gc->Draw("AC"); 

  gc->GetYaxis()->SetRangeUser(0,800);
  gc->GetXaxis()->SetLimits(0,800);

  for(j = 0; j < contLevel->GetSize(); j++){

    c1->cd(j+2);
    gc = (TGraph*)curv->Clone();
    gc->Draw("AC");
    gc->SetName(name);
    if (j==1) gc->Write();    
    curv = (TGraph*)contLevel->After(curv); // Get Next graph

    }  

  c1->Update();
  
}

