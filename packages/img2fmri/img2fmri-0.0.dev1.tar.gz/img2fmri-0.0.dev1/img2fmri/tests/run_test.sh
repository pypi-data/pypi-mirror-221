#!/bin/bash
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
pushd $parent_path

echo "Predicting test movie with command line interface:"
img2fmri --input img2fmri/tests/test_data/landscape.mp4 --predict_movie=1 \
          --output img2fmri/tests/test_data/output
ret=$?
if [ $ret -ne 0 ]; then
    echo "Tests Failed, see error and warning above."
    exit
fi

echo "\nPredicting individual images with python function:"
# python -c 'from run_test import test_predict, test_CLI; test_predict(); test_CLI();'
python img2fmri/tests/run_test.py
ret=$?
if [ $ret -ne 0 ]; then
    echo "Tests Failed, see error and warning above."
    exit
fi

popd