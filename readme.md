# Niftyreg-Python-Utilities

This repository contains functionality for running [NiftyReg](https://github.com/KCL-BMEIS/niftyreg) registration methods over directories of images. 

## Installation instructions 

1) Clone/download repository.

2) Change directory into repository.

3) Install:
	```
	pip install .
    ```
	
## How to use it 

- Function imports.

- Command line (use full paths):

	- reg_aladin_dir e.g.:
		```
		reg_aladin_dir --niftyreg_exe_dir C:\Users\pmeht\packages\niftyreg_python_utilities\niftyreg_exe --ref_dir C:\Users\pmeht\packages\niftyreg_python_utilities\sample_data\0_sample_t2w --flo_dir C:\Users\pmeht\packages\niftyreg_python_utilities\sample_data\0_sample_adc --res_dir C:\Users\pmeht\packages\niftyreg_python_utilities\sample_data\1_reg_aladin_adc --param_str "-interp 1"
		```

	- reg_f3d_dir e.g.:
		```
		reg_f3d_dir --niftyreg_exe_dir C:\Users\pmeht\packages\niftyreg_python_utilities\niftyreg_exe --ref_dir C:\Users\pmeht\packages\niftyreg_python_utilities\sample_data\0_sample_t2w --flo_dir C:\Users\pmeht\packages\niftyreg_python_utilities\sample_data\0_sample_adc --aff_dir C:\Users\pmeht\packages\niftyreg_python_utilities\sample_data\1_reg_aladin_adc\aff --res_dir C:\Users\pmeht\packages\niftyreg_python_utilities\sample_data\2_reg_f3d_adc --param_str "-sx 10 -be 0.5 --lncc 5 -le 0 -ln 5 -lp 3 -vel -interp 1"
		```

	- apply_transform_dir e.g. transform masks from t2w space to dwi space:
		```
		apply_transform_dir --niftyreg_exe_dir C:\Users\pmeht\packages\niftyreg_python_utilities\niftyreg_exe --ref_dir C:\Users\pmeht\packages\niftyreg_python_utilities\sample_data\0_sample_adc --flo_dir C:\Users\pmeht\packages\niftyreg_python_utilities\sample_data\0_sample_mask_in_t2w_space --res_dir C:\Users\pmeht\packages\niftyreg_python_utilities\sample_data\3_mask_in_dwi_space --trans_dir C:\Users\pmeht\packages\niftyreg_python_utilities\sample_data\2_reg_f3d_adc\cpp\backward --param_str "-inter 0"
		```
