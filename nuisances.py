# nuisances

nuisances = {}

# name of samples here must match keys in samples.py

##############################################################################################
################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity
# ------------------- lumi

nuisances['lumi']  = {
    'name'  : 'lumi_13TeV_2018',
    'samples'  : {
        'SSWW'      : '1.025',
        'WpWp_QCD'  : '1.025',
        'WZ_EWK'    : '1.025',
        'WZ_QCD'    : '1.025',
        'ZZ'        : '1.025',
        'TTV'       : '1.025',
        'tZq'       : '1.025',
        'VgS1_H'    : '1.025',
        'VgS1_L'    : '1.025',
#        'WW'        : '1.025',  # data driven
#        'DY'        : '1.025',  # data driven
        'Higgs'     : '1.025',
        'VVV'       : '1.025',
    },
    'type'  : 'lnN',
}

# ------------------- trigger
trig_syst = ['((TriggerEffWeight_2l_u)/(TriggerEffWeight_2l))*(TriggerEffWeight_2l>0.02) + (TriggerEffWeight_2l<=0.02)', '(TriggerEffWeight_2l_d)/(TriggerEffWeight_2l)']

nuisances['trigg'] = {
    'name': 'CMS_eff_hwwtrigger_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc)
}

# ------------------- fakes
nuisances['fake_syst']  = {
               'name'  : 'fake_syst',
               'type'  : 'lnN',
               'samples'  : {
                   'Fake_lep' : '1.30',
                   },
}

# ------------------- electron efficiency and energy scale
nuisances['eff_e'] = {
    'name': 'CMS_eff_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc)
}
nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'ElepTup',
    'mapDown': 'ElepTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['SSWW','WpWp_QCD','WZ_EWK']), # did not process the up/do variations
    'folderUp': makeMCDirectory('ElepTup_suffix'),
    'folderDown': makeMCDirectory('ElepTdo_suffix'),
    'AsLnN': '1'
}


# ------------------- muon efficiency and energy scale
nuisances['eff_m'] = {
    'name': 'CMS_eff_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc)
}
nuisances['muonpt'] = {
    'name': 'CMS_scale_m_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['SSWW','WpWp_QCD','WZ_EWK']), # did not process the up/do variations
    'folderUp': makeMCDirectory('MupTup_suffix'),
    'folderDown': makeMCDirectory('MupTdo_suffix'),
    'AsLnN': '1'
}

# ------------------- JER
#nuisances['JER'] = {
#                'name': 'CMS_res_j_2018',
#                'kind': 'suffix',
#                'type': 'shape',
#                'mapUp': 'JERup',
#                'mapDown': 'JERdo',
#                'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['SSWW','WpWp_QCD','WZ_EWK']), # did not process the up/do variations
#                'folderUp' : makeMCDirectory('JERup_suffix'),
#                'folderDown' : makeMCDirectory('JERdo_suffix'),
#                'AsLnN'      : '1',
#}

# ------------------- JES
# ----- new way to deal with JES, is it correct?
#nuisances['JES'] = {
#                'name': 'CMS_jes_RDF_2018',
#                'kind': 'suffix',
#                'type': 'shape',
#                'mapUp': 'JESup',
#                'mapDown': 'JESdo',
#                'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['SSWW','WpWp_QCD','WZ_EWK']), # did not process the up/do variations
#                'folderUp' : makeMCDirectory('RDF__JESup_suffix'),
#                'folderDown' : makeMCDirectory('RDF__JESdo_suffix'),
#                'AsLnN'      : '1',
#}

# ----- old way to deal with JES, no longer working (no folders)
#jes_systs = ['JESAbsolute','JESAbsolute_2016','JESBBEC1','JESBBEC1_2016','JESEC2','JESEC2_2016','JESFlavorQCD','JESHF','JESHF_2016','JESRelativeBal','JESRelativeSample_2016']
#folderup = ""
#folderdo = ""
#
#for js in jes_systs:
#  if 'Absolute' in js:
#    folderup = makeMCDirectory('JESAbsoluteup_suffix')
#    folderdo = makeMCDirectory('JESAbsolutedo_suffix')
#  elif 'BBEC1' in js:
#    folderup = makeMCDirectory('JESBBEC1up_suffix')
#    folderdo = makeMCDirectory('JESBBEC1do_suffix')
#  elif 'EC2' in js:
#    folderup = makeMCDirectory('JESEC2up_suffix')
#    folderdo = makeMCDirectory('JESEC2do_suffix')
#  elif 'HF' in js:
#    folderup = makeMCDirectory('JESHFup_suffix')
#    folderdo = makeMCDirectory('JESHFdo_suffix')
#  elif 'Relative' in js:
##    folderup = makeMCDirectory('JESRelativeup_suffix')
##    folderdo = makeMCDirectory('JESRelativedo_suffix')
##  elif 'FlavorQCD' in js:
##    folderup = makeMCDirectory('JESFlavorQCDup_suffix')
##    folderdo = makeMCDirectory('JESFlavorQCDdo_suffix')
##
##  nuisances[js] = {
##      'name': 'CMS_scale_'+js,
##      'kind': 'suffix',
##      'type': 'shape',
##      'mapUp': js+'up',
##      'mapDown': js+'do',
##      'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['SSWW','WpWp_QCD','WZ_EWK']),
##      'folderUp': folderup,
##      'folderDown': folderdo,
##      'AsLnN': '1'
##  }
#
# ------------------- btagging
for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2018'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc),
    }

## ------------------- pile up
## ------------------- pileup sf
## ------------------- parton shower (ISR,FSR)
## ------------------- SSWW pert ord
## ------------------- pdf weight
## ------------------- QCD scale
## ------------------- MET (new, I completely did not have it before)
nuisances['met'] = {
    'name': 'CMS_scale_met_2018',
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
#
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
