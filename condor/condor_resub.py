#!/usr/bin/env python
import os, re, sys, commands, math, time, calendar

print '\nSTART\n'
            
# JobDic = {"JetHT_Run2018D_skim_1626872153":["D",1],
         # "SingleMuon_Run2018D_skim_1626872153":["D",3]}
         
JobDic = {"JetHT_Run2018D_skim_1626872153":["D",1]}

print(JobDic)
         
for jobName, info in JobDic.items():
   print(jobName)
               
   year = "UL2018"
   sourceType = "data"
   # era = "dummy"
   era = info[0]
   jobCfg = "run_skimmer.py"
   jobScript = "run_skimmer.sh"
   rel = "CMSSW_10_6_27"
   eosDir = "/eos/user/x/xuyan/TrijetSkim/" + jobName + "/resubmit/"

   rootDir = os.environ["CMSSW_BASE"] + "/src/PhysicsTools/DijetSkimmer/condor/"
   jobDir = rootDir + jobName + "_resubmit/"
   ret = 0
   files_batch = 1
   chunks = info[1]

   if ret == 0:
      ret = os.system("mv " + jobName + " " + jobDir)
      ret = os.system("mkdir -p " + eosDir)
      ret = os.system("mkdir -p " + eosDir + "hist/")
      ret = os.system("mkdir -p " + eosDir + "log/")
      ret = os.system("mkdir -p " + eosDir + "rootfile/")
      ret = os.system("mkdir -p " + jobDir + "out/")
      ret = os.system("mkdir -p " + jobDir + "err/")
      ret = os.system("mkdir -p " + jobDir + "log/")
      ret = os.chdir(os.environ["CMSSW_BASE"]+"/../")
      print('Tarballing ' + rel + "/ into " + jobName + "_resubmit" + ".tgz...")
      ret = os.system("tar --exclude='ignore' --exclude='.git' " + "-zcf " + jobName + "_resubmit" + ".tgz " + rel)
      print 'Done!'
      ret = os.system("mv " + jobName + "_resubmit" + ".tgz " + eosDir) 
      ret = os.chdir(jobDir)
      # ret = os.system("cp /tmp/x509up_u93529 /afs/cern.ch/user/x/xuyan/private/x509up/x509up_u93529")
      proxy_path = "/afs/cern.ch/user/x/xuyan/private/x509up/x509up_u93529"
      
      ret = os.system("tar -cvf filelist.tgz filelist_tmp_*")
      
      with open(jobName + "_resubmit" + '.jdl', 'w') as jdl:
         jdl.write("universe = vanilla\n")
         jdl.write("Executable = " + rootDir + jobScript + "\n")
         jdl.write("Should_Transfer_Files = YES\n")
         jdl.write("WhenToTransferOutput = ON_EXIT\n")
         jdl.write("Transfer_Input_Files = " + rootDir + jobScript + ", " + rootDir + jobCfg + ", filelist.tgz" + "\n")
         jdl.write("Output = "     + jobDir + "out/$(ProcId).out\n")
         jdl.write("Error = "      + jobDir + "err/$(ProcId).err\n")
         jdl.write("Log = "        + jobDir + "log/$(ProcId).log\n")
         jdl.write("Arguments = " + eosDir + " " + jobName + "_resubmit" + " " + rel + " $(ProcId) " + jobCfg + " filelist_tmp_$(ProcId).list " + proxy_path + " " + jobName + " " + sourceType + " " + year + " " + era + "\n")
         jdl.write("+JobFlavour = " + "\"tomorrow\"" + "\n")
         # jdl.write("+MaxRuntime = 28800\n")
         # jdl.write("on_exit_remove = (ExitBySignal == False) && (ExitCode == 0)\n")
         # jdl.write("max_retries = 3\n")
         # jdl.write("requirements = Machine =!= LastRemoteHost\n")
         jdl.write("Queue " + str(chunks) + "\n")      

      os.system("condor_submit " + jobName + "_resubmit" + ".jdl")
      print str(chunks) + " jobs submitted."
      os.system("condor_q")
      os.chdir(rootDir)
   else:
      print("Submission failed: {}".format(jobDir))