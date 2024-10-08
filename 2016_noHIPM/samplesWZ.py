import os, glob
mcProduction = 'Summer20UL16_106x_nAODv9_noHIPM_Full2016v9'
dataReco = 'Run2016_UL2016_nAODv9_noHIPM_Full2016v9'
mcSteps = 'MCl1loose2016v9__MCCorr2016v9NoJERInHorn__l2tightOR2016v9'
fakeSteps = 'DATAl1loose2016v9__l2loose__fakeW'
dataSteps = 'DATAl1loose2016v9__l2loose__l2tightOR2016v9'

##############################################
###### Tree base directory for the site ######
##############################################
treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
limitFiles = -1


def makeMCDirectory(var=""):
    _treeBaseDir = treeBaseDir + ""
    if var == "":
        return "/".join([_treeBaseDir, mcProduction, mcSteps])
    else:
        return "/".join([_treeBaseDir, mcProduction, mcSteps + "__" + var])

mcDirectory = makeMCDirectory()
fakeDirectory = os.path.join(treeBaseDir, dataReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)

samples = {}

from mkShapesRDF.lib.search_files import SearchFiles
searchFiles = SearchFiles()

useXROOTD = False
redirector = 'root://eoscms.cern.ch/'

def nanoGetSampleFiles(path, name):
    _files = searchFiles.searchFiles(path, name, redirector=redirector)
    #_files = glob.glob(path + f"/nanoLatino_{name}__part*.root")
    if limitFiles != -1 and len(_files) > limitFiles:
        return [(name, _files[:limitFiles])]
    else:
        return  [(name, _files)]

def CombineBaseW(samples, proc, samplelist):
    _filtFiles = list(filter(lambda k: k[0] in samplelist, samples[proc]['name']))
    _files = list(map(lambda k: k[1], _filtFiles))
    _l = list(map(lambda k: len(k), _files))
    leastFiles = _files[_l.index(min(_l))]
    dfSmall = ROOT.RDataFrame("Runs", leastFiles)
    s = dfSmall.Sum('genEventSumw').GetValue()
    f = ROOT.TFile(leastFiles[0])
    t = f.Get("Events")
    t.GetEntry(1)
    xs = t.baseW * s

    __files = []
    for f in _files:
        __files += f
    df = ROOT.RDataFrame("Runs", __files)
    s = df.Sum('genEventSumw').GetValue()
    newbaseW = str(xs / s)
    weight = newbaseW + '/baseW'

    for iSample in samplelist:
        addSampleWeight(samples, proc, iSample, weight) 

def addSampleWeight(samples, sampleName, sampleNameType, weight):
    obj = list(filter(lambda k: k[0] == sampleNameType, samples[sampleName]['name']))[0]
    samples[sampleName]['name'] = list(filter(lambda k: k[0] != sampleNameType, samples[sampleName]['name']))
    if len(obj) > 2:
        samples[sampleName]['name'].append((obj[0], obj[1], obj[2] + '*(' + weight + ')'))
    else:
        samples[sampleName]['name'].append((obj[0], obj[1], '(' + weight + ')' ))

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
    ['F','Run2016F-UL2016-v1'],
    ['G','Run2016G_UL2016-v1'],
    ['H','Run2016H_UL2016-v1'],
]

DataSets = ['MuonEG','SingleMuon','SingleElectron','DoubleMuon', 'DoubleEG']

DataTrig = {
    'MuonEG'         : ' Trigger_ElMu' ,
    'SingleMuon'     : '!Trigger_ElMu && Trigger_sngMu' ,
    'SingleElectron' : '!Trigger_ElMu && !Trigger_sngMu && Trigger_sngEl',
    'DoubleMuon'     : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && Trigger_dblMu',
    'DoubleEG'       : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && !Trigger_dblMu && Trigger_dblEl'
}

################################################
############ BASIC MC WEIGHTS ##################
################################################

Nlep='3'

eleWP = 'mvaFall17V2Iso_WP90_SS_tthmva_70'
#muWP  = 'cut_Tight_HWWW_tthmva_80'
muWP = 'cut_Tight80x_tthmva_80'

