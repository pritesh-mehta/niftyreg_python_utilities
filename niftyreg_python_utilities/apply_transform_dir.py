"""
@author: pritesh-mehta
"""

import os
from argparse import ArgumentParser

def apply_transform_dir(niftyreg_exe_dir, ref_dir, flo_dir, res_dir, trans_dir,
                   param_str='-inter 1', extension='nii.gz'):
    '''Apply transform to flo_dir
    '''
    ref = os.listdir(ref_dir)
    flo = os.listdir(flo_dir)
      
    ref = [x for x in ref if extension in x]
    flo = [x for x in flo if extension in x]
      
    for file in ref:
        ref = os.path.join(ref_dir, file)
        flo = os.path.join(flo_dir, file)
        res = os.path.join(res_dir, file)
        trans = os.path.join(trans_dir, "nrr_cpp_" + file)
        os.system(r"cd " + str(niftyreg_exe_dir) + " & reg_resample -ref " + str(ref) + " -flo " + 
                  str(flo) + " -res " + str(res) + " -trans " + str(trans) + " " + str(param_str))
    return None
       
def process():
    parser = ArgumentParser()
    parser.add_argument('--niftyreg_exe_dir', required=True, type=str)
    parser.add_argument('--ref_dir', required=True, type=str)
    parser.add_argument('--flo_dir', required=True, type=str)
    parser.add_argument('--res_dir', required=True, type=str)
    parser.add_argument('--trans_dir', required=True, type=str)
    parser.add_argument('--param_str', required=False, type=str, default='-inter 1')
    parser.add_argument('--extension', required=False, type=str, default='.nii.gz')
      
    args = parser.parse_args()
    
    apply_transform_dir(args.niftyreg_exe_dir, args.ref_dir, args.flo_dir, 
                   args.res_dir, args.trans_dir,
                   param_str=args.param_str, extension=args.extension)
    
if __name__ == "__main__":
    process()