import os
import glob
import ROOT

# Make index of nanoskim files
mc_datasets = [
	"DijetSkim_QCD_Pt_1000to1400", 
	"DijetSkim_QCD_Pt_1400to1800", 
	"DijetSkim_QCD_Pt-15to7000_Flat", 
	"DijetSkim_QCD_Pt-15to7000_Flat2017", 
	"DijetSkim_QCD_Pt_1800to2400", 
	"DijetSkim_QCD_Pt_2400to3200", 
	"DijetSkim_QCD_Pt_300to470", 
	"DijetSkim_QCD_Pt_3200toInf", 
	"DijetSkim_QCD_Pt_470to600", 
	"DijetSkim_QCD_Pt_600to800", 
	"DijetSkim_QCD_Pt_800to1000", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-1000_R-0p1-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-1000_R-0p2-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-1000_R-0p5-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-1000_R-0p7-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-1000_R-0p9-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-2000_R-0p1-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-2000_R-0p2-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-2000_R-0p5-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-2000_R-0p7-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-2000_R-0p9-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-3000_R-0p1-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-3000_R-0p2-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-3000_R-0p3-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-3000_R-0p5-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-3000_R-0p7-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-3000_R-0p9-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-4000_R-0p1-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-4000_R-0p2-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-4000_R-0p3-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-4000_R-0p5-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-4000_R-0p7-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-4000_R-0p9-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-5000_R-0p1-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-5000_R-0p2-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-5000_R-0p3-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-5000_R-0p5-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-5000_R-0p7-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-5000_R-0p9-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-500_R-0p1-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-500_R-0p2-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-500_R-0p3-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-500_R-0p5-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-500_R-0p7-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-500_R-0p9-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-6000_R-0p1-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-6000_R-0p2-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-6000_R-0p3-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-6000_R-0p5-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-6000_R-0p7-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-6000_R-0p9-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-7000_R-0p1-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-7000_R-0p2-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-7000_R-0p3-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-7000_R-0p5-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-7000_R-0p7-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-7000_R-0p9-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-750_R-0p1-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-750_R-0p2-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-750_R-0p3-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-750_R-0p5-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-750_R-0p7-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-750_R-0p9-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-8000_R-0p1-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-8000_R-0p2-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-8000_R-0p3-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-8000_R-0p5-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-8000_R-0p7-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-8000_R-0p9-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-9000_R-0p1-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-9000_R-0p2-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-9000_R-0p3-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-9000_R-0p5-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-9000_R-0p7-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2GluTo3Glu_M1-9000_R-0p9-madgraph-pythia8", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-1000_R-0p1", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-1000_R-0p2", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-1000_R-0p3", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-1000_R-0p5", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-1000_R-0p7", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-1000_R-0p9", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-2000_R-0p1", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-2000_R-0p2", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-2000_R-0p3", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-2000_R-0p5", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-2000_R-0p7", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-2000_R-0p9", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-3000_R-0p1", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-3000_R-0p2", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-3000_R-0p5", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-3000_R-0p7", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-3000_R-0p9", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-4000_R-0p1", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-4000_R-0p2", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-4000_R-0p3", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-4000_R-0p5", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-4000_R-0p7", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-4000_R-0p9", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-5000_R-0p1", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-5000_R-0p2", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-5000_R-0p3", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-5000_R-0p7", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-500_R-0p1", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-500_R-0p2", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-500_R-0p5", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-500_R-0p7", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-500_R-0p9", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-6000_R-0p1", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-6000_R-0p2", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-6000_R-0p3", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-6000_R-0p5", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-6000_R-0p7", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-6000_R-0p9", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-7000_R-0p1", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-7000_R-0p2", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-7000_R-0p3", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-7000_R-0p5", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-750_R-0p2", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-750_R-0p5", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-750_R-0p7", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-750_R-0p9", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-8000_R-0p1", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-8000_R-0p2", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-8000_R-0p3", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-8000_R-0p5", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-8000_R-0p7", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-8000_R-0p9", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-9000_R-0p1", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-9000_R-0p2", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-9000_R-0p3", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-9000_R-0p5", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-9000_R-0p7", 
	"DijetSkim_Res1ToRes2QTo3Q_M1-9000_R-0p9", 
]

