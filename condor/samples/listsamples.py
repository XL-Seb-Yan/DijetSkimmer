import os
from pprint import pprint

signalMCDir = {
	"UL2016": {
		"ZprimeTo3Gluon": "/eos/user/x/xuyan/TrijetData/NanoAODs/ZprimeTo3Glu_2016UL"
	},
	"UL2017": {
		"ZprimeTo3Gluon": "/eos/user/x/xuyan/TrijetData/NanoAODs/ZprimeTo3Glu_2017UL"
	},
	"UL2018": {
		"ZprimeTo3Gluon": "/eos/user/x/xuyan/TrijetData/NanoAODs/ZprimeTo3Glu_2018UL"
	}
}

data = {
	"UL2016": {
		"JetHT" : ["/JetHT/Run2016B-ver1_HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD",
					"/JetHT/Run2016B-ver2_HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD",
					"/JetHT/Run2016C-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD",
					"/JetHT/Run2016D-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD",
					"/JetHT/Run2016E-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD",
					"/JetHT/Run2016F-HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD",
					"/JetHT/Run2016F-UL2016_MiniAODv1_NanoAODv2-v2/NANOAOD",
					"/JetHT/Run2016G-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD",
					"/JetHT/Run2016H-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD"], 
		"SingleMuon" : ["/SingleMuon/Run2016B-ver1_HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD",
						"/SingleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD",
						"/SingleMuon/Run2016C-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD",
						"/SingleMuon/Run2016D-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD",
						"/SingleMuon/Run2016E-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD",
						"/SingleMuon/Run2016F-HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD",
						"/SingleMuon/Run2016F-UL2016_MiniAODv1_NanoAODv2-v4/NANOAOD",
						"/SingleMuon/Run2016G-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD",
						"/SingleMuon/Run2016H-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD"], 
		"QCD" : ["/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM", 				
				"/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM",
				"/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM",
				"/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM",
				"/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM",
				"/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM",
				"/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM",
				"/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM",
				"/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM"]
	},
	"UL2017": {
		"JetHT" : ["/JetHT/Run2017B-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD",
					"/JetHT/Run2017C-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD",
					"/JetHT/Run2017D-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD",
					"/JetHT/Run2017E-UL2017_MiniAODv1_NanoAODv2-v2/NANOAOD",
					"/JetHT/Run2017F-UL2017_MiniAODv1_NanoAODv2-v2/NANOAOD"], 
		"SingleMuon" : ["/SingleMuon/Run2017B-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD",
						"/SingleMuon/Run2017C-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD",
						"/SingleMuon/Run2017D-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD",
						"/SingleMuon/Run2017E-UL2017_MiniAODv1_NanoAODv2-v2/NANOAOD",
						"/SingleMuon/Run2017F-UL2017_MiniAODv1_NanoAODv2-v2/NANOAOD"], 
		"QCD" : ["/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",
				"/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",
				"/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",
				"/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",
				"/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",
				"/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",
				"/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",
				"/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",
				"/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM"]
	},
	"UL2018": {
		"JetHT" : ["/JetHT/Run2018A-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD",
					"/JetHT/Run2018B-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD",
					"/JetHT/Run2018C-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD",
					"/JetHT/Run2018D-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"], 
		"SingleMuon" : ["/SingleMuon/Run2018A-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD",
						"/SingleMuon/Run2018B-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD",
						"/SingleMuon/Run2018C-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD",
						"/SingleMuon/Run2018D-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"], 
		"QCD" : ["/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
				"/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
				"/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
				"/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
				"/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
				"/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
				"/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
				"/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
				"/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM"]
	}
}

if __name__ == "__main__":
	for year in ["UL2016","UL2017","UL2018"]:
		print(year)
		
		# Read signal MC files first
		for sample, directory in signalMCDir[year].items():
			filelist = open("%s_%s.txt" % (year, sample), "w")
			path = directory
			for path, subdirs, files in os.walk(directory):
				for filename in files:
					if ".root" not in filename or "hist" in filename:
						continue
					filelist.write("%s\n" % os.path.join(path, filename))
			filelist.close()
		
		for sample, subsamples in data[year].items():
			for subsample in subsamples:
				pdname = subsample.split("/")[1]
				if("QCD" in sample):
					samplename = year + "_" + pdname
				else:
					pdpostfix = subsample.split("/")[2].split("-")[0]
					samplename = year + "_" + pdname + "_" + pdpostfix
				os.system("dasgoclient -query=\"file dataset={}\" 2>&1 | tee {}.txt".format(subsample, samplename))