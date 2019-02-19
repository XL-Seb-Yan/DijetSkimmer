import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection,Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetSmearer import jetSmearer

import copy

import ROOT
ROOT.gInterpreter.Declare("#include \"PhysicsTools/DijetSkimmer/interface/NanoAODBase.h\"")
ROOT.gSystem.Load(os.path.expandvars("$CMSSW_BASE/lib/$SCRAM_ARCH/libPhysicsToolsDijetSkimmer.so"))


from enum import Enum
class Year(Enum):
	k2016 = 1
	k2017 = 2
	k2018 = 3

class Source(Enum):
	kMC = 1
	kDATA = 2

class Dataset(Enum):
	kJetHT = 1
	kSingleMuon = 2
	kNone = 3

class DijetSkimmer(Module):
	def __init__(self, year=Year.k2016, source=Source.kDATA, dataset=Dataset.kNone):
		self._year = year
		self._source = source
		self._dataset = dataset

	def beginJob(self):
		# Setup output tree
		

		# Configure JES and JER
		self._jes_uncs = []
		self._gt = ""
		self._jet_smearer = None
		if self._source == Source.kMC:
			if self._year == Year.k2016: 
				self._jes_uncs = jesUncertaintySources2016
				self._gt = "Summer16_23Sep2016V4_MC"

			elif self._year == Year.k2017:
				self._jes_uncs = jesUncertaintySources2017
				self._gt =  "Fall17_17Nov2017_V8_MC"

			elif self._year == Year.k2018:
				self._jes_uncs = jesUncertaintySources2018
				self._gt =  "Autumn18_V2_MC"

			self._jet_smearer = jetSmearer(self._gt, "AK4PFCHS", "Summer16_25nsV1_MC_PtResolution_AK8PFPuppi.txt", "Summer16_25nsV1_MC_SF_AK8PFPuppi.txt")
			self._jet_smearer.beginJob()

		elif self._source == Source.kDATA:
			# JECs are already applied to NanoAOD, so nothing to do
			pass

	def endJob(self):
		if self._source == Source.kMC:
			self._jet_smearer.endJob()
	
	def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
		pass

	def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
		pass

	def analyze(self, event):
		# Bookkeeping
		self._counters["processed"] += 1

		# Trigger selection
		trigger_result = self.getTriggerResult()
		if not trigger_result:
			return False
		self._counters["triggered"] += 1

		# Jet selection: two jets with pT>30
		n_jets = 0
		pass_njets = False
		for ijet in xrange(event.nJets):
			if event.Jet_pt[ijet] > 30.:
				n_jets += 1
				
			if n_jets >= 2:
				pass_njets
				break
		if not pass_njets:
			return False
		self._counters["njets"] += 1

		return True

	def getTriggerResult(self):
		if self._source == kDATA:
			if self._dataset == kJetHT:
				if self._year == k2016:
					trigger_result = event.HLT_PFHT800 \
										or event.HLT_PFHT900 \
										or event.HLT_AK8PFJet450 \
										or event.HLT_AK8PFJet500 \
										or event.HLT_PFJet500 \
										or event.HLT_CaloJet500_NoJetID 

				elif self._year == k2017 or self._year == k2018:
					trigger_result = event.HLT_PFHT1050 \
										or event.HLT_AK8PFJet500 \
										or event.HLT_AK8PFJet550 \
										or event.HLT_CaloJet500_NoJetID \
										or event.HLT_CaloJet550_NoJetID \
										or event.HLT_PFJet500 
			elif self._dataset == kSingleMuon:
				if self._year == k2016:
					trigger_result = event.HLT_IsoMu24 \
						or event.HLT_IsoTkMu24 \
						or event.HLT_Mu50 \
						or event.HLT_TkMu50
				if self._year == k2017:
					trigger_result = event.HLT_IsoMu27 \
						or event.HLT_Mu50 \
						or event.HLT_Mu50 \
						or event.HLT_OldMu100 \
						or event.HLT_TkMu100
				if self._year == k2018:
					trigger_result = event.HLT_IsoMu24 \
						or event.HLT_Mu50 \
						or event.HLT_OldMu100 \
						or event.HLT_TkMu100
		else:
			trigger_result = True


