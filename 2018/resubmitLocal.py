import os
import glob
import subprocess 

#resubmitLine = "queue 1 Folder in DATA_0 DATA_1"
resubmitLine = "queue 1 Folder in ZZ_33 ZZ_51 ZZ_68 TTV_3 WW_3 Top_0 Top_1 Top_2 Top_3 Top_4 Top_5 Top_6 Top_7 Top_8 Top_9 Top_10 Top_11 Top_12 Top_13 Top_14 Top_15 Top_16 Top_17 Top_18 Top_19 Top_20 Top_21 Top_22 Top_23 Top_24 Top_25 Top_26 Top_27 Top_28 Top_29 Top_30 Top_31 Top_32 Top_33 Top_34 Top_35 Top_36 Top_37 Top_38 Top_39 Top_40 Top_41 Top_42 Top_43 Top_44 Top_45 Top_46 Top_47 Top_48 Top_49 Top_50 Top_51 Top_52 Top_53 Top_54 Top_55 Top_56 Top_57 Top_58 Top_59 Top_60 Top_61 Top_62 Top_63 Top_64 Top_65 Top_66 Top_67 Top_68 Top_69 Top_70 Top_71 Top_72 Top_73 Top_74 Top_75 Top_76 DY_1 DY_8 DY_13 DY_16 DY_18 DY_20 DY_21 DY_22 DY_26 DY_29 DY_34 DY_44 DY_45 DY_46 DY_48 DY_49 DY_50 DY_51 DY_55 DY_57 DY_58 DY_60 DY_62 DY_63 DY_66 DY_68 DY_69 DY_72 DY_77 DY_80 DY_84 DY_86 DY_87 DY_88 DY_93 qqH_hww_3 qqH_hww_4 ggH_hww_0 ggH_hww_1 ggH_hww_2 ggH_hww_5 ggH_hww_6 ggH_hww_7 ggH_hww_8 ggH_hww_9 ggH_hww_10 ggH_hww_11 ggH_hww_13 ggH_hww_14 ggH_hww_15 ggH_hww_16 ggH_hww_18 ggH_hww_19 ggH_hww_21 ggH_hww_24 ttH_hww_2 ttH_hww_3 ttH_hww_4 ttH_hww_8 ttH_hww_10 ttH_hww_15 ttH_hww_17 ttH_hww_19 ttH_hww_20 ttH_hww_26 ttH_hww_27 ttH_hww_28 ttH_hww_31 ttH_hww_37 ttH_hww_40 ttH_hww_42 ttH_hww_43 ttH_hww_46 ttH_hww_47 VVV_0 VVV_1 VVV_2 VVV_4 VVV_7 VVV_9 VVV_10 VVV_12 Fake_lep_13 Fake_lep_18"
condorFolder = 'condor/VBS_WZ_2018_31082022/'

samples = resubmitLine[len('queue 1 Folder in '):].split(' ')
print(str(samples))

condorFolder = os.path.abspath(condorFolder)

proc = subprocess.Popen('which python3', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = proc.communicate()
out = out.decode("utf-8")
frameworkPath = '/'.join(out.split('\n')[0].split('/')[:-3]) + '/'


for sample in samples:


    fSh  = '#!/bin/bash\n'
    fSh += f'cd {condorFolder}/{sample}\n'
    fSh += f'mkdir tmp\n'
    fSh += f'cd tmp\n'
    fSh += f'cp ../script.py . \n'
    fSh += f'cp ../../run.sh . \n'
    fSh += f'cp {frameworkPath}mkShapesRDF/include/headers.hh . \n'
    fSh += f'cp {frameworkPath}mkShapesRDF/shapeAnalysis/runner.py . \n'
    fSh += f'echo "run locally" >../err.txt\n'
    fSh += f'./run.sh {sample} 2>>../err.txt 1>../out.txt\n'
    fSh += f'cd ..; rm -r tmp\n'

    fileName = f'tmp_run_{sample}.sh'

    with open(fileName, 'w') as file:
        file.write(fSh)

    proc = subprocess.Popen(f'chmod +x {fileName}; ./{fileName}; rm {fileName}', shell=True)
    proc.wait()
