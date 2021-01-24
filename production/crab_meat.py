#!/usr/bin/env python
import os
import sys
#import PhysicsTools
#import PhysicsTools.NanoAODTools
#import PhysicsTools.NanoAODTools.postprocessing
#import PhysicsTools.NanoAODTools.postprocessing.framework
#import PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.framework.enums import *
#from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jecUncertainties import jec_global_tags, jecUncertProducerCpp
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import createJMECorrector
from  PhysicsTools.DijetSkimmer.dijet_skimmer import DijetSkimmer, Year, Source, Dataset

import argparse
parser = argparse.ArgumentParser(description="Run a skim job")
parser.add_argument("jobID", type=str, help="JobID (CRAB passes this as the first arg)")
parser.add_argument("--source", type=str, help="data or mc")
parser.add_argument("--dataset", type=str, default=None, help="Dataset name; controls trigger selection")
parser.add_argument("--year", type=int, default=None, help="2016, 2017, or 2018")
parser.add_argument("--haddFileName", type=str, default="nanoskim.root", help="hadd filename")
args = parser.parse_args()

print "crab_meat arguments:"
print args

if args.source == "data":
    branch_list_file = "skim_branches_data.txt"
    data_source = Source.kDATA
elif args.source == "mc":
    branch_list_file = "skim_branches_mc.txt"
    data_source = Source.kMC
else:
    print "ERROR : --source data or --source mc is mandatory"
    sys.exit(1)

if args.dataset == "JetHT":
    dataset = Dataset.kJetHT
elif args.dataset == "SingleMuon":
    dataset = Dataset.kSingleMuon
else:
    dataset = Dataset.kNone

if args.year == 2016:
    year = Year.k2016
elif args.year == 2017:
    year = Year.k2017
elif args.year == 2018:
    year = Year.k2018
else:
    print "ERROR : --year is mandatory."
    sys.exit(1)

if data_source == Source.kMC:
     jme_corrector = createJMECorrector(isMC=True, dataYear=args.year, applyHEMfix=(args.year==2018))  

if data_source == Source.kDATA:
    modules_list = [DijetSkimmer(year=year, source=data_source, dataset=dataset, hist_file="./hists_{}.root".format(args.jobID))]
else:
    modules_list = [jme_corrector(), DijetSkimmer(year=year, source=data_source, dataset=dataset, hist_file="./hists_{}.root".format(args.jobID))]

print "Printing modules_list:"
print modules_list

if args.jobID == -1:
    # Local test
    skimmer = PostProcessor(outputDir=".",
        #inputFiles=["root://cmsxrootd.fnal.gov//store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/25DF8860-C198-2947-8BCB-60A43CCA34EF.root"],
        inputFiles=["root://xrootd-cms.infn.it//store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/25DF8860-C198-2947-8BCB-60A43CCA34EF.root"],
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

