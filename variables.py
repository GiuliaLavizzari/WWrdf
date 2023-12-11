# variables

variables = {}

#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

variables['events']  = {   'name': '1',
                           'range' : (1,0,2),
                           'xaxis' : 'events',
                           'fold' : 3
}

variables['ptj1']  = {   'name': 'Alt(CleanJet_pt,0,-9999.)',
                           'range' : (15,0.,200),
                           'xaxis' : 'p_{T} 1st jet',
                           'fold'  : 3
                           }

variables['ptj2']  = {   'name': 'Alt(CleanJet_pt,1,-9999.)',
                           'range' : (15,0.,150),
                           'xaxis' : 'p_{T} 2nd jet',
                           'fold'  : 3
                           }
variables['ptl1']  = {   'name': 'Alt(Lepton_pt,0,-9999.)',
                           'range' : (15,0.,200),
                           'xaxis' : 'p_{T} 1st jet',
                           'fold'  : 3
                           }

variables['ptl2']  = {   'name': 'Alt(Lepton_pt,1,-9999.)',
                           'range' : (15,0.,150),
                           'xaxis' : 'p_{T} 2nd jet',
                           'fold'  : 3
                           }

variables['mjj']  = {  'name': 'mjj', # for comparison with paper (ww)
                       'range': ([500,650,800, 1000,1200, 1500, 1800, 2300, 3000],),
                       'xaxis': 'mjj [GeV]',
                       'fold': 3,
                       }

variables['mll']  = {   'name': 'mll',
                        'range' : ([20,80,140,240,500],),
                        'xaxis' : 'mll [GeV]',
                        'fold' : 3,
                        }

variables['mll_v1']  = {   'name': 'mll',
                        'range' : (10,20,500),
                        'xaxis' : 'mll [GeV]',
                        'fold' : 3,
                        }

variables['mll_v2']  = {   'name': 'mll',
                        'range' : (20,20,500),
                        'xaxis' : 'mll [GeV]',
                        'fold' : 3,
                        }

variables = {k:v for k,v in variables.items() if k in ['events','mjj','mll','mll_v1','mll_v2','ptl1','ptl2','ptj1','ptj2']}

#variables = {k:v for k,v in variables.items() if k in ['events','mjj']}
