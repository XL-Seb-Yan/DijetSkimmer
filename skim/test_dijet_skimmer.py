#!/usr/bin/env python
import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.framework.enums import *

from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jecUncertainties import jec_global_tags, jecUncertProducerCpp
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import jetmetUncertaintiesProducer

from  PhysicsTools.DijetSkimmer.dijet_skimmer import DijetSkimmer, Year, Source, Dataset

#p_testdata=PostProcessor(outputDir=".",
#	inputFiles=["root://xrootd-cms.infn.it//store/data/Run2016C/JetHT/NANOAOD/Nano14Dec2018-v1/280000/FDCE1B38-A947-D444-8F4B-1DDFC776056B.root"],
#	cut=None,
#	branchsel="skim_branches_data.txt",
#	outputbranchsel="skim_branches_data.txt",
#	modules=[DijetSkimmer(year=Year.k2016, source=Source.kDATA, dataset=Dataset.kJetHT, hist_file="./test_data.root")],
#	provenance=True,
#	maxEntries=10000
#	)
#p_testdata.run()

p_testmc=PostProcessor(outputDir=".",
	inputFiles=["root://xrootd-cms.infn.it//store/mc/RunIIFall17NanoAODv4/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/NANOAODSIM/PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/10000/09245774-45B9-E545-A1D7-0FF6DBBEB29A.root"],
	cut=None,
	branchsel="skim_branches_mc.txt",
	outputbranchsel="skim_branches_mc.txt",
	modules=[
		#jecUncertProducerCpp(jec_global_tags[Year.k2016], doCppOutput=True),
		jetmetUncertaintiesProducer(
			era=Year.k2017, 
			globalTag=jec_global_tags[Year.k2017],
			jesUncertainties=["Total"], 
			jetType=JetType.kAK4PFchs, 
			redoJEC=False, 
			noGroom=False),
		DijetSkimmer(year=Year.k2017, source=Source.kMC, dataset=Dataset.kNone, hist_file="./test_mc.root")],
	provenance=True,
	maxEntries=10000
	)
p_testmc.run()
