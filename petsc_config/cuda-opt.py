#!/usr/bin/env python3

'''
This file is intended to be used to configure PETSc for dynamite.
It should be run in the PETSc root source directory.

To see all possible options, run "./configure --help" in the PETSc root directory.
You may want to pipe to "less"; it is a big help page ;)
'''

from os import environ

configure_option_dict = {

    # use native complex numbers for scalars. currently required for dynamite.
    '--with-scalar-type': 'complex',

    # GPU support
    '--with-cuda': None,  # none just means no value for this arg

    # ensure correct c++ dialect
    '--with-cxx-dialect': 'cxx14',
    '--with-cuda-dialect': 'cxx14',

    # some PETSc optimization flags
    '--with-debugging': '0',
    '--with-fortran-kernels': '1',

    # compiler optimization flags
    '--COPTFLAGS': '-O3',
    '--CXXOPTFLAGS': '-O3',
    '--FOPTFLAGS': '-O3',
    '--CUDAOPTFLAGS': '-O3',

    # may need/want to adjust to match your hardware's compute capability,
    # e.g. '80' for compute capability 8.0
    # can also adjust with DNM_CUDA_ARCH environment variable (see below)
    '--with-cuda-arch': '70',

    #'--download-scalapack': None,
    #'--download-mumps': None,

    # required to work with spin chains larger than 31 spins
    '--with-64-bit-indices': None,

    # uncomment if you don't have an MPI implementation already installed
    #'--download-openmpi': None,
   '--with-mpi-dir': '/lustre/opt/cascadelake/linux-centos7-cascadelake/gcc-9.3.0/openmpi-4.1.1-tofo6uuqy57ju4makxliq5frdjvjijyj',
    '--download-fblaslapack' : '1',
}

if 'DNM_CUDA_ARCH' in environ:
    configure_option_dict['--with-cuda-arch'] = environ['DNM_CUDA_ARCH']

if __name__ == '__main__':
    import sys
    import os
    sys.path.insert(0, os.path.abspath('config'))
    import configure

    configure_options = []
    for key, val in configure_option_dict.items():
        if val is None:
            configure_options.append(key)
        else:
            configure_options.append(key+'='+val)

    configure_options += sys.argv[1:]
    configure.petsc_configure(configure_options)
