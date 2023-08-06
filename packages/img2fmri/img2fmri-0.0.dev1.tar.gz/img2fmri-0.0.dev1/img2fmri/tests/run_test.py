import img2fmri
from img2fmri import utils

import os
import numpy as np
import nibabel as nib
import glob
from pathlib import Path
from natsort import natsorted


here = os.path.dirname(__file__)
input_dir = os.path.join(here, 'test_data','images')
output_dir = os.path.join(here, 'test_data','output')
movie_output = os.path.join(here, 'test_data','output','landscape.nii.gz')
ALL_ROIS = ['EarlyVis', 'OPA', 'LOC', 'RSC', 'PPA']
roi_list = ['EarlyVis', 'OPA', 'LOC', 'RSC']

def test_predict(roi_list=['EarlyVis', 'OPA', 'LOC', 'RSC']):
    img2fmri.predict(input_dir,
                    output_dir=output_dir,
                    sigma=1.25,
                    roi_list=roi_list)
    
    overlap = utils.get_subj_overlap(roi_list)
    file_list = natsorted(glob.glob(f'{input_dir}/*'))
    predictions = np.zeros((len(file_list),np.count_nonzero(overlap)))
    for i, f in enumerate(file_list):
        pred_brain = nib.load(os.path.join(here,output_dir,f'{Path(f).stem}.nii.gz')).get_fdata()
        predictions[i] = pred_brain[overlap]

    # Make sure the horse and amusement park predictions and are more correlated within groups
    # than across groups
    corr = np.corrcoef(predictions)
    for i in range(0,len(file_list),2):
        assert(np.isclose(corr[i,i+1],np.max(np.delete(corr[i], i))))
        assert(np.isclose(corr[i,i+1],np.max(np.delete(corr[i+1], i+1))))
    

    # Make sure output predictions are properly saved to their ROIs
    for i, f in enumerate(file_list):
        pred_brain = nib.load(os.path.join(here,output_dir,f'{Path(f).stem}.nii.gz')).get_fdata()

        # Make sure all predicted voxels in roi_list have a non-zero value:
        assert(np.count_nonzero(pred_brain[overlap]) == np.count_nonzero(overlap))

        # Make sure that any ROIs not predicted to don't have every voxel predicted (some still will
        # have nonzero values given overlap):
        unpredicted_rois = [x for x in ALL_ROIS if x not in roi_list]
        assert(np.count_nonzero(pred_brain[utils.get_subj_overlap(unpredicted_rois)]) != 
               np.count_nonzero(utils.get_subj_overlap(unpredicted_rois)))

def test_CLI():
    # Ensure command line interface and predict_movie work properly (Note: these fMRI predictions
    # are made from the command line before running this file. See run_tests.sh for info.)
    try:
        pred_nib = nib.load(movie_output) 
        pred_brain = pred_nib.get_fdata()
        # Ensure predicted movie brain matches 4D MNI shape of (x,y,z,frames)
        assert(len(pred_brain.shape) == 4)

    except:
        FileNotFoundError
        print("\nNo CLI movie prediction from ./run_tests.sh was found to evaluate.")

if __name__ == '__main__':
    test_predict(roi_list)
    test_CLI()
    print("\nTests passed.")