data_datasets = [
	"DijetSkim_JetHTRun2016Bver2", 
	"DijetSkim_JetHTRun2016C", 
	"DijetSkim_JetHTRun2016D", 
	"DijetSkim_JetHTRun2016E", 
	"DijetSkim_JetHTRun2016F", 
	"DijetSkim_JetHTRun2016G", 
	"DijetSkim_JetHTRun2016H", 
	"DijetSkim_JetHTRun2017B", 
	"DijetSkim_JetHTRun2017C", 
	"DijetSkim_JetHTRun2017D", 
	"DijetSkim_JetHTRun2017E", 
	"DijetSkim_JetHTRun2017F", 
	"DijetSkim_JetHTRun2018A", 
	"DijetSkim_JetHTRun2018B", 
	"DijetSkim_JetHTRun2018C", 
	"DijetSkim_JetHTRun2018Dver2", 
	"DijetSkim_SingleMuonRun2016Bver1", 
	"DijetSkim_SingleMuonRun2016Bver2", 
	"DijetSkim_SingleMuonRun2016C", 
	"DijetSkim_SingleMuonRun2016D", 
	"DijetSkim_SingleMuonRun2016E", 
	"DijetSkim_SingleMuonRun2016F", 
	"DijetSkim_SingleMuonRun2016G", 
	"DijetSkim_SingleMuonRun2016H", 
	"DijetSkim_SingleMuonRun2017B", 
	"DijetSkim_SingleMuonRun2017C", 
	"DijetSkim_SingleMuonRun2017D", 
	"DijetSkim_SingleMuonRun2017E", 
	"DijetSkim_SingleMuonRun2017F", 
	"DijetSkim_SingleMuonRun2018A", 
	"DijetSkim_SingleMuonRun2018B", 
	"DijetSkim_SingleMuonRun2018C", 
	"DijetSkim_SingleMuonRun2018Dver2"
]

processed_events = {}
dataset_files = {}

index_dir = os.path.expandvars("$CMSSW_BASE/src/PhysicsTools/DijetSkimmer/data/nanoskim")
ciaran_dir = "/mnt/hadoop/store/user/cgodfrey/"
version = "1_0_1"

for dataset in mc_datasets:
	dataset_files[dataset] = glob.glob("{}/{}_{}/*/*/*/*/nanoskim*root".format(ciaran_dir, dataset, version))
	with open("{}/v{}/{}.dat".format(index_dir, version, dataset), 'w') as f:
		for x in dataset_files[dataset]:
			f.write(x + "\n")

	hist_files = glob.glob("{}/{}_{}/*/*/*/*/hist*root".format(ciaran_dir, dataset, version))
	processed_events[dataset] = 0
	for hist_filename in hist_files:
		hist_file = ROOT.TFile(hist_filename, "READ")
		processed_events[dataset] += hist_file.Get("h_ProcessedEvents").Integral()
		hist_file.Close()


david_dir = "/mnt/hadoop/store/user/dryu/"
for dataset in data_datasets:
	dataset_files[dataset] = glob.glob("{}/{}_{}/*/*/*/*/nanoskim*root".format(david_dir, dataset, version))
	with open("{}/v{}/{}.dat".format(index_dir, version, dataset), 'w') as f:
		for x in dataset_files[dataset]:
			f.write(x + "\n")

	hist_files = glob.glob("{}/{}_{}/*/*/*/*/hist*root".format(david_dir, dataset, version))
	processed_events[dataset] = 0
	for hist_filename in hist_files:
		hist_file = ROOT.TFile(hist_filename, "READ")
		processed_events[dataset] += hist_file.Get("h_ProcessedEvents").Integral()
		hist_file.Close()

for dataset in sorted(processed_events.keys()):
	print "{} =>\t{}".format(dataset, processed_events[dataset])

import pickle
with open("{}/v{}/nevents.pkl".format(index_dir, version), "w") as f:
	pickle.dump(processed_events, f)

datadef = {}
for dataset in sorted(dataset_files.keys()):
	
	datadef[dataset] = {
		"files":dataset_files[dataset],
		"xs":xs, 
	}
            datadef[pd] = {
                'files': urllist,
                'xs': xs,
                'bytes': int(nbytes.sum()),
                'entries': int(nentries.sum()),
            }
