#!/usr/bin/env python
import os, re, sys, commands, math, time, calendar

print '\nSTART\n'
ts = calendar.timegm(time.gmtime())
               
# PDNameDic = {"QCD_Pt_170to300_TuneCP5_13TeV_pythia8":"",
            # "QCD_Pt_300to470_TuneCP5_13TeV_pythia8":"",
            # "QCD_Pt_470to600_TuneCP5_13TeV_pythia8":"",
            # "QCD_Pt_600to800_TuneCP5_13TeV_pythia8":"",
            # "QCD_Pt_800to1000_TuneCP5_13TeV_pythia8":"",
            # "QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8":"",
            # "QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8":"",
            # "QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8":"",
            # "QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8":"",
            # "QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8":""}
            
# PDNameDic = {"QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8":"",
            # "QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8":"",
            # "QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8":"",
            # "QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8":"",
            # "QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8":"",
            # "QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8":"",
            # "QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8":""}
            
# PDNameDic = {"JetHT_Run2016B-ver1":"B",
            # "JetHT_Run2016B-ver2":"B",
            # "JetHT_Run2016C-UL2016":"C",
            # "JetHT_Run2016D-UL2016":"D",
            # "JetHT_Run2016E-UL2016":"E",
            # "JetHT_Run2016F-HIPM":"F",
            # "SingleMuon_Run2016B-ver1":"B",
            # "SingleMuon_Run2016B-ver2":"B",
            # "SingleMuon_Run2016C-UL2016":"C",
            # "SingleMuon_Run2016D-UL2016":"D",
            # "SingleMuon_Run2016E-UL2016":"E",
            # "SingleMuon_Run2016F-HIPM":"F",}
            
# PDNameDic = {"JetHT_Run2016B-ver1":"B",
            # "JetHT_Run2016B-ver2":"B",
            # "JetHT_Run2016C-UL2016":"C",
            # "JetHT_Run2016D-UL2016":"D",
            # "JetHT_Run2016E-UL2016":"E",
            # "JetHT_Run2016F-HIPM":"F"}
            
# PDNameDic = {"JetHT_Run2016F-UL2016":"F",
            # "JetHT_Run2016G-UL2016":"G",
            # "JetHT_Run2016H-UL2016":"H"}
            
# PDNameDic = {"JetHT_Run2017B-UL2017":"B",
            # "JetHT_Run2017C-UL2017":"C",
            # "JetHT_Run2017D-UL2017":"D",
            # "JetHT_Run2017E-UL2017":"E",
            # "JetHT_Run2017F-UL2017":"F"}
            
# PDNameDic = {"JetHT_Run2018A-UL2018":"A",
            # "JetHT_Run2018B-UL2018":"B",
            # "JetHT_Run2018C-UL2018":"C",
            # "JetHT_Run2018D-UL2018":"D"}
            
# PDNameDic = {"JetHT_Run2018D-UL2018":"D"}
            
            
PDNameDic = {"ZprimeTo3GluonNarrow":""}

