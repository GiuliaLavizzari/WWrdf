
#ifndef MISCHARGE
#define MISCHARGE

#include <vector>

#include "TVector2.h"
#include "Math/Vector4Dfwd.h"
#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"

#include <iostream>
#include "ROOT/RVec.hxx"

using namespace ROOT;
using namespace ROOT::VecOps;

#include <iostream>

double misID_sf (
                 int   nLepton,
                 RVecI Lepton_pdgId,
                 RVecF Lepton_pt, 
                 RVecF Lepton_eta
                )
{
  unsigned nL = nLepton;
  if (nL < 2)
    return 0.;

  // more lepton selections
  std::vector<unsigned> iPromptL{};
  iPromptL.reserve(nL);

  for (unsigned iL{0}; iL != nL; ++iL) {
    unsigned absId{static_cast<unsigned>(std::abs(Lepton_pdgId[iL]))};
    if (absId != 11 && absId != 13)
      continue;
    iPromptL.push_back(iL);
  }

  if (iPromptL.size() < 2)
    return 0.; // false
  //if(Lepton_pdgId->At(iPromptL[0])*Lepton_pdgId->At(iPromptL[1])!=-11*11)
  //  return 0.;
  
  double chargeflip_rate[3]={5.53316e-05,3.72575e-04,1.14568e-03};
  //double chargeflip_rate[3]={4.65073e-05,2.44799e-04,9.31889e-04};
  //double sf[3]={1.18974,1.52196,1.22942};
  int idx1=0;
  int idx2=0;
  if(abs(Lepton_eta[iPromptL[0]])>=0 && abs(Lepton_eta[iPromptL[0]])<1.0){
    idx1=0;
  }else if(abs(Lepton_eta[iPromptL[0]])>=1.0 && abs(Lepton_eta[iPromptL[0]])<1.5){
    idx1=1;
  }else if(abs(Lepton_eta[iPromptL[0]])>=1.5 && abs(Lepton_eta[iPromptL[0]])<2.5){
    idx1=2;
  }

  if(abs(Lepton_eta[iPromptL[1]])>=0 && abs(Lepton_eta[iPromptL[1]])<1.0){
    idx2=0;
  }else if(abs(Lepton_eta[iPromptL[1]])>=1.0 && abs(Lepton_eta[iPromptL[1]])<1.5){
    idx2=1;
  }else if(abs(Lepton_eta[iPromptL[1]])>=1.5 && abs(Lepton_eta[iPromptL[1]])<2.5){
    idx2=2;
  }

  //double _sf1=sf[idx1];
  //double _sf2=sf[idx2];
  double _rate1=chargeflip_rate[idx1];
  double _rate2=chargeflip_rate[idx2];
  if (abs(Lepton_pdgId[iPromptL[0]])!=11){
    _rate1=0;
  }
  if (abs(Lepton_pdgId[iPromptL[1]])!=11){
    _rate2=0;
  }
  //double mis_id_sf= _rate1*_sf1*(1-_rate2*_sf2)+(1-_rate1*_sf1)*_rate2*_sf2;
  double mis_id_sf= _rate1*(1-_rate2)+(1-_rate1)*_rate2;
  return mis_id_sf;
}

#endif
