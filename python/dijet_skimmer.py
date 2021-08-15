import os
import copy
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection,Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import *

ROOT.gSystem.Load(os.path.expandvars("$CMSSW_BASE/lib/$SCRAM_ARCH/libPhysicsToolsDijetSkimmer.so"))

class DijetSkimmer(Module):

	def getTriggerResult(self, event):
		trigger_result = 0
		for i, trigger in enumerate(self._trigger_list_file):
			trigger_result |= getattr(event, trigger) << i
		return trigger_result

	def __init__(self, year="UL2017", source="data", dataset="", hist_file=None):
		self._year = year
		self._source = source
		self._dataset = dataset
		if hist_file:
			self._hist_file = ROOT.TFile(hist_file, "RECREATE")

	def beginJob(self):
		# Histograms
		if self._hist_file:
			self._histograms = {}
			self._histograms["NJets"]           = ROOT.TH1D("h_NJets", "h_NJets", 21, -0.5, 20.5)
			self._histograms["ProcessedEvents"] = ROOT.TH1D("h_ProcessedEvents", "h_ProcessedEvents", 1, 0, 1)
			self._histograms["TriggeredEvents"] = ROOT.TH1D("h_TriggeredEvents", "h_TriggeredEvents", 1, 0, 1)
			self._histograms["SelectedEvents"]  = ROOT.TH1D("h_SelectedEvents", "h_SelectedEvents", 1, 0, 1)

			if self._source == "data":
				self._trigger_list = []
				if "JetHT" in self._dataset :
					if "UL2016" in self._year:
						self._trigger_list = ["HLT_PFHT900", "HLT_AK8PFJet500", "HLT_AK8PFJet360_TrimMass30", "HLT_CaloJet500_NoJetID", "HLT_PFJet450",
						"HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63","HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58","HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54","HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53","HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52",
						"HLT_PFHT650_WideJetMJJ900DEtaJJ1p5"]
					elif "UL2017" in self._year or "UL2018" in self._year:
						self._trigger_list = ["HLT_PFHT1050", "HLT_AK8PFJet500", "HLT_AK8PFJet550", "HLT_CaloJet500_NoJetID", "HLT_CaloJet550_NoJetID", "HLT_PFJet500"]
				elif "SingleMuon" in self._dataset:
					self._trigger_list = ["HLT_Mu50"]
				else:
					print("[DijetSkimmer::beginFile] WARNING : Undefined dataset: ", self._dataset)
					
				self._histograms["TriggerPass"] = ROOT.TH1D("h_TriggerPass", "h_TriggerPass", len(self._trigger_list), -0.5, len(self._trigger_list) - 0.5)
				
 				for i, trigger in enumerate(self._trigger_list):
 					self._histograms["TriggerPass"].GetXaxis().SetBinLabel(i+1, trigger)

			elif self._source == "mc":
			# JECs are already applied to NanoAOD, so nothing to do
				pass

	def endJob(self):
		for hist_name in ["ProcessedEvents", "TriggeredEvents", "NJets", "SelectedEvents"]:
			print "[DijetSkimmer::endJob] INFO : {} = {}".format(hist_name, self._histograms[hist_name].Integral())
		self._hist_file.cd()
		for hist_name, hist in self._histograms.iteritems():
			hist.Write()

	def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
		if self._source == "data":
			# Make a list of triggers that are actually present in the TTree
			self._trigger_list_file = []
			for trigger_name in self._trigger_list:
				if inputTree.GetBranch(trigger_name):
					self._trigger_list_file.append(trigger_name)
				else:
					print "[DijetSkimmer::beginFile] WARNING : Trigger {} is not present in the input ntuple! Skipping this trigger.".format(trigger_name)

	def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
		pass

	def analyze(self, event):
		# Bookkeeping
		self._histograms["ProcessedEvents"].Fill(0)

		# Trigger selection
		if self._source == "data":
			trigger_result = self.getTriggerResult(event)
			for i, trigger in enumerate(self._trigger_list_file):
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
