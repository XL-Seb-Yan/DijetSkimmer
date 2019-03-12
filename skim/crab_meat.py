#!/usr/bin/env python
import os
import sys
sys.path
import PhysicsTools
import PhysicsTools.NanoAODTools
import PhysicsTools.NanoAODTools.postprocessing
import PhysicsTools.NanoAODTools.postprocessing.framework
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis #this takes care of converting the input files from CRAB
from PhysicsTools.NanoAODTools.postprocessing.framework.enums import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jecUncertainties import jec_global_tags, jecUncertProducerCpp
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import jetmetUncertaintiesProducer
from  PhysicsTools.DijetSkimmer.dijet_skimmer import DijetSkimmer, Year, Source, Dataset

import argparse
parser = argparse.ArgumentParser(description="Run a skim job")
parser.add_argument("jobID", type=str, help="JobID (CRAB passes this as the first arg)")
parser.add_argument("--source", type=str, help="data or mc")
parser.add_argument("--dataset", type=str, default=None, help="Dataset name; controls trigger selection")
args = parser.parse_args()

if args.source == "data":
	branch_list_file = "skim_branches_data.txt"
	data_source = Source.kDATA
elif args.source == "mc":
	branch_list_file = "skim_branches_mc.txt"
	data_source = Source.kMC

if args.dataset == "JetHT":
	dataset = Dataset.kJetHT
elif args.dataset == "SingleMuon":
	dataset = Dataset.kSingleMuon
else:
	dataset = Dataset.kNone

skimmer = PostProcessor(outputDir=".",
	inputFiles=inputFiles(),
	cut=None,
	branchsel=branch_list_file,
	outputbranchsel=branch_list_file,
	modules=[DijetSkimmer(year=Year.k2016, source=data_source, dataset=dataset, hist_file="./skim_{}.root".format(args.jobID))],
	provenance=True)
skimmer.run(maxEvents=-1)

os.system("ls -lR")
print "Done with crab_meat"

