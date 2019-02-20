import os
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection,Object
from PhysicsTools.NanoAODTools.postprocessing.framework.module import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import *
from PhysicsTools.NanoAODTools.postprocessing.framework.enums import *

ROOT.gInterpreter.Declare("#include \"PhysicsTools/DijetSkimmer/interface/NanoAODBase.h\"")
ROOT.gSystem.Load(os.path.expandvars("$CMSSW_BASE/lib/$SCRAM_ARCH/libPhysicsToolsDijetSkimmer.so"))

class DijetSkimmer(Module):
	def __init__(self, year=Year.k2016, source=Source.kDATA, dataset=Dataset.kNone, hist_file=None):
		self._year = year
		self._source = source
		self._dataset = dataset
		if hist_file:
			self.addHistogramFile(hist_file)

	def beginJob(self):
		# Histograms
		if self._hist_file:
			self._histograms = {}
			self._histograms["NJets"]           = ROOT.TH1D("h_NJets", "h_NJets", 21, -0.5, 20.5)
			self._histograms["ProcessedEvents"] = ROOT.TH1D("h_ProcessedEvents", "h_ProcessedEvents", 1, 0, 1)
			self._histograms["TriggeredEvents"] = ROOT.TH1D("h_TriggeredEvents", "h_TriggeredEvents", 1, 0, 1)
			self._histograms["SelectedEvents"]  = ROOT.TH1D("h_SelectedEvents", "h_SelectedEvents", 1, 0, 1)

			if self._source == Source.kDATA:
				self._trigger_list = []
				if self._dataset == Dataset.kJetHT:
					if self._year == Year.k2016:
						self._trigger_list = ["HLT_PFHT800", "HLT_PFHT900", "HLT_AK8PFJet450", "HLT_AK8PFJet500", "HLT_PFJet500", "HLT_CaloJet500_NoJetID"]
					elif self._year == Year.k2017 or self._year == Year.k2018:
						self._trigger_list = ["HLT_PFHT1050", "HLT_AK8PFJet500", "HLT_AK8PFJet550", "HLT_CaloJet500_NoJetID", "HLT_CaloJet550_NoJetID", "HLT_PFJet500"]
				elif self._dataset == Dataset.kSingleMuon:
					if self._year == Year.k2016:
						self._trigger_list = ["HLT_IsoMu24", "HLT_IsoTkMu24", "HLT_Mu50", "HLT_TkMu50"]
					elif self._year == Year.k2017:
						self._trigger_list = ["HLT_IsoMu27", "HLT_Mu50", "HLT_Mu50", "HLT_OldMu100", "HLT_TkMu100"]
					elif self._year == Year.k2018:
						self._trigger_list = ["HLT_IsoMu24", "HLT_Mu50", "HLT_OldMu100", "HLT_TkMu100"]
				self._histograms["TriggerPass"] = ROOT.TH1D("h_TriggerPass", "h_TriggerPass", len(self._trigger_list), -0.5, len(self._trigger_list) - 0.5)
 				for i, trigger in enumerate(self._trigger_list):
 					self._histograms["TriggerPass"].GetXaxis().SetBinLabel(i+1, trigger)


		elif self._source == Source.kDATA:
			# JECs are already applied to NanoAOD, so nothing to do
			pass

	def endJob(self):
		for hist_name in ["ProcessedEvents", "TriggeredEvents", "NJets", "SelectedEvents"]:
			print "[DijetSkimmer::endJob] INFO : {} = {}".format(hist_name, self._histograms[hist_name].Integral())
	
	def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
		pass

	def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
		pass

	def analyze(self, event):
		# Bookkeeping
		self._histograms["ProcessedEvents"].Fill(0)

		# Trigger selection
		if self._source == Source.kDATA:
			trigger_result = self.getTriggerResult(event)
			for i, trigger in enumerate(self._trigger_list):
				if trigger_result >> i & 1:
					self._histograms["TriggerPass"].Fill(i)
		else:
			trigger_result = 1
		if trigger_result == 0:
			return False
		self._histograms["TriggeredEvents"].Fill(0)

		# Jet selection: two jets with pT>30 and |eta|<2.5
		n_selected_jets = 0
		pass_njets = False
		for ijet in xrange(event.nJet):
			if event.Jet_pt[ijet] > 30. and abs(event.Jet_eta[ijet]) < 2.5:
				n_selected_jets += 1
				
			if n_selected_jets >= 2:
				pass_njets = True
				break
		if not pass_njets:
			return False
		self._histograms["NJets"].Fill(n_selected_jets)

		self._histograms["SelectedEvents"].Fill(0)
		return True

	def getTriggerResult(self, event):
		trigger_result = 0
		for i, trigger in enumerate(self._trigger_list):
			trigger_result |= getattr(event, trigger) << i
		return trigger_result