# PDNameDic = {"Res1ToRes2QTo3Q_1750_0p3":"",
            # "Res1ToRes2QTo3Q_1750_0p4":"",
            # "Res1ToRes2QTo3Q_1750_0p5":"",
            # "Res1ToRes2QTo3Q_1750_0p6":"",
            # "Res1ToRes2QTo3Q_1750_0p7":"",
            # "Res1ToRes2QTo3Q_2000_0p3":"",
            # "Res1ToRes2QTo3Q_2500_0p3":"",
            # "Res1ToRes2QTo3Q_3000_0p3":"",
            # "Res1ToRes2QTo3Q_3500_0p3":"",
            # "Res1ToRes2QTo3Q_4000_0p3":"",
            # "Res1ToRes2QTo3Q_4500_0p3":"",
            # "Res1ToRes2QTo3Q_5000_0p3":"",
            # "Res1ToRes2QTo3Q_6000_0p3":"",
            # "Res1ToRes2QTo3Q_7000_0p3":"",
            # "Res1ToRes2QTo3Q_8000_0p3":"",
            # "Res1ToRes2QTo3Q_9000_0p3":"",
            # "Res1ToRes2QTo3Q_10000_0p3":"",
            # "Res1ToRes2QTo3Q_2000_0p4":"",
            # "Res1ToRes2QTo3Q_2500_0p4":"",
            # "Res1ToRes2QTo3Q_3000_0p4":"",
            # "Res1ToRes2QTo3Q_3500_0p4":"",
            # "Res1ToRes2QTo3Q_4000_0p4":"",
            # "Res1ToRes2QTo3Q_4500_0p4":"",
            # "Res1ToRes2QTo3Q_5000_0p4":"",
            # "Res1ToRes2QTo3Q_6000_0p4":"",
            # "Res1ToRes2QTo3Q_7000_0p4":"",
            # "Res1ToRes2QTo3Q_8000_0p4":"",
            # "Res1ToRes2QTo3Q_9000_0p4":"",
            # "Res1ToRes2QTo3Q_10000_0p4":"",
            # "Res1ToRes2QTo3Q_2000_0p5":"",
            # "Res1ToRes2QTo3Q_2500_0p5":"",
            # "Res1ToRes2QTo3Q_3000_0p5":"",
            # "Res1ToRes2QTo3Q_3500_0p5":"",
            # "Res1ToRes2QTo3Q_4000_0p5":"",
            # "Res1ToRes2QTo3Q_4500_0p5":"",
            # "Res1ToRes2QTo3Q_5000_0p5":"",
            # "Res1ToRes2QTo3Q_6000_0p5":"",
            # "Res1ToRes2QTo3Q_7000_0p5":"",
            # "Res1ToRes2QTo3Q_8000_0p5":"",
            # "Res1ToRes2QTo3Q_9000_0p5":"",
            # "Res1ToRes2QTo3Q_10000_0p5":"",
            # "Res1ToRes2QTo3Q_2000_0p6":"",
            # "Res1ToRes2QTo3Q_2500_0p6":"",
            # "Res1ToRes2QTo3Q_3000_0p6":"",
            # "Res1ToRes2QTo3Q_3500_0p6":"",
            # "Res1ToRes2QTo3Q_4000_0p6":"",
            # "Res1ToRes2QTo3Q_4500_0p6":"",
            # "Res1ToRes2QTo3Q_5000_0p6":"",
            # "Res1ToRes2QTo3Q_6000_0p6":"",
            # "Res1ToRes2QTo3Q_7000_0p6":"",
            # "Res1ToRes2QTo3Q_8000_0p6":"",
            # "Res1ToRes2QTo3Q_9000_0p6":"",
            # "Res1ToRes2QTo3Q_10000_0p6":"",
            # "Res1ToRes2QTo3Q_2000_0p7":"",
            # "Res1ToRes2QTo3Q_2500_0p7":"",
            # "Res1ToRes2QTo3Q_3000_0p7":"",
            # "Res1ToRes2QTo3Q_3500_0p7":"",
            # "Res1ToRes2QTo3Q_4000_0p7":"",
            # "Res1ToRes2QTo3Q_4500_0p7":"",
            # "Res1ToRes2QTo3Q_5000_0p7":"",
            # "Res1ToRes2QTo3Q_6000_0p7":"",
            # "Res1ToRes2QTo3Q_7000_0p7":"",
            # "Res1ToRes2QTo3Q_8000_0p7":"",
            # "Res1ToRes2QTo3Q_9000_0p7":"",
            # "Res1ToRes2QTo3Q_10000_0p7":"",
# }


