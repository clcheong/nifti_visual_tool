import nibabel as nib
import numpy as np
from mayavi import mlab

# Load the image file
img = nib.load("C://Users//User//Downloads//testing_3d_anatomy//completor_dataset//dataset//train//incomplete//s0777//s0777_2.nii.gz")

# Get the image data
data = img.get_fdata()

# Visualize the 3D data using mayavi
mlab.contour3d(data, contours=8, opacity=0.5)
mlab.show()
