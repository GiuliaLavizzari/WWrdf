# cuts
cuts = {}
# ----------------------------------
# Jet and MET VBS-like selections
preselections = 'Alt(CleanJet_pt,0,-9999.) >50 && Alt(CleanJet_pt,1,-9999.) >50 && mll > 20 && MET_pt > 30 && mjj > 500 && abs(detajj) > 2.5'

# ----------------------------------
# lepton selections for WW
ww = 'nLepton>1 && Alt(Lepton_pt,0,0.)>25 && Alt(Lepton_pt,1,0.)>20 && Alt(Lepton_pt,2,0.)<10'
#
triple_charge = '(((abs(Alt(Lepton_pdgId,0,-9999))==11 && Alt(Electron_tightCharge,Lepton_electronIdx[0],-9999)==2) || abs(Alt(Lepton_pdgId,0,-9999))==13) \
               && ((abs(Alt(Lepton_pdgId,1,-9999))==11 && Alt(Electron_tightCharge,Lepton_electronIdx[1],-9999)==2) || abs(Alt(Lepton_pdgId,1,-9999))==13))'
# leppenfeld variable
zlep=' (abs((Alt(Lepton_eta,0,-9999.) - (Alt(CleanJet_eta,0,-9999.)+Alt(CleanJet_eta,1,-9999.))/2)/abs(detajj)) < 0.75) \
     &&(abs((Alt(Lepton_eta,1,-9999.) - (Alt(CleanJet_eta,0,-9999.)+Alt(CleanJet_eta,1,-9999.))/2)/abs(detajj)) < 0.75)'
# veto on Z mass window
zveto ='((abs(Alt(Lepton_pdgId,0,-9999)) * abs(Alt(Lepton_pdgId,1,-9999)) == 11*13) || (abs(mll - 91) > 15))'

# ----------------------------------
# lepton selections for WZ
wz = 'nLepton>2 && Alt(Lepton_pt,3,0.)<10'
#
wz_zmass_one_two =  "(( abs(mll - 91) < abs(mllOneThree - 91) ) && ( abs(mll - 91) < abs(mllTwoThree - 91) )  &&  ( Alt(Lepton_pt,0,0.)>25 )  && ( Alt(Lepton_pt,1,0.)>10 ) && ( Alt(Lepton_pt,2,0.)>20 ))"
wz_zmass_two_three =  "(( abs(mllTwoThree - 91) < abs(mllOneThree - 91) ) && ( abs(mllTwoThree - 91) < abs(mll - 91) )  &&  ( Alt(Lepton_pt,1,0.)>25 )  && ( Alt(Lepton_pt,2,0.)>10 ) && ( Alt(Lepton_pt,0,0.)>20 ))"
wz_zmass_one_three =  "(( abs(mllOneThree - 91) < abs(mll - 91) ) && ( abs(mllOneThree - 91) < abs(mllTwoThree - 91) )  &&  ( Alt(Lepton_pt,0,0.)>25 ) && ( Alt(Lepton_pt,2,0.)>10 ) && ( Alt(Lepton_pt,1,0.)>20 ))"
wz_zmass = '(' +  wz_zmass_one_two + " || " + wz_zmass_two_three + " || " + wz_zmass_one_three + ')'
#
triple_charge_wz = '((abs(Alt(Lepton_pdgId,0,-9999))==11 && Alt(Electron_tightCharge,Lepton_electronIdx[0],-9999)==2) || abs(Alt(Lepton_pdgId,0,-9999))==13) && ((abs(Alt(Lepton_pdgId,1,-9999))==11 && Alt(Electron_tightCharge,Lepton_electronIdx[1],-9999)==2) || abs(Alt(Lepton_pdgId,1,-9999))==13) && ((abs(Alt(Lepton_pdgId,2,-9999))==11 && Alt(Electron_tightCharge,Lepton_electronIdx[2],-9999)==2) || abs(Alt(Lepton_pdgId,2,-9999))==13)'
# leppenfeld variable
zlep_wz='\
(abs((Alt(Lepton_eta,0,-9999.) - (Alt(CleanJet_eta,0,-9999.)+Alt(CleanJet_eta,1,-9999.))/2)/abs(detajj)) < 1.0) \
&&(abs((Alt(Lepton_eta,1,-9999.) - (Alt(CleanJet_eta,0,-9999.)+Alt(CleanJet_eta,1,-9999.))/2)/abs(detajj)) < 1.0) \
&&(abs((Alt(Lepton_eta,2,-9999.) - (Alt(CleanJet_eta,0,-9999.)+Alt(CleanJet_eta,1,-9999.))/2)/abs(detajj)) < 1.0)'
# Z tag
ztag ='WH3l_mlll > 100 \
&& abs(Alt(Lepton_pdgId,0,-9999) + Alt(Lepton_pdgId,1,-9999) + Alt(Lepton_pdgId,2,-9999)) < 20 \
&& ((abs(mll - 91) < 15 && Alt(Lepton_pdgId,0,-9999) * Alt(Lepton_pdgId,1,-9999) <0) \
|| (abs(mllOneThree - 91) < 15 && Alt(Lepton_pdgId,0,-9999) * Alt(Lepton_pdgId,2,-9999) < 0) \
|| (abs(mllTwoThree - 91) < 15 && Alt(Lepton_pdgId,1,-9999) * Alt(Lepton_pdgId,2,-9999) < 0))'

# ----------------------------------
cuts['ssww']=ww+'&& bVeto &&'+zlep+'&&'+zveto+'&&'+triple_charge+'&& tauVeto_ww'
cuts['btagCR']=ww+'&& bReq &&'+zlep+'&&'+zveto+'&&'+triple_charge+'&& tauVeto_ww'
cuts['WZ']= wz +' && ' + wz_zmass + ' && bVeto &&'+zlep_wz+'&&'+ztag+'&&'+triple_charge_wz+'&& tauVeto_wz'
cuts['WZb']= wz + ' && ' + wz_zmass + ' && bReq &&'+zlep_wz+'&&'+ztag+'&&'+triple_charge_wz+'&& tauVeto_wz'
