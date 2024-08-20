# nuisances
# S.D. = Susan Dittmer's cfg https://github.com/latinos/PlotsConfigurations/blob/40d4ef1db7d96aea22acfc863d64b83966c12d32/Configurations/WW/FullRunII/Full2016_v9/inclusive/nuisances.py

nuisances = {}

# name of samples here must match keys in samples.py

##############################################################################################
################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity
# ------------------- lumi

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2016',
    'type': 'lnN',
    'samples': dict((skey, '1.010') for skey in mc if skey not in ['tVx'])
}

nuisances['lumi_Correlated'] = {
    'name': 'lumi_13TeV_correlated',
    'type': 'lnN',
    'samples': dict((skey, '1.006') for skey in mc if skey not in ['tVx'])
}
# ------------------- trigger
trig_syst = ['((TriggerEffWeight_2l_u)/(TriggerEffWeight_2l))*(TriggerEffWeight_2l>0.02) + (TriggerEffWeight_2l<=0.02)', '(TriggerEffWeight_2l_d)/(TriggerEffWeight_2l)']

nuisances['trigg'] = {
    'name': 'CMS_eff_hwwtrigger_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc)
}

# ------------------- fakes
#nuisances['fake_syst']  = {
#               'name'  : 'fake_syst',
#               'type'  : 'lnN',
#               'samples'  : {
#                   'Fake_lep' : '1.30',
#                   },
#}

nuisances['fake_syst_em'] = {
    'name': 'CMS_fake_syst_em',
    'type': 'lnN',
    'samples': {
    'Fake_lep_em': '1.3'
    },
}

nuisances['fake_syst_me'] = {
    'name': 'CMS_fake_syst_me',
    'type': 'lnN',
    'samples': {
    'Fake_lep_me': '1.3'
    },
}

nuisances['fake_ele'] = {
    'name': 'CMS_fake_e_2016',
    'kind': 'weight',
    'type': 'shape',
    'AsLnN': '0',
    'samples': {
        'Fake_lep': ['fakeWEleUp', 'fakeWEleDown'],
    }
}

nuisances['fake_ele_stat'] = {
    'name': 'CMS_fake_stat_e_2016',
    'kind': 'weight',
    'type': 'shape',
    'AsLnN': '0',
    'samples': {
        'Fake_lep': ['fakeWStatEleUp', 'fakeWStatEleDown']
    }
}

nuisances['fake_mu'] = {
    'name': 'CMS_fake_m_2016',
    'kind': 'weight',
    'type': 'shape',
    'AsLnN': '0',
    'samples': {
        'Fake_lep': ['fakeWMuUp', 'fakeWMuDown'],
    }
}

nuisances['fake_mu_stat'] = {
    'name': 'CMS_fake_stat_m_2016',
    'kind': 'weight',
    'type': 'shape',
    'AsLnN': '0',
    'samples': {
        'Fake_lep': ['fakeWStatMuUp', 'fakeWStatMuDown'],
    }
}

# ------------------- electron efficiency and energy scale
nuisances['eff_e'] = {
    'name': 'CMS_eff_e_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc if skey not in ['ggH_htt'])
}
nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2016',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'ElepTup',
    'mapDown': 'ElepTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['ggH_htt']),
    'folderUp': makeMCDirectory('ElepTup_suffix'),
    'folderDown': makeMCDirectory('ElepTdo_suffix'),
    'AsLnN': '1'
}


# ------------------- muon efficiency and energy scale
nuisances['eff_m'] = {
    'name': 'CMS_eff_m_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc if skey not in ['ggH_htt'])
}
nuisances['muonpt'] = {
    'name': 'CMS_scale_m_2016',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['ggH_htt']),
    'folderUp': makeMCDirectory('MupTup_suffix'),
    'folderDown': makeMCDirectory('MupTdo_suffix'),
    'AsLnN': '1'
}

# ------------------- JER
nuisances['JER'] = {
                'name': 'CMS_res_j_2016',
                'kind': 'suffix',
                'type': 'shape',
                'mapUp': 'JERup',
                'mapDown': 'JERdo',
                'samples': dict((skey, ['1','1']) for skey in mc if skey not in ['ggH_htt']),
                'folderUp' : makeMCDirectory('JERup_suffix'),
                'folderDown' : makeMCDirectory('JERdo_suffix'),
                'AsLnN'      : '1',
}

