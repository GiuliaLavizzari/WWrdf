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

mcBSM     = [skey for skey in samples if 'lin' in skey or 'quad' in skey or 'sm' in skey]
mcEFT     = [skey for skey in samples if 'lin' in skey or 'quad' in skey] 
mcSM      = [skey for skey in samples if skey not in ('DATA', 'Fake_lep') and skey not in mcBSM]
mc        = [skey for skey in samples if skey not in ('DATA', 'Fake_lep') and skey not in mcEFT]
mcALL     = [skey for skey in samples if skey not in ('DATA', 'Fake_lep')]
OSsamples = [skey for skey in mc if skey in ('WW','DY','Higgs','qqH_htt','qqH_hww','ggH_hww','ggH_htt','ttH_hww','Top')]
SSsamples = [skey for skey in samples if skey not in OSsamples] # 'Top' shoud be here

print ("\nmcBSM", mcBSM)
print ("\nmcEFT", mcEFT)
print ("\nmc", mc)
print ("\nmcALL", mcALL)
print ("\nSSsamples", SSsamples)
print ("\nOSsamples", OSsamples)

# -------- tau veto
aliases['tauVeto_ww'] = {
    'expr': '(Sum(Tau_pt > 18 && abs(Tau_eta)<2.3 && Tau_decayMode &&sqrt( pow(Tau_eta - Lepton_eta[0], 2) + pow(abs(abs(Tau_phi - Lepton_phi[0])-3.1415)-3.1415, 2) ) >= 0.4 && sqrt( pow(Tau_eta - Lepton_eta[1], 2) + pow(abs(abs(Tau_phi - Lepton_phi[1])-3.1415)-3.1415, 2) ) >= 0.4) == 0)'
}

aliases['tauVeto_wz'] = {
    'expr': '(Sum(Alt(Lepton_pt,0,0.)>25 && Alt(Lepton_pt,1,0.)>20 && Alt(Lepton_pt,2,0.)>20 && Alt(Lepton_pt,3,0.)<10 && sqrt( pow(Tau_eta - Alt(Lepton_eta,0,-9999.), 2) + pow(abs(abs(Tau_phi - Alt(Lepton_phi,0,-9999.))-M_PI)-M_PI, 2) ) > 0.4 && sqrt( pow(Tau_eta - Alt(Lepton_eta,1,-9999.), 2) + pow(abs(abs(Tau_phi - Alt(Lepton_phi,1,-9999.))-M_PI)-M_PI, 2) ) > 0.4 && sqrt( pow(Tau_eta - Alt(Lepton_eta,2,-9999.), 2) + pow(abs(abs(Tau_phi - Alt(Lepton_phi,2,-9999.))-M_PI)-M_PI, 2) ) > 0.4) == 0)'
}

# -------- lepton misidentification SF
aliases['__chargeflip_w'] = {
    'linesToAdd': ['#include "/afs/cern.ch/user/g/glavizza/private/testmkshaped2D_2/mkShapesRDF/examples/2018/mischarge_sf.cc"\n'],
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
    'samples': mcALL
}
aliases['PromptGenLepMatch3l'] = {
     'expr': 'Alt(Lepton_promptgenmatched,0,0)*Alt(Lepton_promptgenmatched,1,0)*Alt(Lepton_promptgenmatched,2,0)',
     'samples': mcALL
 }
aliases['PromptGenLepMatch4l'] = {
    'expr': 'Alt(Lepton_promptgenmatched,0,0)*Alt(Lepton_promptgenmatched,1,0)*Alt(Lepton_promptgenmatched,2,0)*Alt(Lepton_promptgenmatched,3,0)',
    'samples': mcALL
}

# -------- lepton WP
aliases['LepWPCut'] = {
    'expr': 'LepCut3l__ele_'+eleWP+'__mu_'+muWP
}