LepWPCut        = 'LepCut'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP
LepWPweight     = 'LepSF'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

XSWeight      = 'XSWeight'
SFweight      = 'SFweight'+Nlep+'l*'+LepWPweight+'*'+LepWPCut
PromptGenLepMatch   = 'PromptGenLepMatch'+Nlep+'l'

mcCommonWeight = 'SFweight_mod*btagSF*PromptGenLepMatch'+Nlep+'l*samesign_requirement'
mcCommonWeightNoMatch = 'SFweight_mod*btagSF*samesign_requirement'
mcCommonWeightOS =  'SFweight_mod*btagSF*PromptGenLepMatch'+Nlep+'l*oppositesign_requirement'
# btag SF here bc maybe its different from the one of the central samples

###########################################
#############  BACKGROUNDS  ###############
###########################################

files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_EWK_UL')
samples['SSWW'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_QCD_UL')
samples['WpWp_QCD'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectory, 'WLLJJ_WToLNu_EWK_UL')
samples['WZ_EWK'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectory, 'WZTo3LNu')
samples['WZ_QCD'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}


samples['ZZ'] = {  'name'  :   nanoGetSampleFiles(mcDirectory,'ZZTo2L2Nu')
                            # + nanoGetSampleFiles(directory,'ZZTo2L2Nu_ext2')
                             + nanoGetSampleFiles(mcDirectory,'ZZTo2Q2L_mllmin4p0')
                             + nanoGetSampleFiles(mcDirectory,'ZZTo4L'),
                    'weight' :  XSWeight+'*'+SFweight+'*samesign_requirement*((nLepton==2)*PromptGenLepMatch2l + (nLepton==3)*PromptGenLepMatch3l + (nLepton>3)*PromptGenLepMatch4l)*'+METFilter_MC,
                    'FilesPerJob' : 3,
                 }

#ZZ2LbaseW   = getBaseWnAOD(mcDirectory,'Summer20UL18_106x_nAODv9_Full2018v9',['ZZTo2L2Nu'])
#ZZ4LbaseW   = getBaseWnAOD(mcDirectory,'Summer20UL18_106x_nAODv9_Full2018v9',['ZZTo4L'])
#ggZZbaseW   = getBaseWnAOD(mcDirectory,'Summer20UL18_106x_nAODv9_Full2018v9',['ggZZ4m',        'ggZZ4m_ext1'])

#addSampleWeight(samples,'ZZ','ZZTo2L2Nu',"1.07*"+ZZ2LbaseW+"/baseW") ## The non-ggZZ NNLO/NLO k-factor, cited from https://arxiv.org/abs/1405.2219v1 
#addSampleWeight(samples,'ZZ','ZZTo2L2Q',      "1.07") 
#addSampleWeight(samples,'ZZ','ZZTo4L',   "1.07*"+ZZ4LbaseW+"/baseW")


files = nanoGetSampleFiles(mcDirectory, 'TTZToLLNuNu_M-10') + \
        nanoGetSampleFiles(mcDirectory, 'TTWJetsToLNu') + \
        nanoGetSampleFiles(mcDirectory, 'tZq_ll_4f')
samples['tVx'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectory, 'ZGToLLG') + \
        nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin0p1')
samples['VgS1'] = {
    'name': files,
    'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
    'FilesPerJob': 4,
    'subsamples': {
        'L': 'gstarLow',
        'H': 'gstarHigh'
    }
}
#addSampleWeight(samples, 'VgS1', 'WGJJ', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples, 'VgS1', 'ZGToLLG', '(Gen_ZGstar_mass > 0)')
addSampleWeight(samples, 'VgS1', 'WZTo3LNu_mllmin0p1', '(Gen_ZGstar_mass > 0.1 && Gen_ZGstar_mass<4)')

### Wrong-sign
files = nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENEN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENMN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENTN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNEN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNMN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNTN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNEN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNMN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNTN')
samples['WW'] = {
    'name': files,
    'weight': mcCommonWeightOS,
    'FilesPerJob': 17,
}

# flavia had also: 'ST_s-channel_ext1' 'ST_t-channel_antitop' 'ST_t-channel_top'
# susan had also: 
files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
        nanoGetSampleFiles(mcDirectory, 'ST_tW_top') + \
        nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop')
samples['Top'] = {
    'name': files,
    'weight': mcCommonWeightOS,
    'FilesPerJob': 3,
}
#addSampleWeight(samples,'Top','TTTo2L2Nu','Top_pTrw')

ptllDYW_NLO = '(0.87*(gen_ptll<10)+(0.379119+0.099744*gen_ptll-0.00487351*gen_ptll**2+9.19509e-05*gen_ptll**3-6.0212e-07*gen_ptll**4)*(gen_ptll>=10 && gen_ptll<45)+(9.12137e-01+1.11957e-04*gen_ptll-3.15325e-06*gen_ptll**2-4.29708e-09*gen_ptll**3+3.35791e-11*gen_ptll**4)*(gen_ptll>=45 && gen_ptll<200) + 1*(gen_ptll>200))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'
files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50')  + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50') ### FIXME MISSING SAMPLE
samples['DY'] = {
    'name': files,
    'weight':  mcCommonWeightOS+'*( !(Sum(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 &&\
        Sum(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )',
    'FilesPerJob': 3,
}

