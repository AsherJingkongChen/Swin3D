"""
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""
import glob
import os
from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

with open('Swin3D/__init__.py') as f:
    __version__ = f.read().split("'")[1]

extra_compile_args = {
    'cxx': ['-O3'],
    'nvcc': ['-O3', '--expt-relaxed-constexpr'],
}

setup(
    name='Swin3D',
    version=__version__,
    packages=find_packages(),
    ext_modules=[
        CUDAExtension(
            name='Swin3D.sparse_dl.attn_cuda',
            sources=glob.glob('Swin3D/src/attn/*.cu') + glob.glob('Swin3D/src/attn/*.cpp'),
            extra_compile_args=extra_compile_args,
        ),
        CUDAExtension(
            name='Swin3D.sparse_dl.knn_cuda',
            sources=glob.glob('Swin3D/src/knn/*.cu') + glob.glob('Swin3D/src/knn/*.cpp'),
            extra_compile_args=extra_compile_args,
        ),
    ],
    install_requires=['ninja', 'torch'],
    cmdclass={'build_ext': BuildExtension.with_options(use_ninja=True)},
)