for PDName, era in PDNameDic.items():
   
   year = "UL2017"
   # jobName = "{}_skim_{}".format(PDName, year) new
   jobName = "{}_skim_{}".format(PDName, year)
   sourceType = "mc"
   jobtype = ""
   jobCfg = "run_skimmer.py"
   jobScript = "run_skimmer.sh"
   
   print(PDName, year, era, jobCfg, jobScript)
   
   rel = "CMSSW_10_6_27"
   eosDirMain = "/eos/user/x/xuyan/TrijetSkim/" + jobName + "/"
   eosDir = "/eos/user/x/xuyan/TrijetSkim/" + jobName + jobtype + "/"

   rootDir = os.environ["CMSSW_BASE"] + "/src/PhysicsTools/DijetSkimmer/condor/"
   jobDir = rootDir + jobName + jobtype + "/"
   ret = 0
   files_batch = 5

   fileList = "{}/samples/{}_{}.txt".format(rootDir, year, PDName)

   if ret == 0:
      ret = os.system("mkdir -p " + jobDir)
      ret = os.system("mkdir -p " + eosDir + "hist/")
      ret = os.system("mkdir -p " + eosDir + "log/")
      ret = os.system("mkdir -p " + eosDir + "rootfile/")
      ret = os.system("mkdir -p " + jobDir + "out/")
      ret = os.system("mkdir -p " + jobDir + "err/")
      ret = os.system("mkdir -p " + jobDir + "log/")
      ret = os.system("rm filelist_tmp_*.list")
      ret = os.system("rm filelist.tgz")
      ret = os.chdir(os.environ["CMSSW_BASE"]+"/../")
      print('Tarballing ' + rel + "/ into " + jobName + ".tgz...")
      ret = os.system("tar --exclude='ignore' --exclude='.git' " + "-zcf " + jobName + ".tgz " + rel)
      print 'Done!'
      ret = os.system("mv " + jobName + ".tgz " + eosDir) 
      ret = os.chdir(jobDir)
      # ret = os.system("cp /tmp/x509up_u93529 /afs/cern.ch/user/x/xuyan/private/x509up/x509up_u93529")
      proxy_path = "/afs/cern.ch/user/x/xuyan/private/x509up/x509up_u93529"
      
      file1 = open(fileList, 'r')
      file_content = file1.readlines()
      chunks = len(file_content) / files_batch + 1
      
      for ichunk in range(chunks):
         filelist_name = "filelist_tmp_%i.list" %(ichunk)
         filelist_tmp = open(filelist_name, 'w')
         for file in file_content[ichunk*files_batch:(ichunk+1)*files_batch]:
            filelist_tmp.write(file)
         filelist_tmp.close()
      ret = os.system("tar -cvf filelist.tgz filelist_tmp_*")
      
      with open(jobName + '.jdl', 'w') as jdl:
         jdl.write("universe = vanilla\n")
         jdl.write("Executable = " + rootDir + jobScript + "\n")
         jdl.write("Should_Transfer_Files = YES\n")
         jdl.write("WhenToTransferOutput = ON_EXIT\n")
         jdl.write("Transfer_Input_Files = " + rootDir + jobScript + ", " + rootDir + jobCfg + ", filelist.tgz" + "\n")
         jdl.write("Output = "     + jobDir + "out/$(ProcId).out\n")
         jdl.write("Error = "      + jobDir + "err/$(ProcId).err\n")
         jdl.write("Log = "        + jobDir + "log/$(ProcId).log\n")
         jdl.write("Arguments = " + eosDir + " " + jobName + " " + rel + " $(ProcId) " + jobCfg + " filelist_tmp_$(ProcId).list " + proxy_path + " " + PDName + " " + sourceType + " " + year + " " + era + " " + eosDirMain + "\n")
         jdl.write("+JobFlavour = " + "\"tomorrow\"" + "\n")
         jdl.write("priority = 15" + "\n")
         # jdl.write("+MaxRuntime = 28800\n")
         # jdl.write("on_exit_remove = (ExitBySignal == False) && (ExitCode == 0)\n")
         # jdl.write("max_retries = 3\n")
         # jdl.write("requirements = Machine =!= LastRemoteHost\n")
         jdl.write("Queue " + str(chunks) + "\n")      

      os.system("condor_submit " + jobName + ".jdl")
      print str(chunks) + " jobs submitted."
      os.system("condor_q")
      os.chdir(rootDir)
   else:
      print("Submission failed: {}".format(jobName))