# -------- top pt
aliases['Top_pTrw'] = {
    'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt(TMath::Exp(0.0615 - 0.0005 * topGenPt) * TMath::Exp(0.0615 - 0.0005 * antitopGenPt))) + (topGenPt * antitopGenPt <= 0.)',
    'samples': ['Top']
}
# -------- fake lepton weights and variations
aliases['fakeW'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_2l2j',
    'samples': ['Fake_lep']
}
aliases['fakeWEleUp'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_2l2jElUp',
    'samples': ['Fake_lep']
}
aliases['fakeWEleDown'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_2l2jElDown',
    'samples': ['Fake_lep']
}
aliases['fakeWMuUp'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_2l2jMuUp',
    'samples': ['Fake_lep']
}
aliases['fakeWMuDown'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_2l2jMuDown',
    'samples': ['Fake_lep']
}
aliases['fakeWStatEleUp'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_2l2jstatElUp',
    'samples': ['Fake_lep']
}
aliases['fakeWStatEleDown'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_2l2jstatElDown',
    'samples': ['Fake_lep']
}
aliases['fakeWStatMuUp'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_2l2jstatMuUp',
    'samples': ['Fake_lep']
}
aliases['fakeWStatMuDown'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_2l2jstatMuDown',
    'samples': ['Fake_lep']
}
#aliases['fakeW'] = {
#    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3l',
#    'samples': ['Fake_lep']
#}
#aliases['fakeWEleUp'] = {
#    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lElUp',
#    'samples': ['Fake_lep']
#}
#aliases['fakeWEleDown'] = {
#    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lElDown',
#    'samples': ['Fake_lep']
#}
#aliases['fakeWMuUp'] = {
#    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lMuUp',
#    'samples': ['Fake_lep']
#}
#aliases['fakeWMuDown'] = {
#    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lMuDown',
#    'samples': ['Fake_lep']
#}
#aliases['fakeWStatEleUp'] = {
#    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lstatElUp',
#    'samples': ['Fake_lep']
#}
#aliases['fakeWStatEleDown'] = {
#    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lstatElDown',
#    'samples': ['Fake_lep']
#}
#aliases['fakeWStatMuUp'] = {
#    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lstatMuUp',
#    'samples': ['Fake_lep']
#}
#aliases['fakeWStatMuDown'] = {
#    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lstatMuDown',
#    'samples': ['Fake_lep']
#}


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
    'samples': mcALL
}
aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape,CleanJet_jetIdx)+1*(CleanJet_pt<=30 || abs(CleanJet_eta)>=2.5))))',
    'samples': mcALL
}
aliases['btagSF'] = {
    'expr': 'bVeto*bVetoSF + bReq*bReqSF',
    'samples': mcALL
}



for shift in ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']:

    for targ in ['bVeto', 'bReq']:
        alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        alias['expr'] = alias['expr'].replace('btagSF_deepjet_shape', 'btagSF_deepjet_shape_up_%s' % shift)

        alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        alias['expr'] = alias['expr'].replace('btagSF_deepjet_shape', 'btagSF_deepjet_shape_down_%s' % shift)

    aliases['btagSF%sup' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
        'samples': mc
    }

    aliases['btagSF%sdown' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
        'samples': mc
    }


# ---------------------------- SFweight (new)
aliases['SFweight_mod'] = {
    'expr': ' * '.join(['XSWeight',
                        'SFweight3l',
                        'LepSF3l__ele_' + eleWP + '__mu_' + muWP, 
                        'LepWPCut',
                        'METFilter_MC']),
    'samples': mcALL
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
    'expr': 'LepSF3l__ele_'+eleWP+'__Up',
    'samples': mc
}
aliases['SFweightEleDown'] = {
    'expr': 'LepSF3l__ele_'+eleWP+'__Do',
    'samples': mc
}
aliases['SFweightMuUp'] = {
    'expr': 'LepSF3l__mu_'+muWP+'__Up',
    'samples': mc
}
aliases['SFweightMuDown'] = {
    'expr': 'LepSF3l__mu_'+muWP+'__Do',
    'samples': mc
}

# --------------------------- PU weights
aliases['Jet_PUIDSF'] = {
  'expr' : 'TMath::Exp(Sum((Jet_jetId>=2)*LogVec(Jet_PUIDSF_loose)))',
  'samples': mc
}

aliases['Jet_PUIDSF_up'] = {
  'expr' : 'TMath::Exp(Sum((Jet_jetId>=2)*LogVec(Jet_PUIDSF_loose_up)))',
  'samples': mc
}

aliases['Jet_PUIDSF_down'] = {
  'expr' : 'TMath::Exp(Sum((Jet_jetId>=2)*LogVec(Jet_PUIDSF_loose_down)))',
  'samples': mc
}

# --------------------------- EFT weights
##########################################################################
################## EFT reweighting weights ###############################

