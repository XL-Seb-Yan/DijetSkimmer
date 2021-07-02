# DijetSkimmer
For making NanoAOD skims of dijet/trijet/Njet analyses.

Instructions:

Prompt reco:
```
cmsrel CMSSW_10_2_11_patch1
cd CMSSW_10_2_11_patch1/src
cmsenv
git clone ssh://git@github.com/DryRun/nanoAOD-tools PhysicsTools/NanoAODTools
git clone ssh://git@github.com/DryRun/DijetSkimmer PhysicsTools/DijetSkimmer
scram b -j8
cd PhysicsTools/DijetSkimmer/skim
python run_dijet_skimmer.py
```

Legacy reco:
```
scram project -n "CMSSW_10_6_27_skim" CMSSW_10_6_27
cd CMSSW_10_6_27_skim/src
cmsenv
#git clone ssh://git@github.com/DryRun/nanoAOD-tools PhysicsTools/NanoAODTools
git clone https://github.com/cms-nanoAOD/nanoAOD-tools.git PhysicsTools/NanoAODTools
git clone ssh://git@github.com/DryRun/DijetSkimmer PhysicsTools/DijetSkimmer
scram b -j8
cd PhysicsTools/DijetSkimmer/skim
python run_dijet_skimmer.py
```