# ------------------ Higgs all together 
#files = nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2Nu_M125') + \
#        nanoGetSampleFiles(mcDirectory, 'GluGluHToTauTau_M125') + \
#        nanoGetSampleFiles(mcDirectory, 'VBFHToWWTo2L2Nu_M125') + \
#        nanoGetSampleFiles(mcDirectory, 'VBFHToTauTau_M125') + \
#        nanoGetSampleFiles(mcDirectory, 'ttHToNonbb_M125')
#samples['Higgs'] = {
#    'name': files,
#    'weight': mcCommonWeightOS,
#    'FilesPerJob': 17,
#}

# ------------------ Splitting Higgs
# VBF H->WW 2l2nu
samples['qqH_hww'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBFHToWWTo2L2Nu_M125'),
    'weight': mcCommonWeightOS,
    'FilesPerJob': 4
}

# gg H->WW 2l2nu
samples['ggH_hww'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2Nu_M125'),# + nanoGetSampleFiles(mcDirectory, 'GGHjjToWWTo2L2Nu_minloHJJ_M125'),
    'weight': mcCommonWeightOS,
    'FilesPerJob': 1,
}
#addSampleWeight(samples, 'ggH_hww', 'GluGluHToWWTo2L2Nu_M125', '(HTXS_stage1_1_cat_pTjet30GeV<107)*Weight2MINLO*1092.7640/1073.2567') #only non GE2J categories with the weight to NNLOPS and renormalize integral                          
# addSampleWeight(samples, 'ggH_hww', 'GGHjjToWWTo2L2Nu_minloHJJ_M125', '(HTXS_stage1_1_cat_pTjet30GeV>106)*1092.7640/1073.2567')

# VBF H->tautau
samples['qqH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBFHToTauTau_M125'),
   'weight': mcCommonWeightOS,
    'FilesPerJob': 10
}

# gg H->tautau
samples['ggH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToTauTau_M125'),
   'weight': mcCommonWeightOS,
    'FilesPerJob': 20
}

#ttH
samples['ttH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'ttHToNonbb_M125'),
   'weight': mcCommonWeightOS,
    'FilesPerJob': 1
}
# ------------------


files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWW') + \
        nanoGetSampleFiles(mcDirectory, 'WWG')
