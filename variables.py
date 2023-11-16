# variables

variables = {}

#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

variables['events']  = {   'name': '1',
'range' : (1,0,2),
'xaxis' : 'events',
'fold' : 3
}


variables['nJet']  = {   'name': 'nJet',
                         'range' : (6,0,6),
                         'xaxis' : 'njets',
                         'fold' : 3
                         }
variables['nJet_v2']  = {   'name': 'Sum$(CleanJet_pt>30)',
                            'range' : (4,0,4),
                            'xaxis' : 'njets',
                            'fold' : 3
                            }


#variables['nLepton'] =  {
#    'name': '1*(Alt$(Lepton_pt[0],0.)>20) + 1*(Alt$(Lepton_pt[1],0.)>20) + 1*(Alt$(Lepton_pt[2],0.)>20)+ 1*(Alt$(Lepton_pt[3],0.)>20) + 1*(Alt$(Lepton_pt[4],0.)>20)',
#    'range': (5,0,5),
#    'xaxis': '# leptons',
#    'fold': 3
#}

variables['mtw1']  = {   'name': 'mtw1',            #   variable name
                         'range' : ([10,20,30,40,50,60,70.75,80,85,90,100,110,120],),    #   variable range
                         'xaxis' : 'mtw1 [GeV]',  #   x axis name
                         'fold' : 3
                         }
    
variables['mtw2']  = {   'name': 'mtw2',            #   variable name
                         'range' : ([10,20,30,40,50,60,70.75,80,85,90,100,110,120],),    #   variable range
                         'xaxis' : 'mtw2 [GeV]',  #   x axis name
                         'fold' : 3
                         }

#variables['jetpt1']  = {   'name': 'Alt$(Jet_pt[0],-9999.)',
#                           'range' : (15,0.,200),
#                           'xaxis' : 'p_{T} 1st jet',
#                           'fold'  : 3
#                           }
#
#variables['jetpt2']  = {   'name': 'Alt$(Jet_pt[1],-9999.)',
#                           'range' : (15,0.,150),
#                           'xaxis' : 'p_{T} 2nd jet',
#                           'fold'  : 3
#                           }
#
#
#variables['met']  = {   'name': 'MET_pt',            #   variable name
#                        'range' : (10,0,200),    #   variable range
#                        'xaxis' : 'pfmet [GeV]',  #   x axis name
#                        'fold' : 3
#                        }
#
#variables['etaj1'] = {  'name': 'Alt$(Jet_eta[0],-9999.)',
#                        'range': (10,-5,5),
#                        'xaxis': 'etaj1',
#                        'fold': 3
#                        }
#
#variables['etaj2'] = {         'name': 'Alt$(Jet_eta[1],-9999.)',
#                               'range': (10,-5,5),
#                               'xaxis': 'etaj2',
#                               'fold': 3
#                               }
#
#variables['Zlep1']  = {  'name': '(Alt$(Lepton_eta[0],-9999.) - (Alt$(Jet_eta[0],-9999.)+Alt$(Jet_eta[1],-9999.))/2)/detajj',
#                         'range': (10,-1.5,1.5),
#                         'xaxis': 'Z^{lep}_{1}',
#                         'fold': 3
#                         }
#
#variables['Zlep2']  = {  'name': '(Alt$(Lepton_eta[1],-9999.) - (Alt$(Jet_eta[0],-9999.)+Alt$(Jet_eta[1],-9999.))/2)/detajj',
#                         'range': (10,-1.5,1.5),
#                         'xaxis': 'Z^{lep}_{2}',
#                         'fold': 3
#                         }



###############################################################################
variables['mjj']  = {  'name': 'mjj', # for comparison with paper (ww)
                       'range': ([500,650,800, 1000,1200, 1500, 1800, 2300, 3000],),
                       'xaxis': 'mjj [GeV]',
#                       'cuts': ['WZ_tri_tauVeto_incl','WZb_tri_tauVeto_incl','WZQCD_tri_incl'],
                       'fold': 3,
#                       'blind': { c:[1200,3000] for c in cuts if "WZ_" in c}
                       }
variables['mjj_v4']  = {  'name': 'mjj', # for comparison with paper (wz qcd enriched)
                          'range': (12,200,500),
                          'xaxis': 'mjj [GeV]',
                          'fold': 3
                       }
variables['mjj_v2']  = {  'name': 'mjj', # for 1D fitting
                          'range': ([500,800,1200,1500,1800,2200,2600,3000],), 
                          'xaxis': 'mjj [GeV]',
                          'cuts': ['WZ_tri_tauVeto_incl','WZb_tri_tauVeto_incl','WZQCD_tri_incl'],
                          'fold': 3,
                          'blind': { c:[1200,3000] for c in cuts if "WZ_" in c}
                          }
variables['mjj_v3']  = {  'name': 'mjj', # for comparison with paper (btag cr)
                          'range': ([500,800,1200,1800,3000],),
                          'xaxis': 'mjj [GeV]',
                          'fold': 3,
                          'cuts': ['WZ_tri_tauVeto_incl','WZb_tri_tauVeto_incl','WZQCD_tri_incl'],
                          'blind': { c:[1200,3000] for c in cuts if "WZ_" in c}
                          }

variables['mll']  = {   'name': 'mll',
                        'range' : ([20,80,140,240,500],),
                        'xaxis' : 'mll [GeV]',
                        'fold' : 3,
                        'cuts': ['WZ_tri_tauVeto_incl','WZb_tri_tauVeto_incl','WZQCD_tri_incl'],
                        'blind': { c:[20,500] for c in cuts if "WZ_" in c}
                        }

variables['detajj']  = {  'name': 'detajj',
                          'range': (16,0.0,8.0),
                          'xaxis': 'detajj',
                          'fold': 3,
                          'cuts': ['WZ_tri_tauVeto_incl','WZb_tri_tauVeto_incl','WZQCD_tri_incl'],
                          'blind': { c:[0,8] for c in cuts if "WZ_" in c}
                          }
variables['detajj_v2']  = {  'name': 'detajj', # for comparison with paper wz qcd enriched
                          'range': (22,0.0,8.0),
                          'xaxis': 'detajj',
                          'fold': 3,
                          'cuts': ['WZ_tri_tauVeto_incl','WZb_tri_tauVeto_incl','WZQCD_tri_incl'],
                          'blind': { c:[0,8] for c in cuts if "WZ_" in c}
                          }

variables['mll_mjj']  = {   'name': 'mll:mjj',
                            'range' : ([500,800,1200,1800,3000],[20,80,140,240,600]),
                            'xaxis' : 'mll:mjj [GeV]',
                            'fold' : 3,
                            'doWeight' : 1,
                            'binX'     : 4,
                            'binY'     : 4
                            }
variables['mll_mjj_v2']  = {   'name': 'mll:mjj', # same as the paper for 2D fitting
                               'range' : ([500,650,800, 1000,1200, 1500, 1800, 2300, 3000],[20,80,140,240,600]),
                               'xaxis' : 'mll:mjj [GeV]',
                               'fold' : 3,
                               'doWeight' : 1,
                               'binX'     : 4,
                               'binY'     : 4
                               }

###############################################################################


#variables = {k:v for k,v in variables.items() if k in ["events", "mjj", "pt2", "pt1", "mll", "detajj", "mtw1", "mtw2"]} #["events", "mjj", "pt2", "pt1", "mll", "detajj", "mtw1", "mtw2"]
variables = {k:v for k,v in variables.items() if k in ['events','mjj']}
