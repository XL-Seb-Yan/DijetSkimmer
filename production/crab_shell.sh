#this is not mean to be run locally
#
echo Check if TTY
if [ "`tty`" != "not a tty" ]; then
  echo "YOU SHOULD NOT RUN THIS IN INTERACTIVE, IT DELETES YOUR LOCAL FILES"
else

ls -lR .
echo "ENV..................................."
env 
echo "VOMS"
voms-proxy-info -all
echo "CMSSW BASE, python path, pwd"
echo $CMSSW_BASE 
echo $PYTHON_PATH
echo $PWD 

# Is this garbage necessary?
mkdir hide
mv $CMSSW_BASE/lib/ hide
mv $CMSSW_BASE/src/ hide
#mv $CMSSW_BASE/module/ hide
mv $CMSSW_BASE/python/ hide
mv python $CMSSW_BASE/python
mv lib $CMSSW_BASE/lib
mv src $CMSSW_BASE/src
#mv module $CMSSW_BASE/module

cd $CMSSW_BASE/src
rm -f $CMSSW_BASE/src/PhysicsTools/DijetSkimmer/python/__init__.py
rm -f $CMSSW_BASE/src/PhysicsTools/NanoAODTools/python/__init__.py
rm -f $CMSSW_BASE/src/PhysicsTools/NanoAODTools/python/postprocessing/__init__.py
eval `scramv1 runtime -sh`
scram b -j8
cd -

# Output filename
#export HADDFILENAME="nanoskim_$1.root"
#sed -i "s/nanoskim.root/$HADDFILENAME/g" PSet.py
#echo "jkl print PSet:"
#cat PSet.py

echo Found Proxy in: $X509_USER_PROXY
echo "asdf"
#ls -lrth

python -c "import PhysicsTools"
python -c "import PhysicsTools.NanoAODTools"
python -c "import PhysicsTools.NanoAODTools.postprocessing"
python -c "import PhysicsTools.NanoAODTools.postprocessing.framework"

python crab_meat.py "$@" #--haddFileName $HADDFILENAME
hadd hists.root hists_*.root

#cp "nanoskim_$1.root" nanoskim.root
echo "Python path:"
python -c "import sys; print sys.path;"
ls -l
echo "lsing CMSSW cfipython:"
ls -lRth $CMSSW_BASE/cfipython/slc7_amd64_gcc700
echo "lsing CMSSW python:"
ls -lRth $CMSSW_BASE/python
echo "lsing python:"
ls -lRth python
echo "jkl;"
fi
