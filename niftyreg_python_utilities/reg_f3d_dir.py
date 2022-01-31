"""
@author: pritesh-mehta
"""

import os
from pathlib import Path
from argparse import ArgumentParser

def reg_f3d_dir(niftyreg_exe_dir, ref_dir, flo_dir, aff_dir, res_dir,
                   param_str='-interp 1', extension='nii.gz'):
    '''Apply niftyreg reg_f3d to dir
    '''
    ref = os.listdir(ref_dir)
    flo = os.listdir(flo_dir)
      
    ref = [x for x in ref if extension in x]
    flo = [x for x in flo if extension in x]
    
    cpp_dir = Path(res_dir) / "cpp"
      
    for file in ref:
        ref = os.path.join(ref_dir, file)
        flo = os.path.join(flo_dir, file)
        aff = os.path.join(aff_dir, file.replace(extension, "") + "_aff.txt")
        res = os.path.join(res_dir, file)
        cpp = os.path.join(cpp_dir,"nrr_cpp_" + file)
        os.system(r"cd " + str(niftyreg_exe_dir) + " & reg_f3d -ref " + str(ref) + " -flo " + 
                  str(flo) + " -res " + str(res) + " -aff " + str(aff) + " -cpp " + str(cpp) + " " + str(param_str))
    return None
       
def process():
    parser = ArgumentParser()
    parser.add_argument('--niftyreg_exe_dir', required=True, type=str)
    parser.add_argument('--ref_dir', required=True, type=str)
    parser.add_argument('--flo_dir', required=True, type=str)
    parser.add_argument('--res_dir', required=True, type=str)
    parser.add_argument('--aff_dir', required=True, type=str)
    parser.add_argument('--param_str', required=False, type=str, default='-interp 1')
    parser.add_argument('--extension', required=False, type=str, default='.nii.gz')
      
    args = parser.parse_args()
    
    reg_f3d_dir(args.niftyreg_exe_dir, args.ref_dir, args.flo_dir, 
                   args.aff_dir, args.res_dir,
                   param_str=args.param_str, extension=args.extension)
    
if __name__ == "__main__":
    process()