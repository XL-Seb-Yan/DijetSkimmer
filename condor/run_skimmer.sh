#!/bin/bash
echo "Starting job on " `date` #Date/time of start of job
echo "Running on: `uname -a`" #Condor job is running on this node
echo "System software: `cat /etc/redhat-release`" #Operating System on that node
source /cvmfs/cms.cern.ch/cmsset_default.sh  ## if a bash script, use .sh instead of .csh
export X509_USER_PROXY=${7}
voms-proxy-info -all
voms-proxy-info -all -file ${7}
### for case 1. EOS have the following line, otherwise remove this line in case 2.
#Arguments 1)eosDir 2)jobName 3)rel 4)iJob 5)jobCfg 6)inputFilelist 7)proxy

# You need to move transfered files to the working area
ls /eos/home-x/xuyan/TrijetData/NanoAODs/XYgToggg/Res1ToRes2GluTo3Glu_M1-2000_R-0p3_TuneCP5_13TeV-madgraph-pythia8/nanoAOD_0.root
root -l -q /eos/home-x/xuyan/TrijetData/NanoAODs/XYgToggg/Res1ToRes2GluTo3Glu_M1-2000_R-0p3_TuneCP5_13TeV-madgraph-pythia8/nanoAOD_0.root
cp ${1}${2}.tgz .
tar -xf ${2}.tgz
rm ${2}.tgz
mv ${5} ${3}/src/PhysicsTools/DijetSkimmer/condor
mv filelist.tgz ${3}/src/PhysicsTools/DijetSkimmer/condor

cd ${3}/src/
scramv1 b ProjectRename
eval `scramv1 runtime -sh` # cmsenv is an alias not on the workers
cd PhysicsTools/DijetSkimmer/condor
tar -xf filelist.tgz
cp /afs/cern.ch/work/x/xuyan/TrijetProj/Skimmer/CMSSW_10_6_27/src/PhysicsTools/DijetSkimmer/condor/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt ./
cp /afs/cern.ch/work/x/xuyan/TrijetProj/Skimmer/CMSSW_10_6_27/src/PhysicsTools/DijetSkimmer/condor/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt ./
cp /afs/cern.ch/work/x/xuyan/TrijetProj/Skimmer/CMSSW_10_6_27/src/PhysicsTools/DijetSkimmer/condor/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt ./
ls ./
stdbuf -oL -eL echo "Processing: ${8}" >> ${1}/log/log_${4}.txt

file=${12}/rootfile/nanoskim_${4}.root
if test -f "$file"; then
  stdbuf -oL -eL echo "$file already exists in the main output" >> ${1}/log/log_${4}.txt
  exit 1
else
  stdbuf -oL -eL python run_skimmer.py --ijob ${4} --source ${9} --dataset ${8} --year ${10} --era ${11} >> ${1}/log/log_${4}.txt
  cp nanoskim.root ${1}/rootfile/nanoskim_${4}.root
  cp hists.root ${1}/hist/hists_${4}.root
  cp nanoskim.root ${1}/rootfile/nanoskim_${4}.root
  cp hists.root ${1}/hist/hists_${4}.root
  
  file=${1}/rootfile/nanoskim_${4}.root
  if test -f "$file"; then
    stdbuf -oL -eL echo "$file exists in the 2nd check" >> ${1}/log/log_${4}.txt
    exit 2
  else
    stdbuf -oL -eL echo "$file DOES NOT exists, retrying in 1mins..." >> ${1}/log/log_${4}.txt
    stdbuf -oL -eL ls ${1}/rootfile/ >> ${1}/log/log_${4}.txt
    sleep 1m
    echo "Retrying..." >> ${1}/log/log_${4}.txt
    stdbuf -oL -eL python run_skimmer.py --ijob ${4} --source ${9} --dataset ${8} --year ${10} --era ${11} >> ${1}/log/log_${4}.txt
    cp nanoskim.root ${1}/rootfile/nanoskim_${4}.root
    cp hists.root ${1}/hist/hists_${4}.root
  fi
fi

cd ${_CONDOR_SCRATCH_DIR}
rm -rf ${3}