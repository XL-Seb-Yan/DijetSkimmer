import os
from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config, getUsernameFromSiteDB

config = Configuration()
job_name = "DijetSkim_0_0_1"

config.section_("General")
config.General.requestName = job_name
config.General.transferLogs=True
config.section_("JobType")
config.JobType.pluginName = 'Analysis'

# Setup the custom executable
config.JobType.psetName = os.path.expandvars('$CMSSW_BASE/src/PhysicsTools/DijetSkimmer/skim/PSet.py') # CRAB modifies this file to contain the input files and lumis
config.JobType.scriptExe = os.path.expandvars('$CMSSW_BASE/src/PhysicsTools/DijetSkimmer/skim/crab_shell.sh') # CRAB then calls scriptExe jobId <scriptArgs>
config.JobType.scriptArgs = ["source=data", "dataset=SingleMuon"]
config.JobType.inputFiles = [os.path.expandvars('$CMSSW_BASE/src/PhysicsTools/DijetSkimmer/skim/crab_meat.py'), os.path.expandvars('$CMSSW_BASE/src/PhysicsTools/NanoAODTools/scripts/haddnano.py')] #hadd nano will not be needed once nano tools are in cmssw
config.JobType.sendPythonFolder	 = True
config.JobType.allowUndistributedCMSSW = True
config.section_("Data")
#config.Data.inputDataset = '/JetHT/Run2018C-Nano14Dec2018-v1/NANOAOD'
#config.Data.inputDBS = 'phys03'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
#config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 2
config.Data.totalUnits = 10
config.JobType.allowUndistributedCMSSW = True
config.Data.outLFNDirBase = '/store/user/{}/{}'.format(getUsernameFromSiteDB(), job_name)
config.Data.publication = False
config.Data.outputDatasetTag = job_name
#config.Data.ignoreLocality = True

config.section_("Site")
config.Site.storageSite = "T3_US_Brown"
config.Data.inputDataset = '/SingleMuon/Run2018B-Nano14Dec2018-v1/NANOAOD'