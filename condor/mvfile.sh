#!/bin/bash
for dataset in `ls /eos/user/x/xuyan/TrijetSkim/`
do
  echo "Processing ${dataset}"
  cd /eos/user/x/xuyan/TrijetSkim/${dataset}
  mkdir hist
  mkdir log
  mkdir rootfile
  `mv hist* hist/`
  `mv log* log/`
  `mv nano* rootfile/`
  `rm hist/*.tgz`
done
  