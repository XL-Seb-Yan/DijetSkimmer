#!/usr/bin/env python
import os
import sys
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import createJMECorrector
from  PhysicsTools.DijetSkimmer.dijet_skimmer import DijetSkimmer

import argparse
parser = argparse.ArgumentParser(description="Run a skim job")
parser.add_argument("--njobs", type=int, help="number of jobs, -1 for testing")
parser.add_argument("--source", type=str, help="data or mc")
parser.add_argument("--dataset", type=str, default=None, help="Dataset name; controls trigger selection")
parser.add_argument("--year", type=str, default=None, help="Use UL2016_preVFP, UL2016, UL2017, or UL2018")
parser.add_argument("--era", type=str, default=None, help="Era; controls JECR")
parser.add_argument("--haddFileName", type=str, default="nanoskim.root", help="hadd filename")
args = parser.parse_args()

print "crab_meat arguments:"
print args

if args.source == "data":
    branch_list_file = "skim_branches_data.txt"
elif args.source == "mc":
    branch_list_file = "skim_branches_mc.txt"
else:
    print "ERROR : --source data or --source mc is mandatory"
    sys.exit(1)
    
if args.year is None:
    print "ERROR: year must be specified"
    sys.exit(1)
    
if args.source == "data" and args.era is None:
    print "ERROR: for data, era must be specified"
    sys.exit(1)

if args.source == "mc":
    jme_corrector = createJMECorrector(isMC=True, dataYear=args.year, applyHEMfix=("2018" in args.year))  
elif args.source == "data":
    jme_corrector = createJMECorrector(isMC=False,
                                       dataYear=args.year,
                                       runPeriod=args.era,
                                       applyHEMfix=("2018" in args.year)
                                       )
else:
    print "ERROR: Unknown source"
    sys.exit(1)

if args.source == "data":
    modules_list = [jme_corrector(), DijetSkimmer(year=args.year, source=args.source, dataset=args.dataset, hist_file="./hists.root")]
else:
    modules_list = [jme_corrector(), DijetSkimmer(year=args.year, source=args.source, dataset=args.dataset, hist_file="./hists.root")]

print "Printing modules_list:"
print modules_list

if args.njobs == -1:
    # Local test
    skimmer = PostProcessor(outputDir=".",
        #inputFiles=["root://cmsxrootd.fnal.gov//store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/25DF8860-C198-2947-8BCB-60A43CCA34EF.root"],
        inputFiles=["/eos/user/x/xuyan/TrijetData/NanoAODs/ZprimeTo3Glu_2017UL/nanoAOD_0.root",
                    "/eos/user/x/xuyan/TrijetData/NanoAODs/ZprimeTo3Glu_2017UL/nanoAOD_1.root"],
        cut=None,
        branchsel=branch_list_file,
        outputbranchsel=branch_list_file,
        modules=modules_list,
        provenance=True,
        fwkJobReport=True,
        haddFileName=args.haddFileName)
else:
    from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis #this takes care of converting the input files from CRAB
    skimmer = PostProcessor(outputDir=".",
        inputFiles=inputFiles(),
        cut=None,
        branchsel=branch_list_file,
        outputbranchsel=branch_list_file,
        modules=modules_list,
        provenance=True,
        fwkJobReport=True,
        haddFileName=args.haddFileName)
skimmer.run()


os.system("ls -lR")
print "Done with crab_meat"