op = ["cW", "cHDD", "cHW", "cHWB", "cHbox", "cHj1", "cHj3", "cHl1", "cHl3", "cll1", "cjj11", "cjj31", "cjj18", "cjj38"]
# the following (ls) contains the operators in the same order as in the LHEReweightingWeight vector
ls = ['SM', 'cW_m1', 'cW', 'cHDD_m1', 'cHDD', 'cHW_m1', 'cHW', 'cHWB_m1', 'cHWB', 'cHbox_m1', 'cHbox', 'cHj1_m1', 'cHj1', 'cHj3_m1', 'cHj3', 'cHl1_m1', 'cHl1', 'cHl3_m1', 'cHl3', 'cll1_m1', 'cll1', 'cjj11_m1', 'cjj11', 'cjj31_m1', 'cjj31', 'cjj18_m1', 'cjj18', 'cjj38_m1', 'cjj38']
# te following (mix) contains all the operators with mixed terms as well, in the LHEReweightingWeight order
mix = ['SM', 'cW_m1', 'cW', 'cHDD_m1', 'cHDD', 'cHW_m1', 'cHW', 'cHWB_m1', 'cHWB', 'cHbox_m1', 'cHbox', 'cHj1_m1', 'cHj1', 'cHj3_m1', 'cHj3', 'cHl1_m1', 'cHl1', 'cHl3_m1', 'cHl3', 'cll1_m1', 'cll1', 'cjj11_m1', 'cjj11', 'cjj31_m1', 'cjj31', 'cjj18_m1', 'cjj18', 'cjj38_m1', 'cjj38', 'cW_cHDD', 'cW_cHW', 'cW_cHWB', 'cW_cHbox', 'cW_cHj1', 'cW_cHj3', 'cW_cHl1', 'cW_cHl3', 'cW_cll1', 'cW_cjj11', 'cW_cjj31', 'cW_cjj18', 'cW_cjj38', 'cHDD_cHW', 'cHDD_cHWB', 'cHDD_cHbox', 'cHDD_cHj1', 'cHDD_cHj3', 'cHDD_cHl1', 'cHDD_cHl3', 'cHDD_cll1', 'cHDD_cjj11', 'cHDD_cjj31', 'cHDD_cjj18', 'cHDD_cjj38', 'cHW_cHWB', 'cHW_cHbox', 'cHW_cHj1', 'cHW_cHj3', 'cHW_cHl1', 'cHW_cHl3', 'cHW_cll1', 'cHW_cjj11', 'cHW_cjj31', 'cHW_cjj18', 'cHW_cjj38', 'cHWB_cHbox', 'cHWB_cHj1', 'cHWB_cHj3', 'cHWB_cHl1', 'cHWB_cHl3', 'cHWB_cll1', 'cHWB_cjj11', 'cHWB_cjj31', 'cHWB_cjj18', 'cHWB_cjj38', 'cHbox_cHj1', 'cHbox_cHj3', 'cHbox_cHl1', 'cHbox_cHl3', 'cHbox_cll1', 'cHbox_cjj11', 'cHbox_cjj31', 'cHbox_cjj18', 'cHbox_cjj38', 'cHj1_cHj3', 'cHj1_cHl1', 'cHj1_cHl3', 'cHj1_cll1', 'cHj1_cjj11', 'cHj1_cjj31', 'cHj1_cjj18', 'cHj1_cjj38', 'cHj3_cHl1', 'cHj3_cHl3', 'cHj3_cll1', 'cHj3_cjj11', 'cHj3_cjj31', 'cHj3_cjj18', 'cHj3_cjj38', 'cHl1_cHl3', 'cHl1_cll1', 'cHl1_cjj11', 'cHl1_cjj31', 'cHl1_cjj18', 'cHl1_cjj38', 'cHl3_cll1', 'cHl3_cjj11', 'cHl3_cjj31', 'cHl3_cjj18', 'cHl3_cjj38', 'cll1_cjj11', 'cll1_cjj31', 'cll1_cjj18', 'cll1_cjj38', 'cjj11_cjj31', 'cjj11_cjj18', 'cjj11_cjj38', 'cjj31_cjj18', 'cjj31_cjj38', 'cjj18_cjj38']


### lin and quad components
aliases['rw_SM'] = {
    'expr' : 'LHEReweightingWeight[0]',
    'samples': mcBSM
}

for o in op:
    ip = ls.index(o)
    im = ls.index(o+'_m1')
    print (o, ip, im)

    aliases['rw_LIN_'+o] = {
        'expr' : '0.5*(LHEReweightingWeight['+str(ip)+'] - LHEReweightingWeight['+str(im)+'])',
        'samples': mcBSM
    }
    aliases['rw_QUAD_'+o] = {
        'expr' : '0.5*(LHEReweightingWeight['+str(ip)+'] + LHEReweightingWeight['+str(im)+'] - 2*LHEReweightingWeight[0])',
        'samples': mcBSM
    }


for i in range(len(op)):
    for j in range(len(op)):
        if j > i:
            term = op[i]+'_'+op[j]
            ix = mix.index(term)

            aliases['rw_MIX_'+term] = {
                'expr' : 'LHEReweightingWeight['+str(ix)+']',
                'samples': mcBSM
            }



