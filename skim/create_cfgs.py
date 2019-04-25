import os
import sys

version = "1_1_6" 
# 1_0_1 
#	- first try. job name parsing removed too much of the name, resulting in 2016/2017/2018 name clashes.
# 1_1_1
# 	- Try running over many datasets in the same job, so they end up in e.g. NanoSkim_v<version>/<dataset>/...
# 1_1_2
# 	- Missing trigger fix didn't work, try again.
# 1_1_3
#   - git pulled while 1_1_1 submission was still ongoing.
# 1_1_4
# 	- request names clashed in 1_1_3
# 1_1_5
# 	- Some MC samples have "ext#" in the second part. Include this in the job name. 
# 1_1_6
#   - Less files per job for MC, since the skim efficiency is basically 100%
datasets = {
	2016:[
		"/JetHT/Run2016B_ver1-Nano14Dec2018_ver1-v1/NANOAOD",
		"/JetHT/Run2016B_ver2-Nano14Dec2018_ver2-v1/NANOAOD",
		"/JetHT/Run2016C-Nano14Dec2018-v1/NANOAOD",
		"/JetHT/Run2016D-Nano14Dec2018-v1/NANOAOD",
		"/JetHT/Run2016E-Nano14Dec2018-v1/NANOAOD",
		"/JetHT/Run2016F-Nano14Dec2018-v1/NANOAOD",
		"/JetHT/Run2016G-Nano14Dec2018-v1/NANOAOD",
		"/JetHT/Run2016H-Nano14Dec2018-v1/NANOAOD",

		"/SingleMuon/Run2016B_ver1-Nano14Dec2018_ver1-v1/NANOAOD",
		"/SingleMuon/Run2016B_ver2-Nano14Dec2018_ver2-v1/NANOAOD",
		"/SingleMuon/Run2016C-Nano14Dec2018-v1/NANOAOD",
		"/SingleMuon/Run2016D-Nano14Dec2018-v1/NANOAOD",
		"/SingleMuon/Run2016E-Nano14Dec2018-v1/NANOAOD",
		"/SingleMuon/Run2016F-Nano14Dec2018-v1/NANOAOD",
		"/SingleMuon/Run2016G-Nano14Dec2018-v1/NANOAOD",
		"/SingleMuon/Run2016H-Nano14Dec2018-v1/NANOAOD",

		#"/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",
		#"/QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",
		#"/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",
		#"/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext2-v1/NANOAODSIM",
		#"/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",
		#"/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",
		#"/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",
		#"/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",
		"/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",
		"/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",
		"/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",
		"/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",
		"/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",
		"/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",
		"/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",
		"/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",
		"/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",
		"/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",
		"/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",
		"/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",
		"/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",
		"/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",
		"/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",
		"/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",
	], 2017:[
		"/JetHT/Run2017B-Nano14Dec2018-v1/NANOAOD",
		"/JetHT/Run2017C-Nano14Dec2018-v1/NANOAOD",
		"/JetHT/Run2017D-Nano14Dec2018-v1/NANOAOD",
		"/JetHT/Run2017E-Nano14Dec2018-v1/NANOAOD",
		"/JetHT/Run2017F-Nano14Dec2018-v1/NANOAOD",

		"/SingleMuon/Run2017B-Nano14Dec2018-v1/NANOAOD",
		"/SingleMuon/Run2017C-Nano14Dec2018-v1/NANOAOD",
		"/SingleMuon/Run2017D-Nano14Dec2018-v1/NANOAOD",
		"/SingleMuon/Run2017E-Nano14Dec2018-v1/NANOAOD",
		"/SingleMuon/Run2017F-Nano14Dec2018-v1/NANOAOD",

		"/QCD_Pt-15to7000_TuneCP5_Flat2017_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/QCD_Pt-15to7000_TuneCP5_Flat_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		#"/QCD_Pt_15to30_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		#"/QCD_Pt_15to30_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM",
		#"/QCD_Pt_30to50_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		#"/QCD_Pt_30to50_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM",
		#"/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		#"/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM",
		#"/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		#"/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM",
		#"/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		#"/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		#"/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM",
		"/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM",
		"/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM",
		"/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM",
		"/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM",
		"/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM",
		"/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM",
		"/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",

		"/Res1ToRes2GluTo3Glu_M1-1000_R-0p1_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-1000_R-0p2_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-1000_R-0p3_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-1000_R-0p5_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-1000_R-0p7_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-1000_R-0p9_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-2000_R-0p1_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-2000_R-0p2_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-2000_R-0p5_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-2000_R-0p7_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-2000_R-0p9_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-3000_R-0p1_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-3000_R-0p2_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-3000_R-0p3_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-3000_R-0p5_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-3000_R-0p7_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-3000_R-0p9_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-4000_R-0p1_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-4000_R-0p2_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-4000_R-0p3_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-4000_R-0p5_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-4000_R-0p7_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-4000_R-0p9_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-5000_R-0p1_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-5000_R-0p2_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-5000_R-0p3_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-5000_R-0p5_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-5000_R-0p7_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-5000_R-0p9_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-500_R-0p1_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-500_R-0p2_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-500_R-0p3_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-500_R-0p5_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-500_R-0p7_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-500_R-0p9_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-6000_R-0p1_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-6000_R-0p2_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-6000_R-0p3_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-6000_R-0p5_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-6000_R-0p7_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-6000_R-0p9_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-7000_R-0p1_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-7000_R-0p2_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-7000_R-0p3_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-7000_R-0p5_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-7000_R-0p7_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-7000_R-0p9_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-750_R-0p1_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-750_R-0p2_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-750_R-0p3_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-750_R-0p5_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-750_R-0p7_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-750_R-0p9_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-8000_R-0p1_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-8000_R-0p2_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-8000_R-0p3_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-8000_R-0p5_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-8000_R-0p7_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-8000_R-0p9_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-9000_R-0p1_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-9000_R-0p2_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-9000_R-0p3_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-9000_R-0p5_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-9000_R-0p7_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2GluTo3Glu_M1-9000_R-0p9_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",

		"/Res1ToRes2QTo3Q_M1-1000_R-0p1_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-1000_R-0p2_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-1000_R-0p3_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-1000_R-0p5_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-1000_R-0p7_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-1000_R-0p9_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-2000_R-0p1_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-2000_R-0p2_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-2000_R-0p3_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-2000_R-0p5_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-2000_R-0p7_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-2000_R-0p9_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-3000_R-0p1_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-3000_R-0p2_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-3000_R-0p5_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-3000_R-0p7_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-3000_R-0p9_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-4000_R-0p1_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-4000_R-0p2_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-4000_R-0p3_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-4000_R-0p5_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-4000_R-0p7_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-4000_R-0p9_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-5000_R-0p1_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-5000_R-0p2_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-5000_R-0p3_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-5000_R-0p5_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-5000_R-0p7_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-5000_R-0p9_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-500_R-0p1_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-500_R-0p2_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-500_R-0p5_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-500_R-0p7_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-500_R-0p9_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-6000_R-0p1_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-6000_R-0p2_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-6000_R-0p3_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-6000_R-0p5_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-6000_R-0p7_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-6000_R-0p9_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-7000_R-0p1_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-7000_R-0p2_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-7000_R-0p3_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-7000_R-0p5_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-750_R-0p2_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-750_R-0p3_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-750_R-0p5_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-750_R-0p7_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-750_R-0p9_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-8000_R-0p1_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-8000_R-0p2_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-8000_R-0p3_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-8000_R-0p5_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-8000_R-0p7_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-8000_R-0p9_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-9000_R-0p1_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-9000_R-0p2_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-9000_R-0p3_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-9000_R-0p5_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-9000_R-0p7_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
		"/Res1ToRes2QTo3Q_M1-9000_R-0p9_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",
	], 2018:[
		"/JetHT/Run2018A-Nano14Dec2018-v1/NANOAOD",
		"/JetHT/Run2018B-Nano14Dec2018-v1/NANOAOD",
		"/JetHT/Run2018C-Nano14Dec2018-v1/NANOAOD",
		"/JetHT/Run2018D-Nano14Dec2018_ver2-v1/NANOAOD",

		"/SingleMuon/Run2018A-Nano14Dec2018-v1/NANOAOD",
		"/SingleMuon/Run2018B-Nano14Dec2018-v1/NANOAOD",
		"/SingleMuon/Run2018C-Nano14Dec2018-v1/NANOAOD",
		"/SingleMuon/Run2018D-Nano14Dec2018_ver2-v1/NANOAOD",

		#"/QCD_Pt_15to30_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM",
		#"/QCD_Pt_30to50_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM",
		#"/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM",
		#"/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM",
		#"/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM",
		#"/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM",
		#"/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM",
		"/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM",
		"/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM",
		"/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM",
		"/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM",
		"/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM",
		"/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM",
		"/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM",
		"/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM",
		"/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM",
		"/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM",
		"/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM",
		"/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM",
		"/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM",
		"/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext2-v1/NANOAODSIM",
	]
}

