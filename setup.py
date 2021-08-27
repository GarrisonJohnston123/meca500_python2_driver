#!/usr/bin/env python
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='MecademicRobot',
    version='1.0.2',
    author='Garrison Johnston',
    author_email='Garrison.L.Johnston@vanderbilt.edu',
    license='MIT',
    description='A package to control the Mecademic Robots through python2',
    long_description=long_description,
    long_description_content_type='markdown',
    url='https://github.com/GarrisonJohnston123/meca500_python2_driver',
    packages=setuptools.find_packages(),
    data_files=[('',['LICENSE', 'README.md'])],
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
    
)