# ------------------- JES
# ----- from Susan's cfg
#jes_systs = ['JESAbsolute','JESAbsolute_2016','JESBBEC1','JESBBEC1_2016','JESEC2','JESEC2_2016','JESFlavorQCD','JESHF','JESHF_2016','JESRelativeBal','JESRelativeSample_2016']
#
#for js in jes_systs:
#    nuisances[js] = {
#        'name': 'CMS_scale_'+js,
#        'kind': 'suffix',
#        'type': 'shape',
#        'mapUp': js+'up',
#        'mapDown': js+'do',
#        'samples': dict((skey, ['1', '1']) for skey in mcSM), # FIXME should be mc
#        'folderUp': makeMCDirectory('RDF__JESup_suffix'),
#        'folderDown': makeMCDirectory('RDF__JESdo_suffix'),
#        'reweight' : ['btagSF'+js.replace('JES','jes')+'up/btagSF','btagSF'+js.replace('JES','jes')+'down/btagSF'],
#        'AsLnN': '0'
#    }

# ------------------- btagging
for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2016'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc if skey not in ['ggH_htt']),
    }

# ------------------- pile up
nuisances['PU']  = {
                'name'  : 'CMS_PU_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                    s : ['(puWeightUp/puWeight)',
                         '(puWeightDown/puWeight)'] for s in mc if s not in ['ggH_htt']}, 
                'AsLnN'      : '1',
}

# ------------------- pileup sf
puid_syst = ['Jet_PUIDSF_up/Jet_PUIDSF', 'Jet_PUIDSF_down/Jet_PUIDSF']

nuisances['jetPUID'] = {
    'name': 'CMS_PUID_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, puid_syst) for skey in mc if skey not in ['ggH_htt'])
}

# ------------------- parton shower (ISR,FSR)
nuisances['PS_ISR']  = {
    'name': 'PS_ISR',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['PSWeight[2]', 'PSWeight[0]']) for skey in mc if skey not in ['ggH_htt']),
}

nuisances['PS_FSR']  = {
    'name': 'PS_FSR',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['PSWeight[3]', 'PSWeight[1]']) for skey in mc if skey not in ['ggH_htt']),
}

# ------------------- Underlying Event (from S.D.)
nuisances['UE']  = {
                'name'  : 'UE_CP5',
                'skipCMS' : 1,
                'type': 'lnN',
                'samples': dict((skey, '1.015') for skey in mc if skey not in ['WW','WW']), 
}

# ------------------- XS
apply_on = {
    'Top': [
        '(topGenPt * antitopGenPt <= 0.) * 1.0816 + (topGenPt * antitopGenPt > 0.)',
        '(topGenPt * antitopGenPt <= 0.) * 0.9184 + (topGenPt * antitopGenPt > 0.)'
    ]
}

nuisances['singleTopToTTbar'] = {
    'name': 'singleTopToTTbar',
    'skipCMS': 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': apply_on
}
# ------------------- PDF
valuesggh = "1.032" #HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH','125.09','pdf','sm')
nuisances['pdf_Higgs_gg'] = {
    'name': 'pdf_Higgs_gg',
    'samples': {
        'ggH_hww': valuesggh,
        'ggH_htt': valuesggh,
    },
    'type': 'lnN',
}

values = "1.036" #HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ttH','125.09','pdf','sm')
nuisances['pdf_Higgs_ttH'] = {
    'name': 'pdf_Higgs_ttH',
    'samples': {
        'ttH_hww': values
    },
    'type': 'lnN',
}

valuesqqh = "1.021" #HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','pdf','sm')
nuisances['pdf_Higgs_qqbar'] = {
    'name': 'pdf_Higgs_qqbar',
    'type': 'lnN',
    'samples': {
        'qqH_hww': valuesqqh,
        'qqH_htt': valuesqqh,
    },
}

# pdf_qqbar
# pdf_qqbar accept

nuisances['pdf_Higgs_gg_ACCEPT'] = {
    'name': 'pdf_Higgs_gg_ACCEPT',
    'samples': {
        'ggH_hww': '1.006',
        'ggH_htt': '1.006',
    },
    'type': 'lnN',
}

#nuisances['pdf_gg_ACCEPT'] = {
#    'name': 'pdf_gg_ACCEPT',
#    'samples': {
#        'ggWW': '1.006',
#    },
#    'type': 'lnN',
#}

nuisances['pdf_Higgs_qqbar_ACCEPT'] = {
    'name': 'pdf_Higgs_qqbar_ACCEPT',
    'type': 'lnN',
    'samples': {
        'qqH_hww': '1.002',
        'qqH_htt': '1.002',
    },
}


# ------------------- QCD scale



