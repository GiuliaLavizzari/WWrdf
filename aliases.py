import os
import copy
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file

aliases = {}
aliases = OrderedDict()

bAlgo = 'DeepB'
bWP = '0.4184'

eleWP = 'mvaFall17V2Iso_WP90_SS_tthmva_70'
muWP  = 'cut_Tight_HWWW_tthmva_80'

mc = [skey for skey in samples if skey not in ('DATA', 'Fake_lep')]
SSsamples = [skey for skey in samples if skey not in ('WW','DY','Higgs')] # 'Top' shoud be here
OSsamples = [skey for skey in mc if skey in ('WW','DY','Higgs')]


# -------- tau veto
aliases['tauVeto_ww'] = {
    'expr': '(Sum(Tau_pt > 18 && abs(Tau_eta)<2.3 && Tau_decayMode &&sqrt( pow(Tau_eta - Lepton_eta[0], 2) + pow(abs(abs(Tau_phi - Lepton_phi[0])-3.1415)-3.1415, 2) ) >= 0.4 && sqrt( pow(Tau_eta - Lepton_eta[1], 2) + pow(abs(abs(Tau_phi - Lepton_phi[1])-3.1415)-3.1415, 2) ) >= 0.4) == 0)'
}

aliases['tauVeto_wz'] = {
    'expr': '(Sum(Alt(Lepton_pt,0,0.)>25 && Alt(Lepton_pt,1,0.)>20 && Alt(Lepton_pt,2,0.)>20 && Alt(Lepton_pt,3,0.)<10 && sqrt( pow(Tau_eta - Alt(Lepton_eta,0,-9999.), 2) + pow(abs(abs(Tau_phi - Alt(Lepton_phi,0,-9999.))-M_PI)-M_PI, 2) ) > 0.4 && sqrt( pow(Tau_eta - Alt(Lepton_eta,1,-9999.), 2) + pow(abs(abs(Tau_phi - Alt(Lepton_phi,1,-9999.))-M_PI)-M_PI, 2) ) > 0.4 && sqrt( pow(Tau_eta - Alt(Lepton_eta,2,-9999.), 2) + pow(abs(abs(Tau_phi - Alt(Lepton_phi,2,-9999.))-M_PI)-M_PI, 2) ) > 0.4) == 0)'
}

# -------- lepton misidentification SF
aliases['__chargeflip_w'] = {
    'linesToAdd': ['#include "/afs/cern.ch/user/g/glavizza/private/mkShapesRDF/examples/WWSR/mischarge_sf.cc"\n'],
    'samples': OSsamples
}
aliases['chargeflip_w'] = {
    'expr' : 'misID_sf(nLepton,Lepton_pdgId,Lepton_pt,Lepton_eta)',
    'samples': OSsamples
}

# -------- weights for VgS1
aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4',
    'samples': ['VgS1']
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4',
    'samples': ['VgS1']
}

# -------- gen-matching to prompt only (GenLepMatch2l matches to *any* gen lepton)
aliases['PromptGenLepMatch2l'] = {
    'expr': 'Alt(Lepton_promptgenmatched,0,0)*Alt(Lepton_promptgenmatched,1,0)',
    'samples': mc
}
aliases['PromptGenLepMatch3l'] = {
     'expr': 'Alt(Lepton_promptgenmatched,0,0)*Alt(Lepton_promptgenmatched,1,0)*Alt(Lepton_promptgenmatched,2,0)',
     'samples': mc
 }
aliases['PromptGenLepMatch4l'] = {
    'expr': 'Alt(Lepton_promptgenmatched,0,0)*Alt(Lepton_promptgenmatched,1,0)*Alt(Lepton_promptgenmatched,2,0)*Alt(Lepton_promptgenmatched,3,0)',
    'samples': mc
}

# -------- lepton WP
aliases['LepWPCut'] = {
    'expr': 'LepCut2l__ele_'+eleWP+'__mu_'+muWP,
}

# -------- fake lepton weights and variations
aliases['fakeW'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_2l2j',
    'samples': ['Fake_lep']
}

# ---------------------------- btagging (new)
#loose 0.1241
#medium 0.4184
#tight 0.7527
aliases['bVeto'] = {
    'expr': '(Sum(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Take(Jet_btagDeepB,CleanJet_jetIdx) > 0.4184) == 0)'
}

aliases['bReq'] = {
    'expr': '(Sum(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Take(Jet_btagDeepB,CleanJet_jetIdx) > 0.4184) >= 1)'
}
aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape,CleanJet_jetIdx)+1*(CleanJet_pt<=20 || abs(CleanJet_eta)>=2.5))))',
    'samples': mc
}
aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape,CleanJet_jetIdx)+1*(CleanJet_pt<=30 || abs(CleanJet_eta)>=2.5))))',
    'samples': mc
}
aliases['btagSF'] = {
    'expr': 'bVeto*bVetoSF + bReq*bReqSF',
    'samples': mc
}

# ---------------------------- SFweight (new)
aliases['SFweight_mod'] = {
    'expr': ' * '.join(['XSWeight',
                        'SFweight2l',
                        'LepSF2l__ele_' + eleWP + '__mu_' + muWP, 
                        'LepWPCut',
                        'METFilter_MC']),
    'samples': mc
}

aliases['samesign_requirement'] = {
    'expr': '(Alt(Lepton_pdgId,0,-9999) * Alt(Lepton_pdgId,1,-9999) > 0)',
    'samples':SSsamples
}

aliases['oppositesign_requirement'] = {
    'expr': 'chargeflip_w*(Alt(Lepton_pdgId,0,-9999) * Alt(Lepton_pdgId,1,-9999) < 0)',
    'samples':OSsamples
}

# --------------------------- ele/mu SF weights

aliases['SFweightEleUp'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Up',
    'samples': mc
}
aliases['SFweightEleDown'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Do',
    'samples': mc
}
aliases['SFweightMuUp'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Up',
    'samples': mc
}
aliases['SFweightMuDown'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Do',
    'samples': mc
}





########################################################################## 
############### my own weights for the nuisances #########################

#aliases['SFweightEleUp'] = {
#    'expr': 'LepSF2l__ele_'+eleWP+'__Up',
#    'samples': mc
#}
#aliases['SFweightEleDown'] = {
#    'expr': 'LepSF2l__ele_'+eleWP+'__Do',
#    'samples': mc
#}
#aliases['SFweightMuUp'] = {
#    'expr': 'LepSF2l__mu_'+muWP+'__Up',
#    'samples': mc
#}
#aliases['SFweightMuDown'] = {
#    'expr': 'LepSF2l__mu_'+muWP+'__Do',
#    'samples': mc
#}
#
#aliases['Jet_PUIDSF'] = {
#  'expr' : 'TMath::Exp(Sum((Jet_jetId>=2)*LogVec(Jet_PUIDSF_loose)))',
#  'samples': mc
#}
#
#aliases['Jet_PUIDSF_up'] = {
#  'expr' : 'TMath::Exp(Sum((Jet_jetId>=2)*LogVec(Jet_PUIDSF_loose_up)))',
#  'samples': mc
#}
#
#aliases['Jet_PUIDSF_down'] = {
#  'expr' : 'TMath::Exp(Sum((Jet_jetId>=2)*LogVec(Jet_PUIDSF_loose_down)))',
#  'samples': mc
#}