samples['VVV'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

###########################################
################## FAKE ###################
###########################################

samples['Fake_lep'] = {
  'name': [],
  'weight': 'METFilter_DATA*fakeW*samesign_requirement',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 20
}

for _, sd in DataRun:
  for pd in DataSets:
    tag = pd + '_' + sd
    if 'DoubleMuon' in pd and 'Run2016G' in sd:
        print("sd      = {}".format(sd))
        print("pd      = {}".format(pd))
        print("Old tag = {}".format(tag))
        tag = tag.replace('v1','v2')
        print("New tag = {}".format(tag))

    files = nanoGetSampleFiles(fakeDirectory,tag)

    samples['Fake_lep']['name'].extend(files)
    samples['Fake_lep']['weights'].extend([DataTrig[pd]] * len(files))

samples['Fake_lep']['subsamples'] = {
  'em': 'abs(Lepton_pdgId[0]) == 11',
  'me': 'abs(Lepton_pdgId[0]) == 13'
}

###########################################
################## DATA ###################
###########################################

samples['DATA'] = {
  'name': [],
  'weight': 'LepWPCut*METFilter_DATA*samesign_requirement',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 50
}

for _, sd in DataRun:
  for pd in DataSets:
    tag = pd + '_' + sd
    if 'DoubleMuon' in pd and 'Run2016G' in sd: 
        print("sd      = {}".format(sd))
        print("pd      = {}".format(pd))
        print("Old tag = {}".format(tag))
        tag = tag.replace('v1','v2')
        print("New tag = {}".format(tag))

    files = nanoGetSampleFiles(dataDirectory,tag)

    samples['DATA']['name'].extend(files)
    samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))

#####################################################
######################################### EFT samples
#redirector = 'root://eoshome-g.cern.ch/'
#def nanoGetSampleFiles(path, name):
#    _files = searchFiles.searchFiles(path, name, redirector=redirector)
#    #_files = glob.glob(path + f"/nanoLatino_{name}__part*.root")
#    if limitFiles != -1 and len(_files) > limitFiles:
#        return [(name, _files[:limitFiles])]
#    else:
#        return  [(name, _files)]
#MCDirEFT = "/eos/user/g/glavizza/nanoAOD/UltraLegacy_EFT/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9"
#files =  nanoGetSampleFiles(MCDirEFT, 'SSWW_EFTdim6_UL')

