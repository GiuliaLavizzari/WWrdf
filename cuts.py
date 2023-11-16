# cuts
cuts = {}
# ----------------------------------
# Jet and MET VBS-like selections
preselections = 'nLepton>1 && Alt(CleanJet_pt,0,-9999.) >50 && Alt(CleanJet_pt,1,-9999.) >50 && mll > 20 && MET_pt > 30 && mjj > 500 && abs(detajj) > 2.5'
# lepton selections for WW
ww = 'Alt(Lepton_pt,0,0.)>25 && Alt(Lepton_pt,1,0.)>20 && Alt(Lepton_pt,2,0.)<10'
triple_charge = '(((abs(Alt(Lepton_pdgId,0,-9999))==11 && Alt(Electron_tightCharge,Lepton_electronIdx[0],-9999)==2) || abs(Alt(Lepton_pdgId,0,-9999))==13) \
               && ((abs(Alt(Lepton_pdgId,1,-9999))==11 && Alt(Electron_tightCharge,Lepton_electronIdx[1],-9999)==2) || abs(Alt(Lepton_pdgId,1,-9999))==13))'
# leppenfeld variable
zlep=' (abs((Alt(Lepton_eta,0,-9999.) - (Alt(CleanJet_eta,0,-9999.)+Alt(CleanJet_eta,1,-9999.))/2)/abs(detajj)) < 0.75) \
     &&(abs((Alt(Lepton_eta,1,-9999.) - (Alt(CleanJet_eta,0,-9999.)+Alt(CleanJet_eta,1,-9999.))/2)/abs(detajj)) < 0.75)'
# veto on Z mass window
zveto ='((abs(Alt(Lepton_pdgId,0,-9999)) * abs(Alt(Lepton_pdgId,1,-9999)) == 11*13) || (abs(mll - 91) > 15))'

# ----------------------------------
cuts['ssww_tri_tauVeto']=ww+'&& bVeto &&'+zlep+'&&'+zveto+'&&'+triple_charge+'&& tauVeto_ww'

