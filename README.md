# DijetSkimmer
For making NanoAOD skims of dijet/trijet/Njet analyses.

Instructions:
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