files =  nanoGetSampleFiles(mcDirectory, 'SSWW_EFTdim6_UL')
op = ["cW", "cHDD", "cHW", "cHWB", "cHbox", "cHj1", "cHj3", "cHl1", "cHl3", "cll1", "cjj11", "cjj31", "cjj18", "cjj38"]
#op = ["cW", "cHbox"]
# the following (ls) contains the operators in the same order as in the LHEReweightingWeight vector
ls = ['SM', 'cW_m1', 'cW', 'cHDD_m1', 'cHDD', 'cHW_m1', 'cHW', 'cHWB_m1', 'cHWB', 'cHbox_m1', 'cHbox', 'cHj1_m1', 'cHj1', 'cHj3_m1', 'cHj3', 'cHl1_m1', 'cHl1', 'cHl3_m1', 'cHl3', 'cll1_m1', 'cll1', 'cjj11_m1', 'cjj11', 'cjj31_m1', 'cjj31', 'cjj18_m1', 'cjj18', 'cjj38_m1', 'cjj38']
# the following (mix) contains all the operators with mixed terms as well, in the LHEReweightingWeight order
mix = ['SM', 'cW_m1', 'cW', 'cHDD_m1', 'cHDD', 'cHW_m1', 'cHW', 'cHWB_m1', 'cHWB', 'cHbox_m1', 'cHbox', 'cHj1_m1', 'cHj1', 'cHj3_m1', 'cHj3', 'cHl1_m1', 'cHl1', 'cHl3_m1', 'cHl3', 'cll1_m1', 'cll1', 'cjj11_m1', 'cjj11', 'cjj31_m1', 'cjj31', 'cjj18_m1', 'cjj18', 'cjj38_m1', 'cjj38', 'cW_cHDD', 'cW_cHW', 'cW_cHWB', 'cW_cHbox', 'cW_cHj1', 'cW_cHj3', 'cW_cHl1', 'cW_cHl3', 'cW_cll1', 'cW_cjj11', 'cW_cjj31', 'cW_cjj18', 'cW_cjj38', 'cHDD_cHW', 'cHDD_cHWB', 'cHDD_cHbox', 'cHDD_cHj1', 'cHDD_cHj3', 'cHDD_cHl1', 'cHDD_cHl3', 'cHDD_cll1', 'cHDD_cjj11', 'cHDD_cjj31', 'cHDD_cjj18', 'cHDD_cjj38', 'cHW_cHWB', 'cHW_cHbox', 'cHW_cHj1', 'cHW_cHj3', 'cHW_cHl1', 'cHW_cHl3', 'cHW_cll1', 'cHW_cjj11', 'cHW_cjj31', 'cHW_cjj18', 'cHW_cjj38', 'cHWB_cHbox', 'cHWB_cHj1', 'cHWB_cHj3', 'cHWB_cHl1', 'cHWB_cHl3', 'cHWB_cll1', 'cHWB_cjj11', 'cHWB_cjj31', 'cHWB_cjj18', 'cHWB_cjj38', 'cHbox_cHj1', 'cHbox_cHj3', 'cHbox_cHl1', 'cHbox_cHl3', 'cHbox_cll1', 'cHbox_cjj11', 'cHbox_cjj31', 'cHbox_cjj18', 'cHbox_cjj38', 'cHj1_cHj3', 'cHj1_cHl1', 'cHj1_cHl3', 'cHj1_cll1', 'cHj1_cjj11', 'cHj1_cjj31', 'cHj1_cjj18', 'cHj1_cjj38', 'cHj3_cHl1', 'cHj3_cHl3', 'cHj3_cll1', 'cHj3_cjj11', 'cHj3_cjj31', 'cHj3_cjj18', 'cHj3_cjj38', 'cHl1_cHl3', 'cHl1_cll1', 'cHl1_cjj11', 'cHl1_cjj31', 'cHl1_cjj18', 'cHl1_cjj38', 'cHl3_cll1', 'cHl3_cjj11', 'cHl3_cjj31', 'cHl3_cjj18', 'cHl3_cjj38', 'cll1_cjj11', 'cll1_cjj31', 'cll1_cjj18', 'cll1_cjj38', 'cjj11_cjj31', 'cjj11_cjj18', 'cjj11_cjj38', 'cjj31_cjj18', 'cjj31_cjj38', 'cjj18_cjj38']

samples['sm'] = {
    'name': files,
    'weight': mcCommonWeight+'*rw_SM',
    'FilesPerJob': 20
}

for o in op:
    ip = ls.index(o)
    im = ls.index(o+'_m1')
    samples['lin_'+o] = {
        'name': files,
        'weight': mcCommonWeight+'*rw_LIN_'+o,
        'FilesPerJob': 4
    }
    samples['quad_'+o] = {
        'name': files,
        'weight': mcCommonWeight+'*rw_QUAD_'+o,
        'FilesPerJob': 20
    }
    samples['sm_lin_quad_'+o] = {
        'name': files,
        'weight': mcCommonWeight+'*LHEReweightingWeight['+str(ip)+']',
        'FilesPerJob': 20
    }


for i in range(len(op)):
    for j in range(len(op)):
        if j > i:
            term = op[i]+'_'+op[j]
            samples['sm_lin_quad_mixed_'+term] = {
                'name': files,
                'weight': mcCommonWeight+'*rw_MIX_'+term,
                'FilesPerJob': 20
            }

#samples =  {k:v for k,v in samples.items() if k in ['SSWW', 'WpWp_QCD', 'WZ_EWK', 'WZ_QCD', 'Fake_lep', 'DATA']}
samples = {k:v for k,v in samples.items() if 'sm' not in k and 'lin' not in k and 'quad' not in k} # SM ONLY
#samples = {k:v for k,v in samples.items() if 'sm' in k or 'lin' in k or 'quad' in k} # EFT ONLY
#samples = {k:v for k,v in samples.items() if k in ['ggH_hww']}
#samples = {k:v for k,v in samples.items() if k in ['Higgs','tZq', 'Fake_lep', 'WZ_QCD']}#,'sm','lin_cW','quad_cW']}