import re
re_ver = re.compile("(?P<version>ver\d)")
re_year_data = re.compile("Run(?P<year>\d\d\d\d)")
re_ext = re.compile("(?P<ext>ext\d)")

def make_cfg(year, dataset, version):
	# For the cfg filename, create a string uniquely representing each dataset above
	dataset_short = dataset.split("/")[1]
	for remove_str in remove_strs:
		dataset_short = dataset_short.replace(remove_str, "")

	second_piece = dataset.split("/")[2]
	# For data, add the run-period to the short name
	if "JetHT" in dataset_short or "SingleMuon" in dataset_short:
		print second_piece
		dataset_short += second_piece[:8]
		re_ver_match = re_ver.search(second_piece)
		if re_ver_match:
			dataset_short += re_ver_match.group("version")
		re_year_match = re_year_data.search(dataset)
		if re_year_match:
			year = re_year_match.group("year")
		else:
			print "ERROR : Failed to regex year out of {}".format(dataset)
			sys.exit(1)
	else:
		# Look for "ext#" in second part
		re_ext_match = re_ext.search(second_piece)
		if re_ext_match:
			ext_str = re_ext_match.group("ext")
			dataset_short += ext_str

	cfg_path = os.path.expandvars("$CMSSW_BASE/src/PhysicsTools/DijetSkimmer/skim/crab/skim_{}_{}_cfg.py".format(dataset_short, year))
	print version
	if "test" in version:
		cfg_path = cfg_path.replace("cfg.py", "test_cfg.py")
	print cfg_path
	with open(cfg_path, 'w') as f_out:
		with open("skim_cfg_base.py", 'r') as f_in:
			for line in f_in:
				if "config.JobType.scriptArgs" in line:
					if "JetHT" in dataset_short:
						f_out.write("config.JobType.scriptArgs = [\"--source=data\", \"--dataset=JetHT\", \"--year={}\"]\n".format(year))
					elif "SingleMuon" in dataset_short:
						f_out.write("config.JobType.scriptArgs = [\"--source=data\", \"--dataset=SingleMuon\", \"--year={}\"]\n".format(year))
					else:
						f_out.write("config.JobType.scriptArgs = [\"--source=mc\", \"--year={}\"]\n".format(year))
				elif "unitsPerJob" in line:
					if not ("JetHT" in dataset_short or "SingleMuon" in dataset_short):
						f_out.write("config.Data.unitsPerJob = 1\n")
					else:
						f_out.write("config.Data.unitsPerJob = 4\n")
				else:
					f_out.write(line.replace("DATASET", dataset_short).replace("VERSION", version).replace("YEAR", str(year)))
		f_out.write("config.Data.inputDataset = '{}'".format(dataset))
	return cfg_path

if __name__ == "__main__":

	submit_script = open(os.path.expandvars("$CMSSW_BASE/src/PhysicsTools/DijetSkimmer/skim/crab/submit.sh"), "w")
	resubmit_script = open(os.path.expandvars("$CMSSW_BASE/src/PhysicsTools/DijetSkimmer/skim/crab/submit.sh"), "w")
	status_script = open(os.path.expandvars("$CMSSW_BASE/src/PhysicsTools/DijetSkimmer/skim/crab/submit.sh"), "w")

	remove_strs = ["_TuneCP5", "_TuneCUETP8M1", "_13TeV", "_pythia8", "_madgraph", "-pythia8", "-madgraph"]

	for year in [2016, 2017, 2018]:
		for dataset in datasets[year]:
			cfg_path = make_cfg(year=year, dataset=dataset, version=version)
			submit_script.write("crab submit -c {}\n".format(cfg_path))


	# Make a test cfg
	make_cfg(year=year, dataset="/JetHT/Run2018A-Nano14Dec2018-v1/NANOAOD", version="test37")
	make_cfg(year=year, dataset="/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM", version="test37")
