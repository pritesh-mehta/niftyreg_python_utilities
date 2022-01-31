"""
@author: pritesh-mehta
"""

from setuptools import setup, find_packages

setup(name='niftyreg_python_utilities',
      version='1.0',
      description='Python interface for niftyreg',
      url='https://github.com/pritesh-mehta/niftyreg_python_utilities',
      python_requires='>=3.6',
      author='Pritesh Mehta',
      author_email='pritesh.mehta@kcl.ac.uk',
      license='Apache 2.0',
      zip_safe=False,
      install_requires=[
      'argparse',
      ],
      entry_points={
        'console_scripts': [
            'reg_aladin_dir=niftyreg_python_utilities.reg_aladin_dir:process',
            'reg_f3d_dir=niftyreg_python_utilities.reg_f3d_dir:process',
            'apply_transform_dir=niftyreg_python_utilities.apply_transform_dir:process',
            ],
      },
      packages=find_packages(include=['niftyreg_python_utilities']),
      classifiers=[
          'Intended Audience :: Science/Research',
          'Programming Language :: Python',
          'Topic :: Scientific/Engineering',
      ]
      )