# ------------------- SSWW pert ord
#nuisances['ssww_pert_ord'] = {
#    'name': 'ssww_pert_ord',
#    'type': 'lnN',
#    'samples': dict((skey, '1.1') for skey in mc if skey in ['SSWW']) 
#}
#
## ------------------- pdf weight
#nuisances['pdf_weight'] = { 
#    'name'  : 'pdf_weight_1718',
#    'kind'  : 'weight_envelope',
#    'type'  : 'shape',
#    'samples' :  { s: [' Alt(LHEPdfWeight,'+str(i)+', 1.)' for i in range(0,103)] for s in mc if s not in ['DPS']}, # if s not in ['DPS']}, # hoping DPS is now fixed
#    'AsLnN':  '1'
#}
##nuisances['pdf_weight_accept'] = {
##     'name'  : 'pdf_weight_1718_accept',
##     'kind'  : 'weight_envelope',
##     'type'  : 'shape',
##     'samples': { k : [ 'Alt(PDFweight_normalized,'+str(i)+', 1.)' for i in range(0,103) ] for k in ['SSWW', 'WZ_EWK']}
## }
#
## ------------------- QCD scale
#nuisances['QCD_scale_accept'] = {
#            'name'  : 'QCDscale_QCD_WW_accept',
#            'kind'  : 'weight',
#            'type'  : 'shape',
#            'samples': { k:["LHEScaleWeight[0]", "LHEScaleWeight[8]"] for k in mc }
#        }
#
# ------------------- MET (new, I completely did not have it before)
nuisances['met'] = {
    'name': 'CMS_scale_met_2016',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'METup',
    'mapDown': 'METdo',
    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['SSWW','WpWp_QCD','WZ_EWK']),
    'folderUp': makeMCDirectory('METup_suffix'),
    'folderDown': makeMCDirectory('METdo_suffix'),
    'AsLnN': '1'
}

# ------------------- rateparams
nuisances['norm_WZb']  = {
               'name'  : 'norm_WZb',
               'samples'  : {
                   'tVx' : '1.00',
                   },
               'type'  : 'rateParam',
              }

# ------------------- stats
autoStats = True
if autoStats:
    nuisances['stat'] = {
        'type': 'auto',
        'maxPoiss': '10',
        'includeSignal': '1',
        'samples': {}
}
# 'maxPoiss' =  Number of threshold events for Poisson modelling
# 'includeSignal' =  Include MC stat nuisances on signal processes (1=True, 0=False)

# -------------------------------

########################################################################################
################################ THEORY UNCERTAINTIES  #################################
# nuisances['QCDscale']  = {
#     'name'  : 'QCDscale',
#     'type'  : 'lnN',
#     'samples'  : {
#         'WZ'   : '1.10',
#         'ZZ'   : '1.10',
#         'VVV'  : '1.10',
#         'DPS'   : '1.10',
#         'Vg'    : '1.10' ,
#         'WpWp_EWK': '1.10' ,
#         'WW_strong': '1.10' ,
#     },
# }

# nuisances['QCDscale_gg_accept']  = {
#     'name'  : 'QCDscale_gg_accept',
#     'type'  : 'lnN',
#     'samples'  : {
#          'DY': '0.976/1.012' ,
#          'WpWp_EWK': '0.994/0.981' ,
#     },
#  }


# # pdf uncertainty

# nuisances['pdf']  = {
#     'name'  : 'pdf',
#     'type'  : 'lnN',
#     'samples'  : {
#         'WZ'   : '1.01',
#         'ZZ'   : '1.01',
#         'VVV'  : '1.01',
#         'DPS'   : '1.01',
#         'Vg'    : '1.01' ,
#         'WpWp_EWK': '1.01' ,
#         'WW_strong': '1.01' ,
#     },
# }


# ################################ BKG ESTIMATION UNCERTAINTIES  #################################

# nuisances['WZ_norm']  = {
#                'name'  : 'WZ_norm',
#                'samples'  : {
#                    'WZ'   : '1.3',
# 		},
#                'type'  : 'lnN',
# }

# #7% of uncertainty due to systematic uncertainties on simulations

# # 30% of global uncertainty
# nuisances['fake_syst']  = {
#                'name'  : 'fake_syst',
#                'type'  : 'lnN',
#                'samples'  : {
#                    'Fake_lep' : '1.30',
#                    },
# }



# # statistical fluctuation
# # on MC/data
# # "stat" is a special word to identify this nuisance
# # Use the following if you want to apply the automatic combine MC stat nuisances->Faster than bin-by-bin
# nuisances['stat']  = {
#               'type'  : 'auto',
#               'maxPoiss'  : '10',
#               'includeSignal'  : '1',
#               'samples' : {}
#              }




# # Differnt type of uncentainties: type->ln N: (modify only event yeld) use a lognorm distributions with sigma = uncertainty. For normalization rateParam
#                                         # can be used--> use a uniform distribution;
#                                       # Shape: modify not only the events yelds but the event selection too (the shape) will run the varied shapes
#                                              # according to the following two possible kinds
#                                 # kind-> weight: Use the specified weight to reweight events;
#                                        # tree: uses the provided alternative trees;
# # The MC statistics is a particular uncertainty: is caused by our finite statistics used to elaborate the template fits. Two approach: unfied and bin-by-bin (bbb)


